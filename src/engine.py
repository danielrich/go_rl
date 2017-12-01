import sgfmill # I like this library better
import gtp

class trainingEngine(object):

    def __init__(self, size=9, komi=6.5):
        self.size = size
        if size != 9:
            assert "Not supported Yet"

        self.komi = komi
        self.game = None # figure out how I want to store this. I might want to store it as the feature planes to make it easier.


    def clear(self):
        self.game = None # clear the board and history

    def make_move(self, color, vertex):
        return True # assume a good move

    def set_komi(self, komi):
        self.komi = komi

    def set_size(self, n):
        self.size = n
        assert n == 9

    def get_move(self, color):
        """
        Makes a move.
        This entails.
        1. convert the current game to feature planes.
        2. Do the MCTS playouts. Make this threaded
        3. Queue up the network evalutations. Use tensorflow serving
        4. Apply and choose the move.
        5. save off the information about the network probabilities and game outcome.
        6. return the move.
        """
        return (0,0) # a pass


