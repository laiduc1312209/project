import requests
import re
import os
import colorama
from colorama import Fore, Style

def bypass_link():
    os.system("cls")  # Clear console screen
    colorama.init()   # Initialize colorama
    
    while True:
            key = input(Fore.YELLOW + "[?] Enter your link (If the wrong format is entered, an error may occur) : ")
            
            api_url = f"https://api.bypass.vip/bypass?url={key}"
            
            response = requests.get(api_url)
            
            if response.status_code == 200:
                content = response.content.decode()
                key_search = re.search('"result":"(.*?)"', content)
                
                if key_search:
                    key = key_search.group(1)
                    print(Fore.CYAN + "----------------------------------------------------")
                    print(f"\n      \033[1;32m [ Your link ] \033[1;32m: \033[1;32m{key}")
                    print(Fore.CYAN + "----------------------------------------------------")
                    print(Fore.BLUE + "VI : Giữ phím Ctrl và ấn vào link để mở link")
                    print(Fore.BLUE + "EN : Hold Ctrl key and click on the link to open the link")
                else:
                    print(Fore.CYAN + "----------------------------------------------------")
                    print(Fore.RED + "\n                [ERROR]" + Style.RESET_ALL)
                    print(Fore.CYAN + "----------------------------------------------------")
            else:
                print(Fore.CYAN + "----------------------------------------------------")
                print(Fore.RED + f"\n               [ERROR] : {response.status_code}")
                print(Fore.CYAN + "----------------------------------------------------")
                
            choice = input(Fore.MAGENTA + "\nDo you want to bypass another link? (y/n): ").strip().lower()
            if choice != 'y':
                os.system('cls')
                break  # Exit loop if user does not want to bypass another link
if __name__ == "__main__":
    bypass_link()