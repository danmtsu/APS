import tkinter as tk
from model.pieces import Peca
from PIL import Image, ImageDraw, ImageTk

class ViewPiece:
    def __init__(self, position, pieces):
        self.__posicoes = position
        self.__pieces = pieces
        self.__time1 = [(0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (2, 5), (1, 5), (0, 5)]
        self.__time2 = [(11, 2), (10, 2), (9, 2), (9, 3), (9, 4), (9, 5), (11, 5), (10, 5)]
        self.size = 30
        self.border_width = 1

    def cria_pecas(self):
        id = 0
        for i in self.__time1:
            self.__posicoes[f"{i}"].ocupada = True
            self.__pieces[id] = Peca(id,1,self.__posicoes[f"{i}"])
            self.desenha_peca(i[0],i[1],'#4a46ff')
            self.desenha_peca(i[0],i[1],'#4a46ff')
            id += 1

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
        peca = tk.Label(image=photo_image, bd=self.border_width, bg=self['bg'])
        peca.image = photo_image
        peca.place(x=x - radius, y=y - radius)
