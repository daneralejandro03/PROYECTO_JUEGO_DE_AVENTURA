from Modelo.Personaje import Personaje

class JuegoAventura:

    __id:str
    __nombre:str
    __informacion:str

    __personajes = list[Personaje]

    def __init__(self, id:str, nombre:str, informacion:str):
        self.__id = id
        self.__nombre = nombre
        self.__informacion = informacion
        self.__personajes = []

    def getId(self):
        return self.__id

    def setId(self, id:str):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre:str):
        self.__nombre = nombre

    def getInformacion(self):
        return self.__informacion

    def setInformacion(self, informacion:str):
        self.__informacion = informacion

    def getPersonajes(self):
        return self.__personajes

    def setPersonajes(self, personajes:list[Personaje]):
        self.__personajes = personajes

    def addPersonaje(self, personaje:Personaje):
        self.__personajes.append(personaje)

    def removePersonaje(self, personaje:Personaje):
        for i in range(len(self.__personajes)):
            if self.__personajes[i].getId() == personaje.getId():
                self.__personajes.pop(i)
                break
        return self.__personajes

    def toStr(self) -> str:
        return f"Juego de Aventura: {self.__id}, Nombre: {self.__nombre}, Informacion: {self.__informacion}"
