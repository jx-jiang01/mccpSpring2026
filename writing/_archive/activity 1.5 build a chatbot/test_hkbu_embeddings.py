#!/usr/bin/env python3
"""
Test HKBU API key for embeddings using the correct endpoint
Based on: https://genai.hkbu.edu.hk/general/specification/embeddings-swagger?fullscreen=true
"""

import sys
import json
from pathlib import Path
import requests

# Read API key from HKBUAPIkey.md
API_KEY_PATH = Path(__file__).parent.parent.parent / "LLM" / "HKBUAPIkey.md"

# HKBU API Configuration (from Swagger documentation)
BASE_URL = "https://genai.hkbu.edu.hk/api/v0/rest"
API_VERSION = "2023-12-01-preview"  # Default version
MODEL_DEPLOYMENT = "text-embedding-3-small"  # Available: text-embedding-3-small, text-embedding-3-large

def test_hkbu_embeddings():
    """Test HKBU embeddings API"""
    
    # Read API key
    try:
        with open(API_KEY_PATH, 'r') as f:
            content = f.read().strip()
            lines = content.split('\n')
            api_key = lines[0].strip()
    except FileNotFoundError:
        print(f"❌ API key file not found: {API_KEY_PATH}")
        return False
    
    print(f"🔑 API Key: {api_key[:20]}...")
    print(f"📁 Key file: {API_KEY_PATH}")
    print()
    
    # Construct the endpoint URL
    endpoint = f"{BASE_URL}/openai/deployments/{MODEL_DEPLOYMENT}/embeddings"
    url = f"{endpoint}?api-version={API_VERSION}"
    
    print(f"🌐 Testing HKBU Embeddings API...")
    print(f"   Base URL: {BASE_URL}")
    print(f"   Endpoint: {endpoint}")
    print(f"   Model: {MODEL_DEPLOYMENT}")
    print(f"   API Version: {API_VERSION}")
    print()
    
    # Prepare payload
    payload = {
        "input": "This is a test sentence for embeddings."
    }
    
    print(f"📤 Sending request...")
    print(f"   Request body: {json.dumps(payload, indent=2)}")
    print()
    
    # Try different authentication formats
    auth_formats = [
        ("Bearer", {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}),
        ("api-key", {"api-key": api_key, "Content-Type": "application/json"}),
        ("x-api-key", {"x-api-key": api_key, "Content-Type": "application/json"}),
        ("Authorization api-key", {"Authorization": f"api-key {api_key}", "Content-Type": "application/json"}),
    ]
    
    for auth_name, headers in auth_formats:
        print(f"🔐 Trying authentication: {auth_name}")
        print(f"   Headers: {list(headers.keys())}")
        
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=30
            )
            
            print(f"   Response Status: {response.status_code}")
            
            if response.status_code == 200:
                # Success!
                result = response.json()
                if "data" in result and len(result["data"]) > 0:
                    embedding = result["data"][0]["embedding"]
                    print(f"✅ Success with authentication: {auth_name}!")
                    print(f"   Embedding dimension: {len(embedding)}")
                    print(f"   First 5 values: {embedding[:5]}")
                    print()
                    return True
                else:
                    print(f"⚠️  Response received but no embedding data found")
            elif response.status_code == 401:
                print(f"   ❌ Unauthorized (401)")
            else:
                print(f"   ⚠️  Status {response.status_code}")
                try:
                    error_detail = response.json()
                    print(f"   Response: {json.dumps(error_detail, indent=2)[:200]}")
                except:
                    print(f"   Response text: {response.text[:200]}")
        
        except requests.exceptions.ConnectionError as e:
            print(f"   ❌ Connection Error: {e}")
            print(f"   Unable to connect to {BASE_URL}")
            return False
        except requests.exceptions.Timeout as e:
            print(f"   ❌ Timeout Error: {e}")
            return False
        except Exception as e:
            print(f"   ❌ Error: {type(e).__name__}: {e}")
        
        print()
    
    # Final summary
    print(f"❌ All authentication formats failed")
    print()
    print(f"💡 Possible issues:")
    print(f"   1. API key might be invalid or expired")
    print(f"   2. API key might need to be obtained from: https://genai.hkbu.edu.hk/settings/api-docs")
    print(f"   3. API key might be for a different service/endpoint")
    print(f"   4. Authentication method might be different (check Swagger docs)")
    
    return False


if __name__ == "__main__":
    print("=" * 70)
    print("🧪 HKBU Embeddings API Test")
    print("=" * 70)
    print()
    
    success = test_hkbu_embeddings()
    
    print("=" * 70)
    if success:
        print("✅ Test PASSED - HKBU API key is working for embeddings!")
    else:
        print("❌ Test FAILED - HKBU API key is not working")
        print("   Check the API key or authentication method")
    print("=" * 70)
    
    sys.exit(0 if success else 1)
