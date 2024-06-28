import subprocess
import time
import json
import signal
import sys
import os
from colorama import Fore, Style
from app.functions import banner1

def cleanup():
    subprocess.run(["pkill", "-f", "python3 web_app.py"], check=True)
    subprocess.run(["killall", "cloudflared"], check=True)

def signal_handler(sig, frame):
    cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    os.system("clear")
    banner1()
    message = f"""\n{Style.BRIGHT}{Fore.YELLOW}
    Select the method!
-------------------  
1-{Fore.GREEN} localhost{Fore.YELLOW}       |
-------------------
2-{Fore.GREEN} cloudflared{Fore.YELLOW}     |
-------------------"""
    

    print(message)
    choose = input()
    if choose == '2':
        subprocess.Popen(["python3", "web_app.py"])
        time.sleep(2)
        os.system("clear")
        banner1()
        subprocess.Popen(["cloudflared", "tunnel", "--no-autoupdate", "--metrics", "localhost:55555", "--url", "http://localhost:8080"], stderr=subprocess.DEVNULL)
        print(f"{Fore.YELLOW}Cloudflared starting....")
        time.sleep(4)
        result = subprocess.run(["curl", "-s", "http://localhost:55555/quicktunnel"], capture_output=True, text=True)
        time.sleep(1)
        if result.stdout.strip():
            data = json.loads(result.stdout.strip())
            url = f"https://{data['hostname']}"
            message = f"""{Style.BRIGHT}{Fore.YELLOW} 
            URLs: 
------------------------------------------------
{Fore.GREEN}{url}{Fore.YELLOW}
------------------------------------------------
"""
            print(message)
        else:
            raise ValueError("Empty response or invalid JSON format")
    elif choose == '1':
        subprocess.Popen(["python3", "web_app.py"])
        time.sleep(2)
        os.system("clear")
        banner1()
        message = f"{Style.BRIGHT}{Fore.GREEN}-URL: \nhttp://127.0.0.1:8080{Style.RESET_ALL}"
        print(message)
    
    else:
        print(f"{Fore.RED}Please enter a valid number!")
    signal.pause()

except json.JSONDecodeError as e:
    cleanup()

except subprocess.CalledProcessError as e:
    cleanup()