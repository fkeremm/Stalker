import os, time, sys
from colorama import Fore
os.system("clear")

print(Fore.RED + """
 [ MD5 ] { SHA1 }


CODED + BY + SAEP 
""")

cryptology = input(Fore.BLUE + "["+ Fore.GREEN + " Word To Be Encrypted " + Fore.BLUE + "] : ")

os.system("echo -n " + cryptology + " | md5sum")
os.system("echo -n " + cryptology + " | sha1sum")
