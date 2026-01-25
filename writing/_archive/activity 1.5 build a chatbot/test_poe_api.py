#!/usr/bin/env python3
"""
Test script for Poe API key
"""

import sys
from pathlib import Path

# Read API key from poe.md
API_KEY_PATH = Path(__file__).parent.parent.parent / "LLM" / "poe.md"

try:
    import openai
    
    # Read API key
    with open(API_KEY_PATH, 'r') as f:
        api_key = f.read().strip().split('\n')[0]
    
    print(f"🔑 API Key: {api_key[:20]}...")
    print(f"📁 Key file: {API_KEY_PATH}")
    print()
    
    # Initialize OpenAI client with Poe endpoint
    print("🚀 Initializing Poe API client...")
    client = openai.OpenAI(
        api_key=api_key,
        base_url="https://api.poe.com/v1"
    )
    print("✓ Client initialized successfully")
    print()
    
    # Test with a simple chat completion
    print("💬 Testing API with a simple message...")
    try:
        response = client.chat.completions.create(
            model="Assistant",  # Poe model name
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
        print("✅ Poe API key is working correctly!")
        
    except Exception as e:
        print(f"❌ Error calling API: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
        
except ImportError:
    print("❌ openai package not installed. Run: pip install openai")
    sys.exit(1)
except FileNotFoundError:
    print(f"❌ API key file not found: {API_KEY_PATH}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
