import tkinter as tk
import pyautogui
import shelve
import threading
import time
import tkinter.ttk as tkk
import subprocess

subprocess.Popen("AutoBruh.py", shell=True)

    # Global variable to control the clicking loop
clicking = False

# Create a function to show the values_window
def show_values_window():
    values_window.deiconify()  # show the values_window

    # function to show the mouse position with a delay of 3 seconds
def show_position_delayed():
    values_window.after(3000, show_position)  # show_position function to be called after 3 seconds

def start_clicking():
    global num_times  # Declare num_times as a global variable
    global clicking
    clicking = True
    # Update the num_times variable
    num_times = int(num_times_entry.get())
    
    # new thread to run the clicking loop
    thread = threading.Thread(target=click_loop)
    thread.start()

def stop_clicking():
    global clicking
    clicking = False

def click_loop():
    global x_entries
    global y_entries
    global delay_entries
    global num_times
    current_iteration = 0
    while clicking:
        for j in range(num_times):
            for i in range(len(x_entries)):
                # Get the x and y values from the input fields
                x = x_entries[i].get()
                y = y_entries[i].get()
                
                # Check if the x and y values are empty strings
                if x == "" or y == "":
                    # If the x or y value is an empty string, skip this iteration
                    continue
                
                # Convert the x and y values to integers
                x = int(x)
                y = int(y)
                
                # Perform a mouse click at the specified coordinates
                pyautogui.click(x, y)
                
                # Get the delay value from the corresponding input field
                delay = delay_entries[i].get()
                
                # Check if the delay value is an empty string
                if delay == "":
                    # If the delay value is an empty string, skip this iteration
                    continue
                
                # Convert the delay value to a float
                delay = float(delay)
                
                # Wait for the specified delay
                time.sleep(delay)
                
            # Increment the current iteration count
            current_iteration += 1
            
            # Check if the current iteration count has exceeded the original value of num_times
            if current_iteration >= num_times:
                # If the current iteration count has exceeded the original value of num_times, stop clicking
                stop_clicking()

def show_position():
    # Get the current mouse position
    x, y = pyautogui.position()

    # Update the X and Y input fields in window
    x_entry.delete(0, tk.END)
    x_entry.insert(0, str(x))
    y_entry.delete(0, tk.END)
    y_entry.insert(0, str(y))

def save_data():
    # Open the shelve database
    with shelve.open("mouse_data") as db:
        # Save the data from the input fields
        db["x"] = [entry.get() for entry in x_entries]
        db["y"] = [entry.get() for entry in y_entries]
        db["delay"] = [entry.get() for entry in delay_entries]

def load_data():
    #  shelve database
    with shelve.open("mouse_data") as db:
        # Load data from the shelve database
        x_data = db.get("x", [])
        y_data = db.get("y", [])
        delay_data = db.get("delay", [])

        # Update the input fields with the loaded data
        for i in range(20):
            x_entries[i].delete(0, tk.END)
            x_entries[i].insert(0, x_data[i])
            y_entries[i].delete(0, tk.END)
            y_entries[i].insert(0, y_data[i])
            delay_entries[i].delete(0, tk.END)
            delay_entries[i].insert(0, delay_data[i])

#  the main window
root = tk.Tk()
root.title("Mouse Position")

#  a frame to hold the input fields
input_frame = tk.Frame(root)
input_frame.pack()

# labels for the input fields
tk.Label(input_frame, text="#").grid(row=0, column=0)
tk.Label(input_frame, text="X").grid(row=0, column=1)
tk.Label(input_frame, text="Y").grid(row=0, column=2)
tk.Label(input_frame, text="Delay (seconds)").grid(row=0, column=3)
tk.Label(input_frame, text="Repeat X Times").grid(row=0, column=4)

#  the buttons
save_button = tkk.Button(input_frame, text="Save", command=save_data)
load_button = tkk.Button(input_frame, text="Load", command=load_data)
start_button = tkk.Button(input_frame, text="Start", command=start_clicking)
stop_button = tkk.Button(input_frame, text="Stop", command=stop_clicking)
values_button = tkk.Button(input_frame, text="Get X & Y", command=show_values_window)

# Create empty label widgets to add space between the buttons (didn't end up using)
space1 = tk.Label(input_frame, width=5)

# Add buttons to the input_frame
values_button.grid(row=22, column=0)
save_button.grid(row=22, column=1)
load_button.grid(row=22, column=2)
start_button.grid(row=22, column=3)
stop_button.grid(row=22, column=4)



#input fields
num_times = 1
x_entry = tk.Entry(input_frame)
y_entry = tk.Entry(input_frame)
x_entry.grid(row=1, column=1)
y_entry.grid(row=1, column=2)
num_times_entry = tk.Entry(input_frame)
num_times_entry.grid(row=1, column=4)
x_entries = []
y_entries = []
delay_entries = []
num_times = 0


for i in range(2, 22):
    tk.Label(input_frame, text=str(i-1)).grid(row=i, column=0)
    x_entries.append(tk.Entry(input_frame))
    x_entries[-1].grid(row=i, column=1)
    y_entries.append(tk.Entry(input_frame))
    y_entries[-1].grid(row=i, column=2)
    delay_entries.append(tk.Entry(input_frame))
    delay_entries[-1].grid(row=i, column=3)

# Create a second window
values_window = tk.Toplevel(root)
values_window.title("Simple Auto")
values_window.geometry("400x400")
values_window.withdraw()  # hide the values_window initially

# Create a button to show the mouse position
button = tkk.Button(values_window, text="Get Mouse Position", command=show_position)
button.pack()

# button with delay of 3 seconds
delayed_position_button = tkk.Button(values_window, text="Get Mouse Position (3 second delay)", command=show_position_delayed)
delayed_position_button.pack()

# Run the GUI
root.mainloop()