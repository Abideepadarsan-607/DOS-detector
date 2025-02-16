#!/usr/bin/env python3

from scapy.all import *
from scapy.layers.dot11 import Dot11

# Get Network Interface from user
interface = input('Enter your Network Interface > ')

# Set Packet Counter
Packet_Counter = 1

# Extract info of the packet
def info(packet):
    global Packet_Counter
    if packet.haslayer(Dot11):
        # Deauth frame check (type 0 = management, subtype 12 = deauth)
        if packet.type == 0 and packet.subtype == 12:
            print(f"[+] Deauthentication Packet detected! Count: {Packet_Counter}")
            Packet_Counter += 1

# Start Sniffing and Detecting Deauth Packets
sniff(iface=interface, prn=info, store=False)

