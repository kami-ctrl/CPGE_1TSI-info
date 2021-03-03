
"""
_________________________variable utile______________________
"""

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
num = ["8", "7", "6", "5", "4", "3", "2", "1"]
I = [0, 1, 2, 3, 4, 5, 6, 7]

"""
____________________fcts auxiliaires______________________
"""
def identificateur(arg):
    objet = arg[0:2]
    col = arg[2]
    lig = arg[3]
    assert col in alpha and lig in num, "impossible de placer abord "
    recueil = {"PB": pion_blanc, "RB": (roi,9812), "DB": (dame,9813),
               "FB": (fou,9815), "TB": (tour,9814), "CB": (cavalier,9816),
               "PN": pion_noir, "RN": (roi,9818), "DN": (dame,9819),
               "FN": (fou,9821), "TN": (tour,9820), "CN": (cavalier,9822)}
    data = recueil.get(objet)
    if objet == "PN" or objet == "PB":
        return data
    piece = data[0]
    piece.sys(piece,data[1])
    return piece

def placeur(arg, symb, matrice):
    col,lig = alpha.index(arg[0]), num.index(arg[1])
    matrice[lig][col] = symb
    return matrice

"""
________________________chess class def_________________
"""

class pion_blanc:
    number = 9817

    def mvt(self,arg):
        col = arg[0]
        lig = int(arg[1])
        assert lig != 1, "pas de pion blanc dans la ligne 1 "
        if lig == 2:
            lig, lig_2 = str(lig + 2), str(lig + 1)
            return [col + lig, col + lig_2]
        elif lig < 8:
            lig = str(lig + 1)
            return [col + lig]
        elif lig == 8:
            return []

class pion_noir:
    number = 9823

    def mvt(self,arg):
        col = arg[0]
        lig = int(arg[1])
        assert lig != 8, "pas de pion noir a la ligne 8 "
        if lig == 7:
            lig, lig_2 = str(lig - 2), str(lig - 1)
            return [col + lig, col + lig_2]
        elif lig > 1:
            lig = str(lig - 1)
            return [col + lig]
        elif lig == 1:
            return []

class roi:
    def sys(self, number):
        self.number = number

    def mvt(self,arg):
        res = []
        col = alpha.index(arg[0])
        lig = num.index(arg[1])
        for i in range(3):
            b = lig - 1 + i
            if b not in I:
                continue
            lig_1 = num[b]
            for j in range(3):
                a = col - 1 + j
                if a not in I:
                    continue
                col_1 = alpha[a]
                res.append(col_1 + str(lig_1))
        res.remove(arg)
        return res

class tour:
    def sys(self, number):
        self.number = number

    def mvt(self,arg):
        res = [arg[0]+i for i in num if i != arg[1]]
        res+=[i+arg[1] for i in alpha if i != arg[0]]
        return res

class fou:
    def sys(self, number):
        self.number = number

    def mvt(self,arg):
        res = []
        col = alpha.index(arg[0])
        lig = num.index(arg[1])
        for i in range(1,8) :
            a,b = col +i ,lig -i
            c,d = col -i ,lig +i
            if a in I and b  in I:
                res.append(alpha[a]+num[b])
            if c in I and d in I :
                res.append(alpha[c]+num[d])
            a, b = col + i, lig + i
            c, d = col - i, lig - i
            if a in I and b in I:
                res.append(alpha[a] + num[b])
            if c in I and d in I:
                res.append(alpha[c] + num[d])
        return res

class dame:
    def sys(self, number):
        self.number = number

    def mvt(self,arg):
        res = []
        col = alpha.index(arg[0])
        lig = num.index(arg[1])
        for i in range(1, 8):
            a, b = col + i, lig - i
            c, d = col - i, lig + i
            if a in I and b in I:
                res.append(alpha[a] + num[b])
            if c in I and d in I:
                res.append(alpha[c] + num[d])
            a, b = col + i, lig + i
            c, d = col - i, lig - i
            if a in I and b in I:
                res.append(alpha[a] + num[b])
            if c in I and d in I:
                res.append(alpha[c] + num[d])
        res += [arg[0] + i for i in num if i != arg[1]]
        res += [i + arg[1] for i in alpha if i != arg[0]]
        return res

class cavalier:
    def sys(self,number):
        self.number = number

    def mvt(self,arg):
        res = []
        col = arg[0]
        lig = arg[1]
        J = [(1,1),(1,-1),(-1,1),(-1,-1)]
        for i in J :
            a = alpha.index(col)+i[0]*2
            b = num.index(lig)+i[1]
            if a in I and b in I:
                res.append(alpha[a]+num[b])
        for i in J :
            a = alpha.index(col) + i[0]
            b = num.index(lig) + i[1]*2
            if a in I and b in I:
                res.append(alpha[a] + num[b])
        return res

"""
____________________main proramme__________________________
"""

def deplacer(arg):
    objet = identificateur(arg)
    coor = arg[2::]
    return objet.mvt(objet,coor)

def afficher(arg):
    matrice = [['_', '_', '_', '_', '_', '_', '_', '_'],
               ['_', '_', '_', '_', '_', '_', '_', '_'],
               ['_', '_', '_', '_', '_', '_', '_', '_'],
               ['_', '_', '_', '_', '_', '_', '_', '_'],
               ['_', '_', '_', '_', '_', '_', '_', '_'],
               ['_', '_', '_', '_', '_', '_', '_', '_'],
               ['_', '_', '_', '_', '_', '_', '_', '_'],
               ['_', '_', '_', '_', '_', '_', '_', '_']]
    objet = identificateur(arg)
    coor = arg[2::]
    possibilite = objet.mvt(objet, coor,)
    symbole = chr(objet.number)
    for i in possibilite:
        matrice = placeur(i, "x", matrice)
    matrice = placeur(coor, symbole, matrice)
    return matrice