import requests
from datetime import datetime
import json

time = int(datetime.now().timestamp())
csrf = None
mid = None
ig_did = None
ig_nrcb = None

def IsExists(user, password, user_agent):
    global csrf, mid, ig_did, ig_nrcb

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

    try:
        response = requests.post(url, headers=headers, data=payload)
            
        
        csrf = response.cookies.get("csrftoken")
        mid = response.cookies.get("mid")
        ig_did = response.cookies.get("ig_did")
        ig_nrcb = response.cookies.get("ig_nrcb")

        headers.update({
            'X-Csrftoken': csrf,
            'Cookie': f"csrftoken={csrf}; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb};"
        })


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

def two_factor(code, identifier, username, user_agent,methode):
    global csrf, mid, ig_did, ig_nrcb

    if not user_agent:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

    url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/two_factor/"

    payload = {
        'identifier': identifier,
        'queryParams': '{"next":"/"}',
        'trust_signal': 'true',
        'username': username,
        'verification_method': methode, #deyisir (sms=1,app=3)
        'verificationCode': code
    }

    headers = {
        'Host': 'www.instagram.com',
        'Cookie': f"csrftoken={csrf}; wd=1920x921; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb};",
        'X-Csrftoken': csrf,
        'User-Agent': user_agent,
    }

    try:
        response = requests.post(url, headers=headers, data=payload)

        cookies_dict = response.cookies.get_dict()
        cookies = json.dumps(cookies_dict)

        try:
            final = response.json()
        except Exception as e:
            final = {'user': True, 'authenticated': False, 'status': 'ok'}

        return final, cookies

    except Exception as e:
        print(f"Hata: {e}")
        return {'user': True, 'authenticated': False, 'status': 'ok'}, {}
