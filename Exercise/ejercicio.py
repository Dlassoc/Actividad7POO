import dataclasses


@dataclasses.dataclass

class Elemento:
    nombre: str


def __eq__(self, other):
    return e1 == e2


e1 = Elemento("hola")
e2 = Elemento("hola")

class Conjunto:
    CONTADOR = 0
    def __init__(self, nombre: str):
        self.lista: list[Elemento] = []
        self.nombre: str = nombre
        self.__class__.CONTADOR +=1
        self.__id = 2222

    @property
    def get_id(self):
        return self.__id


    def contiene(self):
        print(e1|)

c1 = Conjunto("a")
print(c1.CONTADOR)
print(c1.get_id)
print(c1.contiene())


print(e1 == e2)
