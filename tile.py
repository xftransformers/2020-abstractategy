'''module used for store tile data'''
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


import random as rnd


class Tile:

    def __init__(self, col=''):
        self.col = col
        if self.col == 'lime' or None:
            self.col = '#00FF00'
        if self.col == 'r':
            self.col = rnd.choice(('#00FF00', 'green', 'black'))

    def __str__(self):
        return self.col


if __name__ == '__main__':
    import os
    os.startfile('Transformers_2020_project.py')
