import dataclasses
from typing import Optional


@dataclasses.dataclass
class Elemento:
    nombre: str


def __eq__(self, other):
    return e1 == e2


class Conjunto:
    CONTADOR = 0

    def __init__(self, nombre: str):
        self.lista: list[Elemento] = []
        self.nombre: str = nombre
        self.__class__.CONTADOR += 1
        self.__id = 2222

    @property
    def get_id(self):
        return self.__id

    def contiene(self, other_element: Elemento):
        return other_element in self.lista

    def agregar_elemento(self, other_element: Elemento):
        if self.contiene(other_element) is False:
            self.lista.append(other_element)
            print(self.lista)
        else:
            print("El elemento ya existe, no se puede agregar")


    def unir(self, c2):
        if self.contiene(c2) is False:
            self.lista.append(c2.lista)
            print(f"aaaaaaaaaaaaaaa{self.lista}")

    def __iadd__(self, c2):
        self.lista += c2.lista
        return self

    def intersectar(self, c1, c2):
        pass
e1 = Elemento("hola")
e2 = Elemento("hola")
c1 = Conjunto("a")
c2 = Conjunto("b")
# print(c1.CONTADOR)
# print(c1.get_id)
print(c1.contiene("hola"))
c1.agregar_elemento("hola")
print(c1.contiene("hola"))
c1.agregar_elemento("perro")
c2.agregar_elemento("pato")
#c1.unir(c2)
print(c1.lista + c2.lista) #Tengo dudas pero parece que funciona


