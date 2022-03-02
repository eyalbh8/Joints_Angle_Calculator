import tkinter as tk
from visualization import visualizer

joints_list = ["left_wrist", "left_elbow", "left_shoulder", "left_hip",
               "left_knee", "left_ankle", "right_wrist", "right_elbow",
               "right_shoulder", "right_hip", "right_knee", "right_ankle"]


def start():
    visualizer(value_inside.get())
    window.destroy()


window = tk.Tk()

value_inside = tk.StringVar(window)
value_inside.set("The joints")

option_menu = tk.OptionMenu(window, value_inside, *joints_list)
option_menu.grid(row=1, column=0)

start_visualization = tk.Button(window, text='start', command=start)
start_visualization.grid(row=1, column=3)

window.mainloop()
