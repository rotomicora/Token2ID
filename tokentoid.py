import os, base64;from colorama import Fore
w=Fore.LIGHTWHITE_EX;g=Fore.LIGHTGREEN_EX;re=Fore.LIGHTRED_EX;cy=Fore.LIGHTCYAN_EX;ye=Fore.LIGHTYELLOW_EX;bl=Fore.LIGHTBLUE_EX;b=Fore.LIGHTBLACK_EX;m=Fore.LIGHTMAGENTA_EX;y=Fore.LIGHTYELLOW_EX
token=input(f"{m}[{w}>{m}] {b}Token -{m}>{y} ").split(".")
id=base64.b64decode(token[0]+"==").decode("utf-8")
os.system("cls" if os.name == "nt" else "clear")
print(f"{m}[{w}>{m}] {b}ID -{m}>{y} {id}")
