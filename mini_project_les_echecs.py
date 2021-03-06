
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
    recueil = {"PB": pion_blanc, "RB": roi_blanc, "DB": dame_blanche,
               "FB": fou_blanc, "TB": tour_blanche, "CB": cavalier_blanc,
               "PN": pion_noir, "RN": roi_noir, "DN": dame_noire,
               "FN": fou_noir, "TN": tour_noire, "CN": cavalier_noir}
    return recueil.get(objet)

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
        prise = []
        col = arg[0]
        lig = int(arg[1])
        assert lig != 1, "pas de pion blanc dans la ligne 1 "
        if lig == 2:
            lig, lig_2 = str(lig + 2), str(lig + 1)
            a = num.index(arg[1])
            b = alpha.index(col) +1
            b_1 = alpha.index(col) -1
            if b in I:
                prise.append(alpha[b]+num[int(a)-1])
            if b_1 in I:
                prise.append(alpha[b_1]+num[int(a)-1])
            return [col + lig, col + lig_2],prise
        elif lig < 8:
            lig = str(lig + 1)
            a = num.index(arg[1])
            b = alpha.index(col) + 1
            b_1 = alpha.index(col) - 1
            if b in I:
                prise.append(alpha[b] + num[int(a)-1])
            if b_1 in I:
                prise.append(alpha[b_1] + num[int(a)-1])
            return [col + lig],prise
        elif lig == 8:
            return []


class pion_noir:
    number = 9823

    def mvt(self,arg):
        prise = []
        col = arg[0]
        lig = int(arg[1])
        assert lig != 8, "pas de pion noir a la ligne 8 "
        if lig == 7:
            lig, lig_2 = str(lig - 2), str(lig - 1)
            a = num.index(arg[1])
            b = alpha.index(col) + 1
            b_1 = alpha.index(col) - 1
            if b in I:
                prise.append(alpha[b] + num[int(a)+1])
            if b_1 in I:
                prise.append(alpha[b_1] + num[int(a)+1])
            return [col + lig, col + lig_2],prise
        elif lig > 1:
            lig = str(lig - 1)
            a = num.index(arg[1])
            b = alpha.index(col) + 1
            b_1 = alpha.index(col) - 1
            if b in I:
                prise.append(alpha[b] + num[int(a)+1])
            if b_1 in I:
                prise.append(alpha[b_1] + num[int(a)+1])
            return [col + lig],prise
        elif lig == 1:
            return []


class roi_blanc:
    number = 9812

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


class roi_noir:
    number = 9818

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


class tour_blanche:
    number = 9814

    def mvt(self,arg):
        res = [arg[0]+i for i in num if i != arg[1]]
        res+=[i+arg[1] for i in alpha if i != arg[0]]
        return res


class tour_noire:
    number = 9820

    def mvt(self,arg):
        res = [arg[0] + i for i in num if i != arg[1]]
        res += [i + arg[1] for i in alpha if i != arg[0]]
        return res


class fou_blanc:
    number = 9815

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


class fou_noir:
    number = 9821

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
        return res


class dame_blanche:
    number = 9813

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


class dame_noire:
    number = 9819

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


class cavalier_blanc:
    number = 9816

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


class cavalier_noir:
    number = 9822

    def mvt(self,arg):
        res = []
        col = arg[0]
        lig = arg[1]
        J = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i in J:
            a = alpha.index(col) + i[0] * 2
            b = num.index(lig) + i[1]
            if a in I and b in I:
                res.append(alpha[a] + num[b])
        for i in J:
            a = alpha.index(col) + i[0]
            b = num.index(lig) + i[1] * 2
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
    coor = arg[2::]
    objet = identificateur(arg)
    symbole = chr(objet.number)
    possibilite = objet.mvt(objet,coor)
    if len(possibilite) == 2 :
        for i in possibilite[1]:
            matrice=placeur(i,'●',matrice)
        possibilite = possibilite[0]
    for i in possibilite:
        matrice = placeur(i, "x", matrice)
    matrice = placeur(coor, symbole, matrice)
    return matrice