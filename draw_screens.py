import pygame
import os
import main as m
import objects as o

pygame.font.init()

TITLE_FONT = pygame.font.SysFont("leelawadee", 90)
PLAYER_INFO_FONT = pygame.font.SysFont("calibri", 35)
FINAL_SCORE_FONT = pygame.font.SysFont("cambria", 40)

BACKGROUND = pygame.image.load(os.path.join("Assets", "Background.png")).convert_alpha()
PLAY_BUTTON = pygame.image.load(os.path.join("Assets", "PLAY.png")).convert_alpha()
EXIT_BUTTON = pygame.image.load(os.path.join("Assets", "EXIT.png")).convert_alpha()


GAME_OVER_FONT = pygame.font.SysFont("cambria", 85)
GAME_OVER = GAME_OVER_FONT.render("GAME OVER", True, (255, 255, 0))

def draw_main_menu_screen():
    TITLE = TITLE_FONT.render("I HATE INSECTS", False, (32, 226, 27))

    m.WINDOW.blit(BACKGROUND, (0, 0))
    m.WINDOW.blit(PLAY_BUTTON, (565, 350))
    m.WINDOW.blit(EXIT_BUTTON, (565, 480))
    m.WINDOW.blit(TITLE, (345, 100))

def draw_main_game_screen(player, Bullets, Enemies):
    PLAYER_LIVES = PLAYER_INFO_FONT.render(f"Lives: {player.lives}", True, (0, 0, 0))
    PLAYER_SCORE = PLAYER_INFO_FONT.render(f"Score: {player.score}", True, (0, 0, 0))

    m.WINDOW.blit(BACKGROUND, (0, 0))

    player.draw(m.PLAYER, m.WINDOW)

    #for enemy in e.Enemies:
    #    enemy.draw(ENEMY)

    for bullet in Bullets:
        pygame.draw.rect(m.WINDOW, (0, 0, 0), bullet)

    for enemy in Enemies:
        enemy.draw(m.WINDOW)
        enemy.move(player, Bullets, o.Delete_Enemies, o.Delete_Bullets)

    m.WINDOW.blit(PLAYER_LIVES, (10, 625))
    m.WINDOW.blit(PLAYER_SCORE, (10, 660))


def game_over(SCORE):
    FINAL_SCORE = FINAL_SCORE_FONT.render(f"Your Score: {SCORE}", True, (255, 255, 0))

    m.WINDOW.blit(GAME_OVER, (400, 300))
    m.WINDOW.blit(FINAL_SCORE, (500, 400))
    pygame.display.update()
    pygame.time.delay(5000)
