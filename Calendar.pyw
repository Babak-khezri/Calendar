from calendar import month
from tkinter import Button, Entry, Label, PhotoImage, Tk, mainloop


def Get_Calender(year):  # get the months day and put in list unsorted
    Calendar = []
    for Month in range(1, 13):
        Month = month(year, Month)
        Month = Month.split('\n')
        if len(Month) != 9:  # make it sorted
            Month[-1] = " " * 20
        if len(Month) == 9:  # fix the monthes that have 8 line string
            Month.pop(-1)
        if len(Month[-2]) != 20:  # make is better look
            for i in range(20-len(Month[-2])):
                Month[-2] += " "
        if len(Month[0]) != 20:  # make is better look
            for i in range(20-len(Month[0])):
                Month[0] += " "
        if len(Month) == 8:
            Month.append("." * 20)
        if len(Month[-2]) != 20:
            Month[-2] += ' ' * (20 - len(Month[-2]))
        Month = "\n".join(Month)
        Calendar.append(Month)
    Show(Calendar)


def Show(calender):
    win = Tk()
    win.title('Calender')
    win.resizable(False, False)
    for i in range(0, 3):
        Label(win, text=calender[i], font='consolas 14 bold',bg='#00001a', padx=25,fg='#1affff').grid(row=2, column=i)
    for i in range(3, 6):
        Label(win, text=calender[i], font='consolas 14 bold',bg='#00001a', padx=25,fg='#40ff00').grid(row=3, column=i-3)
    for i in range(6, 9):
        Label(win, text=calender[i], font='consolas 14 bold',bg='#00001a', padx=25,fg='#ffff00').grid(row=4, column=i-6)
    for i in range(9, 12):
        Label(win, text=calender[i], font='consolas 14 bold',bg='#00001a', padx=25,fg='#ff4000').grid(row=5, column=i-9)
    win.mainloop()


def tkinter():

    def Accept(event):
        year = enter.get()
        if year != '':
            try:
                Get_Calender(int(year))
            except:
                print("ERROR")

    win = Tk()
    win.title("Calender")
    win.geometry("700x600")
    photo = PhotoImage(file="C:\\Users\\Babak\\Desktop\\python\\EXTRA_FILES\\calen.png")
    win.iconphoto(False, photo)
    Label(win, text="<< Welcome to my calender >>",fg="purple", font=("Comic sans MS", 32, 'bold')).pack()
    Label(win, text="Enter the year : ", font=("Aryal", 32, 'bold')).pack()
    enter = Entry(win, bd=15,justify='center',font=("Comic sans MS", 32, 'bold'), bg="pink")
    enter.pack()
    Label(win).pack()
    but = Button(win, text="ENTER",relief="sunken", bg="green", font=("Aryal", 20, 'bold'))
    but.config(bd=20, command=lambda:Accept('event'))
    but.pack()
    win.bind('<Return>',Accept)
    mainloop()


tkinter()
