from keyboard import is_pressed
from time import time, sleep
from settings import *
from colorama import Style

class Field():
    def __init__(self, _size, _players, fps):
        self.run = True
        
        self.size = _size
        self.cells = {}
        self.players = _players.copy()
        self.dead_players = []
        
        self.last_tick_time = time()
        self.accumulator = 0
        self.slice = 1/fps

    def tick(self):
        for player in self.players:
            color = player[0]
            position = player[1]
            rotation = player[2]
            keys = player[3]

            self.cells[tuple(position)] = color

            # Rotate
            if is_pressed(keys[0]) and rotation != "d":
                rotation = "u"
            elif is_pressed(keys[1]) and rotation != "r":
                rotation = "l"
            elif is_pressed(keys[2]) and rotation != "u":
                rotation = "d"
            elif is_pressed(keys[3]) and rotation != "l":
                rotation = "r"
            
            player[2] = rotation

            # Move
            if rotation == "u":
                position[1] -= 1
            elif rotation == "d":
                position[1] += 1
            elif rotation == "l":
                position[0] -= 1
            else:
                position[0] += 1

            player[1] = position

            # Collide
            if tuple(position) in self.cells or \
            position[0] < 0 or \
            position[0] >= self.size[0] or \
            position[1] < 0 or \
            position[1] >= self.size[1]:
                self.dead_players.append(player)
                continue
            
        for dead_player in self.dead_players:
            self.players.remove(dead_player)

        self.dead_players.clear()

        if len(self.players) <= 1: self.run = False

    def draw(self):
        print(SPACER)
        screen = [[FIELD_COLOR + FIELD_SYMBOL, *([FIELD_SYMBOL] * (self.size[0] - 1))] for _ in range(self.size[1])]
        
        for cell in self.cells:
            screen[cell[1]][cell[0]] = TRAIL_COLORS[self.cells[cell]] + TRAIL_SYMBOL + FIELD_COLOR

        for player in self.players:
            screen[player[1][1]][player[1][0]] = COLORS[player[0]] + SYMBOL + FIELD_COLOR

        for line in screen:
            print("".join(line))
        
        print(Style.RESET_ALL)

    def cycle(self):
        while self.run:
            now_time = time()
            self.accumulator += now_time - self.last_tick_time

            while self.accumulator >= self.slice:
                self.tick()
                self.draw()
                self.accumulator -= self.slice

            self.last_tick_time = now_time

        input("You can see who won. Press return to exit... ")
        print()