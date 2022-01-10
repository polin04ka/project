import pygame


def getColorByNumber(number):
    number2Color_dict = {2: ['#eee4da', '#776e65'], 4: ['#ede0c8', '#776e65'], 8: ['#f2b179', '#f9f6f2'],
                         16: ['#f59563', '#f9f6f2'], 32: ['#f67c5f', '#f9f6f2'], 64: ['#f65e3b', '#f9f6f2'],
                         128: ['#edcf72', '#f9f6f2'], 256: ['#edcc61', '#f9f6f2'], 512: ['#edc850', '#f9f6f2'],
                         1024: ['#edc53f', '#f9f6f2'], 2048: ['#edc22e', '#f9f6f2'], 4096: ['#eee4da', '#776e65'],
                         8192: ['#edc22e', '#f9f6f2'], 16384: ['#f2b179', '#776e65'], 32768: ['#f59563', '#776e65'],
                         65536: ['#f67c5f', '#f9f6f2'], 'null': ['#9e948a', None]}
    return number2Color_dict[number]


def drawGameMatrix(screen, game_matrix, cfg):
    for i in range(len(game_matrix)):
        for j in range(len(game_matrix[i])):
            number = game_matrix[i][j]
            x = (j + 1) * cfg.MARGIN_SIZE + j * cfg.MATRIX_SIZE
            y = (i + 1) * cfg.MARGIN_SIZE + i * cfg.MATRIX_SIZE

            pygame.draw.rect(screen, pygame.Color(getColorByNumber(number)[0]),
                             (x, y, cfg.MATRIX_SIZE, cfg.MATRIX_SIZE))

            if number != 'null':
                font_color = pygame.Color(getColorByNumber(number)[1])
                font_size = cfg.MATRIX_SIZE - cfg.MARGIN_SIZE * len(str(number))
                font = pygame.font.Font(cfg.FONTPATH, font_size)
                text = font.render(str(number), True, font_color)
                text_rect = text.get_rect()
                text_rect.centerx, text_rect.centery = x + cfg.MATRIX_SIZE / 2, y + cfg.MATRIX_SIZE / 2
                screen.blit(text, text_rect)


def drawScore(screen, score, cfg):
    font_color = (255, 255, 255)
    font_size = 30
    font = pygame.font.Font(cfg.FONTPATH, font_size)
    text_score = font.render('результат:  ' + str(score), True, font_color)

    start_x = cfg.GAME_MATRIX_SIZE[1] * cfg.MATRIX_SIZE + (cfg.GAME_MATRIX_SIZE[1] + 1) * cfg.MARGIN_SIZE

    screen.blit(text_score, (start_x + 10, 20 + text_score.get_height()))
    start_y = 30 + text_score.get_height() * 2

    return (start_x, start_y)


def drawGameIntro(screen, start_x, start_y, cfg):
    start_y += 40
    font_color = (255, 255, 255)
    font_size_big = 30
    font_size_small = 20
    font_big = pygame.font.Font(cfg.FONTPATH, font_size_big)
    font_small = pygame.font.Font(cfg.FONTPATH, font_size_small)
    intros = ['советик:', 'используй кнопки стрелочек']
    for idx, intro in enumerate(intros):
        font = font_big if idx == 0 else font_small
        text = font.render(intro, True, font_color)
        screen.blit(text, (start_x + 10, start_y))
        start_y += font.get_height() + 10
