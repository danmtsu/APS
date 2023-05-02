from model.posicao import Posicao
import tkinter as tk
from view.Viewpecas import Piece

class Board(tk.Toplevel, Posicao):
    def __init__(self, parent, rows=12, columns=8, size=30, color1="#CCE5FF", color2="#FFCCE5", border_color="#000000", border_width=1):
        tk.Toplevel.__init__(self, parent)
        self.title("Tabuleiro")
        self.geometry(f"{columns*size}x{rows*size}")
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.border_color = border_color
        self.border_width = border_width
        self.rectangles = {}
        self.__posicoes = []
        self.__pique1 = [3,4,11,12]
        self.__pique2 = [82,83,91,92]
        self.__times = [[2,4,10,13],[81,83,90,91]]
        self.time1 = []


        for row in range(self.rows):
            for column in range(self.columns):
                x1 = column*self.size
                y1 = row * self.size
                x2 = x1 + self.size
                y2 = y1 + self.size
                if row < self.rows // 2:
                    color = self.color1
                else:
                    color = self.color2
                rectangle = tk.Frame(self, width=self.size, height=self.size, bg=color, highlightthickness=self.border_width, highlightbackground=self.border_color)
                rectangle.grid(row=row, column=column)
                self.rectangles[row,column] = rectangle
                self.__posicoes.append(Posicao(row,column))

        self.make_pique()

    def make_pique(self):
        self.set_color(1,4,'#003366')
        self.set_color(1,3,'#003366')
        self.set_color(0,4,'#003366')
        self.set_color(0,3,'#003366')
        self.set_color(11,4, '#990000')
        self.set_color(11,3, '#990000')
        self.set_color(10,4, '#990000')
        self.set_color(10,3, '#990000')
        self.model_pique()
    def model_pique(self):
        for i in [3,4,11,12]:
            self.__posicoes[i].epique = True
        for i in [82,83,91,92]:
            self.__posicoes[i].epique = True

    def get_cell(self, row, column):
        return self.rectangles[row, column]

    def desenha_pecas(self,):
        for i in [2,4,10,13]:
            self.time1.append(Piece)

    def set_color(self, row, column, color):
        rectangle = self.rectangles[row, column]
        rectangle.config(bg=color)

