from model.posicao import Posicao
import tkinter as tk


class Piece:
    def __init__(self, position):
        self.position = position

    def draw(self, canvas, size, color):
        row, column = self.position
        x = column * size
        y = row * size
        r = size / 2
        canvas.create_oval(x+r, y+r, x-r, y-r, fill=color, outline="black", width=2)