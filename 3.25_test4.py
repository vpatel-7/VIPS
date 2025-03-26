import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Graph in Tkinter")
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 1, 3, 5]
figure, axes = plt.subplots()
axes.plot(x_values, y_values)
axes.set_xlabel("X-axis Label")
axes.set_ylabel("Y-axis Label")
axes.set_title("Graph Title")

tk.mainloop()