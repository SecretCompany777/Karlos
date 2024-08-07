import requests
import os
import pystyle
import sys
import subprocess
from colorama import init, Fore, Style

def menu():
    subprocess.run(["python", "main.py"])

def spn(pn):
    api_key = "UYXXd2qpcpWJ1127vT2qo7ZcILbaNnTJ"
    url = f"https://api.apilayer.com/number_verification/validate?number={pn}"
    headers = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200 and data['valid']:
            result = "╔═══                                                     ═══╗\n" \
                     "║  Nombor Telephone: " + data['number'] + "                 ║\n" \
                     "   Format local: " + data['local_format'] + "\n" \
                     "   Format international: " + data['international_format'] + "\n" \
                     "   Code Negara: " + data['country_prefix'] + "\n" \
                     "   Negara: " + data['country_code'] + "\n" \
                     "   Nama Negara: " + data['country_name'] + "\n" \
                     "   Operator Simcard: " + data['carrier'] + "\n" \
                     "║  Device: " + data['line_type'] + "                        ║\n" \
                     "╚═══                                                     ═══╝\n"
            return result
        else:
            return "Nombor telephone invalid bro isi betul betul."
    except Exception as e:
        return f"pepatah cina pernah mengakatan LANCAU : {str(e)}"

pc_username = os.getlogin()
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW
if __name__ == "__main__":
    print(f'\n┌──<{pc_username}@SCAGENCY>─[~] {y}(Enter International Phone Number)')
    pn = input(f'{r}└──╼ $ {b}').lstrip("0")
    result = spn(pn)
    re = pystyle.Center.XCenter("\n" + result)
    print(r + re + "\n")
    input("Press ENTER untuk balik rumah.")
    menu()
