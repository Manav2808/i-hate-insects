import pygame
import os
import threading
import time
import draw_screens as ds
import objects as o

pygame.font.init()

WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My First Game")

PLAYER = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Player_Green.png")), (81, 81)).convert_alpha()
ENEMY = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Enemy.png")), (64, 64)).convert_alpha()

FPS = 60
Gen_En = 0

screen_counter = 1

def generate_enemies():
    while True:
        enemy = o.Enemy(ENEMY)
        o.Enemies.append(enemy)
        time.sleep(1)

def main():
    global Gen_En
    global screen_counter

    player = o.Player(600, 600, PLAYER)
    running = True

    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen_counter == 1 and 565 <= mouse[0] <= 715 and 350 <= mouse[1] <= 450:
                    screen_counter = 2
                    gen_en = threading.Thread(target = generate_enemies)
                if screen_counter == 1 and 565 <= mouse[0] <= 715 and 480 <= mouse[1] <= 580:
                    running = False

                bullet = o.Bullet(player.rect.x, player.rect.y)

        if screen_counter == 1:
            pygame.mouse.set_visible(True)
            ds.draw_main_menu_screen()
        elif screen_counter == 2:
            pygame.mouse.set_visible(False)
            ds.draw_main_game_screen(player, o.Bullets, o.Enemies)
            if Gen_En == 0:
                gen_en.start()
                Gen_En = 1

            keys_pressed = pygame.key.get_pressed()
            player.move(keys_pressed)

            o.bullet_movement(o.Bullets, o.Delete_Bullets)

        if player.lives == 0:
            ds.game_over(player.score)
            running = False

        for enemies in o.Delete_Enemies:
            del enemies

        for bullets in o.Delete_Bullets:
            del bullets

        mouse = pygame.mouse.get_pos()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
