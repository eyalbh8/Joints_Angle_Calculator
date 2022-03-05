import tkinter as tk
import json as js

from numpy import empty
from client_visualization import visualizer
from add_new_exercise_functions import exercises

joints_list = ["left_wrist", "left_elbow", "left_shoulder", "left_hip",
               "left_knee", "left_ankle", "right_wrist", "right_elbow",
               "right_shoulder", "right_hip", "right_knee", "right_ankle"]


def start():
    if exercise_inside.get() is not empty:
        exercise_joints_list = []
        for joint in Data[exercise_inside.get()]:
            exercise_joints_list.append(joint)
        
        for i in range(5 - len(exercise_joints_list)):
            exercise_joints_list.append("")

        visualizer(exercise_joints_list[0], exercise_joints_list[1], 
                   exercise_joints_list[2], exercise_joints_list[3], 
                   exercise_joints_list[4])
        window.destroy()
    
    else:
        visualizer(first_value_inside.get(), second_value_inside.get(), third_value_inside.get(),
               fourth_value_inside.get(), fifth_value_inside.get())
        window.destroy()

    
def add_new_exercise():
    exercises()

exercises_list = []

with open("exercises_db.json") as file:
        Data = js.load(file)

for exercise in Data:
    exercises_list.append(exercise)


window = tk.Tk()
window.geometry("300x250")
window.title("!!!בהצלחה")

instructions_label = tk.Label(window, text="     תבחרו את המפרקים שתרצו", font=('calibre', 16, 'bold'))
instructions_label.grid(row=0, column=8)
result_label = tk.Label(window, text="      לראות את הזוויות שלהם", font=('calibre', 16, 'bold'))
result_label.grid(row=2, column=8)

exercise_inside = tk.StringVar(window)
exercise_inside.set("The exercises")
exercise_option_menu = tk.OptionMenu(window, exercise_inside, *exercises_list)
exercise_option_menu.grid(row=8, column=8)

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

add_new_exercise_button = tk.Button(window, text='add new exercise', command=add_new_exercise)
add_new_exercise_button.grid(row=22, column=8)


window.mainloop()