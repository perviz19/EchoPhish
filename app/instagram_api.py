import requests
from datetime import datetime
import json

time = int(datetime.now().timestamp())
csrf = None
mid = None
ig_did = None
ig_nrcb = None
tor_active = False  

def IsExists(user, password, user_agent):
    global csrf, mid, ig_did, ig_nrcb, tor_active

    try:
        from app.config import tor_active as app_tor_active
        tor_active = app_tor_active
    except ImportError:
        tor_active = False

    
    if not user_agent:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"

    
    payload = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
        'optIntoOneTap': 'false',
        'queryParams': {},
        'username': user
    }

    headers = {
        'User-Agent': user_agent.strip(),
    }

    
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    
    try:
        if tor_active:
            response = requests.post(url, headers=headers, data=payload, proxies=proxies)
        else:
            response = requests.post(url, headers=headers, data=payload)
            
        
        csrf = response.cookies.get("csrftoken")
        mid = response.cookies.get("mid")
        ig_did = response.cookies.get("ig_did")
        ig_nrcb = response.cookies.get("ig_nrcb")

        headers.update({
            'X-Csrftoken': csrf,
            'Cookie': f"csrftoken={csrf}; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb};"
        })

        if tor_active:
            response = requests.post(url, headers=headers, data=payload, proxies=proxies)
        else:
            response = requests.post(url, headers=headers, data=payload)

        cookies_dict = response.cookies.get_dict()
        cookies = json.dumps(cookies_dict)

        try:
            final = response.json()
        except Exception as e:
            final = {'user': True, 'authenticated': False, 'status': 'ok'}

        return final, cookies

    except Exception as e:
        return {'user': True, 'authenticated': False, 'status': 'ok'}, {}

def two_factor(code, identifier, username, user_agent):
    global csrf, mid, ig_did, ig_nrcb, tor_active

    try:
        from app.config import tor_active as app_tor_active
        tor_active = app_tor_active
    except ImportError:
        tor_active = False

    if not user_agent:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/two_factor/"

    payload = {
        'identifier': identifier,
        'queryParams': '{"next":"/"}',
        'trust_signal': 'true',
        'username': username,
        'verification_method': '3',
        'verificationCode': code
    }

    headers = {
        'Host': 'www.instagram.com',
        'Cookie': f"csrftoken={csrf}; wd=1920x921; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb};",
        'X-Csrftoken': csrf,
        'User-Agent': user_agent,
    }

    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    try:
        if tor_active:
            response = requests.post(url, headers=headers, data=payload, proxies=proxies)
        else:
            response = requests.post(url, headers=headers, data=payload)

        cookies_dict = response.cookies.get_dict()
        cookies = json.dumps(cookies_dict)

        try:
            final = response.json()
        except Exception as e:
            print(f"Hata: {e}")
            final = {'user': True, 'authenticated': False, 'status': 'ok'}

        return final, cookies

    except Exception as e:
        print(f"Hata: {e}")
        return {'user': True, 'authenticated': False, 'status': 'ok'}, {}
