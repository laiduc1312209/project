import requests
import subprocess
import time
import os
import re
import colorama
from colorama import Fore, Style
import wmi  # Import the wmi module

# Define ASCII art and developer info
ascii_art = f"""
        {Fore.CYAN}_____       _     _ _            _____  _____ __      __
       {Fore.RED}|  __ \     | |   | (_)          |  __ \|  ____\ \    / /
       {Fore.CYAN}| |__) |   _| |__ | |_ _ __   ___| |  | | |__   \ \  / / 
       {Fore.RED}|  ___/ | | | '_ \| | | '_ \ / _ \ |  | |  __|   \ \/ /  
       {Fore.CYAN}| |   | |_| | |_) | | | | | |  __/ |__| | |____   \  /   
       {Fore.RED}|_|    \__,_|_.__/|_|_|_| |_|\___|_____/|______|   \/                                                              
       """
ten = Fore.CYAN + "                            -Dev : LaiDuc1312-" + Style.RESET_ALL

# Define main menu
menu = f"""
       ╭────────────────────────────────┬─────────────────────────────────╮
       │               Option           │          Description            │
       ├────────────────────────────────┼─────────────────────────────────┤
       │                  {Fore.MAGENTA}1{Style.RESET_ALL}             │           {Fore.MAGENTA}Bypass tool{Style.RESET_ALL}           │
       ├────────────────────────────────┼─────────────────────────────────┤
       │                  {Fore.MAGENTA}2{Style.RESET_ALL}             │           {Fore.MAGENTA}Windows tool{Style.RESET_ALL}          │
       ├────────────────────────────────┼─────────────────────────────────┤
       │                  {Fore.MAGENTA}3{Style.RESET_ALL}             │           {Fore.MAGENTA}System Info{Style.RESET_ALL}           │
       ├────────────────────────────────┼─────────────────────────────────┤
       │                  {Fore.MAGENTA}4{Style.RESET_ALL}             │           {Fore.MAGENTA}Comming soon !{Style.RESET_ALL}        │
       ├────────────────────────────────┼─────────────────────────────────┤
       │                  {Fore.MAGENTA}5{Style.RESET_ALL}             │           {Fore.MAGENTA}Comming soon !{Style.RESET_ALL}        │
       ├────────────────────────────────┼─────────────────────────────────┤
       │                  {Fore.MAGENTA}6{Style.RESET_ALL}             │           {Fore.MAGENTA}Comming soon !{Style.RESET_ALL}        │
       ├────────────────────────────────┼─────────────────────────────────┤
       │                {Fore.MAGENTA}Exit{Style.RESET_ALL}            │           {Fore.MAGENTA}Exit program{Style.RESET_ALL}          │
       ╰────────────────────────────────┴─────────────────────────────────╯
       """

# Define submenu for option 1
dmm = f"""
       ╭────────────────────────────────┬─────────────────────────────────╮
       │               Option           │          Description            │
       ├────────────────────────────────┼─────────────────────────────────┤
       │                  {Fore.MAGENTA}1{Style.RESET_ALL}             │          {Fore.MAGENTA}Bypass excutor{Style.RESET_ALL}         │
       ├────────────────────────────────┼─────────────────────────────────┤
       │                  {Fore.MAGENTA}2{Style.RESET_ALL}             │         {Fore.MAGENTA}Bypass linkvertise{Style.RESET_ALL}      │
       ├────────────────────────────────┼─────────────────────────────────┤
       │                  {Fore.MAGENTA}3{Style.RESET_ALL}             │         {Fore.MAGENTA}Back to main menu{Style.RESET_ALL}       │
       ╰────────────────────────────────┴─────────────────────────────────╯
       """
dmm1 = f"""
        ╭────────────────────────────────┬────────────────────────────────┬──────────────────────────────────╮
        │               Option           │              Commands          │           Description            │
        ├────────────────────────────────┼────────────────────────────────┼──────────────────────────────────┤
        │                  {Fore.MAGENTA}1{Style.RESET_ALL}             │                 💩             │       {Fore.MAGENTA}Tool for active windows{Style.RESET_ALL}    │
        ├────────────────────────────────┼────────────────────────────────┼──────────────────────────────────┤
        │                  {Fore.MAGENTA}2{Style.RESET_ALL}             │                 💩             │          {Fore.MAGENTA}Christitus Tweak{Style.RESET_ALL}        │
        ╰────────────────────────────────┴────────────────────────────────┴──────────────────────────────────╯

        ╭────────────────────────────────┬────────────────────────────────╮
        │                  {Fore.MAGENTA}3{Style.RESET_ALL}             │        {Fore.MAGENTA}Back to main menu{Style.RESET_ALL}       │
        ╰────────────────────────────────┴────────────────────────────────╯
"""

