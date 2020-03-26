from calendar import month
from click import getchar
from colorama import Fore ,init
from os import system
init(convert = True)
print(Fore.BLUE + "Welcome to my Calendar \nEnter the year : ")
year = int(input())
def monthes():#get the monthes day and put in list unsorted
    calendar = []
    for monthes in range(1,13):
        mon = month(year,monthes)
        mon = mon.split('\n')
        if len(mon) != 9:#make it sorted
            mon[-1] = " " * 20
        if len(mon) == 9:#fix the monthes that have 8 line string
            mon.pop(-1)
        if len(mon[-2]) != 20:#make is better look
            for i in range(20-len(mon[-2])):
                mon[-2] += " "
        if len(mon[0]) != 20:#make is better look
            for i in range(20-len(mon[0])):
                mon[0] += " "
        calendar.extend(mon)
    printer(calendar)
    print(Fore.LIGHTMAGENTA_EX + "Any key to exit : ...")
    close = getchar()
def printer(calendar):#print the calendar and sort it
    system('cls')
    for i in range(8):
        print(Fore.GREEN + "   {}          {}              {}".format(calendar[i],calendar[i + 8],calendar[i + 16]))
    for i in range(24,32):
        print(Fore.YELLOW + "   {}          {}              {}".format(calendar[i],calendar[i + 8],calendar[i + 16]))
    for i in range(40,48):
        print(Fore.RED + "   {}          {}              {}".format(calendar[i],calendar[i + 8],calendar[i + 16]))
    for i in range(56,64):
        print(Fore.CYAN + "   {}          {}              {}".format(calendar[i],calendar[i + 8],calendar[i + 16]))
monthes()