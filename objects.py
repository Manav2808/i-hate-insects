import pygame
import os
import random

Enemies = []
All_Enemies = []
Bullets = []
Enemy_Counter = 1
bullet_velocity = 12

Delete_Enemies = []
Delete_Bullets = []

class Player:
    def __init__(self, x, y, image):
        self.lives = 3
        self.score = 0
        self.velocity = 8
        self.image = image
        self.rect = self.image.get_rect(topleft = (x, y))

    def draw(self, image, WINDOW):
        WINDOW.blit(self.image, self.rect)

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_w] and self.rect.y - self.velocity >= -10:
            self.rect.y -= self.velocity
        if keys_pressed[pygame.K_s] and self.rect.y + self.velocity <= 660:
            self.rect.y += self.velocity
        if keys_pressed[pygame.K_a] and self.rect.x - self.velocity >= -10:
            self.rect.x -= self.velocity
        if keys_pressed[pygame.K_d] and self.rect.x + self.velocity <= 1220:
            self.rect.x += self.velocity

class Enemy:

    def __init__(self, image):
        self.velocity = 2
        self.x = random.randint(-7, 1235)
        self.y = -30
        self.image = image
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

    def draw(self, WINDOW):
        WINDOW.blit(self.image, self.rect)

    def move(self, player, bullets, Delete_Enemies, Delete_Bullets):
        self.rect.y += self.velocity

        if self.rect.y > 720:
            player.score -= 25
            Enemies.remove(self)
            Delete_Enemies.append(self)
        if self.rect.colliderect(player.rect):
            Delete_Enemies.append(self)
            Enemies.remove(self)
            player.lives -= 1
        for bullet in bullets:
            if self.rect.colliderect(bullet):
                player.score += 100
                Delete_Enemies.append(self)
                Delete_Bullets.append(bullet)
                Enemies.remove(self)
                bullets.remove(bullet)

class Bullet:
    def __init__(self, px_pos, py_pos):
        self.object = pygame.Rect(px_pos + 30, py_pos, 6, 6)
        Bullets.append(self.object)

def bullet_movement(Bullets, Delete_Bullets):
    for bullet in Bullets:
        bullet.y -= bullet_velocity
        if bullet.y < 0:
            Delete_Bullets.append(bullet)
            Bullets.remove(bullet)
            Delete_Bullets = []
