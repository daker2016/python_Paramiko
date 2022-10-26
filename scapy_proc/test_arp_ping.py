import sys

import scapy
from scapy.packet import explore

# from scapy.layers.l2 import Ether, ARP
# #
# # if len(sys.argv) != 2:
# #     print("Usage: arping2tex <net>\n  eg: arping2tex 192.168.1.0/24")
# #     sys.exit(1)
#
# from scapy.all import srp, conf
# from scapy.packet import explore
# from scapy.sendrecv import sniff
#
# conf.verb = 0
#
# ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.1/24"), timeout=2)
#
# print(r"\begin{tabular}{|l|l|}")
# print(r"\hline")
# print(r"MAC & IP\\")
# print(r"\hline")
# for snd, rcv in ans:
#     print(rcv.sprintf(r"%Ether.src% & %ARP.psrc%\\"))
# print(r"\hline")
# print(r"\end{tabular}")
#
#
# def arp_monitor_callback(pkt):
#     if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
#         return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")
#
# sniff(prn=arp_monitor_callback, filter="arp", store=0)
#

explore(scapy.layers.http)