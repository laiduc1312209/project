import wmi

def get_hwid():
    c = wmi.WMI()
    hwid = []

    for item in c.Win32_ComputerSystemProduct():
        hwid.append(item.UUID)

    return hwid
import requests
import re
import os
import colorama
from colorama import Fore, Style
os.system("mode con: cols=70 lines=25")
os.system("cls")
colorama.init()


print(colorama.Fore.CYAN +" __        _ ____          ")
print(colorama.Fore.CYAN +"|  |   ___|_|    | _ _ ___ ")
print(colorama.Fore.CYAN +"|  |__| .'| |  |  | | |  _|")
print(colorama.Fore.CYAN +"|_____|__,|_|____||___|___|")
print(colorama.Fore.RED + '\n-Tool bypass key executor-')
if __name__ == "__main__":
    hwid = get_hwid()
    print(colorama.Fore.MAGENTA + "\nHardware ID(s):", hwid)
print(colorama.Fore.YELLOW + "\n[+] Executor support: Fluxus, Delta, CodeX, Hydrogen")
key = input('\n[?] Input your key : ')
api_url = f"https://api.goatbypassers.xyz/api/bypass?link={key}"
response = requests.get(api_url)
if response.status_code == 200:
    content = response.content.decode()
    key_search = re.search('"key":"(.*?)"', content)
    if key_search:
        key = key_search.group(1)
        print(f"\n\033[1;32m [ OUTPUT ] \033[1;37m: \033[1;33m{key}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nEROR" + Style.RESET_ALL)
else:
    print(Fore.RED + f"\nRequest failed, code status: {response.status_code}" + Style.RESET_ALL)

input(Fore.GREEN + "\nPress Enter key to exit..." + Style.RESET_ALL)
os.system('cls')
break
