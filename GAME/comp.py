from random import randint

class computer:
    def __init__(self, board:list, num: int):
        self.board=board  #The grid that is being played on
        self.whoAmI=num   #The computer ID (-1 for O, 1 for X)
        self.show_thought_process= False #Prints constantly the idea  behind the computer move

    def getNumTurns(self):
        """Finds how many turns have been taken previously"""
        turnsTaken=0
        for i in self.board:
            if i!=0: 
                turnsTaken+=1
        return turnsTaken

    def analysis(self):
        """Decides what is the best strategic move to play"""
        #Checks for a win in this turn
        About_To_Win= self.Is_MatchPoint(True)
        if About_To_Win!=0:
            #Play the winning move
            self.play= self.Block_Or_Win(About_To_Win)
            print(f'report: computer about to win\nmove: {self.play} WIN\n' if self.show_thought_process else '')
            return

        #Checks for a defeat in this turn
        About_To_Loose= self.Is_MatchPoint(False)
        if About_To_Loose!=0:
            #Block the opponent's win
            self.play= self.Block_Or_Win(About_To_Loose)
            print(f'report: opponent about to win\nmove: {self.play} BLOCK\n' if self.show_thought_process else '')
            return
        
        #Play the best move possible
        self.play=self.Best_Move()

    def Is_MatchPoint(self, Match_Point_For_Computer: bool):
        """Checks if one the computer or the player can win in this turn\n
            -> Param Match_Point_For_Computer: if true, we are checking if the computer can win, if not, we are checking if the player can win\n
            -> Return: The return of this function is a codenumber of whether victory/block is possible or 0 if not possible"""
        
        if Match_Point_For_Computer: 
            Searching_For= 2*self.whoAmI
        else:
            Searching_For=-2*self.whoAmI

        if self.board[0]+ self.board[4]+ self.board[8]== Searching_For:
            return 1 #Codenumber for diagonal win left to right
        
        if self.board[2]+self.board[4]+ self.board[6]== Searching_For:
            return 2 #Codenumber for diagonal win right to left

        for i in range (0,9):
            if i in [0, 3, 6]:
                if self.board[i]+self.board[i+1]+self.board[i+2]== Searching_For:
                    return (10+ i) #codenumber for a row win

            if i in [0, 1, 2]:
                if self.board[i]+self.board[i+3]+self.board[i+6]== Searching_For:
                    return (20+ i) #codenumber for a column win
                
        return 0 #Codenumber if win is not possible
    
    def Block_Or_Win(self, codenumber: int):
        """Finds the winning/blocking move\n
            -> Param codenumber: where we should look for the win/block\n
            -> Return: winning/blocking move"""
        match codenumber:
            case 1: #codenumber for diagonal win left to right
                indexesOfPossibleMoves=[0, 4, 8]

            case 2: #codenumber for diagonal win right to left
                indexesOfPossibleMoves=[2,4,6]

            case x if 9<x<18: #codenumbers for row wins
                indexesOfPossibleMoves=[x-10, x-9, x-8]

            case y if 19<y<28: #codenumber for column wins
                indexesOfPossibleMoves=[y-20, y-17, y-14]

            case _: #in case of error, and the codenumber provided doesn't match any of the previous cases
                return self.Random_Move()

        for i in indexesOfPossibleMoves:
            if self.board[i]==0:
                return i
    
    def Random_Move(self):
        """Finds a random available spot in the board for the computer to make it's move"""
        while True:
            RandomMove=randint(0,8)
            if self.board[RandomMove]==0:
                break

        return RandomMove
    
    def Best_Move(self):
        """Finds the best stategic course of action"""
        numTurns= self.getNumTurns() 
        corners=[0,2,6,8]
        cornerOccupied=0
        middle=4
        match numTurns:
            case 0:
                self.firstMove= corners[randint(0,3)]
                print (f'We are the first player \nmove: {self.firstMove} CORNER\n' if self.show_thought_process else '')
                return self.firstMove
            case 1:
                for i in corners:
                    if self.board[i]!=0:
                        cornerOccupied=i
                        break

                if self.board[middle]==0:
                    self.firstMove= middle
                    print(f'We are the second player \nreport: middle unnocupied \nmove: 4 MIDDLE\n' if self.show_thought_process else '')
                
                else:
                    self.firstMove= corners[randint(0,3)]
                    while self.firstMove == cornerOccupied:
                        self.firstMove= corners[randint(0,3)]
                    print(f'We are the second player \nreport:middle occupied \nmove: {self.firstMove} CORNER\n' if self.show_thought_process else '')
                return self.firstMove
                
            case 2:
                if self.board[4]==-1*self.whoAmI:
                    print('report: the opponent responded middle, tie is likely\n' if self.show_thought_process else '')
                if self.firstMove%6==0:
                    plan=self.firstMove+2
                    if self.board[plan]==0 and self.board[self.firstMove+1]==0:
                        self.secondMove= plan
                    
                    else:
                        if self.firstMove==0:
                            self.secondMove=6                      
                        else:
                            self.secondMove=0
                       
                else:
                    plan=self.firstMove-2
                    if self.board[plan]==0 and self.board[self.firstMove-1]==0:
                        self.secondMove= plan
                   
                    else:
                        if self.firstMove==2:
                            self.secondMove=8
                        else:
                            self.secondMove=2

                if self.secondMove==plan:
                    print(f'report: trying horizontal line\nmove: {self.secondMove} CORNER\n' if self.show_thought_process else '')

                else:
                    print(f'report: trying vertical line\nmove: {self.secondMove} CORNER\n' if self.show_thought_process else '')  
                
                return self.secondMove

                    
            case 3:
                if self.firstMove==middle:
                    Hline= self.board[3]+self.board[5]
                    Vline= self.board[1]+self.board[7]
                    if Vline== -2*self.whoAmI or Hline==-2*self.whoAmI:
                        self.secondMove= corners[randint(0,3)]
                        print(f'report: opponent made mistake\n move: {self.secondMove} CORNER\n' if self.show_thought_process else '') 

                if not hasattr(self, 'secondMove'):
                    self.secondMove= self.Random_Move()
                    print(f'report: tie most likely\nmove: {self.secondMove} RANDOM\n' if self.show_thought_process else '') 

                return self.secondMove 
                        
            case 4:
                tri= self.secondMove-self.firstMove
                match tri:    
                    case x if x==2 or x==-2:
                        if self.board[3]==0 and self.board[0]==0 and 6 in [self.firstMove, self.secondMove]:
                            self.thirdMove=0

                        elif self.board[3]!=0 and self.board[2]==0 and 6 in [self.firstMove, self.secondMove]:
                            self.thirdMove=2
                    
                        elif self.board[3]==0 and self.board[6]==0 and 0 in [self.firstMove, self.secondMove]:
                            self.thirdMove=6

                        elif self.board[3]!=0 and self.board[8]==0 and 0 in [self.firstMove, self.secondMove]:
                            self.thirdMove=8           

                    case y if y==6 or y==-6:
                        if self.board[1]==0 and self.board[2]==0 and 6 in [self.firstMove, self.secondMove]:
                            self.thirdMove=2

                        elif self.board[1]!=0 and self.board[8]==0 and 6 in [self.firstMove, self.secondMove]:
                            self.thirdMove= 8
                    
                        elif self.board[1]==0 and self.board[0]==0 and 8 in [self.firstMove, self.secondMove]:
                            self.thirdMove= 0

                        elif self.board[1]!=0 and self.board[6]==0 and 8 in [self.firstMove, self.secondMove]:
                            self.thirdMove=6  
                        
                if not hasattr(self, 'thirdMove'):
                    self.thirdMove=self.Random_Move() 
                    print(f'report: ERROR! \nmove: {self.thirdMove} RANDOM\n' if self.show_thought_process else '') 

                else:
                    print(f'report: we closed the triangle\nmove: {self.thirdMove} CORNER\n' if self.show_thought_process else '')
                
                return self.thirdMove
                        
                        
            case _:
                RandomMove= self.Random_Move()
                print(f'report: playing random move\nmove: {RandomMove} RANDOM\n' if self.show_thought_process else '')
                return RandomMove
    
                 
test=[
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
]      

#c=computer(test, 1)
#c.analysis()
#g= c.play
