from Modelo.Personaje import Personaje
from Interface.Magia import Magia

class Bruja(Personaje, Magia):

    __magia:int
    __conocimiento:int

    def __init__(self, id:str, nombre:str, nivel_Poder:int, magia:int, conocimiento:int):
        super().__init__(id, nombre, nivel_Poder)
        self.__magia = magia
        self.__conocimiento = conocimiento

    def getMagia(self) -> int:
        return self.__magia

    def setMagia(self, magia:int):
        self.__magia = magia

    def getConocimiento(self) -> int:
        return self.__conocimiento

    def setConocimiento(self, conocimiento:int):
        self.__conocimiento = conocimiento

    def toStr(self) -> str:
        return f"Bruja: {super().toStr()}, Magia: {self.__magia}, Conocimiento: {self.__conocimiento}"

    def pelear(self):
        return "La bruja golpea con su escoba"

    def usarMagia(self):
        return "La bruja usa su magia para hacer conversión"