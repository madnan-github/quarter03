"""
Implementation of command-line minesweeper by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 

Project specs, files, code all over the place? Start using Backlog for efficient management!! There is a free tier: https://cutt.ly/ehxImv5
"""

import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row, col = loc // self.dim_size, loc % self.dim_size
            if board[row][col] != '*':
                board[row][col] = '*'
                bombs_planted += 1
        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] != '*':
                    self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        return sum(
            1 for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1)
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1)
            if (r != row or c != col) and self.board[r][c] == '*'
        )

    def dig(self, row, col):
        self.dug.add((row, col))
        if self.board[row][col] == '*':
            return False
        if self.board[row][col] > 0:
            return True
            
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) not in self.dug:
                    self.dig(r, c)
        return True

    def __str__(self):
        visible_board = [
            [str(self.board[r][c]) if (r,c) in self.dug else ' ' 
            for c in range(self.dim_size)] 
            for r in range(self.dim_size)
        ]
        widths = [max(len(visible_board[r][c]) for r in range(self.dim_size)) for c in range(self.dim_size)]
        header = '   ' + '  '.join(f'{i:<{widths[i]}}' for i in range(self.dim_size))
        rows = [f'{i} |' + '|'.join(f'{col:<{widths[idx]}}' for idx, col in enumerate(row)) + '|' 
               for i, row in enumerate(visible_board)]
        divider = '-' * len(rows[0])
        return f'{header}\n{divider}\n' + '\n'.join(rows) + f'\n{divider}'

def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        try:
            row, col = map(int, re.split(',\s*', input("Where would you like to dig? Input as row,col: ")))
            if not (0 <= row < dim_size and 0 <= col < dim_size):
                print("Invalid location. Try again.")
                continue
            if not board.dig(row, col):
                break
        except:
            print("Invalid input. Try again.")
    
    print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!" if len(board.dug) == board.dim_size ** 2 - num_bombs 
          else "SORRY GAME OVER :(")
    board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
    print(board)

if __name__ == '__main__':
    play()