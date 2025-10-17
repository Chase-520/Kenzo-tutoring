from stateTemplate import State
from gifLoader import GIF
class runState(State):
    def __init__(self):
        super().__init__("run")
        self.normal_gif = GIF(r"C:\Users\chase\Downloads\R.gif",scale=0.3)
        self.exit_gif = GIF(r"C:\Users\chase\Downloads\random_1.gif")

