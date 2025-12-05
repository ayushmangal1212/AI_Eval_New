"""
Test DeepSeek API Key
This script tests if the DeepSeek API key is valid and working
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API credentials
api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
model = os.getenv("DEEPSEEK_MODEL", "deepseek-reasoner")

print("=" * 60)
print("DeepSeek API Key Test")
print("=" * 60)

# Check if API key exists
if not api_key:
    print("ERROR: DEEPSEEK_API_KEY not found in .env file!")
    print("\nPlease add your API key to the .env file:")
    print("DEEPSEEK_API_KEY=sk-your-api-key-here")
    exit(1)

print(f"API Key found: {api_key[:10]}...{api_key[-4:]}")
print(f"Base URL: {base_url}")
print(f"Model: {model}")
print()

# Test API connection
print("Testing API connection...")
print()

try:
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage
    
    # Initialize LLM
    llm = ChatOpenAI(
        model=model,
        api_key=api_key,
        base_url=base_url,
        temperature=0.7
    )
    
    print("LLM initialized successfully")
    print()
    
    # Test with a simple question
    print("Sending test message to API...")
    test_message = "Say 'Hello, API is working!' if you can read this."
    
    response = llm.invoke([HumanMessage(content=test_message)])
    
    print("API Response received!")
    print()
    print("Response:")
    print("-" * 60)
    print(response.content)
    print("-" * 60)
    print()
    print("SUCCESS! Your DeepSeek API key is working correctly!")
    print()
    
except Exception as e:
    print("ERROR: API test failed!")
    print()
    print("Error details:")
    print("-" * 60)
    print(str(e))
    print("-" * 60)
    print()
    print("Possible issues:")
    print("1. Invalid API key")
    print("2. Network connection problem")
    print("3. API service is down")
    print("4. Incorrect base URL or model name")
    print()
    print("Please check your .env file and try again.")
    exit(1)

print("=" * 60)
