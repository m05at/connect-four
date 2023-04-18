import random
test = [[0,1,2,3,4,5,6],
[0,1,2,3,4,5,6],
[0,1,2,3,4,5,6],
[0,1,2,3,4,5,6],
[0,1,2,3,4,5,6],
[0,1,2,3,4,5,6]]


class fgColor:
    reset = '\033[m'
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'

class bgColor:
    black='\033[40m'
    red='\033[41m'
    green='\033[42m'
    orange='\033[43m'
    blue='\033[44m'
    purple='\033[45m'
    cyan='\033[46m'
    lightgrey='\033[47m'

    
class Game:
    def __init__(self):

        self.board = [[' ' for i in range(7)] for i in range(6)]
        while True:
            x = input('Do you want 1 player or 2 player? : ')
            if x == '1':
                while True:
                    y = input('Do you want easy or hard? (E/H) : ').lower()
                    if y.startswith('e'):
                        opp = 'comp_easy'
                        break
                    elif y.startswith('h'):
                        opp = 'comp_hard'
                        break
                break
            elif x == '2':
                opp = 'player'
                break
        self.printboard()
        while True:
            self.playerMove('X')
            self.printboard()
            if self.checkWins('X',self.board):
                print(f"{fgColor.green}X{fgColor.reset} wins!")
                break
            if opp == 'comp_easy':
                self.randomCompMove()
            elif opp == 'comp_hard':
                self.HardCompMove()
            elif opp == 'player':
                self.playerMove('O')
            else:
                print('Error')
                break
            self.printboard()
            if self.checkWins('O',self.board):
                print(f"{fgColor.green}O{fgColor.reset} wins!")
                break
            #Check for wins
    def printboard(self):
        for i in self.board:
            for j in i:
                #print(j)
                if j == 'X':
                    print(f"{fgColor.red} X {fgColor.reset}",end=f"{fgColor.blue}|{fgColor.reset}")
                elif j == 'O':
                    print(f"{fgColor.yellow} O {fgColor.reset}",end=f"{fgColor.blue}|{fgColor.reset}")
                else:
                    print(f"{fgColor.blue}   |{fgColor.reset}",end='')
            print()
        print()


    def playerMove(self,le):
        i = 0
        while True:
            i = input('Enter position for ' + le +  ' (1-7) : ')
            if i in ['1','2','3','4','5','6','7']:
                i = int(i) - 1
                if self.place(self.board,le,i):
                    break
                else:
                    print('This column is full!')

    def randomCompMove(self):
        i = random.randint(0,6)
        self.place(self.board,'O',i)

    
    #def canPlace(self,i):
    #    if self.board[0][i] == ' ':
    #        return False
    #    return True

    def place(self,board,le,i):
        if board[0][i] == ' ':
            for row in range(5,-1,-1):
                if board[row][i] == ' ':
                    board[row][i] = le
                    return True
    def checkWins(self,le,bo):
        r = self.checkRows(bo)
        c = self.checkCol(bo)
        d = self.checkDiag(bo)
        if r == le or c == le or d == le:
            return True
    def checkRows(self,bo):
        for i in range(6):
            for j in range(4):
                if bo[i][j] != ' ':
                    if bo[i][j] == bo[i][j + 1] == bo[i][j + 2] == bo[i][j + 3]:
                        return  bo[i][j]

    def checkCol(self,bo):
        for col in range(7):
            for row in range(3):
                if bo[row][col] != ' ':
                    if bo[row][col] == bo[row+1][col] == bo[row+2][col] == bo[row+3][col]:
                        return bo[row][col]

    def checkDiag(self,bo):
        for num in range(3):
            # Diagonals from top left to bottom right -- \
            for i in range(4):
                if bo[num][i] != ' ':
                    if bo[num][i] == bo[num+1][i+1] == bo[num+2][i+2] == bo[num+3][i+3]:
                        return bo[num][i]
            # Diagonals from top right to bottom left -- /
            for i in range(6,-1,-1):
                if bo[num][i] != ' ':
                    if bo[num][i] == bo[num+1][i-1] == bo[num+2][i-2] == bo[num+3][i-3]:
                        return bo[num][i]

    def copyBoard(self):
        boardCopy = []
        for i in self.board:
            row = []
            for j in i:
                row.append(j)
            boardCopy.append(row)
            
        return boardCopy
    def HardCompMove(self):
        for i in range(7):
            c = self.copyBoard()
            if self.place(c,'O',i):
                if self.checkWins('O',c):
                    self.place(self.board,'O',i)
                    return

        for i in range(7):
            c = self.copyBoard()
            if self.place(c,'X',i):
                if self.checkWins('X',c):
                    self.place(self.board,'O',i)
                    return

        x = random.randint(0,6)
        if not self.place(self.board,'O',x):
            print('Error')
                    
        
Game()

#for i,v in enumerate(test):
#    print(i,v)