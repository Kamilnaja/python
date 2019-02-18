# main app class
from player import Player
from bag import Bag


class Game:

    def __init__(self):
        self.play()

    def play(self):
        player = Player(['z', 'a', 'g', 'a', 'd', 'ć', 'u'])
        print(player.combine().__len__())


# start game
game = Game()
bag = Bag()

print(
    bag.getLetters(3)
)
