import threading
import tkinter
import time
from service import run


class RepeatExecute(object):
    def __init__(self,master,t=2000):
        self.master=master
        self.time=t

    def start(self):
        self.GO = True
        self.call_self()
        my_label.config(text="Running")

    def call_self(self):
        if self.GO is True:
            t = self.time
            print(time.time())
            thrd = threading.Thread(target=self.autorun)
            thrd.start()
            self.master.after(t,self.call_self)

    def set_time(self,t):
        self.time=t

    def stop(self):
        self.GO = False
        my_label.config(text="")

    def autorun(self):
        time.sleep(1.0)
        if self.GO is True:
            run()


if __name__=='__main__':
    root =tkinter.Tk()
    RE = RepeatExecute(root,t=2000)
    btn1 = tkinter.Button(root,text='Start',command=RE.start)
    btn1.pack()
    btn2 = tkinter.Button(root,text='Stop',command=RE.stop)
    btn2.pack()
    my_label = tkinter.Label(root, text="")
    my_label.pack(pady=20)
    
    root.mainloop()