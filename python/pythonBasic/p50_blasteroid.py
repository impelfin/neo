#!/usr/bin/env python

import pygame
import math
from p47_spaceship import *
from p48_asteroid import *
from p49_blast import *

ASTEROID_SCORES = [20, 50, 100]
WIDTH = 500
HEIGHT = 500

def main():
    pygame.init()
    total_score = 0
    fps = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    ship = SpaceShip(WIDTH, HEIGHT, 0, 0)
    asteroid_list = pygame.sprite.Group()
    for i in range(4):
        asteroid = Asteroid(0, WIDTH, HEIGHT)
        asteroid_list.add(asteroid)
    blast_list = pygame.sprite.Group()
    pygame.key.set_repeat()

    while True:
        #get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    break
            keystate = pygame.key.get_pressed()
            if (keystate[pygame.K_SPACE] and ship.lives > 0):
                blast = Blast()
                blast.firedfrom(ship)
                blast_list.add(blast)

        keystate = pygame.key.get_pressed()

        #handle player input
        heading = keystate[pygame.K_UP] - keystate[pygame.K_DOWN]
        direction = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
        if (heading > 0):
            ship.accelerate()
        elif (heading < 0):
            ship.decelerate()
        if (direction > 0):
            ship.turn_right()
        elif (direction < 0):
            ship.turn_left()

        ship.update()
        asteroid_list.update()
        blast_list.update()

        #asteroids.collide(ship)
        collide_list = pygame.sprite.spritecollide(ship, asteroid_list, True)
        for asteroid in collide_list:
            asteroid_list.remove(asteroid)
            ship.damage()

        #blasts.collide(asteroids)
        for blast in blast_list:
            hit_list = pygame.sprite.spritecollide(blast, asteroid_list, True)
            for asteroid in hit_list:
                # asteroid splitted
                if (asteroid.type == 0 or asteroid.type == 1):
                    new1 = Asteroid(asteroid.type + 1, WIDTH, HEIGHT)
                    new1.x, new1.y = asteroid.x, asteroid.y
                    asteroid_list.add(new1)
                    new2 = Asteroid(asteroid.type + 1, WIDTH, HEIGHT)
                    new2.x, new2.y = asteroid.x, asteroid.y
                    asteroid_list.add(new2)
                asteroid_list.remove(asteroid)
                blast_list.remove(blast)
                total_score += ASTEROID_SCORES[asteroid.type]

            if blast.x > WIDTH or blast.x < 0 or blast.y > HEIGHT or blast.y < 0:
                blast_list.remove(blast)

        if (len(asteroid_list) == 0):
            for i in range(4):
                asteroid = Asteroid(0, WIDTH, HEIGHT)
                asteroid_list.add(asteroid)
        window.fill(pygame.Color(0, 0, 0))
        asteroid_list.draw(window)
        if (ship.lives > 0):
            window.blit(ship.image, ship.rect)
        blast_list.draw(window)

        font = pygame.font.SysFont("monospace", 24)
        label = font.render(str(total_score), 1, (200,200,200))
        window.blit(label, (50, 10))

        rect = ship.surface.get_rect()
        if (ship.lives >= 1):
            rect.center = (30, 60)
            window.blit(ship.surface, rect)
        if (ship.lives >= 2):
            rect.center = (50, 60)
            window.blit(ship.surface, rect)
        if (ship.lives >= 3):
            rect.center = (70, 60)
            window.blit(ship.surface, rect)
        if (ship.lives == 0):
            font = pygame.font.SysFont("monospace", 36)
            label = font.render("GAME OVER", 1, (200,200,200))
            window.blit(label, (WIDTH/2-100, HEIGHT/2-50))

        pygame.display.update()
        fps.tick(30)

if __name__ == '__main__':
    main()

