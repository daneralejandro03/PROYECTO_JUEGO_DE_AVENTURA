from abc import ABC, abstractmethod

# IArmas como una interfaz (clase abstracta)
class IArmas(ABC):

    @abstractmethod
    def usarArma(self):
        print("El personaje usa su arma para atacar")
        pass
