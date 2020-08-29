''' Multiplayer game where players move the same character towards their goal.
'''
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
import math as m
import tkinter as tk
import time as t
import maps
import player
import tile


w = tk.Tk()
w.title('Abstracttegy')

w.attributes('-fullscreen', True)  # comment out for ease of editing


GAME_STATE = 'START'
TileCol = 'PLAIN'
moves = 1

trueHeight = w.winfo_screenheight()-45
height = trueHeight-50
width = height
tileHeight = 9
tileWidth = tileHeight
tileSize = height/(tileHeight)

c = tk.Canvas(w, height=trueHeight, width=width, bg='gray')
c.pack()


map = maps.Map(tileHeight, tileWidth)
player = player.Player(map)
map[0][tileHeight-1] = tile.Tile('blue')
map[tileWidth-1][0] = tile.Tile('blue')


def OnLClick(event):
    global GAME_STATE
    global moves
    mouseScreenLoc = event.x, event.y
    tileX = m.floor(mouseScreenLoc[0]/tileSize)
    tileY = m.floor(mouseScreenLoc[1]/tileSize)

    if map[tileX][tileY] == tile.Tile('blue'):
        return None
    if tileX == player.x:
        if tileY == player.y:
            return None

    colour = {'RANDOM': 'r',
              'FAST': 'green',
              'PLAIN': 'lime',
              'OBSTACLE': 'black',
              'DOUBLE': 'orange'}

    if GAME_STATE == 'TILE_CHANGE':
        chosen = colour[TileCol]
        map.changeState(tileX, tileY, tile.Tile(chosen))
        GAME_STATE = 'MOVE'
        moves = 1


playerText = c.create_text(10, trueHeight-30, anchor='sw')
cardText = c.create_text(width-10, trueHeight-30, anchor='se')


def Draw(map):
    if GAME_STATE != 'GAMEOVER':
        c.delete('map')
        for y in range(map.height):
            for x in range(map.width):
                tileX = x*tileSize
                tileY = y*tileSize
                tileDim = (tileX, tileY, tileX + tileSize, tileY + tileSize)
                c.create_rectangle(*tileDim, fill=map.map[y][x].col, width=0,
                                   tags='map')
                c.itemconfig(playerText,
                             text=f'X:{player.x},Y:{player.y}, Moves:{moves}')
        w.update()
        return True
    return False


deck = []
for i in range(8):
    deck.append('random')
for i in range(32):
    deck.append('fast')
for i in range(20):
    deck.append('plain')
for i in range(20):
    deck.append('obstacle')
for i in range(2):
    deck.append('double')


def drawCard(event):
    global GAME_STATE
    if GAME_STATE == 'DRAW':
        choice = rnd.choice(deck)
        deck.remove(choice)
        print(choice)
        c.itemconfig(cardText, text=choice)
        print(c.itemcget(cardText, 'text'))
        global TileCol
        TileCol = str(choice).upper()
        w.update()
        GAME_STATE = 'TILE_CHANGE'


def move(event):
    global GAME_STATE
    global moves
    if GAME_STATE == 'MOVE':
        if event.char == 'e':
            successful = False
            moves = 0
        else:
            successful = player.move(event)
        if successful:
            moves -= 1
            print(player.covered.col)
            if player.covered.col == 'green':
                moves += 1
            if player.covered.col == 'orange':
                moves += 2
            elif player.covered.col == 'blue':
                GAME_STATE = 'GAMEOVER'
                c.create_text(width/2, height/2, font=('Helvetica', 36),
                              text='GAME OVER!')
                print('GAME OVER')
                return None

        if moves == 0:
            GAME_STATE = 'DRAW'


c.bind_all('<Key>', move)
c.bind('<Button-1>', OnLClick)
c.bind('<Button-2>', drawCard)


GAME_STATE = 'DRAW'
w.update()
a = True
while a:
    a = Draw(map)
    map[0][tileHeight-1] = tile.Tile('blue')
    map[tileWidth-1][0] = tile.Tile('blue')
