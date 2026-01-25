#!/usr/bin/env python3
"""
RAG Chatbot for Literature Review
Answer questions about specific literature folders using RAG with multiple API backends:
- Poe API
- Z.AI API
- HKBU Gen AI (Azure OpenAI)
- Demo mode (local embeddings)
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from enum import Enum
import requests

# LangChain imports for RAG
from langchain_community.document_loaders import BSHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_core.embeddings import Embeddings


class APIProvider(Enum):
    """Supported API providers"""
    POE = "poe"
    ZAI = "zai"
    HKBU = "hkbu"
    DEMO = "demo"


class HKBUEmbeddings(Embeddings):
    """Custom embeddings class for HKBU GenAI API"""
    
    def __init__(self, api_key: str, model: str = "text-embedding-3-small", api_version: str = "2023-12-01-preview"):
        self.api_key = api_key
        self.model = model
        self.api_version = api_version
        self.base_url = "https://genai.hkbu.edu.hk/api/v0/rest"
        self.embedding_url = f"{self.base_url}/openai/deployments/{model}/embeddings"
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of documents"""
        embeddings = []
        
        # Process in batches to avoid overwhelming the API
        batch_size = 100
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            batch_embeddings = self._embed_batch(batch)
            embeddings.extend(batch_embeddings)
        
        return embeddings
    
    def embed_query(self, text: str) -> List[float]:
        """Embed a single query text"""
        return self._embed_batch([text])[0]
    
    def _embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed a batch of texts"""
        headers = {
            "api-key": self.api_key,
            "Content-Type": "application/json"
        }
        
        # HKBU API accepts array of inputs
        payload = {
            "input": texts if len(texts) > 1 else texts[0]
        }
        
        url = f"{self.embedding_url}?api-version={self.api_version}"
        
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        
        if response.status_code != 200:
            error_msg = f"HKBU API error: {response.status_code}"
            try:
                error_detail = response.json()
                error_msg += f" - {error_detail}"
            except:
                error_msg += f" - {response.text}"
            raise Exception(error_msg)
        
        result = response.json()
        
        if "data" not in result:
            raise Exception(f"HKBU API response missing 'data' field: {result}")
        
        # Extract embeddings
        embeddings = [item["embedding"] for item in result["data"]]
        return embeddings


class RAGChatbot:
    def __init__(self, literature_folder: str, api_provider: str = "poe"):
        """
        Initialize the RAG chatbot for a specific literature folder.
        
        Args:
            literature_folder: Path to the folder containing literature (HTML files)
            api_provider: API provider to use ('poe', 'zai', 'hkbu', or 'demo')
        """
        # Convert to absolute path and ensure it exists
        literature_path = Path(literature_folder)
        if not literature_path.is_absolute():
            # Try to resolve relative to project root
            base_path = Path(__file__).parent.parent.parent
            literature_path = (base_path / literature_folder).resolve()
        
        self.literature_folder = literature_path
        self.api_provider = self._parse_provider(api_provider)
        self.vector_store = None
        self.qa_chain = None
        self.chat_history = []
        self.chunks = None
        self.index = None
        
        # Load API keys and configure
        self.api_key = self._load_api_key()
        self._configure_provider()
        
        provider_name = self.api_provider.value.upper()
        print(f"✓ RAG Chatbot initialized for: {self.literature_folder.name} (Provider: {provider_name})")
    
    def _parse_provider(self, provider: str) -> APIProvider:
        """Parse and validate API provider"""
        provider_lower = provider.lower()
        try:
            return APIProvider(provider_lower)
        except ValueError:
            print(f"⚠️  Unknown provider '{provider}', defaulting to 'demo'")
            return APIProvider.DEMO
    
    def _load_api_key(self) -> Optional[str]:
        """Load API key based on provider"""
        base_path = Path(__file__).parent.parent.parent
        
        key_paths = {
            APIProvider.POE: base_path / "LLM" / "poe.md",
            APIProvider.ZAI: base_path / "LLM" / "zai.md",
            APIProvider.HKBU: base_path / "LLM" / "HKBUAPIkey.md",
        }
        
        if self.api_provider == APIProvider.DEMO:
            return None
        
        key_path = key_paths.get(self.api_provider)
        if key_path and key_path.exists():
            with open(key_path, 'r') as f:
                key = f.read().strip().split('\n')[0]
                return key
        else:
            print(f"⚠️  API key file not found: {key_path}")
            return None
    
    def _configure_provider(self) -> None:
        """Configure API-specific settings"""
        if self.api_provider == APIProvider.DEMO:
            return
        
        # Provider-specific configurations will be set in create_vector_store and setup_qa_chain
        pass
    
    def load_documents(self) -> List:
        """Load HTML documents from the literature folder"""
        documents = []
        
        print(f"\n📂 Loading documents from {self.literature_folder}...")
        
        for file_path in self.literature_folder.glob("*.html"):
            print(f"   - Loading: {file_path.name}")
            try:
                loader = BSHTMLLoader(str(file_path))
                docs = loader.load()
                documents.extend(docs)
            except Exception as e:
                print(f"   ✗ Error loading {file_path.name}: {e}")
        
        if not documents:
            print("✗ No documents loaded!")
            return []
        
        print(f"✓ Loaded {len(documents)} document(s)")
        return documents
    
    def split_documents(self, documents: List) -> List:
        """Split documents into chunks for better retrieval"""
        print("\n🔄 Splitting documents into chunks...")
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,  # Increased for better context
            chunk_overlap=300,  # Increased overlap for better continuity
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        
        chunks = text_splitter.split_documents(documents)
        print(f"✓ Created {len(chunks)} chunks")
        
        return chunks
    
    def create_vector_store(self, chunks: List) -> None:
        """Create vector store using the configured provider"""
        print(f"\n💾 Creating vector store ({self.api_provider.value.upper()})...")
        
        if self.api_provider == APIProvider.DEMO:
            self._create_demo_vector_store(chunks)
        elif self.api_provider == APIProvider.POE:
            self._create_poe_vector_store(chunks)
        elif self.api_provider == APIProvider.ZAI:
            self._create_zai_vector_store(chunks)
        elif self.api_provider == APIProvider.HKBU:
            self._create_hkbu_vector_store(chunks)
    
    def _create_poe_vector_store(self, chunks: List) -> None:
        """Create vector store using Poe API embeddings"""
        # Poe API doesn't support embeddings endpoint, use demo embeddings
        print("⚠️  Poe API doesn't support embeddings, using local embeddings...")
        self._create_demo_vector_store(chunks)
    
    def _create_zai_vector_store(self, chunks: List) -> None:
        """Create vector store using Z.AI API embeddings"""
        try:
            # Z.AI doesn't have direct embedding support in LangChain
            # Fall back to demo mode for embeddings
            print("⚠️  Z.AI embeddings not directly supported, using demo embeddings...")
            self._create_demo_vector_store(chunks)
            
        except Exception as e:
            print(f"⚠️  Error creating Z.AI vector store: {e}")
            print("🔧 Falling back to demo mode...")
            self.api_provider = APIProvider.DEMO
            self._create_demo_vector_store(chunks)
    
    def _create_hkbu_vector_store(self, chunks: List) -> None:
        """Create vector store using HKBU GenAI embeddings"""
        try:
            embeddings = HKBUEmbeddings(
                api_key=self.api_key,
                model="text-embedding-3-small",
                api_version="2023-12-01-preview"
            )
            
            self.vector_store = FAISS.from_documents(chunks, embeddings)
            vector_store_path = self.literature_folder / "vector_store_hkbu"
            self.vector_store.save_local(str(vector_store_path))
            print(f"✓ Vector store created and saved to {vector_store_path}")
            
        except Exception as e:
            print(f"⚠️  Error creating HKBU vector store: {e}")
            print("🔧 Falling back to demo mode...")
            self.api_provider = APIProvider.DEMO
            self._create_demo_vector_store(chunks)
    
    def _create_demo_vector_store(self, chunks: List) -> None:
        """Create demo vector store with local embeddings"""
        try:
            from sentence_transformers import SentenceTransformer
            import numpy as np
            import faiss
            
            print("   Loading local embedding model (first run will download)...")
            model = SentenceTransformer('all-MiniLM-L6-v2')
            
            texts = [chunk.page_content for chunk in chunks]
            embeddings = model.encode(texts, show_progress_bar=True)
            
            dimension = embeddings.shape[1]
            index = faiss.IndexFlatL2(dimension)
            index.add(embeddings.astype('float32'))
            
            self.chunks = chunks
            self.embeddings = embeddings
            self.index = index
            
            print("✓ Demo vector store created with local embeddings")
            
        except ImportError as e:
            print(f"✗ Error importing sentence-transformers: {e}")
            print("   Try: pip install sentence-transformers")
            raise
        except Exception as e:
            print(f"✗ Error creating demo vector store: {e}")
            raise
    
    def setup_qa_chain(self) -> None:
        """Set up the question-answering chain"""
        print(f"\n🔗 Setting up QA chain ({self.api_provider.value.upper()})...")
        
        if self.api_provider == APIProvider.DEMO:
            print("✓ Demo QA chain ready (using local search)")
            return
        
        # Poe and Z.AI use demo embeddings but their own APIs for generation
        # Only HKBU uses full LangChain QA chain
        if self.api_provider == APIProvider.POE:
            print("✓ Poe QA chain ready (local embeddings + Poe generation)")
            return
        elif self.api_provider == APIProvider.ZAI:
            print("✓ Z.AI QA chain ready (local embeddings + Z.AI generation)")
            return
        
        try:
            if self.api_provider == APIProvider.HKBU:
                self._setup_hkbu_qa_chain()
            
            print("✓ QA chain ready")
        except Exception as e:
            print(f"⚠️  Error setting up QA chain: {e}")
            # Don't fall back for HKBU - it can work with just embeddings
            if self.api_provider == APIProvider.HKBU:
                print("   Continuing with HKBU embeddings...")
            else:
                print("🔧 Falling back to demo mode...")
                self.api_provider = APIProvider.DEMO
    
    def _setup_poe_qa_chain(self) -> None:
        """Set up QA chain using Poe API"""
        from langchain.chains import RetrievalQA
        
        try:
            from langchain_openai import ChatOpenAI
            llm = ChatOpenAI(
                openai_api_key=self.api_key,
                base_url="https://api.poe.com/v1",
                model_name="Assistant",
                temperature=0
            )
        except ImportError:
            # Fallback for older LangChain versions
            from langchain_community.chat_models import ChatOpenAI
            llm = ChatOpenAI(
                openai_api_key=self.api_key,
                openai_api_base="https://api.poe.com/v1",
                model_name="Assistant",
                temperature=0
            )
        
        prompt_template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}

Question: {question}

Answer:"""
        
        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(search_kwargs={"k": 5}),  # Reduced for focused retrieval
            chain_type_kwargs={"prompt": PROMPT},
            return_source_documents=True
        )
    
    def _setup_zai_qa_chain(self) -> None:
        """Set up QA chain using Z.AI API"""
        from langchain.chains import RetrievalQA
        from zai import ZaiClient
        
        # Z.AI uses a custom client, need to wrap it for LangChain
        # For now, use a simple wrapper approach
        try:
            zai_client = ZaiClient(api_key=self.api_key)
            
            # Create a simple LLM wrapper for Z.AI
            class ZAILLMWrapper:
                def __init__(self, client, model="glm-4.7"):
                    self.client = client
                    self.model = model
                
                def __call__(self, prompt, **kwargs):
                    response = self.client.chat.completions.create(
                        model=self.model,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    return response.choices[0].message.content
            
            # For embeddings, we're using demo mode
            # For generation, we'll use Z.AI directly in ask_question
            print("✓ Z.AI client initialized (using demo embeddings + Z.AI generation)")
            
        except Exception as e:
            print(f"⚠️  Z.AI setup error: {e}")
            raise
    
    def _setup_hkbu_qa_chain(self) -> None:
        """Set up QA chain using HKBU GenAI"""
        # HKBU uses HKBU embeddings (already created in vector store)
        # For generation, we'll use Poe API (hybrid approach)
        print("✓ HKBU QA chain ready (HKBU embeddings + Poe generation)")
        # Load Poe API key for generation
        poe_key_path = Path(__file__).parent.parent.parent / "LLM" / "poe.md"
        if poe_key_path.exists():
            with open(poe_key_path, 'r') as f:
                self.poe_api_key = f.read().strip().split('\n')[0]
        else:
            raise ValueError("Poe API key not found (needed for HKBU generation)")
    
    def ask_question(self, question: str) -> Dict:
        """Ask a question and get answer with sources"""
        if self.api_provider == APIProvider.DEMO:
            return self._demo_ask_question(question)
        elif self.api_provider == APIProvider.ZAI:
            return self._zai_ask_question(question)
        elif self.api_provider == APIProvider.POE:
            return self._poe_ask_question(question)
        elif self.api_provider == APIProvider.HKBU:
            return self._hkbu_ask_question(question)
        
        # For standard QA chain (not currently used)
        if not self.qa_chain:
            raise ValueError("QA chain not set up. Call setup_qa_chain() first.")
        
        result = self.qa_chain({"query": question})
        
        sources = []
        if "source_documents" in result:
            for doc in result["source_documents"]:
                source_info = {
                    "content": doc.page_content[:200] + "...",
                    "metadata": doc.metadata
                }
                sources.append(source_info)
        
        response = {
            "question": question,
            "answer": result["result"],
            "sources": sources,
            "timestamp": datetime.now().isoformat()
        }
        
        self.chat_history.append(response)
        self.save_chat_history()  # Save immediately after each Q&A pair
        return response
    
    def _zai_ask_question(self, question: str) -> Dict:
        """Ask question using Z.AI with demo embeddings"""
        from zai import ZaiClient
        from sentence_transformers import SentenceTransformer
        
        try:
            # Check if index is initialized
            if self.index is None:
                raise ValueError("Index not initialized. Please initialize the chatbot first.")
            
            # Use demo embeddings for retrieval - retrieve focused chunks
            model = SentenceTransformer('all-MiniLM-L6-v2')
            query_embedding = model.encode([question])
            D, I = self.index.search(query_embedding.astype('float32'), k=5)  # Reduced to 5 for more focused retrieval
            
            # Get context from retrieved chunks
            context_parts = []
            sources = []
            
            for idx in I[0]:
                if idx < len(self.chunks):
                    chunk = self.chunks[idx]
                    context_parts.append(chunk.page_content)
                    sources.append({
                        "content": chunk.page_content[:500] + "..." if len(chunk.page_content) > 500 else chunk.page_content,
                        "metadata": chunk.metadata
                    })
            
            # Combine context
            context = "\n\n---\n\n".join(context_parts)
            
            # Use Z.AI for generation
            zai_client = ZaiClient(api_key=self.api_key)
            
            # Concise, focused prompt
            prompt = f"""Answer the question based ONLY on the context from the two HTML research papers. Be concise and focused.

Context from papers:
{context[:3000]}

Question: {question}

Instructions:
- Answer directly and concisely using only information from the context
- Focus on the key points from the papers
- Be brief - avoid lengthy explanations
- If information is not in the context, say "This information is not available in the provided papers"

Answer:"""
            
            response = zai_client.chat.completions.create(
                model="glm-4.7",
                messages=[{"role": "user", "content": prompt}]
            )
            
            answer = response.choices[0].message.content
            
            result = {
                "question": question,
                "answer": answer,
                "sources": sources,
                "timestamp": datetime.now().isoformat()
            }
            
            self.chat_history.append(result)
            self.save_chat_history()  # Save immediately after each Q&A pair
            return result
            
        except Exception as e:
            print(f"⚠️  Z.AI error: {e}, falling back to demo mode")
            return self._demo_ask_question(question)
    
    def _poe_ask_question(self, question: str) -> Dict:
        """Ask question using Poe API with demo embeddings"""
        import openai
        from sentence_transformers import SentenceTransformer
        
        try:
            # Check if index is initialized
            if self.index is None:
                raise ValueError("Index not initialized. Please initialize the chatbot first.")
            
            # Use demo embeddings for retrieval - retrieve focused chunks
            model = SentenceTransformer('all-MiniLM-L6-v2')
            query_embedding = model.encode([question])
            D, I = self.index.search(query_embedding.astype('float32'), k=5)  # Reduced to 5 for more focused retrieval
            
            # Get context from retrieved chunks
            context_parts = []
            sources = []
            
            for idx in I[0]:
                if idx < len(self.chunks):
                    chunk = self.chunks[idx]
                    context_parts.append(chunk.page_content)
                    sources.append({
                        "content": chunk.page_content[:500] + "..." if len(chunk.page_content) > 500 else chunk.page_content,
                        "metadata": chunk.metadata
                    })
            
            # Combine context
            context = "\n\n---\n\n".join(context_parts)
            
            # Use Poe API for generation
            client = openai.OpenAI(
                api_key=self.api_key,
                base_url="https://api.poe.com/v1"
            )
            
            # Concise, focused prompt
            prompt = f"""Answer the question based ONLY on the context from the two HTML research papers. Be concise and focused.

Context from papers:
{context[:3000]}

Question: {question}

Instructions:
- Answer directly and concisely using only information from the context
- Focus on the key points from the papers
- Be brief - avoid lengthy explanations
- If information is not in the context, say "This information is not available in the provided papers"

Answer:"""
            
            response = client.chat.completions.create(
                model="Assistant",
                messages=[{"role": "user", "content": prompt}]
            )
            
            answer = response.choices[0].message.content
            
            result = {
                "question": question,
                "answer": answer,
                "sources": sources,
                "timestamp": datetime.now().isoformat()
            }
            
            self.chat_history.append(result)
            self.save_chat_history()  # Save immediately after each Q&A pair
            return result
            
        except Exception as e:
            print(f"⚠️  Poe API error: {e}, falling back to demo mode")
            return self._demo_ask_question(question)
    
    def _hkbu_ask_question(self, question: str) -> Dict:
        """Ask question using HKBU embeddings + Poe API for generation"""
        import openai
        
        try:
            # Check if vector store is initialized
            if self.vector_store is None:
                raise ValueError("Vector store not initialized. Please initialize the chatbot first.")
            
            # Use HKBU vector store retriever - retrieve focused chunks
            retriever = self.vector_store.as_retriever(search_kwargs={"k": 5})  # Reduced to 5 for more focused retrieval
            docs = retriever.get_relevant_documents(question)
            
            # Get context from retrieved chunks
            context_parts = []
            sources = []
            
            for doc in docs:
                context_parts.append(doc.page_content)
                sources.append({
                    "content": doc.page_content[:500] + "..." if len(doc.page_content) > 500 else doc.page_content,
                    "metadata": doc.metadata
                })
            
            # Combine context
            context = "\n\n---\n\n".join(context_parts)
            
            # Use Poe API for generation (hybrid approach)
            client = openai.OpenAI(
                api_key=self.poe_api_key,
                base_url="https://api.poe.com/v1"
            )
            
            # Concise, focused prompt
            prompt = f"""Answer the question based ONLY on the context from the two HTML research papers. Be concise and focused.

Context from papers:
{context[:3000]}

Question: {question}

Instructions:
- Answer directly and concisely using only information from the context
- Focus on the key points from the papers
- Be brief - avoid lengthy explanations
- If information is not in the context, say "This information is not available in the provided papers"

Answer:"""
            
            response = client.chat.completions.create(
                model="Assistant",
                messages=[{"role": "user", "content": prompt}]
            )
            
            answer = response.choices[0].message.content
            
            result = {
                "question": question,
                "answer": answer,
                "sources": sources,
                "timestamp": datetime.now().isoformat()
            }
            
            self.chat_history.append(result)
            self.save_chat_history()  # Save immediately after each Q&A pair
            return result
            
        except Exception as e:
            error_msg = str(e)
            # Don't fall back to demo mode - just return error
            result = {
                "question": question,
                "answer": f"Error: {error_msg}\n\nPlease make sure the chatbot is properly initialized with HKBU embeddings.",
                "sources": [],
                "timestamp": datetime.now().isoformat()
            }
            self.chat_history.append(result)
            self.save_chat_history()  # Save immediately even on error
            return result
    
    def _demo_ask_question(self, question: str) -> Dict:
        """Demo mode: simple keyword-based retrieval"""
        from sentence_transformers import SentenceTransformer
        
        # Check if index is initialized
        if self.index is None:
            return {
                "question": question,
                "answer": "Error: Demo mode index not initialized. Please initialize the chatbot first.",
                "sources": [],
                "timestamp": datetime.now().isoformat()
            }
        
        print(f"\n   🔍 Searching for: '{question}'")
        
        model = SentenceTransformer('all-MiniLM-L6-v2')
        query_embedding = model.encode([question])
        D, I = self.index.search(query_embedding.astype('float32'), k=5)  # Reduced to 5 for more focused retrieval
        
        sources = []
        context_parts = []
        
        for i, idx in enumerate(I[0]):
            if idx < len(self.chunks):
                chunk = self.chunks[idx]
                context_parts.append(chunk.page_content)
                sources.append({
                    "content": chunk.page_content[:500] + "..." if len(chunk.page_content) > 500 else chunk.page_content,
                    "metadata": chunk.metadata
                })
        
        # Use focused context
        context = "\n\n---\n\n".join(context_parts[:5]) if context_parts else "No relevant information found."
        
        answer = f"""Based on the papers:

{context[:2500]}

Note: This is demo mode. For full RAG capabilities, use an API provider (poe, zai, or hkbu)."""
        
        response = {
            "question": question,
            "answer": answer,
            "sources": sources,
            "timestamp": datetime.now().isoformat()
        }
        
        self.chat_history.append(response)
        self.save_chat_history()  # Save immediately after each Q&A pair
        return response
    
    def save_chat_history(self) -> None:
        """Save chat history to a JSON file in the literature folder"""
        try:
            # Ensure the folder exists
            self.literature_folder.mkdir(parents=True, exist_ok=True)
            
            chat_history_path = self.literature_folder / "chat_history.json"
            
            with open(chat_history_path, 'w', encoding='utf-8') as f:
                json.dump(self.chat_history, f, indent=2, ensure_ascii=False)
            
            print(f"✓ Chat history saved to {chat_history_path}")
        except Exception as e:
            print(f"⚠️  Warning: Could not save chat history: {e}")
    
    def print_response(self, response: Dict) -> None:
        """Print the response in a readable format"""
        print("\n" + "="*70)
        print(f"❓ Question: {response['question']}")
        print("="*70)
        print(f"\n💡 Answer:\n{response['answer']}")
        
        if response['sources']:
            print(f"\n📚 Sources ({len(response['sources'])}):")
            for i, source in enumerate(response['sources'], 1):
                source_path = source['metadata'].get('source', 'Unknown')
                if isinstance(source_path, str):
                    source_name = Path(source_path).name
                else:
                    source_name = str(source_path)
                print(f"\n  {i}. {source_name}")
                print(f"     {source['content']}")
        
        print("\n" + "="*70 + "\n")
    
    def initialize(self) -> None:
        """Complete initialization: load documents, create vector store, setup QA"""
        print("🚀 Initializing RAG Chatbot...\n")
        
        documents = self.load_documents()
        if not documents:
            return
        
        chunks = self.split_documents(documents)
        self.create_vector_store(chunks)
        self.setup_qa_chain()
        
        print("\n✅ RAG Chatbot is ready! Ask your questions about the literature.\n")


def main():
    """Main function to run the chatbot interactively"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='RAG Literature Chatbot with multiple API backends',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Supported API providers:
  poe   - Poe API (recommended, OpenAI-compatible)
  zai   - Z.AI API (requires balance)
  hkbu  - HKBU Gen AI (Azure OpenAI)
  demo  - Local embeddings (no API required)

Examples:
  python rag_chatbot.py literature/HXChen --api poe
  python rag_chatbot.py literature/HXChen --api demo
        """
    )
    parser.add_argument('literature_folder', help='Path to literature folder')
    parser.add_argument('--api', '--provider', dest='provider', default='poe',
                       choices=['poe', 'zai', 'hkbu', 'demo'],
                       help='API provider to use (default: poe)')
    
    args = parser.parse_args()
    
    # Initialize chatbot
    chatbot = RAGChatbot(args.literature_folder, api_provider=args.provider)
    chatbot.initialize()
    
    print("\n" + "="*70)
    print("🎓 RAG Literature Chatbot")
    print(f"Provider: {chatbot.api_provider.value.upper()}")
    print("Type your questions about the literature below.")
    print("Type 'quit', 'exit', or press Ctrl+C to stop.")
    print("="*70 + "\n")
    
    # Interactive loop
    try:
        while True:
            question = input("❓ Your question: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                break
            
            if not question:
                continue
            
            # Ask question and display response
            response = chatbot.ask_question(question)
            chatbot.print_response(response)
    
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    
    # Save chat history before exiting
    if chatbot.chat_history:
        chatbot.save_chat_history()


if __name__ == "__main__":
    main()
