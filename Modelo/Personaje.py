from platform import release

from Modelo.Arma import Arma
from Interface.IArmas import IArmas
from Modelo import JuegoAventura

from abc import ABC, abstractmethod

class Personaje(ABC):

    __id:str
    __nombre:str
    __nivel_Poder:int

    __armas: list[Arma]
    __arma: IArmas
    __juegoaventura: JuegoAventura

    def __init__(self, id:str, nombre:str, nivel_Poder:int):
        self.__id = id
        self.__nombre = nombre
        if 30 <= nivel_Poder <= 100:
            self.__nivel_Poder = nivel_Poder
        else:
             raise ValueError("El nivel de poder debe estar entre 30 y 100")

        self.__armas = []
        self.__arma = None

    def getId(self):
        return self.__id

    def setId(self, id:str):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre:str):
        self.__nombre = nombre

    def getArmas(self):
        return self.__armas

    def setArmas(self, armas:list[Arma]):
        self.__armas = armas

    def addArma(self, arma:Arma):
        self.__armas.append(arma)

    def removeArma(self, arma:Arma):
        for i in range(len(self.__armas)):
            if self.__armas[i].getId() == arma.getId():
                self.__armas.pop(i)
                break
        return self.__armas

    def getArma(self):
        return self.__arma

    def setArma(self, arma: IArmas) -> None:
        self.__arma = arma

    @property
    def getNivel_Poder(self):
        return self.__nivel_Poder

    @getNivel_Poder.setter
    def setNivel_Poder(self, nivel_Poder:int):
        if 30 <= nivel_Poder <= 100:
            self.__nivel_Poder = nivel_Poder
        else:
            print("El nivel de poder debe estar entre 30 y 100")

    @abstractmethod
    def toStr(self) -> str:
        return f"Personaje: {self.__id}, Nombre: {self.__nombre}, Nivel de Poder: {self.__nivel_Poder}"
        pass

    @abstractmethod
    def pelear(self):
        pass
