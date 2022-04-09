from tkinter import *
from tkinter import messagebox, ttk
#import json
#import os

a = Tk()
a.title("Clicker game by TerminalGoat")
a.geometry("400x500")
a.resizable(height = False, width = False)
####### main ##########################################
def resetscore():
    with open('saved.txt', 'r') as e: 
        COO = int(e.read())
    COO  = COO - COO
    dll = COO
    with open('saved.txt', 'w') as o: o.write('%d' % dll)
    def someshit1():
        LBLl.config(text = dll)
    LBLl = ttk.Label(a, font = ("terminal", 30, 'bold'), background = "black", foreground = 'white', width = 1000)
    LBLl.place(x=150, y=100)
    someshit1()
def click(shit):
    global d
    with open('saved.txt', 'r') as f: 
        
        d = int(f.read())
        f.close
  
    d += 1
    with open('saved.txt', 'w') as s: s.write('%d'% d)
    def someshit():
        LBL.config(text = d)
    LBL = ttk.Label(a, font = ("terminal", 30, 'bold'), background = "black", foreground = 'white')
    LBL.place(x=150, y=100)
    someshit()
def delmessage():
    M = messagebox.askquestion(title = 'reset score', message = 'ARE YOU WANT TO DELETE YOUR SCORE????', icon ='warning' )
    if M == 'yes':
        resetscore()
    else: messagebox.showinfo('OK',' KEEP WORKING :>')
def exit(oooooo):
    quit()
CV =  Canvas(a, bg = 'black', height = 1000, width =1000 )
CV.place(x=-10, y=0)
ttk.Label(text = 'clicker game', font = ('terminal', 20, 'bold')).grid()
#ttk.Label(a, text = f'the reset score button will be update later...', font = ("terminal", 10, 'bold'), background = "black", foreground = 'gray').place(x=20, y =480)
ttk.Label(a, text = f'YOUR SCORE:', font = ("terminal", 20, 'bold'), background = "black", foreground = 'white').place(x=20, y = 60)
Button(text = 'RESET SCORE',font = ('terminal', 11, 'bold'), bg= '#000101', fg = 'white', relief ='flat', command = delmessage).place(x = 320, y=480)
a.bind('<Button -1>', click)
a.bind('<KeyPress- e>', exit )


a.mainloop()

