class Posicao():
    def __init__(self,x, y):
        self.__x = x
        self.__y = y
        self.__ocupada = False
        self.__epique = False


    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self,newvalue):
        self.__ocupada = newvalue
    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def altera_ocupada(self):
        self.__ocupada = not self.__ocupada

    @property
    def epique(self):
        return self.__epique
    @epique.setter
    def epique(self,newValue):
        self.__epique = newValue