import tkinter as tk
from PIL import Image
from random import randint


gifs_list = ['gif1.gif', 'gif2.gif', 'gif3.gif', 'gif4.gif', 'gif5.gif']

root = tk.Tk()

gif_file = gifs_list[randint(0,4)]
gif_info = Image.open(gif_file)
gif_frames = gif_info.n_frames

gif_images = [tk.PhotoImage(file=gif_file, format=f'gif -index {i}') for i in range(gif_frames)]

gif_label = tk.Label(image="")
gif_label.pack()

anim = None
count = 0
def animation(count):
    global anim
    image = gif_images[count]
    gif_label.configure(image=image)

    count += 1
    if count == gif_frames:
        count = 0
    
    anim = root.after(50, lambda: animation(count))

animation(count)
    
root.mainloop()