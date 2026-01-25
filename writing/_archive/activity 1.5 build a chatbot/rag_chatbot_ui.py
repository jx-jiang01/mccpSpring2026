#!/usr/bin/env python3
"""
RAG Chatbot Web UI using Streamlit
Nice graphical interface for the RAG Literature Chatbot
"""

import streamlit as st
import sys
from pathlib import Path
import json
from datetime import datetime

# Add parent directory to path to import rag_chatbot
sys.path.insert(0, str(Path(__file__).parent))

from rag_chatbot import RAGChatbot, APIProvider

# Page configuration
st.set_page_config(
    page_title="RAG Literature Chatbot",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid;
    }
    .user-message {
        background-color: #e3f2fd;
        border-color: #2196f3;
    }
    .assistant-message {
        background-color: #f1f8e9;
        border-color: #8bc34a;
    }
    .source-box {
        background-color: #f5f5f5;
        padding: 0.75rem;
        border-radius: 0.5rem;
        margin-top: 0.5rem;
        font-size: 0.9rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'initialized' not in st.session_state:
    st.session_state.initialized = False

# Sidebar for configuration
with st.sidebar:
    st.title("⚙️ Configuration")
    
    # Literature folder selection
    base_path = Path(__file__).parent.parent.parent
    literature_base = base_path / "literature"
    
    if literature_base.exists():
        folders = [f.name for f in literature_base.iterdir() if f.is_dir()]
        if folders:
            selected_folder = st.selectbox(
                "📂 Literature Folder",
                folders,
                index=0 if "HXChen" in folders else 0
            )
            literature_folder = str(literature_base / selected_folder)
        else:
            st.error("No literature folders found!")
            st.stop()
    else:
        literature_folder = st.text_input(
            "📂 Literature Folder Path",
            value="literature/HXChen",
            help="Path to folder containing HTML files"
        )
    
    # API provider selection
    api_provider = st.selectbox(
        "🔌 API Provider",
        ["poe", "hkbu", "zai", "demo"],
        index=1,  # Default to HKBU
        help="Select API provider for embeddings and generation"
    )
    
    # Initialize button
    if st.button("🚀 Initialize Chatbot", type="primary"):
        with st.spinner("Initializing RAG chatbot..."):
            try:
                st.session_state.chatbot = RAGChatbot(
                    literature_folder=literature_folder,
                    api_provider=api_provider
                )
                st.session_state.chatbot.initialize()
                st.session_state.initialized = True
                st.session_state.chat_history = []
                st.success(f"✅ Chatbot initialized with {api_provider.upper()}!")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error initializing chatbot: {e}")
                st.session_state.initialized = False
    
    st.markdown("---")
    
    # Status
    if st.session_state.initialized:
        st.success("✅ Ready")
        st.info(f"**Provider:** {api_provider.upper()}\n**Folder:** {Path(literature_folder).name}")
    else:
        st.warning("⚠️ Not initialized")
    
    st.markdown("---")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        if st.session_state.chatbot:
            st.session_state.chatbot.chat_history = []
        st.rerun()
    
    # Export chat history
    if st.session_state.chat_history:
        chat_json = json.dumps(st.session_state.chat_history, indent=2, ensure_ascii=False)
        st.download_button(
            label="💾 Download Chat History",
            data=chat_json,
            file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )

# Main content
st.markdown('<div class="main-header">📚 RAG Literature Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Ask questions about your literature using RAG (Retrieval-Augmented Generation)</div>', unsafe_allow_html=True)

# Chat interface
if not st.session_state.initialized:
    st.info("👈 Please configure and initialize the chatbot in the sidebar to get started.")
    st.markdown("""
    ### How to use:
    1. Select a literature folder from the sidebar
    2. Choose an API provider (Poe, HKBU, Z.AI, or Demo)
    3. Click "Initialize Chatbot" to start
    4. Ask questions about your literature!
    """)
else:
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for i, chat in enumerate(st.session_state.chat_history):
            # User message
            st.markdown(f'<div class="chat-message user-message"><strong>❓ You:</strong><br>{chat["question"]}</div>', unsafe_allow_html=True)
            
            # Assistant message
            st.markdown(f'<div class="chat-message assistant-message"><strong>💡 Assistant:</strong><br>{chat["answer"]}</div>', unsafe_allow_html=True)
            
            # Sources
            if chat.get("sources"):
                with st.expander(f"📚 Sources ({len(chat['sources'])})", expanded=False):
                    for j, source in enumerate(chat["sources"], 1):
                        source_name = Path(source["metadata"].get("source", "Unknown")).name
                        st.markdown(f"**{j}. {source_name}**")
                        st.markdown(f'<div class="source-box">{source["content"]}</div>', unsafe_allow_html=True)
                        st.markdown("---")
            
            st.markdown("---")
    
    # Chat input
    user_question = st.chat_input("Ask a question about the literature...")
    
    if user_question:
        # Add user question to history
        st.session_state.chat_history.append({
            "question": user_question,
            "answer": "",
            "sources": [],
            "timestamp": datetime.now().isoformat()
        })
        
        # Get response from chatbot
        with st.spinner("🤔 Thinking..."):
            try:
                response = st.session_state.chatbot.ask_question(user_question)
                
                # Update the last chat entry
                st.session_state.chat_history[-1] = {
                    "question": response["question"],
                    "answer": response["answer"],
                    "sources": response["sources"],
                    "timestamp": response["timestamp"]
                }
                
                # Sync chatbot's history with UI state (chatbot already saved via ask_question)
                if st.session_state.chatbot:
                    st.session_state.chatbot.chat_history = st.session_state.chat_history
                
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.session_state.chat_history[-1]["answer"] = f"Error: {e}"

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; font-size: 0.9rem;'>"
    "📚 RAG Literature Chatbot | Built with Streamlit | "
    "Uses HKBU GenAI, Poe API, Z.AI, or Demo Mode"
    "</div>",
    unsafe_allow_html=True
)
