from tkinter import *
from time import strftime

#function
def time():
    #working clock
    currenttime = strftime("%H:%M:%S")
    clock.configure(text=currenttime, fg = "#EB2188")
    clock.after(200,time)

#creates window
window = Tk()
window.geometry("400x150")
window.configure(bg='#080A52')
window.title("Clock")

#clock label
clock = Label(window, font = ("times",50, "bold"),bg="#080A52")
clock.grid(row = 2, column = 2, pady = 25,padx=100)
time()

#label for text above clock
digital = Label(window,text = "Clock", font = "times 24 bold", bg = "#080A52",fg = "#EB2188")
digital.grid(row=0,column = 2)
window.mainloop()
