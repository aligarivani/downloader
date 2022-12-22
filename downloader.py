import colorama
import requests
import subprocess
from colorama import Fore, init
import os

os.system('cls')
init()
try:
    address = input('\n' + Fore.LIGHTBLUE_EX+'Enter Url > '+Fore.WHITE)
    name_file = input('\n' + Fore.LIGHTBLUE_EX + 'Enter Name File > ' + Fore.WHITE)
    format = input('\n' + Fore.LIGHTBLUE_EX + 'Enter Format ".mp4" , ".mp3" or other standard Format : ')
    url = requests.get(address).content

    file1 = open(f'{name_file}{format}', 'wb').write(url)
    openned = input('File Saved Done you need Open File ? "Y" or "N" : ')
    if openned.lower() == "y" :
        subprocess.getoutput(f'start {name_file}{format}')
        exit("Done")
    else:
        exit('Good Luck')
except requests.exceptions.MissingSchema:
    print(Fore.RED + 'url not True pls try again' + Fore.WHITE)
