import numpy as np
import math
import pygame
import sys

ROW_COUNT = 6
COLUMN_COUNT = 7
EVEN = 0
ODD = 1

def create_board():
    board = np.zeros((6,7))
    return board

def valid(board, position):
    for r in range(ROW_COUNT):
        if board[r][position] == 0:
            return True
    return False
