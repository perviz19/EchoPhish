import requests
from datetime import datetime
import json

time = int(datetime.now().timestamp())
csrf = None
mid = None
ig_did = None
ig_nrcb = None
tor_active = False

def check_tor():
    global tor_active
    tor_active = True

def IsExists(user,password, user_agent):
    global csrf,mid,ig_did,ig_nrcb
    if user_agent == None or "":
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    password=password

    proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
    }

    payload = {'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
    'optIntoOneTap': 'false',
    'queryParams': {},
    'username': user}
    
    headers = {
        'User-Agent':  user_agent.strip(),
    }

    if tor_active:
        response = requests.request("POST", url, headers=headers, data=payload, proxies=proxies)
    else:
        response = requests.request("POST", url, headers=headers, data=payload)

    csrf=response.cookies["csrftoken"]
    mid=response.cookies["mid"]
    ig_did=response.cookies["ig_did"]
    ig_nrcb=response.cookies["ig_nrcb"]
    
    headers = {
        'User-Agent':  user_agent.strip(),
        'X-Csrftoken': f'{csrf}',
        'Cookie': f"csrftoken={csrf}; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb};"
    }

    if tor_active:
        response = requests.request("POST", url, headers=headers, data=payload, proxies=proxies)
    else:
        response = requests.request("POST", url, headers=headers, data=payload)

    cookies_dict = response.cookies.get_dict()
    cookies = json.dumps(cookies_dict)
    
    try:
        final =  response.json()
    except :
        final = {'user': True, 'authenticated': False, 'status': 'ok'}
    return final,cookies


def two_factor(code,identifier,username,user_agent):
    global csrf,mid,ig_did,ig_nrcb,tor_active
    if user_agent == "":
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"    
    url  = "https://www.instagram.com/api/v1/web/accounts/login/ajax/two_factor/"

    proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
    }

    headers = {
    'Host': 'www.instagram.com',
    'Cookie': f"csrftoken={csrf}; wd=1920x921; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb};",
    'X-Csrftoken': csrf,
    'User-Agent': user_agent,
    }


# Payload
    payload = {
        'identifier': identifier,
        'queryParams': '{"next":"/"}',
        'trust_signal': 'true',
        'username': username,
        'verification_method': '3',
        'verificationCode': code
    }
    
    if tor_active:
        response = requests.request("POST", url, headers=headers, data=payload, proxies=proxies)
    else:
        response = requests.request("POST", url, headers=headers, data=payload)
    
    cookies_dict = response.cookies.get_dict()
    cookies = json.dumps(cookies_dict)

    try:
        final =  response.json()
    except :
        final = {'user': True, 'authenticated': False, 'status': 'ok'}
    return final,cookies
