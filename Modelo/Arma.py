from abc import ABC, abstractmethod
from Interface.IArmas import IArmas
from Modelo import Personaje

class Arma(IArmas):

    __id:str
    __información:str
    __daño:int
    __durabilidad:int
    __tipo:str

    __Personaje = Personaje

    def __init__(self, id:str, información:str, daño:int, durabilidad:int, tipo:str):
        self.__id = id
        self.__información = información
        self.__daño = daño
        self.__durabilidad = durabilidad
        self.__tipo = tipo
        self.__Personaje = None

    def getId(self) -> str:
        return self.__id

    def setId(self, id:str):
        self.__id = id

    def getInformación(self) -> str:
        return self.__información

    def setInformación(self, información:str):
        self.__información = información

    def getDaño(self) -> int:
        return self.__daño

    def setDaño(self, daño:int):
        self.__daño = daño

    def getDurabilidad(self) -> int:
        return self.__durabilidad

    def setDurabilidad(self, durabilidad:int):
        self.__durabilidad = durabilidad

    def getTipo(self) -> str:
        return self.__tipo

    def setTipo(self, tipo:str):
        self.__tipo = tipo

    @abstractmethod
    def toStr(self) -> str:
        return f"Arma: {self.__id}, Información: {self.__información}, Daño: {self.__daño}, Durabilidad: {self.__durabilidad}, Tipo: {self.__tipo}"
        pass

    @abstractmethod
    def usarArma(self):
        return "El personaje usa su arma para atacar"
        pass
