from model.posicao import Posicao
import tkinter as tk
from model.pieces import Peca
from PIL import Image, ImageDraw, ImageTk
from .Viewpecas import ViewPiece

class Board(tk.Toplevel, Posicao,Peca):
    def __init__(self, parent, rows=12, columns=8, size=30, color1="#CCE5FF", color2="#FFCCE5", border_color="#000000",
                 border_width=1):
        tk.Toplevel.__init__(self, parent)
        self.title("Tabuleiro")
        self.geometry(f"{columns * size}x{rows * size}")
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.border_color = border_color
        self.border_width = border_width
        self.rectangles = {}
        self.__posicoes = {}
        self.__pieces = {}
        self.__pique1 = [(0, 3), (0, 4), (1, 3), (1, 4)]
        self.__pique2 = [(10, 3), (10, 4), (11, 3), (11, 4)]
        self.__time1 = [(0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (2, 5), (1, 5), (0, 5)]
        self.__time2 = [(11, 2), (10, 2), (9, 2), (9, 3), (9, 4), (9, 5), (11, 5), (10, 5)]
        self.viewPiece = ViewPiece(self.__posicoes,self.__pieces)

        for row in range(self.rows):
            for column in range(self.columns):
                x1 = column * self.size
                y1 = row * self.size
                x2 = x1 + self.size
                y2 = y1 + self.size
                if row < self.rows // 2:
                    color = self.color1
                else:
                    color = self.color2
                rectangle = tk.Frame(self, width=self.size, height=self.size, bg=color,
                                     highlightthickness=self.border_width, highlightbackground=self.border_color)
                rectangle.grid(row=row, column=column)
                self.rectangles[row, column] = rectangle
                self.__posicoes[f'{row, column}'] = Posicao(row, column)

        self.make_pique()
        self.cria_pecas()

    def make_pique(self):
        self.set_color(1, 4, '#003366')
        self.set_color(1, 3, '#003366')
        self.set_color(0, 4, '#003366')
        self.set_color(0, 3, '#003366')
        self.set_color(11, 4, '#990000')
        self.set_color(11, 3, '#990000')
        self.set_color(10, 4, '#990000')
        self.set_color(10, 3, '#990000')

    def models_pique(self, ):
        for i in self.__pique1:
            self.__posicoes[f"{i}"].epique(True)

        for i in self.__pique2:
            self.__posicoes[f"{i}"].epique(True)

    def get_cell(self, row, column):
        return self.rectangles[row, column]

    def set_color(self, row, column, color):
        rectangle = self.rectangles[row, column]
        rectangle.config(bg=color)

    def cria_pecas(self):
        id = 0
        for i in self.__time1:
            self.__posicoes[f"{i}"].ocupada = True
            self.__pieces[id] = Peca(id,1,self.__posicoes[f"{i}"])
            self.desenha_peca(i[0],i[1],'#4a46ff')
            id += 1

            print(i)
        for i in self.__time2:
            self.__posicoes[f"{i}"].ocupada = True
            self.__pieces[id] = Peca(id,1,self.__posicoes[f"{i}"])

            self.desenha_peca(i[0],i[1],'#ff0084')

            id +=1


    def desenha_peca(self, row, column, color):
        x = column * self.size + self.size // 2
        y = row * self.size + self.size // 2
        radius = self.size // 2 - 2

        # cria uma imagem de um círculo
        image = Image.new('RGBA', (radius * 2, radius * 2), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        draw.ellipse((0, 0, radius * 2, radius * 2), fill=color)

        # converte a imagem para o formato do tkinter
        photo_image = ImageTk.PhotoImage(image)

        # cria um label com a imagem do círculo
        peca = tk.Label(self, image=photo_image, bd=self.border_width, bg=self['bg'])
        peca.image = photo_image
        peca.place(x=x - radius, y=y - radius)
