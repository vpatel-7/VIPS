import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Generate a simple graph using Matplotlib
fig, ax = plt.subplots(figsize=(6, 4))

# Graph Title
ax.set_title('Graph Title: Example Graph')

# Axis Titles
ax.set_xlabel('X-Axis Label')
ax.set_ylabel('Y-Axis Label')

# Plot some data
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
ax.plot(x, y, label='y = x^2')

# Show grid
ax.grid(True)

# Run Tkinter event loop
root.mainloop()

