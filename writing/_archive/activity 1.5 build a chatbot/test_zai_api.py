#!/usr/bin/env python3
"""
Test script for Z.AI API key
"""

import sys
from pathlib import Path

# Read API key from zai.md
API_KEY_PATH = Path(__file__).parent.parent.parent / "LLM" / "zai.md"

try:
    from zai import ZaiClient
    
    # Read API key
    with open(API_KEY_PATH, 'r') as f:
        api_key = f.read().strip().split('\n')[0]
    
    print(f"🔑 API Key: {api_key[:20]}...")
    print(f"📁 Key file: {API_KEY_PATH}")
    print()
    
    # Initialize Z.AI client
    print("🚀 Initializing Z.AI client...")
    client = ZaiClient(api_key=api_key)
    print("✓ Client initialized successfully")
    print()
    
    # Test with a simple chat completion
    print("💬 Testing API with a simple message...")
    try:
        response = client.chat.completions.create(
            model='glm-4.7',  # Z.AI model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello! Please respond with 'API test successful' if you can read this."}
            ]
        )
        
        result = response.choices[0].message.content
        print("✓ API call successful!")
        print()
        print("📝 Response:")
        print("-" * 70)
        print(result)
        print("-" * 70)
        print()
        print("✅ Z.AI API key is working correctly!")
        
    except Exception as e:
        print(f"❌ Error calling API: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
        
except ImportError:
    print("❌ zai-sdk not installed. Run: pip install zai-sdk")
    sys.exit(1)
except FileNotFoundError:
    print(f"❌ API key file not found: {API_KEY_PATH}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
