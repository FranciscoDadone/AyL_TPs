class ParserB(object):
    """
   Parser LL1
       Gramática original:
            S → aAS | b
            A → a | bSA
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
            self.match("a")
            self.A()
            self.S()
        elif self.cadena[0] == "b":
            self.match("b")
        else:
            raise Exception("Error", "En S")

    def A(self):
        print("T", self.cadena)
        if self.cadena[0] == "a":
            self.match("a")
        elif self.cadena[0] == "b":
            self.match("b")
            self.S()
            self.A()
        else:
            raise Exception("Error", "En T")

    def match(self, s):
        print("M", self.cadena, s)
        if s == self.cadena[0]:
            self.cadena = self.cadena[1:]
        else:
            raise Exception("Error", "En Match")