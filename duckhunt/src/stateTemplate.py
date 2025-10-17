from gifLoader import GIF
class State:
    def __init__(self, n=""):
        self.name = n
        self.exit = False
        self.stop = False
        self.next_stage = None

        # stage animation gif
        self.enter_gif:GIF = None
        self.normal_gif:GIF = None
        self.exit_gif:GIF = None

    def enter(self, player):
        """Called when entering the state."""
        pass

    def __getFrame(self, img:GIF):
        # get frame and reached_last_frame flag
        frame = img.get_frame()
        reached_last_frame = img.reached_last_frame()

        return frame, reached_last_frame

    def update(self, player, input):
        """Called every frame (game update)."""

        if self.exit:
            # Execute exit animation
            frame, reached_last_frame = self.__getFrame(self.exit_gif)
            if reached_last_frame: # When all frame in exit gif is played
                self.stop=True
            else: # when frame exist
                self.exit_gif.update()
            return frame
        else:
            # normal update
            frame, reached_last_frame = self.__getFrame(self.normal_gif)
            if reached_last_frame:
                self.normal_gif.reset_index()
            
            self.normal_gif.update()
            return frame

    def die(self, player):
        """Called when leaving the state."""
        self.exit = True


    def info(self):
        print(f"you are at {self.name} state!")
