class DartGame:
    def __init__(self):
        self.board = [(i + 1) for i in range(20)]
        self.board.append('Bull')
    
    def practice(self):
        print("You have chosen practice")
        
    def cricket(self):
        print("You have chosen cricket")
        
    def oh1():
        print("You have chosen '01")


def gameType():
    type = input("""What kind of game would you like to play? (1-3)
            1) Practice
            2) Cricket
            3) '01
            """)
    if type == 1:
        pass
    elif type == 2:
        pass
    elif type == 3:
        pass     