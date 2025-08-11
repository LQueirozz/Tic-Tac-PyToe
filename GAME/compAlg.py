from random import randint
class computer:
    def __init__(self, board:list, num: int):
        self.board=board  #The grid that is being played on
        self.whoAmI=num   #The computer ID (-1 for O, 1 for X)
        self.show_thought_process= False #Prints constantly the idea  behind the computer move

    def Get_Num_Turns(self):
        """Finds how many turns have been taken previously"""
        turnsTaken=0
        for i in self.board:
            if i!=0: 
                turnsTaken+=1
        return turnsTaken
    
    def Get_Empty_Positions(self):
        empties= list()
        for i in range(0,9):
            if self.board[i]==0:
                empties.append(i)

        return empties
    
    def mini_max(self, depth, is_maximizing:bool):
        board=self.board
        score= self.Victory()
 
        if score==10:
            return score-depth
        
        elif score==-10:
            return score+depth
        
        if self.Board_Full():
            return 0

        if is_maximizing:
            bestScore=-11
            for position in self.Get_Empty_Positions():
                board[position]= self.whoAmI

                score=self.mini_max(depth+1, False)
                if score>bestScore:
                    bestScore=score

                board[position]=0

            return bestScore
        
        else:
            bestScore=11
            for position in self.Get_Empty_Positions():
                board[position]= -1*self.whoAmI

                score=self.mini_max(depth+1, True)
                if score<bestScore:
                    bestScore=score

                board[position]=0

            return bestScore
            
    def Best_Score(self):
        bestScore=-100
        bestMove=-1
        board=self.board

        for position in self.Get_Empty_Positions():
            board[position]= self.whoAmI

            score=self.mini_max(0, False)
            if score>bestScore:
                bestScore=score
                bestMove=position
            
            board[position]=0

        return bestMove



    def Victory(self):
        """Checks if one the computer or the player has won\n"""
        board= self.board
        winning_patterns= [
            [0, 4, 8], [2, 4, 6],
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8]
        ]

        for pattern in winning_patterns:
            sum=0
            for position in pattern:
                sum+= board[position]

            if sum==3*self.whoAmI:
                return 10
        
            elif sum==-3*self.whoAmI:
                return -10
        
        return 0
        
    def Board_Full(self):
        if 0 not in self.board:
            return True
        
        else:
            return False
    
