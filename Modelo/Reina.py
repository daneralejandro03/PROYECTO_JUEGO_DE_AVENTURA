from Modelo.Personaje import Personaje

class Reina(Personaje):

    __inteligencia:int
    __carisma:int

    def __init__(self, id:str, nombre:str, nivel_Poder:int, inteligencia:int, carisma:int):
        super().__init__(id, nombre, nivel_Poder)
        self.__inteligencia = inteligencia
        self.__carisma = carisma

    def getInteligencia(self) -> int:
        return self.__inteligencia

    def setInteligencia(self, inteligencia:int):
        self.__inteligencia = inteligencia

    def getCarisma(self) -> int:
        return self.__carisma

    def setCarisma(self, carisma:int):
        self.__carisma = carisma

    def toStr(self) -> str:
        return f"Reina: {super().toStr()}, Inteligencia: {self.__inteligencia}, Carisma: {self.__carisma}"

    def pelear(self):
        return "La reina pelea con puños"