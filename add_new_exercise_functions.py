import tkinter as tk
import json as js

joints_list = ["left_wrist", "left_elbow", "left_shoulder", "left_hip",
               "left_knee", "left_ankle", "right_wrist", "right_elbow",
               "right_shoulder", "right_hip", "right_knee", "right_ankle"]


class Exercise:
    def __init__(self, exercise_name, joint1_name, joint1_angle, joint2_name, joint2_angle, joint3_name,
                 joint3_angle, joint4_name, joint4_angle, joint5_name, joint5_angle):
        
        self.exercise_name = exercise_name
        self.joint1_name = joint1_name
        self.joint1_angle = joint1_angle
        self.joint2_name = joint2_name
        self.joint2_angle = joint2_angle
        self.joint3_name = joint3_name
        self.joint3_angle = joint3_angle
        self.joint4_name = joint4_name
        self.joint4_angle = joint4_angle
        self.joint5_name = joint5_name
        self.joint5_angle = joint5_angle
        

def exercises():
    win = tk.Tk()
    win.title("add new exercise")

    exercise_name = tk.StringVar(win)
    exercise_name_label = tk.Label(win, text = "Exercise_name", font=('calibre',10, 'bold'))
    exercise_name_label.grid(row=0,column=0)
    exercise_name_entry = tk.Entry(win,textvariable = exercise_name, font=('calibre',10,'normal'))
    exercise_name_entry.grid(row=0,column=1)


    first_value_inside = tk.StringVar(win)
    first_value_inside.set("The joints")
    first_option_menu = tk.OptionMenu(win, first_value_inside, *joints_list)
    first_option_menu.grid(row=2, column=0)

    joint1_angle = tk.IntVar(win,value=0)
    joint1_angle_label = tk.Label(win, text = "First joint angle", font=('calibre',10, 'bold'))
    joint1_angle_label.grid(row=2,column=3)
    joint1_angle_entry = tk.Entry(win,textvariable = joint1_angle, font=('calibre',10,'normal'))
    joint1_angle_entry.grid(row=2,column=4)
    
    second_value_inside = tk.StringVar(win)
    second_value_inside.set("The joints")
    second_option_menu = tk.OptionMenu(win, second_value_inside, *joints_list)
    second_option_menu.grid(row=4, column=0)

    joint2_angle = tk.IntVar(win,value=0)
    joint2_angle_label = tk.Label(win, text = "Second joint angle", font=('calibre',10, 'bold'))
    joint2_angle_label.grid(row=4,column=3)
    joint2_angle_entry = tk.Entry(win,textvariable = joint2_angle, font=('calibre',10,'normal'))
    joint2_angle_entry.grid(row=4,column=4)

    third_value_inside = tk.StringVar(win)
    third_value_inside.set("The joints")
    third_option_menu = tk.OptionMenu(win, third_value_inside, *joints_list)
    third_option_menu.grid(row=6, column=0)

    joint3_angle = tk.IntVar(win,value=0)
    joint3_angle_label = tk.Label(win, text = "Third joint angle", font=('calibre',10, 'bold'))
    joint3_angle_label.grid(row=6,column=3)
    joint3_angle_entry = tk.Entry(win,textvariable = joint3_angle, font=('calibre',10,'normal'))
    joint3_angle_entry.grid(row=6,column=4)

    fourth_value_inside = tk.StringVar(win)
    fourth_value_inside.set("The joints")
    fourth_option_menu = tk.OptionMenu(win, fourth_value_inside, *joints_list)
    fourth_option_menu.grid(row=8, column=0)

    joint4_angle = tk.IntVar(win,value=0)
    joint4_angle_label = tk.Label(win, text = "Fourth joint angle", font=('calibre',10, 'bold'))
    joint4_angle_label.grid(row=8,column=3)
    joint4_angle_entry = tk.Entry(win,textvariable = joint4_angle, font=('calibre',10,'normal'))
    joint4_angle_entry.grid(row=8,column=4)

    fifth_value_inside = tk.StringVar(win)
    fifth_value_inside.set("The joints")
    fifth_option_menu = tk.OptionMenu(win, fifth_value_inside, *joints_list)
    fifth_option_menu.grid(row=10, column=0)

    joint5_angle = tk.IntVar(win,value=0)
    joint5_angle_label = tk.Label(win, text = "Fifth joint angle", font=('calibre',10, 'bold'))
    joint5_angle_label.grid(row=10,column=3)
    joint5_angle_entry = tk.Entry(win,textvariable = joint5_angle, font=('calibre',10,'normal'))
    joint5_angle_entry.grid(row=10,column=4)


    def end():
        exercise = Exercise(exercise_name.get(), first_value_inside.get(), joint1_angle.get(), 
                            second_value_inside.get(), joint2_angle.get(), 
                            third_value_inside.get(), joint3_angle.get(), 
                            fourth_value_inside.get(), joint4_angle.get(), 
                            fifth_value_inside.get(), joint5_angle.get())
       
        new_data = {
            exercise.joint1_name: exercise.joint1_angle,
            exercise.joint2_name: exercise.joint2_angle,
            exercise.joint3_name: exercise.joint3_angle,
            exercise.joint4_name: exercise.joint4_angle,
            exercise.joint5_name: exercise.joint5_angle 
            }

        with open("exercises_db.json") as file:
            data = js.load(file)

        data[exercise.exercise_name] = new_data
        

        with open("exercises_db.json", 'w') as file:
            js.dump(data,file)

    end = tk.Button(win,bg="black", fg="white",text="Finish",command=end)
    end.grid(row=12,column=0)

    win.mainloop()

exercises()