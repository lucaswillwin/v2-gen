import requests
from colorama import Fore, init


init()

print(Fore.GREEN + "Getting proxies..")
out_file = "proxies.txt"
f = open(out_file,'wb')
r1 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt")
f.write(r1.content)
f.close()
print("Got proxies, you can close this now")
input()
