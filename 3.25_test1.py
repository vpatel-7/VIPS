import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
root = tk.Tk()

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
btn_new_file = tk.Button(root, text='New File', bg='#1E90FF')
btn_new_file.grid(column=2, row=0, sticky='ew')

btn_lab_details = tk.Button(root, text='Lab Details', bg='#B4DCEB')
btn_lab_details.grid(column=3, row=0, sticky='ew')

btn_collect = tk.Button(root, text='Collect', bg='#B0CA99')
btn_collect.grid(column=1, row=3,  sticky='ew')

btn_exit = tk.Button(root, text='Exit', bg='#D9D9D9', command=root.quit)
btn_exit.grid(column=3, row=3, sticky='ew')

# Widgets
lbl_title = tk.Label(root, text='Thrust Stand Experiment', bg='white', fg='black')
lbl_title.grid(column=0, row=0, sticky='nsew')


# Thrust/Position Frame
frame_tp = tk.Frame(root)
frame_tp.grid(column=3, row=1, sticky='ew')
for i in range(4):
    frame_tp.grid_rowconfigure(i, weight=1)
frame_tp.grid_columnconfigure(0, weight=1)

# Thrust
lbl_thrust = tk.Label(frame_tp, text='Thrust')
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
frame_PV = tk.Frame(root)
frame_PV.grid(column=0, row=2, rowspan=2, sticky='nsew')
frame_PV.grid_columnconfigure(0, weight=1)
for i in range(1):
    frame_tp.grid_rowconfigure(i, weight=1)

lbl_PV = tk.Label(frame_PV, text='Velocity vs X-Position', bg='#fff')
lbl_PV.grid(column=0, row=0, sticky='nsew')









root.mainloop()
