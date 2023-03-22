import dataclasses


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
        else:
            print("El elemento ya existe, no se puede agregar")

e1 = Elemento("hola")
e2 = Elemento("hola")
c1 = Conjunto("a")
c1.lista.append((e1.nombre))
print(c1.lista)
c1.agregar_elemento("hola")
# print(c1.CONTADOR)
# print(c1.get_id)
#print(c1.contiene("hola"))

