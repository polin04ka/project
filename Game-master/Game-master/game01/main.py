import pygame
from sys import exit
from modules.game2048 import *
from modules.utils import *
import cfg
from modules.endInterface import *


def main(cfg):
    pygame.init()

    pygame.mixer.music.load(cfg.BGMPATH)
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode(cfg.SCREENSIZE, 0, 32)

    pygame.display.set_caption("2048")

    game_2048 = Game2048(matrix_size=cfg.GAME_MATRIX_SIZE, max_score_filepath=cfg.MAX_SCORE_FILEPATH)

    is_running = True
    while is_running:
        screen.fill(pygame.Color(cfg.BG_COLOR))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    game_2048.setDirection(
                        {pygame.K_UP: 'UP', pygame.K_DOWN: 'DOWN', pygame.K_LEFT: 'LEFT', pygame.K_RIGHT: 'RIGHT'}[
                            event.key])

        game_2048.update()
        if game_2048.isGameOver:
            print('игра закончена :(')
            is_running = False
            game_2048.saveMaxScore()

        drawGameMatrix(screen, game_2048.game_matrix, cfg)
        (start_x, start_y) = drawScore(screen, game_2048.score, cfg)
        drawGameIntro(screen, start_x, start_y, cfg)

        pygame.display.update()

    return endInterface(screen, cfg)


if __name__ == '__main__':
    while True:
        if not main(cfg):
            break
