import subprocess
import sys
import os
import traceback

def perform_action(command: str):
    print(f"📥 Received command: {command}")

    try:
        if "amazon" in command.lower():
            amazon_script = os.path.abspath("app/actions/native_browser_amazon.py")
            print(f"🚀 Launching Amazon script: {amazon_script}")
            subprocess.Popen([sys.executable, amazon_script])
            return "Launched Amazon flow"

        elif "youtube" in command.lower():
            youtube_script = os.path.abspath("app/actions/native_browser_youtube.py")
            print(f"🚀 Launching YouTube script: {youtube_script}")
            subprocess.Popen([sys.executable, youtube_script])
            return "Launched YouTube flow"

        else:
            print(f"⚠️ Unrecognized command: {command}")
            return f"Unknown command: {command}"

    except Exception as e:
        traceback.print_exc()
        return f"Error while executing: {e}"
