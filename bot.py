import snake

def move(snk: snake.Snake):
    # print('\n'.join(['\t'.join([str(i) for i in j]) for j in snk.board]), '\n')

    if snk.facing == 'left':
        try:
            if (snk.x == 0 and snk.y != len(snk.board) - 1) or (snk.x == len(snk.board) - 1 and snk.y == 0):
                snk.down()
            elif (snk.x == len(snk.board) - 1 and snk.y != 0) or (snk.x == 0 and snk.y == len(snk.board) - 1):
                snk.up()

            elif snk.board[snk.y][snk.x - 1] == 1:
                if snk.board[snk.y + 1][snk.x] == 1:
                    snk.up()
                elif snk.board[snk.y - 1][snk.x] == 1:
                    snk.down()
                else:
                    val = 0
                    for i in range(len(snk.board)):
                        if i == snk.y:
                            continue
                        val += (snk.board[i][snk.x]) / (snk.y - i)
                    if val > 0:
                        snk.down()
                    elif val < 0:
                        snk.up()
                    else:
                        snk.up()

            for i in snk.board:
                if 2 in i:
                    if snk.board.index(i) < snk.y and snk.board[snk.y - 1][snk.x] != 1:
                        snk.up()
                    elif snk.board.index(i) > snk.y and snk.board[snk.y + 1][snk.x] != 1:
                        snk.down()

        except IndexError:
            pass

    elif snk.facing == 'right':
        try:
            if (snk.x == 0 and snk.y != len(snk.board) - 1) or (snk.x == len(snk.board) - 1 and snk.y == 0):
                snk.down()
            elif (snk.x == len(snk.board) - 1 and snk.y != 0) or (snk.x == 0 and snk.y == len(snk.board) - 1):
                snk.up()

            elif snk.board[snk.y][snk.x + 1] == 1:
                if snk.board[snk.y + 1][snk.x] == 1:
                    snk.up()
                elif snk.board[snk.y - 1][snk.x] == 1:
                    snk.down()
                else:
                    val = 0
                    for i in range(len(snk.board)):
                        if i == snk.y:
                            continue
                        val += (snk.board[i][snk.x]) / (snk.y - i)
                    if val > 0:
                        snk.down()
                    elif val < 0:
                        snk.up()
                    else:
                        snk.up()

            for i in snk.board:
                if 2 in i:
                    if snk.board.index(i) < snk.y and snk.board[snk.y - 1][snk.x] != 1:
                        snk.up()
                    elif snk.board.index(i) > snk.y and snk.board[snk.y + 1][snk.x] != 1:
                        snk.down()

        except IndexError:
            pass

    elif snk.facing == 'up':
        try:

            if 2 in snk.board[snk.y]:
                if snk.board[snk.y].index(2) < snk.x and snk.board[snk.y][snk.x - 1] != 1:
                    snk.left()
                elif snk.board[snk.y].index(2) > snk.x and snk.board[snk.y][snk.x + 1] != 1:
                    snk.right()
            elif snk.y == 0 and snk.x != 0:
                snk.left()
            elif snk.y == 0 and snk.x == 0:
                snk.right()

            elif snk.board[snk.y - 1][snk.x] == 1:
                if snk.board[snk.y][snk.x + 1] == 1:
                    snk.left()
                elif snk.board[snk.y][snk.x - 1] == 1:
                    snk.right()
                else:
                    val = 0
                    for index, i in enumerate(snk.board[snk.y]):
                        if index == snk.x:
                            continue
                        val += i / (snk.x - index)
                    if val < 0:
                        snk.left()
                    elif val > 0:
                        snk.right()
                    else:
                        snk.left()

        except IndexError:
            pass

    elif snk.facing == 'down':
        try:
            if 2 in snk.board[snk.y]:
                if snk.board[snk.y].index(2) < snk.x and snk.board[snk.y][snk.x - 1] != 1:
                    snk.left()
                elif snk.board[snk.y].index(2) > snk.x and snk.board[snk.y][snk.x + 1] != 1:
                    snk.right()
            elif snk.y == len(snk.board) - 1 and snk.x != len(snk.board) - 1:
                snk.right()
            elif snk.y == len(snk.board) - 1 and snk.x == len(snk.board) - 1:
                snk.left()

            elif snk.board[snk.y + 1][snk.x] == 1:
                if snk.board[snk.y][snk.x + 1] == 1:
                    snk.left()
                elif snk.board[snk.y][snk.x - 1] == 1:
                    snk.right()
                else:
                    val = 0
                    for index, i in enumerate(snk.board[snk.y]):
                        if index == snk.x:
                            continue
                        val += i / (snk.x - index)
                    if val < 0:
                        snk.left()
                    elif val > 0:
                        snk.right()
                    else:
                        snk.left()

        except IndexError:
            pass

    else:
        snk.up()





