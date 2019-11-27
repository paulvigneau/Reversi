# -*- coding: utf-8 -*-

import time

from Evaluator import Evaluator
import Reversi
import sys
from random import randint
from playerInterface import *


class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(10)
        self._mycolor = None

    def getPlayerName(self):
        return "Random Player"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return (-1, -1)

        # Compute player move
        move = self._play()

        self._board.push(move)
        print("I am playing ", move)
        (c, x, y) = move
        assert (c == self._mycolor)
        print("My current board :")
        print(self._board)
        return (x, y)

    def playOpponentMove(self, x, y):
        assert (self._board.is_valid_move(self._opponent, x, y))
        print("Opponent played ", (x, y))
        self._board.push([self._opponent, x, y])

    def newGame(self, color):
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")

    def _play(self):
        # Killer move detection
        # # Corner
        max_value = - sys.maxsize - 1
        best_move = None
        corners = [[0, 0],
                   [0, self._board.get_board_size()-1],
                   [self._board.get_board_size()-1, 0],
                   [self._board.get_board_size()-1, self._board.get_board_size()-1]]
        for m in self._board.legal_moves():
            self._board.push(m)
            (_, x, y) = m
            if [x, y] in corners:
                max_value = max(max_value, Evaluator.eval(self._board, myPlayer))
                best_move = m
            self._board.pop()

        if best_move is not None:
            return best_move

        # # Blocking move
        max_value = - sys.maxsize - 1
        best_move = None
        for m in self._board.legal_moves():
            self._board.push(m)
            if not self._board.at_least_one_legal_move(self._opponent):
                max_value = max(max_value, Evaluator.eval(self._board, myPlayer))
                best_move = m
            self._board.pop()

        if best_move is not None:
            return best_move

        # Opening move

        # minimax
        return self._start_minimax(3)

    def _get_result(self):
        (nb_whites, nb_blacks) = self._board.get_nb_pieces()
        if nb_whites > nb_blacks:
            return 1000 if self._mycolor == 1 else -1000
        elif nb_blacks > nb_whites:
            return 1000 if self._mycolor == 2 else -1000
        else:
            return 0

    def _start_minimax(self, depth):
        if self._board.is_game_over():
            return None

        maxx = - sys.maxsize - 1
        best_move = None
        for m in self._board.legal_moves():
            self._board.push(m)
            value = self._minimax(depth - 1, self._opponent, -sys.maxsize - 1, sys.maxsize)
            if value > maxx:
                maxx = value
                best_move = m
            self._board.pop()

        return best_move

    def _minimax(self, depth, player, alpha, beta):
        # If game is over or depth limit reached
        if depth == 0 or self._board.is_game_over():
            return Evaluator.eval(self._board, self._mycolor)

        # If player cannot move
        if not self._board.at_least_one_legal_move(player):
            p = 2 if player == 1 else 1
            return self._minimax(depth - 1, p, alpha, beta)

        if player == self._mycolor:  # Player turn
            value = - sys.maxsize - 1
            for m in self._board.legal_moves():
                self._board.push(m)
                value = max(value, self._minimax(depth - 1, self._opponent, alpha, beta))
                self._board.pop()
                if value >= beta:
                    break  # Cutoff
                alpha = max(alpha, value)
            return value
        else:  # Opponent turn
            value = sys.maxsize
            for m in self._board.legal_moves():
                self._board.push(m)
                value = min(value, self._minimax(depth - 1, self._mycolor, alpha, beta))
                self._board.pop()
                if alpha >= value:
                    break  # Cutoff
                beta = min(beta, value)
            return value
