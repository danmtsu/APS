class Peca():
    def __init__(self,id,time,posicao):
        self.__id = id
        self.__time = time
        self.__posicao = posicao
        self.__Flag = False
        self.__Freeze = False


    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, newValue):
         self.__posicao = newValue

    def captura_flag(self):
        self.__Flag = True

    def congelado(self):
        self.__Flag = False
        self.__Freeze = True
