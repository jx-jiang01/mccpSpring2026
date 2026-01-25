# RAG Literature Chatbot

A RAG (Retrieval-Augmented Generation) chatbot that answers questions about literature folders using multiple API backends:

- 🟢 **Poe API** (recommended, working)
- 🟡 **Z.AI API** (valid key, requires balance)
- 🔵 **HKBU Gen AI** (Azure OpenAI)
- ⚪ **Demo Mode** (local embeddings, no API required)

## Features

- 🔍 **Document Ingestion**: Loads HTML documents from literature folders
- 💾 **Vector Storage**: Creates semantic search index using FAISS
- 🤖 **RAG Implementation**: Retrieves relevant context and generates accurate answers
- 💬 **Chat History**: Saves conversations to the same folder as documents
- 📚 **Source References**: Provides citations for each answer
- 🔄 **Multiple API Support**: Switch between different API providers easily

## Setup

### 1. Install Dependencies

```bash
cd "writing/activity 1.5 build a chatbot"
pip install -r requirements.txt
```

### 2. API Keys Configuration

API keys are stored in `LLM/` folder:
- `LLM/poe.md` - Poe API key (recommended)
- `LLM/zai.md` - Z.AI API key
- `LLM/HKBUAPIkey.md` - HKBU Gen AI API key

The chatbot automatically reads the appropriate key based on the selected provider.

### 3. Folder Structure

Ensure your literature folder contains HTML files:
```
literature/
└── HXChen/
    ├── EchoWorld_ Learning Motion-Aware World Models for Echocardiography Probe Guidance.html
    └── Goal-conditioned reinforcement learning for ultrasound navigation guidance.html
```

## Usage

### Running the Chatbot

**With Poe API (recommended):**
```bash
python rag_chatbot.py literature/HXChen --api poe
```

**With Z.AI API:**
```bash
python rag_chatbot.py literature/HXChen --api zai
```

**With HKBU Gen AI:**
```bash
python rag_chatbot.py literature/HXChen --api hkbu
```

**Demo Mode (no API required):**
```bash
python rag_chatbot.py literature/HXChen --api demo
```

### Command-Line Options

```bash
python rag_chatbot.py <literature_folder> --api <provider>

Options:
  --api, --provider   API provider to use (default: poe)
                      Choices: poe, zai, hkbu, demo
```

### Example Session (Poe API)

```
✓ RAG Chatbot initialized for: HXChen (Provider: POE)
🚀 Initializing RAG Chatbot...

📂 Loading documents from HXChen...
   - Loading: EchoWorld_ Learning Motion-Aware World Models...
   - Loading: Goal-conditioned reinforcement learning...
✓ Loaded 2 document(s)

🔄 Splitting documents into chunks...
✓ Created 217 chunks

💾 Creating vector store (POE)...
⚠️  Poe API doesn't support embeddings, using local embeddings...
✓ Demo vector store created with local embeddings

🔗 Setting up QA chain (POE)...
✓ Poe QA chain ready (local embeddings + Poe generation)

✅ RAG Chatbot is ready! Ask your questions about the literature.

======================================================================
🎓 RAG Literature Chatbot
Provider: POE
Type your questions about the literature below.
Type 'quit', 'exit', or press Ctrl+C to stop.
======================================================================

❓ Your question: What is EchoWorld?

======================================================================
❓ Question: What is EchoWorld?
======================================================================

💡 Answer:
**EchoWorld** is a **world model** that is **pre-trained from scratch** by **jointly learning spatial and motion dynamics**. It uses a **ViT-S/16 context encoder**, with a **target encoder implemented as an exponential moving average (EMA)** of the context encoder...

📚 Sources (3):

  1. EchoWorld_ Learning Motion-Aware World Models...
     5.1 EchoWorld as a World Model...

  2. EchoWorld_ Learning Motion-Aware World Models...
     Architecture and optimization. EchoWorld is pre-trained from scratch...

======================================================================

❓ Your question: quit

👋 Goodbye!
✓ Chat history saved to literature/HXChen/chat_history.json
```

## API Providers

### 🟢 Poe API (Recommended)

**Status:** ✅ Working

**Features:**
- OpenAI-compatible API
- Fast response times
- Good quality responses
- Has active balance

