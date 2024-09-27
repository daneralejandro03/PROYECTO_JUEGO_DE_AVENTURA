from Modelo.Arma import Arma

class ArcoFlecha(Arma):

    __rango:float
    __material_Cuerda:str

    def __init__(self, id:str, información:str, daño:int, durabilidad:int, tipo:str, rango:float, material_Cuerda:str):
        super().__init__(id, información, daño, durabilidad, tipo)
        self.__rango = rango
        self.__material_Cuerda = material_Cuerda

    def getRango(self) -> float:
        return self.__rango

    def setRango(self, rango:float):
        self.__rango = rango

    def getMaterial_Cuerda(self) -> str:
        return self.__material_Cuerda

    def setMaterial_Cuerda(self, material_Cuerda:str):
        self.__material_Cuerda = material_Cuerda

    def toStr(self) -> str:
        return f"Arco y Flecha: {super().toStr()}, Rango: {self.__rango}, Material de la Cuerda: {self.__material_Cuerda}"

    def usarArma(self):
        return f"{super().usarArma()}: El arco y flecha ataca con sus flechas"