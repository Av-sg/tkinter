from tkinter import *
root = Tk()
root.title("Changing-Mouse")
root.geometry("300x300")
cursors=[
    "arrow", "circle", "clock", "dotbox", "exchange", "fleur", "heart", "man", "spider"
]
for cursor in cursors:
    Button(root, text= cursor, cursor=cursor).pack()
root.mainloop()
