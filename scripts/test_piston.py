import httpx
import json

def test_piston():
    url = "http://localhost:2000/api/v2/execute"
    
    # Simple Python Hello World
    payload = {
        "language": "python",
        "version": "*",
        "files": [
            {
                "content": "print('Hello from Piston!')\nimport sys\nprint(f'Python version: {sys.version}')"
            }
        ]
    }

    print(f"Connecting to Piston at {url}...")
    try:
        response = httpx.post(url, json=payload, timeout=10.0)
        
        if response.status_code == 404:
            print("❌ Error: Language 'python' not found.")
            print("💡 Hint: You need to install the python package first. Run:")
            print("   curl -X POST http://localhost:2000/api/v2/packages -H 'Content-Type: application/json' -d '{\"language\": \"python\", \"version\": \"3.10.0\"}'")
            return

        if response.status_code == 400:
            print(f"❌ Piston Error (400): {response.json().get('message')}")
            return
        
        response.raise_for_status()
        data = response.json()
        
        run = data.get("run", {})
        stdout = run.get("stdout", "").strip()
        stderr = run.get("stderr", "").strip()
        code = run.get("code")

        print("\n--- Execution Result ---")
        if code == 0:
            print(f"✅ Success (Exit Code: {code})")
            print(f"Output:\n{stdout}")
        else:
            print(f"❌ Failed (Exit Code: {code})")
            print(f"Error:\n{stderr}")

    except httpx.ConnectError:
        print("❌ Error: Could not connect to Piston. Is the Docker container running?")
        print("💡 Hint: cd piston && docker compose up -d")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    test_piston()
