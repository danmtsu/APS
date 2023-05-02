import tkinter as tk

class Flag():
    def __init__(self,canvas):
        self.canvas = canvas
        self.__capturada = False
        self.drawFlag()

    def drawFlag(self):
        self.canvas.create_oval(0.5 * 37.5, 3.5 * 37.5, (0.5 + 1) * 37.5,(3.5+ 1) * 37.5, fill='#020611', outline="")
        self.canvas.create_oval(10.5 * 37.5, 3.5 * 37.5, (10.5 + 1) * 37.5,(3.5+ 1) * 37.5, fill='#020611', outline="")