from calendar import month
from click import getchar
from colorama import Fore ,init , Style
from os import system
from tkinter import Entry , mainloop , Label , Tk , Button , PhotoImage
from pyfiglet import figlet_format
init(convert = True)
enter = None
win = Tk()
def monthes():#get the monthes day and put in list unsorted
    year = int(enter.get())
    win.destroy()
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
        if len(mon) == 7:
            mon.append(" " * 20)
        calendar.extend(mon)
    printer(calendar)
    print(Fore.LIGHTMAGENTA_EX + "Any key to exit : ...")
    close = getchar()
def printer(calendar):#print the calendar and sort it
    system('cls')
    for i in range(8):
        print(Fore.CYAN + "   {}            {}            {}".format(calendar[i],calendar[i + 8],calendar[i + 16]))
    for i in range(24,32):
        print(Fore.GREEN + "   {}            {}            {}".format(calendar[i],calendar[i + 8],calendar[i + 16]))
    for i in range(48,56):
        print(Fore.YELLOW + "   {}            {}            {}".format(calendar[i],calendar[i + 8],calendar[i + 16]))
    for i in range(72,80):
        print(Fore.RED + "   {}            {}            {}".format(calendar[i],calendar[i + 8],calendar[i + 16]))
def tkinter():
    text = figlet_format("  C A L E N D E R" , font = "slant")
    print(Fore.LIGHTMAGENTA_EX + text)
    win.title("Calender")
    win.geometry("700x600")
    photo = PhotoImage(file = "calen.png")
    win.iconphoto(False , photo)
    Label(win,text = "<< Wellcome to my calender >>",fg = "purple",font = ("Aryal",32,'bold')).pack()
    background = Label(win, image=photo)
    background.config(font = (20))
    background.pack()
    Label(win,text = "Enter the year : ",font = ("Aryal",32,'bold')).pack()
    global enter
    enter = Entry(win,font = ("Aryal",32,'bold'),bg = "pink")
    enter.pack()
    but = Button(win,text = "ENTER",bg = "green",font = ("Aryal" ,25,'bold'))
    but.config(bd = 10 ,padx = 25 ,pady = 15 ,command = monthes,activebackground = "red")
    but.pack()
    mainloop()
tkinter()