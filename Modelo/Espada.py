from Modelo.Arma import Arma

class Espada(Arma):

    __longitud:float
    __material:str

    def __init__(self, id:str, información:str, daño:int, durabilidad:int, tipo:str, longitud:float, material:str):
        super().__init__(id, información, daño, durabilidad, tipo)
        self.__longitud = longitud
        self.__material = material

    def getLongitud(self) -> float:
        return self.__longitud

    def setLongitud(self, longitud:float):
        self.__longitud = longitud

    def getMaterial(self) -> str:
        return self.__material

    def setMaterial(self, material:str):
        self.__material = material

    def toStr(self) -> str:
        return f"Espada: {super().toStr()}, Longitud: {self.__longitud}, Material: {self.__material}"

    def usarArma(self):
        return f"{super().usarArma()}: La espada ataca con su filo"
