import tkinter as tk
from client_visualization import visualizer

joints_list = ["left_wrist", "left_elbow", "left_shoulder", "left_hip",
               "left_knee", "left_ankle", "right_wrist", "right_elbow",
               "right_shoulder", "right_hip", "right_knee", "right_ankle"]


def start():
    visualizer(first_value_inside.get(), second_value_inside.get(), third_value_inside.get(),
               fourth_value_inside.get(), fifth_value_inside.get())
    window.destroy()


window = tk.Tk()
window.geometry("300x250")
window.title("!!!בהצלחה")

instructions_label = tk.Label(window, text="     תבחרו את המפרקים שתרצו", font=('calibre', 16, 'bold'))
instructions_label.grid(row=0, column=8)
result_label = tk.Label(window, text="      לראות את הזוויות שלהם", font=('calibre', 16, 'bold'))
result_label.grid(row=2, column=8)

first_value_inside = tk.StringVar(window)
first_value_inside.set("The joints")
first_option_menu = tk.OptionMenu(window, first_value_inside, *joints_list)
first_option_menu.grid(row=10, column=8)

second_value_inside = tk.StringVar(window)
second_value_inside.set("The joints")
second_option_menu = tk.OptionMenu(window, second_value_inside, *joints_list)
second_option_menu.grid(row=12, column=8)

third_value_inside = tk.StringVar(window)
third_value_inside.set("The joints")
third_option_menu = tk.OptionMenu(window, third_value_inside, *joints_list)
third_option_menu.grid(row=14, column=8)

fourth_value_inside = tk.StringVar(window)
fourth_value_inside.set("The joints")
fourth_option_menu = tk.OptionMenu(window, fourth_value_inside, *joints_list)
fourth_option_menu.grid(row=16, column=8)

fifth_value_inside = tk.StringVar(window)
fifth_value_inside.set("The joints")
fifth_option_menu = tk.OptionMenu(window, fifth_value_inside, *joints_list)
fifth_option_menu.grid(row=18, column=8)

start_visualization = tk.Button(window, text='start', command=start)
start_visualization.grid(row=20, column=8)

window.mainloop()