import texts

import random
import time
import sys

import pygame


pygame.init()
W, H = 600, 400
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Ветер перемен")

f1 = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
FPS = 10


class Hero:
    """Класс описания героя игры."""

    SKIN = pygame.image.load('pics/oqGmT31MoBkGF6bioD1X--1--6z5jn.jpg').convert()
    SKIN_RECT = SKIN.get_rect(center=(W//2, H//2))
    SKILL = "hit"
    BASE_HP = 1000
    BASE_ATTACK = 50
    BASE_ULTA = 100
    ULTA = "mega hit"
    RANGE_ATTACK = (20, 100)

    def __init__(self,
                 name: str, ):
        self.name = name

    def info(self):
        print(f'Меня зовут {self.name}, \n'
              f'Я умею {self.SKILL}')

    def attack(self) -> int:
        return self.BASE_ATTACK + random.randint(*self.RANGE_ATTACK)

    def ulta(self) -> int:
        return self.BASE_ULTA + random.randint(*self.RANGE_ATTACK)


class Mage(Hero):
    """Тут крутое описание с точкой в конце."""

    SKIN = pygame.image.load('pics/mage.jpg').convert()
    SKIN_RECT = SKIN.get_rect(center=(W//2, H//2))
    SKILL = "Fire ball"
    BASE_HP = 500
    BASE_ATTACK = 100
    BASE_ULTA = 150
    ULTA = "Mega frire ball"
    RANGE_ATTACK = (20, 100)


class Warior(Hero):
    """Тут крутое описание с точкой в конце."""

    SKIN = pygame.image.load('pics/warrior.jpg').convert()
    SKIN_RECT = SKIN.get_rect(center=(W//2, H//2))
    SKILL = "тык пикой"
    BASE_HP = 800
    BASE_ATTACK = 110
    BASE_ULTA = 130
    ULTA = "палкой по ногам"
    RANGE_ATTACK = (20, 100)


class Healer(Hero):
    """Тут крутое описание с точкой в конце."""

    SKIN = pygame.image.load('pics/healer.jpg')
    SKIN_RECT = SKIN.get_rect(center=(W//2, H//2))
    SKILL = "исцелил"
    BASE_HP = 200
    BASE_ATTACK = 50
    BASE_ULTA = 200
    ULTA = "очень хорошо исцелил"
    RANGE_ATTACK = (20, 100)


class BadBoy(Hero):
    SKIN = pygame.image.load('pics/oqGmT31MoBkGF6bioD1X--1--6z5jn.jpg')
    SKIN_RECT = SKIN.get_rect(center=(W // 2, H // 2))
    SKILL = "исцелил"
    BASE_HP = 200
    BASE_ATTACK = 50
    BASE_ULTA = 200
    ULTA = "очень хорошо исцелил"
    RANGE_ATTACK = (20, 100)


def choose_character() -> Hero:
    c = {
        'mage': Mage,
        'warior': Warior,
        'healer': Healer
    }
    character = input(texts.START_TEXT)

    return c[character](input('Введите имя'))


def training(character):
    print(f'\n\nРад познакомиться {character.name}\n'
          f'Ты умеешь {character.SKILL}\n'
          f'Давай начнем тренеровочку!\n'
          f'Для выхода напиши skip')
    action = None

    while action != 'skip':
        a = {
            'a': character.attack(),
            'u': character.ulta()
        }
        action = input('Напишите\n"a" для атаки\n'
                       '"u" для Ульты\n')
        if action in a:
            print(a[action])


def start():
    global Character
    global vrag
    Character = choose_character()
    vrag = BadBoy('Плохиш')


start()
text = f1.render(f'Полетели',
                 True,
                 (180, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                hero_damage = Character.attack()
                text = f1.render(f'Нанес {hero_damage} урона',
                                  False,
                                  (180, 0, 0))
                sc.blit(text, (10, 50))
                pygame.display.update()

                vrag.BASE_HP -= hero_damage

                time.sleep(1)

                damage = vrag.attack()
                text = f1.render(f'{vrag.name} нанес вам {damage} урона',
                                 False,
                                 (180, 0, 0))
                sc.blit(text, (10, 50))
                pygame.display.update()

                Character.BASE_HP -= damage

                if Character.BASE_HP <= 0:
                    print('GAME OVER')
                    break
                if vrag.BASE_HP <= 0:
                    print('YOU WIN')
                    start()
                    time.sleep(2)

    sc.blit(Character.SKIN, Character.SKIN_RECT)

    pygame.display.update()
    clock.tick(FPS)
