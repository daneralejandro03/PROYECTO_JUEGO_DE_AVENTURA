from Modelo.Arma import Arma

class Cuchillo(Arma):

    __longitud:float
    __tipo_Cuchillo:str

    def __init__(self, id:str, información:str, daño:int, durabilidad:int, tipo:str, longitud:float, tipo_Cuchillo:str):
        super().__init__(id, información, daño, durabilidad, tipo)
        self.__longitud = longitud
        self.__tipo_Cuchillo = tipo_Cuchillo

    def getLongitud(self) -> float:
        return self.__longitud

    def setLongitud(self, longitud:float):
        self.__longitud = longitud

    def getTipo_Cuchillo(self) -> str:
        return self.__tipo_Cuchillo

    def setTipo_Cuchillo(self, tipo_Cuchillo:str):
        self.__tipo_Cuchillo = tipo_Cuchillo

    def toStr(self) -> str:
        return f"Cuchillo: {super().toStr()}, Longitud: {self.__longitud}, Tipo de Cuchillo: {self.__tipo_Cuchillo}"

    def usarArma(self):
        return f"{super().usarArma()}: El cuchillo ataca con su filo"
