from tkinter import *

root = Tk()
root.title('Ratnesh')
root.geometry('300x300')

global is_on
is_on = True

# check the process status 
# if running set button to stop it 

def switch():
    global is_on
    if is_on:
        onbutton.config(text="Stop")
        my_label.config(text="Running")
        is_on = False
    else:
        onbutton.config(text="Start")
        my_label.config(text="")
        is_on = True

my_label = Label(root, text="")
my_label.pack(pady=20)

onbutton = Button(root,text="Start", command=switch)
onbutton.pack(pady=40)

root.mainloop()