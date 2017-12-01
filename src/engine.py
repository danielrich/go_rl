import sgfmill # I like this library better
import gtp
import pandas as pd
import numpy as np

class trainingEngine(object):

    def __init__(self, size=9, komi=6.5):
        self.size = size
        if size != 9:
            assert "Not supported Yet"

        self.komi = komi
        self.move_history = []
        self.game = np.zeros((size, size)) # assume 0 is empty, 1 is black and -1 is white


    def clear(self):
        self.game = np.zeros((self.size, self.size)) # assume 0 is empty, 1 is black and -1 is white

    def make_move(self, color, vertex):
        self.move_history.append((color, vertex))
        move_0_based = tuple(np.array(vertex) - np.array((1,1)))
        self.game[move_0_based] = color
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
        # (0,0) is a pass (1,1) is the bottom left 1,1 point
        my_move = self._generate_move(color)
        my_move_1_based = tuple(np.array(my_move) + np.array((1,1)))
        self.move_history.append((color, my_move_1_based))
        self.game[my_move] = color
        return my_move_1_based


    def _generate_move(self, color):
        """
        Generates a legal_move. 0-based
        """
        legal_moves = np.where(self.game.flatten() == 0)[0]
        # TODO handle ko
        legal_vertices = []
        for ix in legal_moves:
            # silly way to do it but moving on
            new_move = np.unravel_index(ix, (9,9))
            #check new move is allowed
            legal_vertices.append(new_move)
        idx = np.random.choice(len(legal_vertices))
        return legal_vertices[idx]




