class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)

    def imprimir(self, nivel=0):
        print("  " * nivel + self.valor)
        for h in self.hijos:
            h.imprimir(nivel + 1)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consumir(self, token):
        if self.actual() == token:
            self.pos += 1
        else:
            raise Exception(f"Error sintáctico: se esperaba {token}")

    def E(self):
        nodo = Nodo("E")
        nodo.agregar_hijo(self.T())
        nodo.agregar_hijo(self.Ep())
        return nodo

    def Ep(self):
        nodo = Nodo("E'")
        if self.actual() == '+':
            self.consumir('+')
            nodo.agregar_hijo(Nodo('+'))
            nodo.agregar_hijo(self.T())
            nodo.agregar_hijo(self.Ep())
        else:
            nodo.agregar_hijo(Nodo("ε"))
        return nodo

    def T(self):
        nodo = Nodo("T")
        nodo.agregar_hijo(self.F())
        nodo.agregar_hijo(self.Tp())
        return nodo

    def Tp(self):
        nodo = Nodo("T'")
        if self.actual() == '*':
            self.consumir('*')
            nodo.agregar_hijo(Nodo('*'))
            nodo.agregar_hijo(self.F())
            nodo.agregar_hijo(self.Tp())
        else:
            nodo.agregar_hijo(Nodo("ε"))
        return nodo

    def F(self):
        nodo = Nodo("F")
        if self.actual() == '(':
            self.consumir('(')
            nodo.agregar_hijo(Nodo('('))
            nodo.agregar_hijo(self.E())
            self.consumir(')')
            nodo.agregar_hijo(Nodo(')'))
        elif self.actual() == 'id':
            self.consumir('id')
            nodo.agregar_hijo(Nodo('id'))
        else:
            raise Exception("Error en F")
        return nodo


# PRUEBA
tokens = ['id', '+', 'id', '*', 'id']
parser = Parser(tokens)
arbol = parser.E()
arbol.imprimir()