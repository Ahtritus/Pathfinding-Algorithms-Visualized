"""Depth First Search"""

import pygame
import sys
import random
import math
from collections import deque
from tkinter import messagebox, Tk, ttk
from tkinter import *

size = (width, height) = 640, 480
pygame.init()

win = pygame.display.set_mode(size)
pygame.display.set_caption('Depth First Search')
clock = pygame.time.Clock()

cols, rows = 40, 40

w = width//cols
h = height//rows

grid = []
stack = []
visited = []
path = []


class Spot:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.visited = False
        # if random.randint(0, 100) < 20:
        #     self.wall = True

    def show(self, win, col):
        if self.wall == True:
            col = (0, 0, 0)
        pygame.draw.rect(win, col, (self.x*w, self.y*h, w-1, h-1))

    def add_neighbors(self, grid):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1])
        # Add Diagonals
        # if self.x < cols - 1 and self.y < rows - 1:
        #     self.neighbors.append(grid[self.x+1][self.y+1])
        # if self.x < cols - 1 and self.y > 0:
        #     self.neighbors.append(grid[self.x+1][self.y-1])
        # if self.x > 0 and self.y < rows - 1:
        #     self.neighbors.append(grid[self.x-1][self.y+1])
        # if self.x > 0 and self.y > 0:
        #     self.neighbors.append(grid[self.x-1][self.y-1])


def clickWall(pos, state):
    i = pos[0] // w
    j = pos[1] // h
    grid[i][j].wall = state


def place(pos):
    i = pos[0] // w
    j = pos[1] // h
    return w, h


for i in range(cols):
    arr = []
    for j in range(rows):
        arr.append(Spot(i, j))
    grid.append(arr)

for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbors(grid)


start = grid[0][0]
end = grid[rows-1][cols-1]
start.wall = False
end.wall = False

stack.append(start)
start.visited = True


def main():

    def onsubmit():
        global start
        global end
        st = startBox.get().split(',')
        ed = endBox.get().split(',')
        start = grid[int(st[0])][int(st[1])]
        end = grid[int(ed[0])][int(ed[1])]
        window.quit()
        window.destroy()

    window = Tk()
    label = Label(window, text='Start(x,y): ')
    startBox = Entry(window)
    label1 = Label(window, text='End(x,y): ')
    endBox = Entry(window)
    submit = Button(window, text='Submit',
                    command=onsubmit)

    submit.grid(columnspan=2, row=3)
    label1.grid(row=1, pady=3)
    endBox.grid(row=1, column=1, pady=3)
    startBox.grid(row=0, column=1, pady=3)
    label.grid(row=0, pady=3)

    window.update()
    mainloop()

    flag = False
    noflag = True
    startflag = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pressed(0):
                    clickWall(pygame.mouse.get_pos(), True)
                if pygame.mouse.get_pressed(2):
                    clickWall(pygame.mouse.get_pos(), False)
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    clickWall(pygame.mouse.get_pos(), True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    startflag = True

        if startflag:
            if len(stack) > 0:
                current = stack.pop()
                if current == end:
                    temp = current
                    while temp.prev:

                        path.append(temp.prev)
                        temp = temp.prev
                    if not flag:
                        flag = True
                        print("Done")
                    elif flag:
                        continue
                if flag == False:
                    if not current.visited and not current.wall:
                        current.visited = True
                    for i in current.neighbors:
                        if not i.visited and not i.wall:
                            i.prev = current
                            stack.append(i)
            else:
                if noflag and not flag:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution")
                    noflag = False
                else:
                    continue

        win.fill((0, 20, 20))
        for i in range(cols):
            for j in range(rows):
                spot = grid[i][j]
                spot.show(win, (255, 255, 255))
                if spot in path:
                    spot.show(win, (25, 120, 250))
                elif spot.visited:
                    spot.show(win, (255, 0, 0))
                if spot in stack:
                    spot.show(win, (0, 255, 0))
                if spot == end:
                    spot.show(win, (0, 120, 255))

        pygame.display.flip()


while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()

    win.fill((0, 20, 20))
    for i in range(cols):
        for j in range(rows):
            spot = grid[i][j]
            spot.show(win, (255, 255, 255))
    pygame.display.update()
    main()
