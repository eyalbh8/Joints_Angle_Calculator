import tkinter as tk
from visualization import visualizer

joints_list = ["left_wrist", "left_elbow", "left_shoulder", "left_hip",
               "left_knee", "left_ankle", "right_wrist", "right_elbow",
               "right_shoulder", "right_hip", "right_knee", "right_ankle"]


def start():
    visualizer(first_value_inside.get(), second_value_inside.get(), third_value_inside.get(),
               fourth_value_inside.get(), fifth_value_inside.get())
    window.destroy()


window = tk.Tk()

first_value_inside = tk.StringVar(window)
first_value_inside.set("The joints")
first_option_menu = tk.OptionMenu(window, first_value_inside, *joints_list)
first_option_menu.grid(row=1, column=0)

second_value_inside = tk.StringVar(window)
second_value_inside.set("The joints")
second_option_menu = tk.OptionMenu(window, second_value_inside, *joints_list)
second_option_menu.grid(row=3, column=0)

third_value_inside = tk.StringVar(window)
third_value_inside.set("The joints")
third_option_menu = tk.OptionMenu(window, third_value_inside, *joints_list)
third_option_menu.grid(row=5, column=0)

fourth_value_inside = tk.StringVar(window)
fourth_value_inside.set("The joints")
fourth_option_menu = tk.OptionMenu(window, fourth_value_inside, *joints_list)
fourth_option_menu.grid(row=7, column=0)

fifth_value_inside = tk.StringVar(window)
fifth_value_inside.set("The joints")
fifth_option_menu = tk.OptionMenu(window, fifth_value_inside, *joints_list)
fifth_option_menu.grid(row=9, column=0)

start_visualization = tk.Button(window, text='start', command=start)
start_visualization.grid(row=11, column=8)

window.mainloop()
