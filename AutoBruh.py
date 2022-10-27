import pyautogui as pyg
import pillow
import tkinter as tk

AutoBruh=AutoBruh.pyg
Window= tk.Tk()
Window.title('AutoBruh')
button = tk.Button(AutoBruh, text='Get Mouse Pos', width=25, command='pyg.position()')
button = tk.Button(Window, text='Setup', width=25, command='')
button = tk.Button(Window, text='Save', width=25, command='')
button = tk.Button(Window, text='Import', width=25, command='')
button = tk.Button(Window, text='Start', width=25, command='')
button = tk.Button(Window, text='Stop', width=25, command=Window.destroy)
button.pack()
Window.mainloop()
pause