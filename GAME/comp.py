from random import randint

class computer:
    def __init__(self, pos:list, num: int):
        self.list=pos
        self.whoAmI=num

    def analysis(self):
        from time import sleep
        a= self.is_MatchPoint(good=True)
        if a!=0:
            self.play= self.Block_Or_Win(a)
            #print(f'We are about to win! {self.play}')

        else:
            a= self.is_MatchPoint(good=False)
            if a!=0:
                self.play= self.Block_Or_Win(a)
                #print(f'We were going to loose! {self.play}')

            else:
                self.play=self.move()

    def is_MatchPoint(self, good: bool):
        if good:
            v= 2*self.whoAmI
        
        else:
            v=-2*self.whoAmI

        if self.list[0]+ self.list[4]+ self.list[8]== v:
            return 1
        
        if self.list[2]+self.list[4]+ self.list[6]== v:
            return 2

        for i in range (0,9):
            if i in [0, 3, 6]:
                if self.list[i]+self.list[i+1]+self.list[i+2]== v:
                    return (10+ i)

            if i in [0, 1, 2]:
                if self.list[i]+self.list[i+3]+self.list[i+6]== v:
                    return (20+ i)
                
        return 0
    
    def Block_Or_Win(self, where: int):
        match where:
            case 1:
                indexes=[0, 4, 8]

            case 2:
                indexes=[2,4,6]

            case x if 9<x<18:
                indexes=[x-10, x-9, x-8]

            case y if 19<y<28:
                indexes=[y-20, x-17, x-14]

        for i in indexes:
            if self.list[i]==0:
                return i
    
    def move(self):
        while True:
            a=randint(0,8)
            if self.list[a]==0:
                break

        return a

     
test=[
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
]      

c=computer(test, 1)
c.analysis()
g= c.play
