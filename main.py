import os
import pystyle 
import time
from colorama import init, Fore, Style
import argparse
import requests
import subprocess

os.system('mode con: cols=128 lines=25')
pc_username = os.getlogin()
r = Fore.RED
b = Fore.BLUE

def c2ddos():
    subprocess.run(["python", "tools/C2DDOS.py"])

def c7ddos():
    subprocess.run(["python", "tools/C7DDOS.py"])

def doxtracking():
    subprocess.run(["python", "tools/DoxTracking.py"])

def phonetools():
    subprocess.run(["python", "tools/PhoneLookup.py"])

def usernamechecker():
    subprocess.run(["python", "tools/UsernameChecker.py"])

logo = r + f'''
          
        .                                                                                                               
        ^:                                                                                                              
        ^!:                                                                                                             
        ^~~^                                                                                                            
        :~~~~.                                                                                                          
        .~~~~~^.                                                                                                        
        .~~~~~~~:.                                                                                                   .^.
         ^~~~~~~!~^.                                                                                              .:^!^ 
         :~~~~~~~~~~^:.                                                                                        .:^~~!^  
          ~~~~~~~~~~~~~^:.                                                                                  .:^~~~~!^   
          :!~~~~~~~~~~~~~~~^:.                                                                          .:^~~~~~~~~^.   
           ~~~~~~~~~~~~~~~~~~~~^^:..                                                                ..^^~~~~~~~~~~^     
           .~~~~~~~~~~~~~~~~~~~~~~~~~: ....::::::::::......                                     .:^~~~~~~~~~~~~~~:      
            :~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^::...                      ..:^~~~~~~~~~~~~~~~~^.       
             :~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^::.           .::^~~~~~~~~~~~~~~~~~~!~:         
              :~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^:..  .^~~~~~~~~~~~~~~~~~~~~~~~^.          
               .~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~^.            
                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!~^.              
                  .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:.                
                     :^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^:                   
                   .:^^::^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:.                     
                 .^~~~~~^:..:^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                        
               :~~~~~~~~~~~^:...:^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.                       
             :~~~~~~~~~~~~~~~~^:.  ..:^~~~~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.                     
           :~~~~~~~~~~~~~~~~~~~~~^:.     ..:^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!^                     
         :~!~~~~~~~~~~~~~~~~~~~~~~~~^.          ..:::^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^:.                     
       .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.                   .....:^~~~~~~~~~~~~~~~~~~~~~~~~~~~~^.. ^^                     
      :~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^                        ^~~~~~~~~~~~..::^^^~~~~^^::..    :!~                     
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^                     .~~~~~~~~~~~~~.                    ~~~.                    
   .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^                    ~~~~~~~~~~~~~^                    .~~~.                    
  .~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:                .^~~~~~~~~~~~~~:                   .~~~~:                    
 .~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^:..       ..:^~~~~~~~~~~~~~~~:                  :~~~~~^                    
 .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~^               .^~~~~~~~~                    
   .:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~. ^^^:::::::^^~~~~~~~~~~~.                   
      :^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^~~!~. ^!~~~~~~~~~~~~~~~~~~~~~.                  
        .^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^:.      ..:. .~~~~~~~~~~~~~~~~~~~~~!~.                 
           :^~~~~~~~^^^:::...........::^~~~~~~~~~~~~~~~~~~~~~~.              :~~~~~~~~~~~~~~~~:::::....                 
             ....         ...:::::^^:   :~~~~~~~~~~~~~~~~~~~~~~:           .^~~~~~~~~~~~~~~~~~  ^~^^^:..                
                 ..::^^~~~~~~~^^^^^^^.   :~~~~~~~~~~~~~~~~~~~~~~~^.      .^~~~~~~~~~~~~~~~~~!^  :^^^^^~~~^:.            
           ..:^^^^^^::...     ...::::::    :~~~~~~~~~~~~~~~~~~~~~~:      .^~~~~~~~~~~~~~~~~~: .^^^:..   ..:^^^.         
       .:^^^^::.        .::^~~~~~~~^^^^.     .:^~~~~~~~~~~~~~^:..           .^^~~~~~~~~~~^:    .::^^~~^:.    .:^:.      
   .:^^::.          .:^~~^^::..    .:^^~~:       ....:::.......            .:.....:::...    ^^^.     .:^~^:.    .^^.    
 .::.           .:^~^^:.        .:~~~~^:..               :^~~!~            ^!~~.            .:^^~^:.     .^^:.    ..    
             .:^^^:.         .:~~~^:.                    ^!~!~.            ~!~^                 ..^^^.      ::          
          .:^^:.           .^~~^.                        .~!^             ^!~:                      .^^.                
         .^:.           .:~~:.                            :^            .^^.                          .:.               
                      .^~^.                           .                 .                                               
                    .^~:.                            :~:                                                                
                  .^^:                               ~~~:            .                                                  
                  ..                           .::::^~~~~^.       .:^.                                                  
                                              :~~~~~~~~~~~~~^^^^^~~~:                                                   
                                              ~~~~~~~~~~~~~~~~~~~~~~.                                                   
                                              ~~~~~~~~~~~~~~~~~~~~~~~                                                   
                                              ~~~~~~~~~~~~~~~~~~~~~!^                                                   
                                              ^~~~~~~~~~~~~~~~~~~~~~.                                                   
                                               .:^^^^^^^^^^^^^^^^^: 

'''
ascii = pystyle.Center.XCenter(logo)
def menu():
    options = f''' 
    ╔═══                              ═══╗ ╔═══                               ═══╗ ╔═══                                 ═══╗
    ║   ({b}01{r}) > C2DDOS              ║ ║         ({b}10{r}) > N/A            ║ ║               ({b}19{r}) > N/A        ║
        ({b}02{r}) > C7DDOS                          ({b}11{r}) > N/A                              ({b}20{r}) > N/A
        ({b}03{r}) > DoxTracking                     ({b}12{r}) > N/A                              ({b}21{r}) > N/A
        ({b}04{r}) > PhoneLookup                     ({b}13{r}) > N/A                              ({b}22{r}) > N/A
        ({b}05{r}) > UsernameChecker                 ({b}14{r}) > N/A                              ({b}23{r}) > N/A
        ({b}06{r}) > N/A                             ({b}15{r}) > N/A                              ({b}24{r}) > N/A
        ({b}07{r}) > N/A                             ({b}16{r}) > N/A                              ({b}25{r}) > N/A
        ({b}08{r}) > N/A                             ({b}17{r}) > N/A                              ({b}26{r}) > N/A
    ║   ({b}09{r}) > N/A                 ║ ║         ({b}18{r}) > N/A             ║ ║              ({b}27{r}) > N/A        ║
    ╚═══                              ═══╝ ╚═══                                ═══╝ ╚═══                                ═══╝
''' 
    os.system('cls' if os.name == 'nt' else 'clear')
    ops = pystyle.Center.XCenter(options)
    print(ascii)
    print(ops)

def update_title(title):
    os.system(f"title SCAGENCY - {pc_username}'s PC ({title})")

os.system(f"title SCAGENCY - {pc_username}\'s PC (MENU)")
menu()
print(f'┌──<{pc_username}@SCAGENCY>─[~]')
i = input(f'└──╼ $ {b}').lstrip("0")
choice = i.upper()
try:

    options = {
        '1': ('C2DDOS', c2ddos),
        '2': ('C7DDOS', c7ddos),
        '3': ('DoxTracking', doxtracking),
        '4': ('PhoneLookup', phonetools),
        '5': ('UsernameChecker', usernamechecker),

    }

    title, cf = options.get(choice, (None, None))

    if cf:
        os.system('cls' if os.name == 'nt' else 'clear')
        update_title(title)
        print(ascii)
        cf()
        time.sleep(1)
    else:
        menu()
except Exception as e:
    print(Fore.RED + f"[!]Error: {e}")
