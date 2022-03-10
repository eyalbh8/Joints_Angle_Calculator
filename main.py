import tkinter as tk
import json as js
from client_visualization import visualizer
from add_new_exercise_functions import exercises

joints_list = ["left_wrist", "left_elbow", "left_shoulder", "left_hip",
               "left_knee", "left_ankle", "right_wrist", "right_elbow",
               "right_shoulder", "right_hip", "right_knee", "right_ankle"]

exercises_list = []

with open("exercises_db.json") as file:
    Data = js.load(file)

for exercise in Data:
    exercises_list.append(exercise)


def start():
    if exercise_inside.get() != "The exercises":
        exercise_joints_list = []
        exercise_angles_list = []

        for joint in Data[exercise_inside.get()]:
            exercise_joints_list.append(joint)
            exercise_angles_list.append(Data[exercise_inside.get()][joint])

        for i in range(5 - len(exercise_joints_list)):
            exercise_joints_list.append("")
            exercise_angles_list.append(False)

        window.destroy()
        visualizer(exercise_joints_list[0], exercise_joints_list[1],
                   exercise_joints_list[2], exercise_joints_list[3],
                   exercise_joints_list[4], exercise_angles_list[0],
                   exercise_angles_list[1], exercise_angles_list[2],
                   exercise_angles_list[3], exercise_angles_list[4],
                   exercise_sets.get())


    else:
        window.destroy()
        visualizer(first_value_inside.get(), second_value_inside.get(),
                   third_value_inside.get(), fourth_value_inside.get(),
                   fifth_value_inside.get(), first_value_angle.get(),
                   second_value_angle.get(), third_value_angle.get(),
                   fourth_value_angle.get(), fifth_value_angle.get(),
                   sets.get())


def add_new_exercise():
    exercises()


window = tk.Tk()
window.geometry("550x340")
window.title("!!!בהצלחה")

instructions_label = tk.Label(window, text="     תבחרו את המפרקים שתרצו", font=('calibre', 16, 'bold'))
instructions_label.grid(row=0, column=4)
result_label = tk.Label(window, text="      לראות את הזוויות שלהם", font=('calibre', 16, 'bold'))
result_label.grid(row=2, column=4)

exercise_inside = tk.StringVar(window)
exercise_inside.set("The exercises")
exercise_option_menu = tk.OptionMenu(window, exercise_inside, *exercises_list)
exercise_option_menu.grid(row=8, column=2)

exercise_sets = tk.IntVar()
exercise_sets_label = tk.Label(window, text="Sets", font=('calibre', 10, 'bold'))
exercise_sets_label.grid(row=8, column=4)
exercise_sets_entry = tk.Entry(window, textvariable=exercise_sets, font=('calibre', 10, 'normal'))
exercise_sets_entry.grid(row=8, column=6)

first_value_inside = tk.StringVar(window)
first_value_inside.set("The joints")
first_option_menu = tk.OptionMenu(window, first_value_inside, *joints_list)
first_option_menu.grid(row=10, column=2)

first_value_angle = tk.IntVar()
first_value_angle_label = tk.Label(window, text="Angle", font=('calibre', 10, 'bold'))
first_value_angle_label.grid(row=10, column=4)
first_value_angle_entry = tk.Entry(window, textvariable=first_value_angle, font=('calibre', 10, 'normal'))
first_value_angle_entry.grid(row=10, column=6)

second_value_inside = tk.StringVar(window)
second_value_inside.set("The joints")
second_option_menu = tk.OptionMenu(window, second_value_inside, *joints_list)
second_option_menu.grid(row=12, column=2)

second_value_angle = tk.IntVar()
second_value_angle_label = tk.Label(window, text="Angle", font=('calibre', 10, 'bold'))
second_value_angle_label.grid(row=12, column=4)
second_value_angle_entry = tk.Entry(window, textvariable=second_value_angle, font=('calibre', 10, 'normal'))
second_value_angle_entry.grid(row=12, column=6)

third_value_inside = tk.StringVar(window)
third_value_inside.set("The joints")
third_option_menu = tk.OptionMenu(window, third_value_inside, *joints_list)
third_option_menu.grid(row=14, column=2)

third_value_angle = tk.IntVar()
third_value_angle_label = tk.Label(window, text="Angle", font=('calibre', 10, 'bold'))
third_value_angle_label.grid(row=14, column=4)
third_value_angle_entry = tk.Entry(window, textvariable=third_value_angle, font=('calibre', 10, 'normal'))
third_value_angle_entry.grid(row=14, column=6)

fourth_value_inside = tk.StringVar(window)
fourth_value_inside.set("The joints")
fourth_option_menu = tk.OptionMenu(window, fourth_value_inside, *joints_list)
fourth_option_menu.grid(row=16, column=2)

fourth_value_angle = tk.IntVar()
fourth_value_angle_label = tk.Label(window, text="Angle", font=('calibre', 10, 'bold'))
fourth_value_angle_label.grid(row=16, column=4)
fourth_value_angle_entry = tk.Entry(window, textvariable=fourth_value_angle, font=('calibre', 10, 'normal'))
fourth_value_angle_entry.grid(row=16, column=6)

fifth_value_inside = tk.StringVar(window)
fifth_value_inside.set("The joints")
fifth_option_menu = tk.OptionMenu(window, fifth_value_inside, *joints_list)
fifth_option_menu.grid(row=18, column=2)

fifth_value_angle = tk.IntVar()
fifth_value_angle_label = tk.Label(window, text="Angle", font=('calibre', 10, 'bold'))
fifth_value_angle_label.grid(row=18, column=4)
fifth_value_angle_entry = tk.Entry(window, textvariable=fifth_value_angle, font=('calibre', 10, 'normal'))
fifth_value_angle_entry.grid(row=18, column=6)

sets = tk.IntVar()
sets_label = tk.Label(window, text="Sets", font=('calibre', 10, 'bold'))
sets_label.grid(row=20, column=4)
sets_entry = tk.Entry(window, textvariable=sets, font=('calibre', 10, 'normal'))
sets_entry.grid(row=20, column=6)

start_visualization = tk.Button(window, text='start', command=start)
start_visualization.grid(row=22, column=6)

add_new_exercise_button = tk.Button(window, text='add new exercise', command=add_new_exercise)
add_new_exercise_button.grid(row=24, column=6)

window.mainloop()
