import requests
from datetime import datetime
import json

time = int(datetime.now().timestamp())
def IsExists(user,password, user_agent):
    url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    password=password
    payload = {'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
    'optIntoOneTap': 'false',
    'queryParams': {},
    'username': user}
    files=[]
    headers = {
        'User-Agent': user_agent,
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    csrf=response.cookies["csrftoken"]
    mid=response.cookies["mid"]
    ig_did=response.cookies["ig_did"]
    ig_nrcb=response.cookies["ig_nrcb"]
    headers = {
        'X-Csrftoken': f'{csrf}',
        'Cookie': f"csrftoken={csrf}; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb};"
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)


    cookies_dict = response.cookies.get_dict()
    cookies = json.dumps(cookies_dict)
    
    try:
        final =  response.json()
    except :
        final = {'user': True, 'authenticated': False, 'status': 'ok'}
    return final,cookies



