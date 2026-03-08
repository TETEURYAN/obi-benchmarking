import httpx
import time
import sys

PISTON_URL = "http://localhost:2000/api/v2"
REQUIRED_LANGUAGES = [
    {"language": "python", "version": "3.10.0"},
    # Add more languages here as needed
]

def wait_for_piston(retries=10):
    for i in range(retries):
        try:
            response = httpx.get(f"{PISTON_URL}/runtimes")
            if response.status_code == 200:
                print("✅ Piston is online.")
                return True
        except Exception:
            pass
        print(f"Waiting for Piston... ({i+1}/{retries})")
        time.sleep(2)
    return False

def install_languages():
    # Get currently installed runtimes
    try:
        response = httpx.get(f"{PISTON_URL}/runtimes")
        installed = response.json()
        installed_names = [r["language"] for r in installed]
    except Exception as e:
        print(f"❌ Could not fetch runtimes: {e}")
        return

    for lang_info in REQUIRED_LANGUAGES:
        lang = lang_info["language"]
        if lang in installed_names:
            print(f"✅ {lang} is already installed.")
            continue
        
        print(f"Installing {lang}...")
        try:
            resp = httpx.post(f"{PISTON_URL}/packages", json=lang_info)
            if resp.status_code == 200:
                print(f"✅ Successfully installed {lang}.")
            else:
                print(f"❌ Failed to install {lang}: {resp.text}")
        except Exception as e:
            print(f"❌ Error installing {lang}: {e}")

if __name__ == "__main__":
    if wait_for_piston():
        install_languages()
    else:
        print("❌ Piston did not start in time. Check 'docker compose ps'.")
        sys.exit(1)
