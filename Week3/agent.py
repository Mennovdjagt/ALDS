import random
import gomoku
import time
import copy
import math

class Node:
    def __init__(self, board, valid_moves, last_move = None, parent = None):
        self.board = board              # the current board state
        #self.finished, self.won
        self.parent = parent            # the parent above
        self.children = []              # all the children
        self.move = last_move           # the last move that was made
        self.Q = 0                      # number of wins
        self.N = 0                      # number of visits
        self.valid_moves = valid_moves  # all the possible moves it can make


    def UCT(self, constant = 1/math.sqrt(2)):
        return ((self.Q/self.N) + constant * (math.sqrt(2 * math.log(self.parent.N)) / self.N))


    def findSpotToExpand(self, node):
        # if node is terminal(game finished).
        if len(node.valid_moves) is 0:
            return node

        # a node is not fully expanded if there are more valid_moves than children.
        if len(node.children) < len(node.valid_moves):
            newBoard = gomoku.gomoku_game(19, node.board)           # create a new board
            newMove = node.valid_moves[len(node.children)]          # get the next move
            newNode = Node(newBoard, node.valid_moves, newMove)     # create new node to expand
            node.children.append(newNode)                           # add node to node's children
            return newNode

        # if all possible children have been added to a node (all valid moves have been visited),
        # we need to select one of the children of the node with the highest uct value.
        if len(node.children) >= len(node.valid_moves):
            if len(node.children) > 0:                  # makes sure there is atleast 1 child
                bestChild = node.children[0]            # makes the first child the best child, to be able to compare with other childs
                for child in node.children:             # loops through all childs to find the one with the highest uct
                    if child.UCT() > bestChild.UCT():   # checks if the old child has a worse utc than the next child
                        bestChild = child               # if the next child is better make it the best child
            return self.findSpotToExpand(bestChild)     # the best node


class BigOof:
    """This class specifies a player that just does random moves.
    The use of this class is two-fold: 1) You can use it as a base random roll-out policy.
    2) it specifies the required methods that will be used by the competition to run
    your player
    """
    def __init__(self, black_=True):
        """Constructor for the player."""
        self.black = black_

    def new_game(self, black_):
        """At the start of each new game you will be notified by the competition.
        this method has a boolean parameter that informs your agent whether you
        will play black or white.
        """
        self.black = black_

    def move(self, board, last_move, valid_moves, max_time_to_move=1000):
        """This is the most important method: the agent will get:
        1) the current state of the board
        2) the last move by the opponent
        3) the available moves you can play (this is a special service we provide ;-) )
        4) the maximimum time until the agent is required to make a move in milliseconds [diverging from this will lead to disqualification].
        """
        return random.choice(valid_moves)

    def id(self):
        """Please return a string here that uniquely identifies your submission e.g., "name (student_id)" """
        return "Menno (1745500)"