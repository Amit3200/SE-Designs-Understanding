# Snake & Ladder

# classes
#     User
#     Game
#     Board
#     GamePlay
#     Ladders
#     Snakes

from abc import ABC, abstractmethod
from collections import deque
from random import random


class Player:
    player_id : int 
    player_name : str 
    won : bool
    position : int
    def __init__(self, player_id, player_name):
        self.player_id = player_id 
        self.player_name = player_name
        self.position = 0
        self.won = False
    
    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position
    
    def get_name(self):
        return self.name


# Game Items
class Dice:
    minValue : int 
    maxValue : int 
    currentValue : int 
    def __init__(self, minValue, maxValue, currentValue):
        self.minValue = minValue
        self.maxValue = maxValue
        self.currentValue = currentValue

    def roll(self):
        return random.randint(self.minValue, self.maxValue + 1)

class Snake:
    head: int 
    tail : int
    def __init__(self, head, tail):
        self.head = head 
        self.tail = tail



class Ladder:
    start : int 
    end : int 
    def __init__(self, start, end):
        self.start = start 
        self.end = end

class Board:
    board : list[list]
    start : int 
    end : int
    size : int
    def __init__(self, board_size):
        self.start = 1
        self.end = self.start + board_size - 1
        self.size = board_size
        self.board = [[0 * board_size] * board_size]
    
    def get_start(self):
        return self.start 
    
    def get_end(self):
        return self.end


class Game:
    number_of_snakes : int 
    number_of_ladders : int 
    players : deque[Player]
    snakes : list = []
    ladders: list = []
    dice : Dice
    def __init__(self, number_of_snakes, number_of_ladder, board_size):
        self.number_of_snakes = number_of_snakes
        self.number_of_ladders = number_of_ladder
        self.board = Board(board_size)
        self.dice = Dice(1,6,2)
        self.initialize_game()
    
    def initialize_game(self):
        allocatedSpace : list = []
        for idx in range(self.number_of_snakes):
            while True:
                snake_start = random.randint(self.board.get_start(), self.board.get_end())
                snake_end   = random.randint(self.board.get_start(), self.board.get_end())
                if snake_end >= snake_start:
                    continue
                allocated_snake_address = str(snake_start) + "_" + str(snake_end)
                if allocated_snake_address not in allocatedSpace:
                    snake = Snake(snake_start, snake_end)
                    self.snakes.append(snake)
                    allocatedSpace.append(allocated_snake_address)
                    break
                
        for idx in range(self.number_of_ladders):
            while True:
                ladder_start = random.randint(self.board.get_start(), self.board.get_end())
                ladder_end   = random.randint(self.board.get_start(), self.board.get_end())
                if ladder_end <= ladder_start:
                    continue 
                allocated_ladder_space = str(ladder_start) + "_" + str(ladder_end)
                if allocated_ladder_space not in allocatedSpace:
                    ladder = Ladder(ladder_start, ladder_end)
                    self.ladders.append(ladder)
                    allocatedSpace.append(ladder)
                    break
        
        def add_player(player):
            self.players.append(player)
        
        def play_game():
            while True:
                player : Player = self.players.popleft()
                val    : int    = self.dice.roll()
                npos   : int    = self.player.get_position() + val
                if npos >= self.board.get_end():
                    player.set_position(player.get_position())
                    self.players.append(player)
                else:
                    player.set_position(self.set_new_position(npos))
                    if player.get_position == self.board.get_end():
                        player.won = True
                        print("Player {p1} Won!!".format(p1 = player.get_name()))
                    else:
                        print("Setting {p1}'s new position to {npos}".format(p1 = player.get_name(), npos = player.get_position()))
                        self.players.append(player)
                if len(self.players) < 2:
                    break
        
        def set_new_position(self,npos):
            for sn in self.snakes:
                if sn.get_head() == npos:
                    print("Snake Bite")
                    return sn.get_tail()
            
            for ld in self.ladders:
                if ld.get_start() == npos:
                    print("Climb Ladder")
                    return ld.get_end()
            return npos




