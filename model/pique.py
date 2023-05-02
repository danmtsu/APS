class Pique():
    def __init__(self):
        self.__time = int
        self.__hasFlag = True

    def change_flag(self):
        self.__hasFlag = not(self.__hasFlag)

    @property
    def time(self,):
        return self.__time

    @time.setter
    def time(self,x):
        self.__time = x