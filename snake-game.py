from tkinter import *

class Snake(Canvas):
    def __init__(self):
        super().__init__(width=600,
        height=620,
        background='black',
        highlightthickness=0)

GUI = Tk()
GUI.title('Snake Game')
GUI.resizable(False,False)



GUI.mainloop()