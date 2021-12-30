import os, time, sys
from colorama import Fore
os.system("clear")

print(Fore.RED + """
 [ 1 ] { WIRESHARK }

 [ 2 ] { NMAP }

 [ 3 ] { NETDİSCOVER }

 [ 4 ] { AİRCRACK-NG }

 [ 5 ] { AİRODUMP-NG }

 [ 6 ] { WİFİTE }

CODED + BY + Furkan 
""")

network = input(Fore.BLUE + "["+ Fore.GREEN + " ENTER YOUR SELECTION " + Fore.BLUE + "] : ")

if web == "1":
	os.system("clear")
	os.system("wireshark")
elif web == "2":
	os.system("clear")
	os.system("nmap")
elif web == "3":
	os.system("clear")
	os.system("netdiscover")
elif web == "4":
	os.system("clear")
	os.system("aircrack-ng")
elif web == "5":
	os.system("clear")
	os.system("airodump-ng")
elif web == "6":
	os.system("clear")
	os.system("wifite")
