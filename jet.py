#!/bin/bash
#Script em Python para verificar ataques DDOS

import socket
import os

#Cria um socket para ouvir o tráfego
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("",0))

#Verifica se há muitos pacotes UDP entrando
num_packets = 0
while True:
    data, addr = s.recvfrom(1024)
    num_packets += 1
    if num_packets > 1000:
        print("Ataque DDOS detectado!")
        os.system("sudo iptables -A INPUT -s " + addr[0] + " -j DROP")
        break
    else:
        print("Nenhum ataque DDOS detectado.")
        break