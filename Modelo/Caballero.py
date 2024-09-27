from Modelo.Personaje import Personaje

class Caballero(Personaje):

    __habilidadMartial:int
    __lealtad:int

    def __init__(self, id:str, nombre:str, nivel_Poder:int, habilidadMartial:int, lealtad:int):
        super().__init__(id, nombre, nivel_Poder)
        self.__habilidadMartial = habilidadMartial
        self.__lealtad = lealtad

    def getHabilidadMartial(self) -> int:
        return self.__habilidadMartial

    def setHabilidadMartial(self, habilidadMartial:int):
        self.__habilidadMartial = habilidadMartial

    def getLealtad(self) -> int:
        return self.__lealtad

    def setLealtad(self, lealtad:int):
        self.__lealtad = lealtad

    def toStr(self) -> str:
        return f"Caballero: {super().toStr()}, Habilidad Martial: {self.__habilidadMartial}, Lealtad: {self.__lealtad}"

    def pelear(self):
        return "El caballero pelea con artes marciales"