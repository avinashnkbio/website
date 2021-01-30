import time;
import tkinter;
import pandas as pd

df = pd.read_excel ('/home/user/Documents/AugSeptexp-2020.xlsx')

import tkinter as tk
from tkinter import messagebox

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')
        
button1 = tk.Button (root, text='Exit Application',command=ExitApplication,bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)
  
root.mainloop()



print("welcome to Keral Piravi quiz Nov 2020\n press enter")




def main():

         name=input( "Please type in your name then hit Enter")                              
    
print ("\nHello there', name, 'I hope you have fun. Enjoy and good luck!!")
tic = time.perf_counter()

print('''
Q1 - 1 Which district of Kerala does maximum number of the rivers flow through?
A Kasargod
B Kannur
C Palakad
D Pathanamthitta
''')

answer = input().lower()
score=0
if answer == "a":
    print(" Correct!! :)  ")
    score=score+1
elif answer == "b":
    print("No - not Kannur :( ")
elif answer == "c":
    print(" Don't be silly! :( ")
elif answer == "d":
    print(" wrong answer :( ")
else:
    print(" pleae choose an option! ")
print('''  
    Q2-Which district of Kerala has the lowest sex-ratio?
    A Idukki 
    B Kasargode 
    C. Wayanad 
    D. Ernakulam 
    ''')

answer = input().lower()
if answer == "a":
    print(" Correct!! :)  ")
    score=score+1
elif answer == "b":
    print("No - not Kasargod :( ")
elif answer == "c":
    print(" not wayanad :( ")
elif answer == "d":
    print(" wrong answer :( ")
else:
    print(" pleae choose an option! ")
toc = time.perf_counter()

print("Completed the quiz in ",toc-tic ,"seconds")
print('your score is',score)
print (df)

