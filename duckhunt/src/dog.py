from gifLoader import GIF
import random
class Dog:
    def __init__(self):
        self.x = random.randint(100,700)
        self.y = 550
        self.vx = random.randint(0,15)
        self.vy = 0
        self.img = GIF(r"duckhunt\img\Anon.png",scale=0.3)

        self.actions = [""]
        self.states = ["search", "catch", "back"]
        self.prev_state = None
        self.current_state = "search"

        self.destination = None
        self.timer = 0
    
    def __check_bound(self, decay=False):
        if self.x<0 or self.x>800:
            self.vx *=-1 if not decay else -0.8
        if self.y<0 or self.y>600:
            self.vy *= -1 if not decay else -0.5

    def __getFrame(self, img:GIF):
        # get frame and reached_last_frame flag
        frame = img.get_frame()
        reached_last_frame = img.reached_last_frame()

        return frame, reached_last_frame
    
    def _updateImg(self):
        self.img.update()
        if self.img.reached_last_frame():
            self.img.reset_index()
    
    def set_destination(self, dest):
            # dest is [x,y]
            self.destination = dest
            self.current_state = 'catch'
            self.prev_state = "search"

    def update(self, action=None):
        # if action in self.actions:
        #     if action=="hit" and self.current_state=="escape":
        #         # move from escape state to die state
        #         self.current_state = "die"
        #         self.prev_state = "escape"

        # Different update for different state:
        if self.current_state == "search":
            self.x += self.vx
            self.y += self.vy
        elif self.current_state == "catch":
            # calculate desire velocity
            x,y  = self.destination
            dx = x - self.x
            dy = y - self.y
            self.vx = min(dx/20,10)
            self.vy = min(dy/20,10)
            

            if abs(dx) <3 or abs(dy)<3:
                # we caught the bird
                self.vx = 0
                self.vy = 0 
                self.current_state = "back"
                self.prev_state = "catch"
                self.destination = None
            
            self.x += self.vx
            self.y += self.vy
        elif self.current_state == "back":
            self.vy = 10
            if self.y <=550: # before it hit the ground (y=600)
                self.y +=  self.vy
                self.timer += 1
            else:
                self.vx = random.randint(0,15)
                self.vy = 0
                self.timer = 0

                self.current_state = "search"
                self.prev_state = "back"
        

        # update img
        self._updateImg()

        # fetech latest frame
        frame, _ = self.__getFrame(self.img)

        # check boundary
        self.__check_bound()

        return frame, [self.x, self.y]


    