def move2(snk: snake.Snake):

    global lastmove
    global lastlastmove

    if snk.facing == 'left':
        try:
            if snk.board[snk.y][snk.x - 1] == 1:
                checkSide(snk, 'left')
            elif snk.board[snk.y + 1][snk.x - 1] == 1 and snk.board[snk.y - 1][snk.x - 1] == 1:
                oneWayCheck(snk, 'left')
            else:
                raise IndexError

        except IndexError:
            if snk.x == 0 and snk.y == 0:
                snk.down()
                lastlastmove = lastmove
                lastmove = 'down'
            elif snk.x == 0 and snk.y == len(snk.board) - 1:
                snk.up()
                lastlastmove = lastmove
                lastmove = 'up'

            elif snk.apple[0] >= snk.x:
                turnDir(snk, 'left')

            elif snk.x == 0:
                checkSide(snk, 'left')

    elif snk.facing == 'right':
        try:
            if snk.board[snk.y][snk.x + 1] == 1:
                checkSide(snk, 'right')
            elif snk.board[snk.y + 1][snk.x + 1] == 1 and snk.board[snk.y - 1][snk.x + 1] == 1:
                oneWayCheck(snk, 'right')
            else:
                raise IndexError

        except IndexError:

            if snk.x == len(snk.board) - 1 and snk.y == 0:
                snk.down()
                lastlastmove = lastmove
                lastmove = 'down'
            elif snk.x == len(snk.board) - 1 and snk.y == len(snk.board) - 1:
                snk.up()
                lastlastmove = lastmove
                lastmove = 'up'

            elif snk.apple[0] <= snk.x:
                turnDir(snk, 'right')

            elif snk.x == len(snk.board) - 1:
                checkSide(snk, 'right')

    elif snk.facing == 'up':
        try:
            if snk.board[snk.y - 1][snk.x] == 1:
                checkSide(snk, 'up')
            elif snk.board[snk.y - 1][snk.x + 1] == 1 and snk.board[snk.y - 1][snk.x - 1] == 1:
                oneWayCheck(snk, 'up')
            else:
                raise IndexError

        except IndexError:
            if snk.y == 0 and snk.x == len(snk.board) - 1:
                snk.left()
                lastlastmove = lastmove
                lastmove = 'left'
            elif snk.y == 0 and snk.x == 0:
                snk.right()
                lastlastmove = lastmove
                lastmove = 'right'

            elif snk.apple[1] >= snk.y:
                turnDir(snk, 'up')

            elif snk.y == 0:
                checkSide(snk, 'up')

    elif snk.facing == 'down':
        try:
            if snk.board[snk.y + 1][snk.x] == 1:
                checkSide(snk, 'down')
            elif snk.board[snk.y + 1][snk.x + 1] == 1 and snk.board[snk.y + 1][snk.x - 1] == 1:
                oneWayCheck(snk, 'down')
            else:
                raise IndexError

        except IndexError:
            if snk.y == len(snk.board) - 1 and snk.x == 0:
                snk.right()
                lastlastmove = lastmove
                lastmove = 'right'
            elif snk.y == len(snk.board) - 1 and snk.x == len(snk.board) - 1:
                snk.left()
                lastlastmove = lastmove
                lastmove = 'left'

            elif snk.apple[1] <= snk.y:
                turnDir(snk, 'down')

            elif snk.y == len(snk.board) - 1:
                checkSide(snk, 'down')

    else:
        snk.up()

def turnDir(snk, d):

    global lastmove
    global lastlastmove

    if d == 'up' or d == 'down':
        try:
            if snk.apple[0] > snk.x and snk.board[snk.y][snk.x + 1] != 1:
                snk.right()
                lastlastmove = lastmove
                lastmove = 'right'
            elif snk.apple[0] <= snk.x and snk.board[snk.y][snk.x - 1] != 1:
                snk.left()
                lastlastmove = lastmove
                lastmove = 'left'

            elif snk.board[snk.y - 1][snk.x] == 1 and d == 'up':
                pass
            elif snk.board[snk.y + 1][snk.x] == 1 and d == 'down':
                pass
        except IndexError:
            checkSide(snk, 'up')

    elif d == 'left' or d == 'right':
        try:
            if snk.apple[1] > snk.y and snk.board[snk.y + 1][snk.x] != 1:
                snk.down()
                lastlastmove = lastmove
                lastmove = 'down'
            elif snk.apple[1] <= snk.y and snk.board[snk.y - 1][snk.x] != 1:
                snk.up()
                lastlastmove = lastmove
                lastmove = 'up'
            elif snk.board[snk.y][snk.x - 1] == 1 and d == 'left':
                pass
            elif snk.board[snk.y][snk.x + 1] == 1 and d == 'right':
                pass
        except IndexError:
            checkSide(snk, 'left')


def checkSide(snk, d):

    global lastmove
    global lastlastmove

    if d == 'up' or d == 'down':
        val = 0
        for index, i in enumerate(snk.board[snk.y]):
            if index == snk.x:
                continue
            val += i / ((snk.x - index) * 10)
        if val < 0 or snk.x == len(snk.board) - 1:
            snk.left()
        elif val > 0 or snk.x == 0:
            snk.right()
        else:
            snk.left() if lastlastmove == 'left' else snk.right()

    elif d == 'left' or d == 'right':
        val = 0
        for i in range(len(snk.board)):
            if i == snk.y:
                continue
            val += (snk.board[i][snk.x]) / ((snk.y - i) * 10)
        if val > 0 or snk.y == 0:
            snk.down()
        elif val < 0 or snk.y == len(snk.board) - 1:
            snk.up()
        else:
            snk.down() if lastlastmove == 'down' else snk.up()


def oneWayCheck(snk, d):

    global lastmove
    global lastlastmove

    if d == 'up' or d == 'down':
        if snk.board[snk.y][snk.x + 1] == 1:
            snk.left()
            lastlastmove = lastmove
            lastmove = 'left'
        elif snk.board[snk.y][snk.x - 1] == 1:
            snk.right()
            lastlastmove = lastmove
            lastmove = 'right'

    elif d == 'left' or d == 'right':
        if snk.board[snk.y + 1][snk.x] == 1:
            snk.up()
            lastlastmove = lastmove
            lastmove = 'up'
        elif snk.board[snk.y - 1][snk.x] == 1:
            snk.down()
            lastlastmove = lastmove
            lastmove = 'down'


lastmove = None
lastlastmove = None