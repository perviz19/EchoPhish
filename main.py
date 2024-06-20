import subprocess
import time
import json
import signal
import sys
from colorama import Fore, Style

def cleanup():
    subprocess.run(["pkill", "-f", "python3 web_app.py"], check=True)
    subprocess.run(["killall", "cloudflared"], check=True)

def signal_handler(sig, frame):
    cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    subprocess.Popen(["python3", "web_app.py"])

    subprocess.Popen(["cloudflared", "tunnel", "--no-autoupdate", "--metrics", "localhost:55555", "--url", "http://localhost:8080"], stderr=subprocess.DEVNULL)

    time.sleep(3)

    result = subprocess.run(["curl", "-s", "http://localhost:55555/quicktunnel"], capture_output=True, text=True)
    time.sleep(1)
    if result.stdout.strip():
        data = json.loads(result.stdout.strip())
        url = f"http://{data['hostname']}"
        message = f"{Style.BRIGHT}{Fore.GREEN}------ URL: {url}{Style.RESET_ALL}"
        print(message)
    else:
        raise ValueError("Empty response or invalid JSON format")

    signal.pause()

except json.JSONDecodeError as e:
    cleanup()

except subprocess.CalledProcessError as e:
    cleanup()
