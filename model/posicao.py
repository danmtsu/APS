class Posicao():
    def __init__(self,x, y):
        self.__x = x
        self.__y = y
        self.ocupada = False
        self.__epique = False

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def ocupa_posicao(self):
        self.ocupada = True

    def desocupa_posicao(self):
        self.ocupada = False

    @property
    def epique(self):
        return self.__epique
    @epique.setter
    def epique(self,newValue):
        self.__epique = newValue