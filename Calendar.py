from calendar import month
from click import getchar
from colorama import Fore ,init
from os import system
init(convert = True)
print(Fore.BLUE + "Welcome to my Calendar \nEnter the year : ")
year = int(input())
system('cls')
printer = []
for mont in range(1,13):
    mon = month(year,mont)
    mon = mon.split('\n')
    if len(mon) != 9:
        mon[-1] = " " * 20
    if len(mon) == 9:
        mon.pop(-1)
    if len(mon[-2]) != 20:
        for i in range(20-len(mon[-2])):
            mon[-2] += " "
    if len(mon[0]) != 20:
        for i in range(20-len(mon[0])):
            mon[0] += " "
    printer.extend(mon)
for i in range(8):
    print(Fore.GREEN + "     {}          {}              {}".format(printer[i],printer[i + 8],printer[i + 16]))
for i in range(24,32):
    print(Fore.YELLOW + "     {}          {}              {}".format(printer[i],printer[i + 8],printer[i + 16]))
for i in range(40,48):
    print(Fore.RED + "     {}          {}              {}".format(printer[i],printer[i + 8],printer[i + 16]))
for i in range(56,64):
    print(Fore.CYAN + "     {}          {}              {}".format(printer[i],printer[i + 8],printer[i + 16]))
i = input()