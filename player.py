"""
    Sam D.  Abstractategy.
    Copyright (C) 2020 Sam D

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You can contact the author and get a copy of the orginial code from:
    https://github.com/xftransformers

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import math as m
import maps
import tile
import random as rnd


class Player:
    def __init__(self, map):
        self.map = map
        self.x = 4
        self.y = 4
        self.covered = map[self.x][self.y]
        self.prev = (self.x, self.y)
        self.update()

    def move(self, event):
        key = event.char

        def checkTile(x, y):
            if 0 <= x < self.map.height:
                if 0 <= y < self.map.width:
                    try:
                        if self.map[x][y].col != 'black':
                            return True
                        else:
                            return False
                    except IndexError:
                        raise IndexError('out of bounds after checks')
                        return False
                else:
                    return False
            else:
                return False

        try:
            if key == 'w':
                if checkTile(self.x-1, self.y):
                    self.prev = (self.x, self.y)
                    self.x -= 1
                    self.update()
                    return True
                else:
                    return False
            elif key == 's':
                if checkTile(self.x+1, self.y):
                    self.prev = (self.x, self.y)
                    self.x += 1
                    self.update()
                    return True
                else:
                    return False
            elif key == 'a':
                if checkTile(self.x, self.y-1):
                    self.prev = (self.x, self.y)
                    self.y -= 1
                    self.update()
                    return True
                else:
                    return False
            elif key == 'd':
                if checkTile(self.x, self.y+1):
                    self.prev = (self.x, self.y)
                    self.y += 1
                    self.update()
                    return True
                else:
                    return False
        except IndexError:
            self.x, self.y = self.prev
            return False

    def update(self):
        self.map[self.prev[0]][self.prev[1]] = self.covered
        self.covered = self.map[self.x][self.y]
        self.map[self.x][self.y] = tile.Tile('red')


if __name__ == '__main__':
    import os
    os.startfile('Transformers_2020_project.py')