**Configuration:**
- API key stored in `LLM/poe.md`
- Uses local embeddings (Poe doesn't support embeddings API)
- Uses Poe API for text generation

**Usage:**
```bash
python rag_chatbot.py literature/HXChen --api poe
```

### 🟡 Z.AI API

**Status:** ⚠️ Valid key but requires balance

**Features:**
- GLM-4.7 model
- Good for Chinese/English tasks
- Requires account balance

**Configuration:**
- API key stored in `LLM/zai.md`
- Uses local embeddings + Z.AI for generation

**Usage:**
```bash
python rag_chatbot.py literature/HXChen --api zai
```

**Note:** If you get a balance error, recharge your Z.AI account or use Poe API instead.

### 🔵 HKBU Gen AI (Azure OpenAI)

**Status:** ⚠️ Connection issues (may require VPN)

**Features:**
- Full LangChain integration
- Azure OpenAI embeddings and chat
- Requires network access to HKBU endpoint

**Configuration:**
- API key stored in `LLM/HKBUAPIkey.md`
- Uses Azure OpenAI for both embeddings and generation

**Usage:**
```bash
python rag_chatbot.py literature/HXChen --api hkbu
```

### ⚪ Demo Mode

**Status:** ✅ Always available

**Features:**
- Works offline after initial model download
- No API keys required
- Local sentence-transformers embeddings
- Basic context retrieval (no LLM generation)

**Usage:**
```bash
python rag_chatbot.py literature/HXChen --api demo
```

**Note:** Demo mode provides semantic search with context retrieval but uses simple text formatting instead of LLM-generated answers.

## Output Files

After running the chatbot, these files will be created in your literature folder:

### 1. `chat_history.json`
- JSON file containing all questions, answers, and sources
- Format:
```json
[
  {
    "question": "What is EchoWorld?",
    "answer": "...",
    "sources": [
      {
        "content": "...",
        "metadata": {
          "source": "path/to/file.html",
          "title": "Paper Title"
        }
      }
    ],
    "timestamp": "2026-01-11T..."
  }
]
```

### 2. `vector_store_*/` (for API modes)
- FAISS index folder (if using API embeddings)
- Can be reused in future sessions

## How It Works

### Architecture

1. **Document Loading**: Parses HTML files and extracts text content
2. **Chunking**: Splits documents into 1000-character chunks with 200-character overlap
3. **Embedding**:
   - **Poe/Z.AI**: Uses local sentence-transformers (Poe/Z.AI don't support embeddings API)
   - **HKBU**: Uses Azure OpenAI text-embedding-ada-002
   - **Demo**: Uses local sentence-transformers
4. **Vector Store**: Stores embeddings in FAISS for fast similarity search
5. **Retrieval**: When you ask a question, finds the most relevant document chunks (top 3-4)
6. **Generation**:
   - **Poe**: Uses Poe API (Assistant model) for answer generation
   - **Z.AI**: Uses Z.AI API (GLM-4.7) for answer generation
   - **HKBU**: Uses Azure OpenAI (GPT-4o-mini) for answer generation
   - **Demo**: Returns formatted context without LLM generation

### Hybrid Approach (Poe/Z.AI)

Since Poe and Z.AI APIs don't support embeddings endpoints, the chatbot uses:
- **Local embeddings** (sentence-transformers) for semantic search
- **API generation** (Poe/Z.AI) for high-quality answer generation

This hybrid approach provides the best of both worlds:
- Fast, reliable semantic search
- High-quality LLM-generated answers

## Troubleshooting

### API Connection Issues

**Poe API:**
- Ensure API key is correct in `LLM/poe.md`
- Check network connectivity

**Z.AI API:**
- If you see "Insufficient balance" error, recharge your account
- API key is valid but account needs credits

**HKBU Gen AI:**
- May require VPN or network access to `https://hkbu-genai.openai.azure.com/`
- Check if endpoint is accessible from your network

### Empty Literature Folder
- Ensure the folder contains HTML files
- Check file permissions

### Memory Issues
- If processing large documents, reduce `chunk_size` in `split_documents()`
- Close other applications to free up memory

### Model Download (First Run)
First run in any mode using local embeddings will download ~120MB model file. This only happens once.

### sentence-transformers Import Error

If you see:
```
ImportError: cannot import name 'cached_download' from 'huggingface_hub'
```

**Solution:**
```bash
pip install --upgrade sentence-transformers
```

## Performance

### Embedding Creation
- **Local (Poe/Z.AI/Demo)**: ~2-3 seconds per 100 chunks (first run slower due to model loading)
- **HKBU (Azure)**: ~1-2 seconds per 10 chunks (network-dependent)

### Question Answering
- **Poe API**: ~3-5 seconds per question
- **Z.AI API**: ~3-5 seconds per question
- **HKBU**: ~3-5 seconds per question (network-dependent)
- **Demo Mode**: ~1-2 seconds per question

## Customization

You can modify these parameters in `rag_chatbot.py`:

```python
# Chunking parameters
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # Adjust for larger/smaller chunks
    chunk_overlap=200,    # Adjust for more/less context overlap
)

# Retrieval parameters
k=3  # Number of document chunks to retrieve
```

## Testing

### Quick Test with Poe API

```bash
echo -e "What is EchoWorld?\nexit" | python3 rag_chatbot.py literature/HXChen --api poe
```

### Quick Test with Demo Mode

```bash
echo -e "What is EchoWorld?\nexit" | python3 rag_chatbot.py literature/HXChen --api demo
```

## API Provider Comparison

| Provider | Embeddings | Generation | Status | Notes |
|----------|-----------|------------|--------|-------|
| Poe | Local | Poe API | ✅ Working | Recommended |
| Z.AI | Local | Z.AI API | ⚠️ Needs Balance | Valid key |
| HKBU | Azure OpenAI | Azure OpenAI | ⚠️ Connection | May need VPN |
| Demo | Local | None | ✅ Always Available | Offline mode |

## License

Educational use for MCCP 6020 course.
