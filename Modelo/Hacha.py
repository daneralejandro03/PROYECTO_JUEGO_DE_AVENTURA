from Modelo.Arma import Arma

class Hacha(Arma):

    __peso:float
    __tipo_Hacha:str

    def __init__(self, id:str, información:str, daño:int, durabilidad:int, tipo:str, peso:float, tipo_Hacha:str):
        super().__init__(id, información, daño, durabilidad, tipo)
        self.__peso = peso
        self.__tipo_Hacha = tipo_Hacha

    def getPeso(self) -> float:
        return self.__peso

    def setPeso(self, peso:float):
        self.__peso = peso

    def getTipo_Hacha(self) -> str:
        return self.__tipo_Hacha

    def setTipo_Hacha(self, tipo_Hacha:str):
        self.__tipo_Hacha = tipo_Hacha

    def toStr(self) -> str:
        return f"Hacha: {super().toStr()}, Peso: {self.__peso}, Tipo de Hacha: {self.__tipo_Hacha}"

    def usarArma(self):
        return f"{super().usarArma()}: El hacha ataca con su filo"