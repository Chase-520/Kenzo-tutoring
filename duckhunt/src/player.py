from gifLoader import GIF
from stateTemplate import State
import random
def update_pos(ls1,ls2):
    res = [0,0]
    # check len
    if len(ls1)!=len(ls2):
        return None
    else:
        for i, n in enumerate(ls1):
            res[i] = n+ls2[i]
    
    return res

class Player:
    def __init__(self):
        self.state = State(n="duck")
        self.state.normal_gif = GIF(r"C:\Users\chase\Downloads\R.gif",scale=0.3)
        self.state.exit_gif = GIF(r"C:\Users\chase\Downloads\random_1.gif")
        self.state.enter(self)
        self.pos = [random.randint(100,700),random.randint(100,500)]
        self.v = [random.randint(0,15),random.randint(0,15)]


    def change_state(self):
        self.state.die(self)

    def check_bound(self, decay=False):
        x,y = self.pos
        if x<0 or x>800:
            self.v[0] *=-1 if not decay else -0.8
        if y<0 or y>600:
            self.v[1] *= -1 if not decay else -0.5
        
    def update(self, input):
        if self.state.exit:
            vx,vy = self.v
            gravity = 2
            self.v = [0,vy+gravity]
            self.check_bound(decay=True)
            self.pos = update_pos(self.pos, self.v)

        else:
            self.check_bound()
            self.pos = update_pos(self.pos,self.v)

        return self.state.update(self, input), self.pos
    

