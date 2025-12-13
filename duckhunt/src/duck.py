from gifLoader import GIF
import random
class Duck:
    def __init__(self):
        self.x = random.randint(100,700)
        self.y = random.randint(100,500)
        self.vx = random.randint(0,15)
        self.vy = random.randint(0,15)
        self.img = GIF(r"C:\Users\kenzo\OneDrive\Documents\GitHub\Kenzo-tutoring\duckhunt\img\Chibi.gif",scale=0.3)

        self.actions = ["hit"]
        self.states = ["escape", "die", "disappear"]
        self.prev_state = None
        self.current_state = "escape"

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
    
    def update(self, action=None):
        if action in self.actions:
            if action=="hit" and self.current_state=="escape":
                # move from escape state to die state
                self.current_state = "die"
                self.prev_state = "escape"

        # Different update for different state:
        if self.current_state == "escape":
            self.x += self.vx
            self.y += self.vy

        elif self.current_state == "die":
            # switch to die animation and start timer
            if self.y <=600: # before it hit the ground (y=600)
                if self.timer ==0:
                    # when you first enter the state
                        self.y = self.y + 25

                # your animaiton logic here
                pass
                # When the __ expire and you are ready to switch to the next state

                # TODO change state
                pass
        elif self.current_state == "disappear":
            # start a timer and wait for certain period
            if self.timer <= 120: # 120 frames ~= 4s
                self.img.set_transparency(0)
                self.timer += 1
            else:
                # TODO change state

                # set transparency to full

                # respawn


                # reset timer
                pass


        # update img
        self._updateImg()

        # fetech latest frame
        frame, _ = self.__getFrame(self.img)

        # check boundary
        self.__check_bound()

        return frame, [self.x, self.y]


    