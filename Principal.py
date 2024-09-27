from Modelo.JuegoAventura import JuegoAventura
from Modelo.Reina import Reina
from Modelo.Rey import Rey
from Modelo.Caballero import Caballero
from Modelo.Trol import Trol
from Modelo.Bruja import Bruja
from Modelo.Espada import Espada
from Modelo.ArcoFlecha import ArcoFlecha

def Principal():

    print("Juego de Aventura\n")
    nuevoJuego = JuegoAventura("1","Juego de Aventura","Juego de Aventura con personajes y armas")
    print(nuevoJuego.toStr())

    personaje1 = Reina("1","Iabel",90,100,100)
    personaje2 = Rey("2","Arturo",100,100,100)
    personaje3 = Caballero("3","Lancelot",100,100,100)
    personaje4 = Trol("4","Trol",50,100,100)
    personaje5 = Bruja("5","Morgana",70,100,100)

    nuevoJuego.addPersonaje(personaje1)
    nuevoJuego.addPersonaje(personaje2)
    nuevoJuego.addPersonaje(personaje3)
    nuevoJuego.addPersonaje(personaje4)
    nuevoJuego.addPersonaje(personaje5)
    print("\nPersonajes del Juego de Aventura:")
    for i in nuevoJuego.getPersonajes():
        print(i.toStr())

    arma1 = Espada("1","Espada",100,100,"Espada",10,"Acero")
    arma2 = ArcoFlecha("2","Arco y Flecha",100,100,"Arco y Flecha",20,"Madera")

    personaje1.addArma(arma1)
    personaje1.addArma(arma2)

    personaje1.setArma(personaje1.getArmas()[0])

    print("\nLista de Armas del Personaje: Caballero")
    indice = 0
    while indice < len(personaje1.getArmas()):
        print(f"{indice}. {personaje1.getArmas()[indice].toStr()}")
        indice += 1

    print("\nUsar Arma del Caballero:")
    print(personaje1.getArma().usarArma())

    print("\nVoy a usar el personaje Trol")
    print(personaje4.toStr())

    print("\nVoy a usar la magia del Trol")
    print(personaje4.usarMagia())

if __name__ == "__main__":
    Principal()