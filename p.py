class Player2():
    def __init__(self):
        self._name = 'sdfdsfs'

class Computer(Player2):
    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    player = Player2()

    print(player.name)