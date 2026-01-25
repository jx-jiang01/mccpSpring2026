# RAG Chatbot Web UI

A beautiful web-based interface for the RAG Literature Chatbot using Streamlit.

## Features

- 🎨 **Modern Web Interface** - Clean, responsive design
- 💬 **Chat Interface** - Easy-to-use chat interface
- 📚 **Source Citations** - Expandable source references
- ⚙️ **Easy Configuration** - Sidebar configuration panel
- 💾 **Export Chat History** - Download conversations as JSON
- 🎯 **Multiple API Support** - Switch between Poe, HKBU, Z.AI, and Demo

## Installation

```bash
cd "writing/activity 1.5 build a chatbot"
pip install -r requirements.txt
```

## Running the Web UI

```bash
streamlit run rag_chatbot_ui.py
```

The web interface will open automatically in your browser at `http://localhost:8501`

## Usage

1. **Select Literature Folder** - Choose a folder from the sidebar (or enter a path)
2. **Choose API Provider** - Select Poe, HKBU, Z.AI, or Demo mode
3. **Initialize** - Click "Initialize Chatbot" button
4. **Ask Questions** - Type your questions in the chat input at the bottom
5. **View Sources** - Expand the "Sources" section to see where answers came from
6. **Export History** - Download chat history as JSON file

## Screenshots

The UI includes:
- Clean chat interface with user and assistant messages
- Color-coded message bubbles
- Expandable source citations
- Sidebar configuration panel
- Export functionality

## Keyboard Shortcuts

- Press Enter to send a message
- Use the sidebar to configure settings
- Click "Clear Chat History" to reset

## Troubleshooting

**Port already in use:**
```bash
streamlit run rag_chatbot_ui.py --server.port 8502
```

**UI not loading:**
- Make sure Streamlit is installed: `pip install streamlit`
- Check that all dependencies are installed: `pip install -r requirements.txt`

## Features in Detail

### Chat Interface
- User messages appear in blue bubbles
- Assistant messages appear in green bubbles
- Sources are expandable and show document references

### Configuration Panel
- Literature folder selector (auto-detects folders)
- API provider dropdown
- Initialize button with status indicator
- Clear chat and export buttons

### Chat History
- Persistent during session
- Exportable as JSON
- Automatically saved to literature folder
