import requests
from bs4 import BeautifulSoup
import os
import pystyle
import sys
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

def menu():
    subprocess.run(["python", "main.py"])

logo = """

 ██████╗ █████╗    █████╗  ██████╗ ███████╗███╗  ██╗ █████╗ ██╗   ██╗
██╔════╝██╔══██╗  ██╔══██╗██╔════╝ ██╔════╝████╗ ██║██╔══██╗╚██╗ ██╔╝
╚█████╗ ██║  ╚═╝  ███████║██║  ██╗ █████╗  ██╔██╗██║██║  ╚═╝ ╚████╔╝
 ╚═══██╗██║  ██╗  ██╔══██║██║  ╚██╗██╔══╝  ██║╚████║██║  ██╗  ╚██╔╝
██████╔╝╚█████╔╝  ██║  ██║╚██████╔╝███████╗██║ ╚███║╚█████╔╝   ██║
╚═════╝  ╚════╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚══╝ ╚════╝    ╚═╝







def googled(sq):
    url = f'https://www.google.com/search?q=site:doxbin.com+"{sq}"'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "Error semasa permintaan HTTP"

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for item in soup.find_all('div', class_='yuRUbf'):
        link = item.find('a')
        if link and 'href' in link.attrs:
            links.append(link['href'])

    if links:
        max_length = max(len(link) for link in links)
        box_width = max_length + 4

        linkoutput = ""
        linkoutput += f"╔{'═' * 3}{' ' * (box_width - 8)}{'═' * 3}╗\n"
        for link in links:
            padding = " " * (box_width - len(link))
            linkoutput += f"  {link}{padding}\n"
        linkoutput += f"╚{'═' * 3}{' ' * (box_width - 8)}{'═' * 3}╝"
        return linkoutput
    else:
        return "Tiada link yang berkaitan ditemui sama seperti anda"

pc_username = os.getlogin()
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW
if __name__ == "__main__":
    print(f'\n┌──<{pc_username}@SCAGENCY>─[~] {y}(Isi hal yang sangat anda penasaran contoh Mia Khalifa)')
    search = input(f'{r}└──╼ $ {b}').lstrip("0")
    result = googled(search)
    re = pystyle.Center.XCenter("\n" + result)
    print(r + re + "\n")
    print(f'\n {y}(anda harus memakai proxy supaya Roket tidak jatuh di rumah anda)')
    input(r + "Press ENTER untuk BOM negara.")
    menu()
