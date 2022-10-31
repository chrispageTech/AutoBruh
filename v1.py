import tkinter as tk
from tkinter import *
import pyautogui as pyauto
import PIL
import time

print ("Loading AutoBruh!")
print ("Loaded!")
AutoBruh = tk.Tk()
AutoBruh.title('AutoBruh')
AutoBruh.geometry("150x200")

coal = pyauto.locateOnScreen('coal.png')
bank = pyauto.locateOnScreen('bank.png')
depall = pyauto.locateOnScreen('dump_inventory.png')
closebank = pyauto.locateOnScreen('close_bank.png')
Test = 0

def AutoBruh_Stop():
        Test = 1

def AutoBruh_Close():
        AutoBruh.destroy()
                     
def AutoBruh_GetPOS():
        pyauto.alert(text=('move your mouse to position, you have 3 seconds'), title='Timed', button='start')
        time.sleep(3)
        Xcordpos, Ycordpos = pyauto.position()
        pyauto.alert(text=(Xcordpos, Ycordpos), title='Your Pos', button='Okay')

# Im so lost coding this

def AutoBruh_Start():
        pyauto.confirm(text='This is experimental there is not way to stop when started', title='Warning')

        while Test == 1:
                

                while Test == 0:
                        exit(0)
        


        
tk.Button(
    AutoBruh,
    text='GetMousePos',
    command=AutoBruh_GetPOS
).pack()
tk.Button(
    AutoBruh,
    text='Setup',
    command='AutoBruh_Setup'
).pack()
tk.Button(
    AutoBruh,
    text='Save',
    command='AutoBruh.close'
).pack()
tk.Button(
    AutoBruh,
    text='Import',
    command='AutoBruh.close'
).pack()
tk.Button(
    AutoBruh,
    text='Start',
    command=AutoBruh_Start
).pack()
tk.Button(
    AutoBruh,
    text='Stop',
    command=AutoBruh_Stop
).pack()

tk.Button(
    AutoBruh,
    text='Exit',
    command=AutoBruh_Close
).pack()

AutoBruh.mainloop()
