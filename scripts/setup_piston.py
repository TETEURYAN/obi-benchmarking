import httpx
import time
import sys
import os
from dotenv import load_dotenv

load_dotenv()

PISTON_URL = os.getenv("PISTON_BASE_URL", "http://localhost:2000") + "/api/v2"

# Languages to pre-install
REQUIRED_LANGUAGES = [
    {"language": "python", "version": "3.10.0"},
    {"language": "cpp", "version": "10.2.0"}, # Standard GCC version in Piston
]

def wait_for_piston(retries=15):
    """Wait for Piston API to be online."""
    for i in range(retries):
        try:
            # Piston might be up but still initializing internal scripts
            response = httpx.get(f"{PISTON_URL}/runtimes", timeout=2.0)
            if response.status_code == 200:
                print("  ✅ Piston API is online and responding.")
                return True
        except (httpx.ConnectError, httpx.RequestError):
            pass
        
        print(f"  ... Waiting for Piston API ({i+1}/{retries})")
        time.sleep(3)
    return False

def install_languages():
    """Check installed languages and install missing ones."""
    try:
        response = httpx.get(f"{PISTON_URL}/runtimes")
        installed = response.json()
        installed_names = [r["language"] for r in installed]
    except Exception as e:
        print(f"  ❌ Could not fetch runtimes: {e}")
        return

    for lang_info in REQUIRED_LANGUAGES:
        lang = lang_info["language"]
        if lang in installed_names:
            print(f"  ✅ {lang} is already installed.")
            continue
        
        print(f"  📥 Installing {lang} ({lang_info['version']})...")
        try:
            resp = httpx.post(f"{PISTON_URL}/packages", json=lang_info, timeout=60.0)
            if resp.status_code == 200:
                print(f"  ✅ Successfully installed {lang}.")
            else:
                # If exact version fails, try without version
                print(f"  ⚠️  Version {lang_info['version']} failed. Trying latest...")
                fallback_payload = {"language": lang, "version": "*"}
                resp = httpx.post(f"{PISTON_URL}/packages", json=fallback_payload, timeout=60.0)
                if resp.status_code == 200:
                    print(f"  ✅ Successfully installed latest {lang}.")
                else:
                    print(f"  ❌ Failed to install {lang}: {resp.text}")
        except Exception as e:
            print(f"  ❌ Error installing {lang}: {e}")

if __name__ == "__main__":
    print("🚀 Piston Setup Script")
    if wait_for_piston():
        install_languages()
    else:
        print("❌ CRITICAL: Piston API failed to start. Check 'docker logs piston_api'.")
        sys.exit(1)
