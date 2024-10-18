from tkinter import * 
from PIL import Image,ImageTk,ImageSequence 
import time
import pygame  
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1500x800")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("david.gif")

    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("jarvis_ringtonee.mp3")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1500,800))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.5)
    root.destroy()

play_gif()
root.mainloop()