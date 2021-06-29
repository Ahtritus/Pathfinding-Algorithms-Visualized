import pygame
import time

N = int(input("Enter size:"))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


def draw(board):

    for i in range(N):
        for j in range(N):

            if board[j][i] == 0:
                pygame.draw.rect(screen, white, [i*50, j*50, 50, 50])
                pygame.draw.rect(screen, black, [i*50, j*50, 50, 50], 1)

            if board[j][i] == 1:
                pygame.draw.rect(screen, black, [i*50, j*50, 50, 50])

            if board[j][i] == 2:
                pygame.draw.rect(screen, red, [i*50, j*50, 50, 50])
                pygame.draw.rect(screen, black, [i*50, j*50, 50, 50], 1)

    pygame.display.update()


def drawfinal(board):

    screen.fill(white)
    for i in range(N):
        for j in range(N):
            if board[j][i] == 1:
                pygame.draw.rect(screen, black, [i*50, j*50, 50, 50])
            else:
                pygame.draw.rect(screen, black, [i*50, j*50, 50, 50], 1)
    pygame.display.update()


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    draw(board)
    pygame.time.Clock().tick(5)


def isSafe(board, row, col):

    for i in range(col):
        if board[row][i] == 1:
            for j in range(col):
                if board[row][j] == 2:
                    board[row][j] = 0
            return False

        board[row][i] = 2
        draw(board)

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[x][y] == 2:
                    board[x][y] = 0
            return False

        board[i][j] = 2
        draw(board)
        pygame.time.Clock().tick(5)

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            for x, y in zip(range(row, N, 1), range(col, -1, -1)):
                if board[x][y] == 2:
                    board[x][y] = 0
            return False

        board[i][j] = 2
        draw(board)
        pygame.time.Clock().tick(5)
    return True


def placeQueen(board, col):
    if col == N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            draw(board)
            pygame.time.Clock().tick(5)

            if placeQueen(board, col + 1) == True:
                return True

            board[i][col] = 0
            draw(board)
            pygame.time.Clock().tick(5)

    return False


def solveNQueen(board):

    if placeQueen(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)

    return True


def main():
    pygame.init()

    global screen
    size = N * 50
    screen = pygame.display.set_mode((size, size))
    screen.fill(white)

    pygame.display.update()

    run = True
    done = False

    board = [[0] * N for _ in range(N)]

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if done == False:
            if solveNQueen(board):
                break

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawfinal(board)


main()
