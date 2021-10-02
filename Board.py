
from Piece import Piece
class Board:
    def __init__(self):
        self.r = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.m = int(len(self.r))
        self.c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        self.n = int(len(self.c))
        self.board = self.getBoard()
    def getBoard(self):
        self.board = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                s = str(self.c[j]+self.r[i])
                p = Piece(0, s)
                row.append(p)
            self.board.append(row)
        return self.board
    
    def getSquares(self):
        squares = []
        for i in range(len(self.r)):
            for j in range(len(self.c)):
                p = self.board[i][j]
                squares.append(str(p.square))
        return squares
    def isEqual(self, other):
        k = 0
        for i in range(self.m):
            for j in range(self.n):
                p = self.board[i][j]
                p1 = other.board[i][j]
                if p.value == p1.value:
                    continue
                else:
                    k += 1
        if k == 0:
            return True
        else:
            return False
    def clone(self):
        other = Board()
        other.board = self.board
        return other
    
    def checkRow(self, i):
        row = self.board[i]
        k = 0
        for j in range(len(row)):
            if row[j].value == self.num:
                k += 1
            else:
                continue
        if k == 0:
            return True
        else:
            print(str(self.num)+' is already in line.')
            return False
    def checkCol(self, j):
        b = self.board
        k = 0
        for i in range(len(b)):
            if b[i][j].value == self.num:
                k += 1
            else:
                continue
        if k == 0:
            return True
        else:
            print(str(self.num)+' is already in column.')
            return False
    def checkSquare(self):
        #self, i, j, num
            return True
    def addPiece(self):
        sq = ''
        while sq not in self.getSquares():
            sq = str(input('Import square: '))
            print(sq)
        num = ''
        L = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        while num not in L:
            num = str(input('Import number: '))
        self.num = int(num)
        #i = self.m-int(sq[1])
        i = int(sq[1])-1
        
        if self.checkRow(i) == True:
            j = 'abcdefghi'.find(sq[0])
            if self.checkCol(j) == True:
                if self.checkSquare() == True:
                    if self.board[i][j].value == 0:
                        pass
                    else:
                        while self.board[i][j].value != 0:
                            i = self.m-int(sq[1])
                            j = 'abcdefghi'.find(sq[0])
                    self.board[i][j].value = self.num
                    return self
    def __str__(self):
        bord = ''
        for i in range(self.m):
            row = '|'
            for j in range(self.n):
                row += str(self.board[i][j])
            bord += row + '\n'
        bord += '*********'*self.n + '\n'
        return bord
