class virus:
    def start(self, n):
        assert n > 2; "must be at least 3x3"
        N , B = chr(9679),chr(9675)
        self.inter = range(n)
        self.data = [[B,(0,n-1)],[B,(n-1,0)],[N,(0,0)],[N,(n-1,n-1)]]
        matrice = [["" for _ in self.inter] for _ in self.inter]
        for i, j in [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]:
            if i == j:  matrice[i][j] = chr(9679)
            else:       matrice[i][j] = chr(9675)
        self.table = matrice

    def check(self):
        b = sum([1 for i in self.data if i[0] == chr(9675)])
        n = sum([1 for i in self.data if i[0] == chr(9679)])
        return b, n

    def move(self, color, coor):
        coord = (coor[0] - 1, coor[1] - 1)
        for i, j in self.data: assert j != coord ; "can't place it  over another pion"
        self.data.append([color, coord])
        self.table[coord[0]][coord[1]] = color
        possibite,update  = [], []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                x, y = coord[0] + i, coord[1] + j
                if x in self.inter and y in self.inter:
                    possibite.append((x, y))
        for k in self.data:
            for i in possibite:
                if i in k:
                    k[0] = color
                    update.append(k)
        for i, (j, k) in update:
            self.table[j][k] = i


class pion:
    def __init__(self, color):
        if color == "blanc":  self.color = chr(9675)
        else:                 self.color = chr(9679)


def afficher(matrice):
    for i in matrice:
        print(i, end="\n")


def jouer(n):
    virus.start(virus, n)
    player_1 = pion("blanc")
    player_2 = pion('noir')
    while True:
        for i in [player_1, player_2]:
            ch = virus.check(virus)
            if ch[0] + ch[1] == n ** 2:
                Player_1_blanc = ch[0], 'Player_1_blanc'
                Player_2_noir = ch[1], 'Player_2_noir'
                win = max(Player_1_blanc, Player_2_noir, key=lambda x: x[0])
                print(f"the winner is {win[1]} acheving the score of {win[0]} agaisnt {n**2-win[0]}")
                return 'FIN'
            while True:
                k = int(input(f"enter the coordonnates << ligne >> of ur piece from 1 to {n}"))
                l = int(input(f"enter the coordonnates << raw >> of ur piece from 1 to {n}"))
                if k in range(1, n + 1) and l in range(1, n + 1):break
            virus.move(virus, i.color, (k, l))
            afficher(virus.table)