import random


class Snake:
    scr = 0
    def __init__(self, boardlen, scr):
        self.board = [[0 for x in range(boardlen)] for y in range(boardlen)]
        self.length = 1
        self.facing = None
        self.snakepos = []
        self.walls = []

        self.block = scr // boardlen
        self.eyes = (self.block // 4, self.block // 8, 3 * self.block // 4, self.block // 8)
        self.pupil = (self.block // 4, self.block // 6 - 3, 3 * self.block // 4, self.block // 6 - 3)

        self.x = boardlen // 2
        self.y = boardlen // 2
        self.board[self.y][self.x] = 1
        self.apple = None

        self.position = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                self.position.append((i, j))
        self.newApple()

        self.death = False

    def up(self):
        if self.facing != 'down':
            self.facing = 'up'
            self.eyes = (self.block // 4, self.block // 6, 3 * self.block // 4, self.block // 6)
            self.pupil = (self.block // 4, self.block // 6 - 3, 3 * self.block // 4, self.block // 6 - 3)
    def down(self):
        if self.facing != 'up':
            self.facing = 'down'
            self.eyes = (self.block // 4, 5 * self.block // 6, 3 * self.block // 4, 5 * self.block // 6)
            self.pupil = (self.block // 4, 5 * self.block // 6 + 3, 3 * self.block // 4, 5 * self.block // 6 + 3)
    def left(self):
        if self.facing != 'right':
            self.facing = 'left'
            self.eyes = (self.block // 6, self.block // 4, self.block // 6, 3 * self.block // 4)
            self.pupil = (self.block // 6 - 3, self.block // 4, self.block // 6 - 3, 3 * self.block // 4)
    def right(self):
        if self.facing != 'left':
            self.facing = 'right'
            self.eyes = (5 * self.block // 6, self.block // 4, 5 * self.block // 6, 3 * self.block // 4)
            self.pupil = (5 * self.block // 6 + 3, self.block // 4, 5 * self.block // 6 + 3, 3 * self.block // 4)

    def update(self):
        if not self.death:
            if self.facing == 'up':
                self.y -= 1
            elif self.facing == 'down':
                self.y += 1
            elif self.facing == 'left':
                self.x -= 1
            elif self.facing == 'right':
                self.x += 1

            if self.x == self.apple[0] and self.y == self.apple[1]:
                self.newApple()
                self.length += 1

            self.snakepos.append((self.x, self.y))

            if self.x > len(self.board) - 1 or self.x < 0 or self.y > len(self.board) - 1 or self.y < 0:
                self.death = True
                return

            if len(self.snakepos) > self.length:
                self.board[self.snakepos[0][1]][self.snakepos[0][0]] = 0
                self.snakepos.pop(0)

            if self.snakepos.count((self.x, self.y)) > 1:
                self.death = True

            self.board[self.y][self.x] = 1

    def newApple(self):
        pos = self.position[:]

        for i in self.snakepos:
            pos.remove(i)

        randpos = random.choice(pos)
        self.apple = (randpos[0], randpos[1])
        self.board[self.apple[1]][self.apple[0]] = 2
        pos.remove(randpos)

        # wall mode
        randpos = random.choice(pos)
        if self.length % 3 == 0:
            self.walls.append((randpos[0], randpos[1]))
            for i in self.walls:
                self.board[i[1]][i[0]] = 1


    def reset(self):
        self.__init__(len(self.board), Snake.scr)
        print('reset')