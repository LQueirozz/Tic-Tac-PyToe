import config
class Win_Or_Draw:
    def __init__(self):
        pass
    
    @staticmethod
    def Win(lst: list):
        if lst[0]==lst[4]==lst[8]!=0:
            return (0,8)
        
        if lst[2]==lst[4]==lst[6]!=0:
            return (2,6)
        
        for i in range (0,9):
            if i in [0, 3, 6]:
                if lst[i]==lst[i+1]==lst[i+2] !=0:
                    return(i, i+2)

            if i in [0, 1, 2]:
                if lst[i]==lst[i+3]==lst[i+6] !=0:
                    return(i, i+6)
            
        return ()
            
  
    @staticmethod
    def Calculate_Line(vicTup:tuple):
        positions= config.O_POS
        a= vicTup[0]
        b= vicTup[1]
        c=b-a
        match c:
            case 8:
                Xstart= positions[0][0]-60
                Ystart= positions[0][1]-60

                Xend= positions[8][0]+ 60
                Yend= positions[8][1]+60

            case 4:
                Xstart= positions[2][0]+60
                Ystart=positions[2][1]-60

                Xend= positions[6][0]-60
                Yend=positions[6][1]+60

            case 2:
                Xstart= positions[a][0]-60
                Ystart= positions[a][1]

                Xend= positions[b][0]+ 60
                Yend= positions[b][1]

            case 6:
                Xstart= positions[a][0]
                Ystart= positions[a][1]-60

                Xend= positions[b][0]
                Yend= positions[b][1]+60

        return [(Xstart, Ystart), (Xend, Yend)]
        

    @staticmethod
    def Tie(lst:list):
        if 0 in lst:
            return False
    
        else:
            return True
