import tkinter as tk
from tkinter import ttk
import os
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import serial 
from datetime import datetime
import webbrowser
import csv


root = tk.Tk()

def open_file():
    file_path = "Users/vpatel07/Downloads/Manual_Sp25VIPSfile.pdf"  # Replace with your file path
    try:
        # os.startfile(file_path) # For Windows
        os.system(f"open {file_path}") # For macOS and Linux
    except FileNotFoundError:
        print("File not found.")

'''Callback for 
newfile
arduinoConnect
labdetails


Collect:
Variables 
thrust
position
'''
def newfile_Callback():
    global file
    global timestamp
    try:
        file.close()
    except:
        #File doesn't exist yet
        ignore=1
    now = datetime.now()
    # Format it as 'YYYY-MM-DD_HH-MM-SS'
    
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    file = open("arduino_data"+timestamp+".csv", "w", newline="")
    print("Writing data to arduino_data.csv...")
    writer = csv.writer(file)
    writer.writerow(["x (mm)", "Pressure (Pa)", "Ambient (Pa)", "Thrust(g)"])  # Header
    file.flush()

def arduinoConnect_Callback():
    # UPDATE with port number once variable is made
    global arduino
    #arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1) 

def labdetails_Callback():
    webbrowser.open_new(r"https://drive.google.com/file/d/1WX5xK7Xqua2Vz-lO5Z7_klDieToz0dC8/view?usp=sharing")
 



# Window
root.title('Thrust Stand Experiment')
root.geometry('1440x900')
root.configure(bg='#f8f8fb')

# Grid
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for j in range(4):
    root.grid_rowconfigure(j, weight=1)

# Buttons
btn_new_file = tk.Button(root, text='New File', bg='#1E90FF', command=newfile_)
btn_new_file.grid(column=2, row=0, sticky='ew')

btn_exit = tk.Button(root, text='Exit', bg='#D9D9D9', command=root.quit)
btn_exit.grid(column=3, row=3, sticky='ew')

btn_lab_details = tk.Button(root, text='Lab Details', bg='#B4DCEB', command=labdetails_Callback)
btn_lab_details.grid(column=3, row=0, sticky='ew')

# Widgets
lbl_title = tk.Label(root, text='Thrust Stand Experiment', bg='white', fg='black')
lbl_title.grid(column=0, row=0, sticky='nsew')

# Collect Button
btn_collect = tk.Button(root, text='Collect', bg='#B0CA99')
btn_collect.grid(column=1, row=3,  sticky='ew')

# Arduino Status
frame_status = tk.Frame(root)
frame_status.grid(column=2, row=3, sticky='nsew')
for i in range(2):
    frame_status.grid_columnconfigure(i, weight=1)
for j in range(2):
    frame_status.grid_rowconfigure(j, weight=1)

lbl_arduino = tk.Label(frame_status, text='Arduino Status:')
lbl_arduino.grid(column=0, row=0, columnspan=2, sticky='nsew')

lbl_not_conn = tk.Label(frame_status, text='Not Connected')
lbl_not_conn.grid(column=0, row=1, sticky='nw')

#lbl_connected = tk.Label(frame_status, text='Connected')
#lbl_connected.grid(column=0, row=1, sticky='nw')

# add connection command if/then statement
#canvas = tk.Canvas(frame, width=200, height=200)
#canvas.pack()

#circle = canvas.create_oval(frame_status, fill="red")
#circle.grid(column=1, row=1, sticky='nsew')



# Thrust/Position Frame
frame_tp = tk.Frame(root)
frame_tp.grid(column=3, row=1, sticky='ew')
frame_tp.grid_columnconfigure(0, weight=1)
for i in range(4):
    frame_tp.grid_rowconfigure(i, weight=1)

# Thrust
lbl_thrust = tk.Label(frame_tp, text='Thrust (g)')
lbl_thrust.grid(column=0, row=0, sticky='ew')

thrust_entry = tk.Entry(frame_tp)
thrust_entry.grid(column=0, row=1, sticky='ew')
# thrust_entry.pack(side='bottom', fill='x', expand=True)

# Position
lbl_position = tk.Label(frame_tp, text="Position:")
lbl_position.grid(column=0, row=2, sticky='ew')

position_entry = tk.Entry(frame_tp)
position_entry.grid(column=0, row=3, sticky='nsew')
# position_entry.pack(side='bottom', fill='x', expand=True)


# Pressure Graph Frame
frame_PX = tk.Frame(root)
frame_PX.grid(column=0, row=1, sticky='ew')
frame_PX.grid_columnconfigure(0, weight=1)
for i in range(1):
    frame_tp.grid_rowconfigure(i, weight=1)

lbl_PX = tk.Label(frame_PX, text='Pressure vs X-Position', bg='#fff')
lbl_PX.grid(column=0, row=0, sticky='nsew')




# Velocity Graph Frame
frame_VX = tk.Frame(root)
frame_VX.grid(column=0, row=2, rowspan=2, sticky='nsew')
frame_VX.grid_columnconfigure(0, weight=1)
for i in range(1):
    frame_tp.grid_rowconfigure(i, weight=1)

lbl_VX = tk.Label(frame_VX, text='Velocity vs X-Position', bg='#fff')
lbl_VX.grid(column=0, row=0, sticky='nsew')



# Data Table Frame
frame_DT = tk.Frame(root)
frame_DT.grid(column=1, row=1, columnspan=2, rowspan=2, sticky='nsew')
for i in range(4):
    frame_DT.grid_columnconfigure(i, weight=1)
for i in range(3):
    frame_tp.grid_rowconfigure(i, weight=1)

lbl_Data_Table = tk.Label(frame_DT, text='Data Table')
lbl_Data_Table.grid(column=0, row=0, sticky='nsew')

lbl_x = tk.Label(frame_DT, text='x (cm)')
lbl_x.grid(column=0, row=1, sticky='ew')

lbl_Ambient = tk.Label(frame_DT, text='Ambient Pressure (Pa)')
lbl_Ambient.grid(column=1, row=1, sticky='ew')

lbl_Pitot_Tube = tk.Label(frame_DT, text='Stagnation (Pa)')
lbl_Pitot_Tube.grid(column=2, row=1, sticky='ew')

lbl_Thrust_DT = tk.Label(frame_DT, text='Thrust (g)')
lbl_Thrust_DT.grid(column=3, row=1, sticky='ew')

root.mainloop()
