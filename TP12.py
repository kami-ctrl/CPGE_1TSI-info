# ------------------------------------source------------------------------------------
"""

python source code
link = https://github.com/kami-ctrl/CPGE_1TSI-info/blob/main/TP12.py

"""


# ----------------------------------pile class----------------------------------------
class Pile:
    def __init__(self):
        self.stack = []

    def ajouter(self, code):
        self.stack.append(code)

    def retirer(self):
        return self.stack.pop()

    def dernier(self):
        return self.stack[-1] if len(self.stack) != 0 else None

    def vide(self):
        return len(self.stack) == 0


# -------------------------------------------EX3-----------------------------------------------------


def estOuvrante(caractere):
    return caractere in ["(", "[", "{"]


def estFerme(caractere):
    return caractere in [")", "]", "}"]


def analyse(expression):
    """
    prend les mots compose de parenthése uniqument et renvoie True si ils sont bien ordonée
    sinon renvoie False
    :param expression:
    :return: Bool
    >>> analyse("[()(())]")
    True
    >>> analyse("{(}(()())))")
    False
    """
    pile = Pile()
    recueil = {")": "(", "]": "[", "}": "{"}
    for i in expression:
        if estOuvrante(i):
            pile.ajouter(i)
        elif estFerme(i):
            ouvert = recueil[i]
            dernier = pile.dernier()
            if dernier == ouvert:
                pile.retirer()
            else:
                return False
    return pile.vide()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)


# --------------------------------------------EX4----------------------------------------------------


def estOperateur(caratere):
    return caratere in ["+", "-", "*", "/"]


def evaluer(expression):
    """
    renvoi le résultat apres avoir décodé la forme post fixé
    :param expression:
    :return: float
    >>> evaluer("53+2*")
    16.0
    >>> evaluer("352*+")
    13.0
    """
    pile = Pile()
    for i in expression:
        if estOperateur(i):
            a = pile.retirer()
            b = pile.retirer()
            c = eval(a + i + b)
            pile.ajouter(str(c))
        else:
            pile.ajouter(i)
    return float(pile.stack[0])


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
