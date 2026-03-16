import json
import urllib.request
import urllib.error

PISTON_URL = "http://localhost:2000/api/v2/execute"

def test_piston():
    payload = {
        "language": "python",
        "version": "3.10.0",
        "files": [{"content": "print('Hello, Piston!')"}],
        "stdin": ""
    }
    
    req = urllib.request.Request(
        PISTON_URL,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(json.dumps(result, indent=2))
    except urllib.error.URLError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_piston()
