import random
import os
import sys
import pyfiglet


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
ascii_banner = pyfiglet.figlet_format("Token  generator")
print(ascii_banner)



ilosc = input("How many tokens to generate: \n")
ilosc = int(ilosc)
os.system('cls')

for i in range(ilosc):
    token1 = ""
    token2 = ""
    token3 = ""

    for c in range(24):
        token1 += random.choice(chars)

    for c in range(6):
        token2 += random.choice(chars)
    for c in range(27):
        token3 += random.choice(chars)

    token1 = str(token1)
    token2 = str(token2)
    token3 = str(token3)

    token1 = token1 + "."
    token2 = token2 + "."


    token = token1 + token2 + token3

    print (token)

print("\n")
sys.stdout.write("\033[1;31m")
print("Tokens generated, if you want to copy tokens press [CTRL A] + [CTRL C]")
sys.stdout.write("\033[0;0m")
input("")
#literówka była
