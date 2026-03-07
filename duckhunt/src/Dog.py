from gifLoader import GIF
import random


class Dog:
    def __init__(self):
        self.x = 40
        self.y = 450
        self.vx = random.randint(0, 15)
        self.vy = random.randint(10, 20)
        self.img = GIF(r"C:\Users\kenzo\OneDrive\Documents\GitHub\Kenzo-tutoring\duckhunt\img\kirbyclear.gif", scale=0.2)

        self.actions = [""]
        self.states = ["hunting", "fetching", "returning"]
        self.prev_state = None
        self.current_state = "hunting"

        self.timer = 0

        self.duckx = None
        self.ducky = None

    def __check_bound(self, decay=False):
        if self.x < 0 or self.x > 800:
            self.vx *= -1 if not decay else -0.8
        if self.y < 0 or self.y > 600:
            self.vy *= -1 if not decay else -0.5

    def __getFrame(self, img: GIF):
        # get frame and reached_last_frame flag
        frame = img.get_frame()
        reached_last_frame = img.reached_last_frame()

        return frame, reached_last_frame

    def _updateImg(self):
        self.img.update()
        if self.img.reached_last_frame():
            self.img.reset_index()

    def duckposition(self, duckx, ducky):
        self.duckx = duckx
        self.ducky = ducky
        self.current_state = "fetching"


    def update(self, action=None):

        # Different update for different state:
        if self.current_state == "hunting":
            self.x += self.vx

        elif self.current_state == "fetching":
            dy = self.ducky - self.y
            dx = self.duckx - self.x
            self.vx = min(dx/20,10)
            self.vy = min(dy / 20, 10)
            self.x += self.vx
            self.y += self.vy
            # # switch to die animation and start timer
            # if self.y <= 600:  # before it hit the ground (y=600)
            #     if self.timer == 0:
            #         # when you first enter the state
            #         self.vy = -15
            #         self.y += self.vy

                ## your animaiton logic here
                # pass
                # self.timer += 1
                # self.y += self.vy
                # self.vy += 2
                ## When the __ expire and you are ready to switch to the next state
            # else:
            #     self.current_state = "disappear"
            #
            #     pass
        elif self.current_state == "disappear":
            # start a timer and wait for certain period
            if self.timer <= 120:  # 120 frames ~= 4s
                self.img.set_transparency(0)
                self.timer += 1
            else:
                # TODO change state
                self.img.set_transparency(255)
                print(self.timer)
                # set transparency to full

                # respawn
                self.current_state = "escape"
                self.prev_state = "disappear"
                self.x = random.randint(100, 700)
                self.y = random.randint(100, 500)
                self.timer = 0
                # reset timer
                pass

        # update img
        self._updateImg()

        # fetech latest frame
        frame, _ = self.__getFrame(self.img)

        # check boundary
        self.__check_bound()

        return frame, [self.x, self.y]