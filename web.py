import os, time, sys
from colorama import Fore
os.system("clear")

print(Fore.RED + """
 [ 1 ] { DIRB }

 [ 2 ] { SQLMAP }

 [ 3 ] { WPSCAN }

 [ 4 ] { COMMIX }

 [ 5 ] { SKIPFISH }

 [ 6 ] { NIKTO}

 [ 7 ] { WAPITI }

CODED + BY + Furkan 
""")

web = input(Fore.BLUE + "["+ Fore.GREEN + " ENTER YOUR SELECTION " + Fore.BLUE + "] : ")

if web == "1":
	os.system("clear")
	os.system("dirb")
elif web == "2":
	os.system("clear")
	os.system("sqlmap")
elif web == "3":
	os.system("clear")
	os.system("wpscan")
elif web == "4":
	os.system("clear")
	os.system("commix")
elif web == "5":
	os.system("clear")
	os.system("skipfish")
elif web == "6":
	os.system("clear")
	os.system("nikto")
elif web == "7":
	os.system("clear")
	os.system("wapiti")
