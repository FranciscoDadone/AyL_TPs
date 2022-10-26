class ParserD(object):
    """
    Parser LL1
        Gramática original:
            S -> A
            S -> B
            A -> aA
            A -> ε
            B -> bB
            B -> ε

        Gramática LL1:
            S -> F
            S -> ε
            F -> aS
            F -> bS
    """

    def __init__(self):
        self.cadena = None

    def evaluate(self, cadena):
        """
        Evalúa la cadena
        :param cadena:
        :return True | False:
        """
        self.cadena = cadena
        self.S()
        return self.cadena[0] == "$"

    def S(self):
        print("S", self.cadena)
        if self.cadena[0] == "a":
            self.F()
        elif self.cadena[0] == "b":
            self.F()
        elif self.cadena[0] == "$":
            pass
        else:
            raise Exception("Error", "En S")

    def F(self):
        print("F", self.cadena)
        if self.cadena[0] == "a":
            self.match("a")
            self.S()
        elif self.cadena[0] == "b":
            self.match("b")
            self.S()
        elif self.cadena[0] == "$":
            pass
        else:
            raise Exception("Error", "En F")

    def match(self, s):
        print("M", self.cadena, s)
        if s == self.cadena[0]:
            self.cadena = self.cadena[1:]
        else:
            raise Exception("Error", "En Match")