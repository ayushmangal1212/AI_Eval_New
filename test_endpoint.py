"""
Test the /api/generate-questions endpoint - Check actual response
"""

import requests

print("=" * 60)
print("Testing /api/generate-questions endpoint")
print("=" * 60)
print()

test_data = {
    "role": "Python Developer",
    "skills": ["Python", "Django", "Flask"],
    "language": "English"
}

try:
    response = requests.post(
        'http://localhost:5000/api/generate-questions',
        json=test_data,
        timeout=10
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-Type', 'Not set')}")
    print()
    print("Raw Response (first 500 chars):")
    print("-" * 60)
    print(response.text[:500])
    print("-" * 60)
    print()
    
    if "login" in response.text.lower() or "redirect" in response.text.lower():
        print("FOUND THE PROBLEM!")
        print("The endpoint is redirecting to the login page.")
        print("This means the @login_required decorator is blocking access.")
        print()
        print("SOLUTION:")
        print("The browser needs to be logged in with a valid session.")
        print("The test script doesn't have a session cookie.")
    
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {str(e)}")

print("=" * 60)
