class Peca():
    def __init__(self,id,time,posicao):
        self.__id = id
        self.__time = time
        self.__posicao = posicao
        self.__Flag = False
        self.__Freeze = False

    def captura_flag(self):
        self.__Flag = True

    def congelado(self):
        self.__Flag = False
        self.__Freeze = True
