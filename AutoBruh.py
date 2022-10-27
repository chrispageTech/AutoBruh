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

def AutoBruh_Close():
    AutoBruh.destroy()
def AutoBruh_GetPOS():
        Xcordpos, Ycordpos = pyauto.position()
        pyauto.alert(text=(Xcordpos, Ycordpos), title='Your Pos', button='Bruh')
def MineCoal():
    AmountCoal = 1
    while AmountCoal < 10:
        pyauto.click(1484, 561)
        time.sleep(25)
        pyauto.click(1512, 489)
        time.sleep(1)
        pyauto.click(1526, 578)
        time.sleep(1)
        pyauto.click(1640, 309)

    AmountCoal += 1

tk.Button(
    AutoBruh,
    text='GetMousePos',
    command=AutoBruh_GetPOS
).pack()
tk.Button(
    AutoBruh,
    text='CoalBuddy',
    command=MineCoal
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
    command='AutoBruh.close'
).pack()
tk.Button(
    AutoBruh,
    text='Stop',
    command='AutoBruh'
).pack()

tk.Button(
    AutoBruh,
    text='Exit',
    command=AutoBruh_Close
).pack()


AutoBruh.mainloop()
time.sleep(5)
