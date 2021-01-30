from tkinter import *
import timeit
import random

#starting screen
window = Tk()
window.geometry("450x200")
window.eval('tk::PlaceWindow . center')
window.title("Speed Test")

#game instance method
def game():
    #quit button
    def close_window():
        windows.destroy()
    #check if word is correct
    def check():
        if box.get() == s:
            end = timeit.default_timer()
            print("Seconds: "+ str(end-start))
            sum1 = (end-start)/60
            print("Characters per minute: " + str(len(s)/sum1))
            commands()
        else:
            print("Wrong Spelling")
    #add two commands to one
    def commands():
        windows.destroy()
        game()
    words = ["a","b","c","d","e","g","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1""2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","{","}","[","]",";",":","","<",">",",",".","?","~","`"]
    s = ""
    randominteger = random.randint(10,20)
    #creates word
    for i in range(randominteger):
        word = random.randint(0, len(words)-1)
        s+=words[word]
    #start of timmer
    start = timeit.default_timer()
    #second window
    windows = Tk()
    windows.geometry("450x200")
    windows.eval('tk::PlaceWindow . center')
    windows.title("Speed Test")
    #string of characters the user has to type
    x1 = Label(windows, text=s, font="times 20")
    x1.place(x=150, y=10)
    #Label at top
    x2 = Label(windows, text = "Spell it out as fast as possible", font="times 20")
    x2.place(x=10, y=50)
    #the place where user types
    box = Entry(windows)
    box.place(x=280, y=55)
    #submit button
    b2 = Button(windows, text="Submit", command=check, width=12, bg='gray')
    b2.place(x=150, y=100)
    #try again button
    b3 = Button(windows, text="Try Again", command=commands, width=12, bg='gray')
    b3.place(x=250, y=100)
    #quit button
    b4 = Button(windows, text="QUIT", command=close_window, width=12, bg='gray')
    b4.place(x=200, y=150)
    windows.mainloop()

def destroy_screen():
    window.destroy()
    game()
#text for starting screen
x = Label(window, text = "Start Game",font = "times 20")
x.place(x=10,y=50)
b1 = Button(window, text= "Start", command = destroy_screen, width = 12,bg='gray')
b1.place(x=150,y=100)

window.mainloop()

