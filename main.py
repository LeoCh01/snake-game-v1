import pygame
import snake
import bot
pygame.init()

scr = 800
snake.Snake.scr = scr
screen = pygame.display.set_mode((scr, scr))
pygame.display.set_caption('Snake Game')

size = 20 # n by n grid
snk = snake.Snake(size, scr)
block = snk.block

sc = [0, 0, 0, 0, 0, 0, 0, 0, 0]
run = 0

clock = pygame.time.Clock()


def scoreboard(score):
    global sc
    sc.append(score)
    sc = sorted(sc)[::-1]
    sc.pop()


def game():
    global run
    if not snk.death:
        snk.update()

    bot.move2(snk)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snk.up()
                break
            elif event.key == pygame.K_s:
                snk.down()
                break
            elif event.key == pygame.K_a:
                snk.left()
                break
            elif event.key == pygame.K_d:
                snk.right()
                break
            elif event.key == pygame.K_r:
                snk.reset()

    for row in range(len(snk.board)):
        for col in range(len(snk.board)):
            pos = (row * block, col * block)

            if snk.board[col][row] == 1 and (row, col) in snk.walls:
                pygame.draw.rect(screen, (51, 255, 255), (pos[0] + 2, pos[1] + 2, block - 4, block - 4), border_radius=2)
            elif snk.board[col][row] == 1:
                pygame.draw.rect(screen, (0, 255, 0), (pos[0] + 2, pos[1] + 2, block - 4, block - 4), border_radius=2)
            elif snk.board[col][row] == 2:
                pygame.draw.rect(screen, (255, 0, 0), (pos[0] + 2, pos[1] + 2, block - 4, block - 4), border_radius=2)
            elif snk.board[col][row] == 0:
                pygame.draw.rect(screen, (40, 40, 40), (pos[0], pos[1], block, block), border_radius=2, width=1)

    pygame.draw.circle(screen, (225, 225, 225), (snk.x * block + snk.eyes[0], snk.y * block + snk.eyes[1]), block // 5)
    pygame.draw.circle(screen, (225, 225, 225), (snk.x * block + snk.eyes[2], snk.y * block + snk.eyes[3]), block // 5)
    pygame.draw.circle(screen, (0, 0, 0), (snk.x * block + snk.pupil[0], snk.y * block + snk.pupil[1]), block // 7)
    pygame.draw.circle(screen, (0, 0, 0), (snk.x * block + snk.pupil[2], snk.y * block + snk.pupil[3]), block // 7)

    if snk.death:
        # gameOverOverlay = pygame.Surface((scr, scr), pygame.SRCALPHA)
        # gameOverOverlay.fill((0, 0, 0, 100))
        # font = pygame.font.SysFont('Arial', scr//10, bold=True)
        # score = font.render('Score: ' + str(snk.length), False, (225, 225, 225))
        # screen.blit(gameOverOverlay, (0, 0))
        # screen.blit(score, (scr//2 - score.get_width()//2, scr//2 - score.get_height()//2))
        scoreboard(snk.length)
        run += 1
        # print('[' + str(run) + ']\tscore: ' + str(snk.length))
        # snk.snakepos = snk.snakepos[::-1]
        # snk.board[snk.snakepos[0][1]][snk.snakepos[0][0]] = 'H'
        # snk.board[snk.snakepos[1][1]][snk.snakepos[1][0]] = 'h'
        # snk.board[snk.snakepos[2][1]][snk.snakepos[2][0]] = 'h'
        # print('\n'.join(['\t'.join([str(i) for i in j]) for j in snk.board]), '\n')
        snk.reset()

    font = pygame.font.SysFont('Arial', scr // 20, bold=True)
    sb = font.render('Scoreboard', False, (225, 225, 225))
    r = font.render(f'[{run}]', False, (150, 150, 150))
    screen.blit(sb, (0, 0))
    screen.blit(r, (scr - r.get_width(), 0))
    font2 = pygame.font.SysFont('Arial', scr // 30, bold=True)

    for i in range(len(sc)):
        s = font2.render(f'{i + 1}. ' + str(sc[i]), False, (225, 225, 225))
        s.set_alpha(100)
        screen.blit(s, (0, sb.get_height() + s.get_height() * i))

    pygame.display.update()
    screen.fill((25, 25, 25))
    clock.tick(100)


while True:
    try:
        game()
    except:
        snk.reset()