def clear_screen():
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def display_menu():
    """Display the main menu."""
    clear_screen()
    colorama.init(autoreset=True)
    print(ascii_art)
    print(ten)
    print(menu)

def run_remote_code(url):
    """Fetch and execute remote code from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        exec(response.text)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[!] Error fetching the code: {e}" + Style.RESET_ALL)

def run_powershell_command(command):
    """Run a PowerShell command."""
    try:
        subprocess.run(["powershell", "-Command", command], check=True)
        print(Fore.GREEN + "[!] PowerShell command executed successfully." + Style.RESET_ALL)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[!] Error executing PowerShell command: {e}" + Style.RESET_ALL)

def display_system_info():
    """Display system information using WMI."""
    try:
        c = wmi.WMI()
        system_info = c.Win32_ComputerSystem()[0]
        os_info = c.Win32_OperatingSystem()[0]
        processor = c.Win32_Processor()[0]
        gpu = c.Win32_VideoController()[0]
        print(Fore.CYAN + "System Information:" + Style.RESET_ALL)
        print(f"Manufacturer: {system_info.Manufacturer}")
        print(f"Model: {system_info.Model}")
        print(f"OS Name: {os_info.Name}")
        print(f"OS Version: {os_info.Version}")
        print(f"Processor: {processor.Name}")
        print(f"Total RAM: {round(float(os_info.TotalVisibleMemorySize) / 1048576, 2)} GB")
        print(f"GPU: {gpu.Name}")
    except Exception as e:
        print(Fore.RED + f"[!] Error fetching system info: {e}" + Style.RESET_ALL)

def main():
    while True:
        display_menu()
        lua_chon = input(Fore.YELLOW + '[?] Please select the option: ' + Style.RESET_ALL).lower()

        if lua_chon == '1':
            clear_screen()
            while True:
                print(dmm)
                lua_chon_con = input(Fore.YELLOW + '[?] Please select the option : ' + Style.RESET_ALL).lower()
                if lua_chon_con == '1':
                    clear_screen()
                    print(Fore.GREEN + "[!] Successful, running remote code. Please wait..." + Style.RESET_ALL)
                    print("Api bị ngu nên sẽ không chạy")
                    time.sleep(5)
                    run_remote_code("https://raw.githubusercontent.com/laiduc1312209/project/main/a.py")
                    time.sleep(1)
                elif lua_chon_con == '2':
                    clear_screen()
                    print(Fore.GREEN + "[!] Successful, running remote code. Please wait..." + Style.RESET_ALL)
                    print("Api bị ngu nên sẽ không chạy")
                    time.sleep(5)
                    run_remote_code("https://raw.githubusercontent.com/laiduc1312209/project/main/b.py")
                    time.sleep(1)
                elif lua_chon_con == '3':
                    clear_screen()
                    display_menu()
                    break
                else:
                    print(Fore.RED + "[!] Error, please re-enter" + Style.RESET_ALL)
                    time.sleep(1)
                    clear_screen()
                    
        elif lua_chon == '2':
            clear_screen()
            while True:
                print(dmm1)
                lua_chon_con = input(Fore.YELLOW + '[?] Please select the option : ' + Style.RESET_ALL).lower()
                if lua_chon_con == '1':
                    clear_screen()
                    print(Fore.GREEN + "[!] Running PowerShell command. Please wait..." + Style.RESET_ALL)
                    run_powershell_command("irm https://massgrave.dev/get | iex")
                    time.sleep(1)
                    clear_screen()
                elif lua_chon_con == '2':
                    clear_screen()
                    print(Fore.GREEN + "[!] Successful, running remote code. Please wait..." + Style.RESET_ALL)
                    print("Vì đoạn này code trong lúc mất điện nên tôi đéo có mạng để lấy command r test 🥸👍")
                    time.sleep(5)
                    clear_screen()
                elif lua_chon_con == '3':
                    clear_screen()
                    display_menu()
                    break
                else:
                    print(Fore.RED + "[!] Error, please re-enter" + Style.RESET_ALL)
                    time.sleep(1)
                    clear_screen()

        elif lua_chon == '3':
            clear_screen()
            print(Fore.GREEN + "[!] Fetching system information..." + Style.RESET_ALL)
            display_system_info()
            input(Fore.YELLOW + "[?] Press Enter to return to the main menu" + Style.RESET_ALL)

        elif lua_chon in ['4', '5', '6']:
            print(Fore.GREEN + "[!] Coming soon!" + Style.RESET_ALL)
            time.sleep(1)

        elif lua_chon == 'exit':
            print(Fore.GREEN + "[!] See you then!" + Style.RESET_ALL)
            time.sleep(1)
            break

        else:
            print(Fore.RED + "[!] Error, please re-enter" + Style.RESET_ALL)
            time.sleep(1)

if __name__ == "__main__":
    main()