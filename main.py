from tkinter import *
import numpy as np
import pandas as pd
import os
import tkinter as tk
import PIL



from tkinter import *
from PIL import ImageTk, Image  

app = Tk()
app.title("Welcome")
img =Image.open('C://Users//Romes//Downloads//ccc.jpg')
bg = ImageTk.PhotoImage(img)

app.geometry("650x450")

# Add image
label = Label(app, image=bg)
label.place(x = 0,y = 0)

# Add text
label2 = Label(app, text = "BTC prediction",
               font=("Times New Roman", 24))

label2.pack(pady = 50)












def ar():
    os.system('python AR.py')


def ari():
    os.system('python ARIMA.py')

def bay():
    os.system('python bayesian.py')

def pol():
    os.system('python var.py')

def sar():
    os.system('python SARIMAX.py')

def auar():
    os.system('python auto-ARIMA.py')
    




pms = Button(app, text="  AR  ", command=ar,bg="#071329",fg="yellow")
pms.place(x = 50,y = 200)

sb = Button(app, text="ARIMA", command=ari,bg="#071329",fg="yellow")
sb.place(x = 50,y = 300)


pms = Button(app, text="  BAYSEAN  ", command=bay,bg="#071329",fg="yellow")
pms.place(x = 150,y = 400)
sb = Button(app, text="VAR", command=pol,bg="#071329",fg="yellow")
sb.place(x = 500,y = 200)

pms = Button(app, text="  SARIMAX  ", command=sar,bg="#071329",fg="yellow")
pms.place(x = 500,y = 300)
sb = Button(app, text="AUTO-ARIMA", command=auar,bg="#071329",fg="yellow")
sb.place(x = 400,y = 400)








# Execute tkinter
app.mainloop()
