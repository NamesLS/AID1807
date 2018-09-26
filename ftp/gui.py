# from tkinter import *
# # top = Tk()
# btn = Button()
# btn.pack()
# # btn["text"] = "Click me!"
# def clicked():
#     print("I was clicked")
# # btn["command"] = clicked
# btn.config(text="Click me!",command= clicked)
# Label(text = "I'm in the f window!").pack()

# # Button(text="Click me!",command= clicked).pack()

# # send = Toplevel()
# # Label(send,text = "I'm in the t window!").pack()

# for i in range(10):
#     Button(text=i).pack

from tkinter import *
top = Tk()
def callback(event):
    print(event.x,event.y)
top.bind("<Button-1>",callback)



















mainloop()