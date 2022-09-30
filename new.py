import tkinter
import subprocess as sb
import os, signal

action_path = os.path.join(os.getcwd(),'service.py')

cmd = ['python', action_path]

global is_on
is_on = True

def set_is_on(switch):
    global is_on
    if not switch:
        print(switch)
        is_on = True
    else:
        print(switch)
        is_on = False
    return is_on

def switch():
    global is_on
    if is_on:
        my_label.config(text=cmd)
        task = sb.Popen(cmd, stdout=sb.PIPE, stderr=sb.PIPE)
        with open("demofile3.txt", "w") as f:
            f.write(str(task.pid))
            f.close()
        onbutton.config(text="Stop")
        my_label.config(text="Running")
        is_on = False
    else:
        pid = None
        with open("demofile3.txt", "r") as f:
            pid = f.read()
            f.close()
        os.kill(int(pid), signal.SIGTERM)
        os.remove("demofile3.txt")
        print('stop')
        onbutton.config(text="Start")
        my_label.config(text="")
        is_on = True

if __name__=='__main__':
    root =tkinter.Tk()
    temp = None
    if os.path.exists(os.path.join(os.getcwd(),"demofile3.txt")):
        with open("demofile3.txt", "r") as f:
                temp = f.read()
                f.close()
    plug = set_is_on(temp)
    print(plug)
    if plug:
        onbutton = tkinter.Button(root,text="Start", command=switch)
        onbutton.pack()
        my_label = tkinter.Label(root, text="")
        my_label.pack(pady=20)
    else:
        onbutton = tkinter.Button(root,text="stop", command=switch)
        onbutton.pack()
        my_label = tkinter.Label(root, text="running")
        my_label.pack(pady=20)
    
    root.mainloop()