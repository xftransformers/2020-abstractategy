'''module containing the map class
[width:x][height:y]'''

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


import tile


class Map:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        Tile = tile.Tile('lime')
        map = [[Tile for i in range(width)] for j in range(height)]
        self.map = map

    def __getitem__(self, name):
        if name >= self.height:
            name -= self.height
        return self.map[min(max(name, 0), self.height)]

    def changeState(self, x, y, newTile):
        y = min(max(y, -self.height), self.height)
        x = min(max(x, -self.width), self.width)
        self.map[y][x] = newTile


if __name__ == '__main__':
    import os
    os.startfile('Transformers_2020_project.py')
