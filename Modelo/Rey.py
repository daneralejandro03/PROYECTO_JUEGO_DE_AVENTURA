from Modelo.Personaje import Personaje

class Rey(Personaje):

    __liderazgo: int
    __sabiduria: int

    def __init__(self, id:str, nombre:str, nivel_Poder:int, liderazgo:int, sabiduria:int):
        super().__init__(id, nombre, nivel_Poder)
        self.__liderazgo = liderazgo
        self.__sabiduria = sabiduria

    def getLiderazgo(self) -> int:
        return self.__liderazgo

    def setLiderazgo(self, liderazgo:int):
        self.__liderazgo = liderazgo

    def getSabiduria(self) -> int:
        return self.__sabiduria

    def setSabiduria(self, sabiduria:int):
        self.__sabiduria = sabiduria

    def toStr(self) -> str:
        return f"Rey: {super().toStr()}, Liderazgo: {self.__liderazgo}, Sabiduria: {self.__sabiduria}"

    def pelear(self):
        return "El rey pelea con patadas"