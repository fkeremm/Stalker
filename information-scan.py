import os, time, sys
from colorama import Fore
os.system("clear")

print(Fore.RED + """
 [ 1 ] { DMITRY }

 [ 2 ] { WAFW00F }

 [ 3 ] { THEHARVESTER }

 [ 4 ] { NBTSCAN }

 [ 5 ] { SNMP-CHECK }

CODED + BY + Furkan 
""")

isc = input(Fore.BLUE + "["+ Fore.GREEN + " ENTER YOUR SELECTION " + Fore.BLUE + "] : ")

if isc == "1":
	os.system("clear")
	os.system("dmitry")
elif isc == "2":
	os.system("clear")
	os.system("wafw00f")
elif isc == "3":
	os.system("clear")
	os.system("theHarvester")
elif isc == "4":
	os.system("clear")
	os.system("nbtscan")
elif isc == "5":
	os.system("clear")
	os.system("snmp-check")

