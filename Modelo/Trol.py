from Modelo.Personaje import Personaje
from Interface.Magia import Magia

class Trol(Personaje, Magia):

    __fuerza:int
    __resistencia:int

    def __init__(self, id:str, nombre:str, nivel_Poder:int, fuerza:int, resistencia:int):
        super().__init__(id, nombre, nivel_Poder)
        self.__fuerza = fuerza
        self.__resistencia = resistencia

    def getFuerza(self) -> int:
        return self.__fuerza

    def setFuerza(self, fuerza:int):
        self.__fuerza = fuerza

    def getResistencia(self) -> int:
        return self.__resistencia

    def setResistencia(self, resistencia:int):
        self.__resistencia = resistencia

    def toStr(self) -> str:
        return f"Trol: {super().toStr()}, Fuerza: {self.__fuerza}, Resistencia: {self.__resistencia}"

    def pelear(self):
        return "El trol pelea con súper fuerza para golpear el suelo"

    def usarMagia(self):
        return "El trol usa su magia para hacerse invisible"