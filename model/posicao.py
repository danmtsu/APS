class Posicao():
    def __init__(self,x, y):
        self.__x = x
        self.__y = y
        self.__ocupada = False
        self.__epique = False

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self,newValue:bool):
        self.__ocupada = newValue

    @property
    def epique(self):
        return self.__epique
    @epique.setter
    def epique(self,newValue):
        self.__epique = newValue