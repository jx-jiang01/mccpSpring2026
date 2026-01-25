#!/usr/bin/env python3
"""
Test script for HKBU API key
"""

import sys
from pathlib import Path

# Read API key from HKBUAPIkey.md
API_KEY_PATH = Path(__file__).parent.parent.parent / "LLM" / "HKBUAPIkey.md"

try:
    from langchain_openai import AzureOpenAIEmbeddings
    from langchain_community.chat_models import AzureChatOpenAI
    
    # Read API key
    with open(API_KEY_PATH, 'r') as f:
        content = f.read().strip()
        lines = content.split('\n')
        api_key = lines[0]
    
    print(f"🔑 API Key: {api_key[:20]}...")
    print(f"📁 Key file: {API_KEY_PATH}")
    print()
    
    # Test embeddings
    print("🧪 Testing HKBU Azure OpenAI Embeddings...")
    try:
        embeddings = AzureOpenAIEmbeddings(
            azure_endpoint="https://hkbu-genai.openai.azure.com/",
            api_key=api_key,
            api_version="2024-02-15-preview",
            deployment="text-embedding-ada-002"
        )
        
        test_text = "This is a test sentence for embeddings."
        result = embeddings.embed_query(test_text)
        
        print(f"✓ Embeddings API working!")
        print(f"  - Embedding dimension: {len(result)}")
        print(f"  - First 5 values: {result[:5]}")
        
    except Exception as e:
        print(f"❌ Error with embeddings: {e}")
        print(f"  Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
    
    print()
    
    # Test chat completion
    print("💬 Testing HKBU Azure OpenAI Chat...")
    try:
        llm = AzureChatOpenAI(
            openai_api_key=api_key,
            azure_endpoint="https://hkbu-genai.openai.azure.com/",
            api_version="2024-02-15-preview",
            deployment_name="gpt-4o-mini"
        )
        
        response = llm.invoke("Say 'API test successful' if you can read this.")
        print(f"✓ Chat API working!")
        print(f"  - Response: {response.content}")
        
    except Exception as e:
        print(f"❌ Error with chat: {e}")
        print(f"  Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
    
    print()
    
    # Check if there's a link in the file
    print("🔗 Links found in API key file:")
    for i, line in enumerate(lines[1:], 1):
        if line.strip() and (line.startswith('http://') or line.startswith('https://')):
            print(f"  {i}. {line.strip()}")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("   Install: pip install langchain-openai langchain-community")
    sys.exit(1)
except FileNotFoundError:
    print(f"❌ API key file not found: {API_KEY_PATH}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
