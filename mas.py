import pygame
import random

# Инициализация игрового окна
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")

# Цвета
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

# Параметры змейки
snake_pos = [100, 50]  # начальное положение змейки
snake_body = [[100, 50], [90, 50], [80, 50]]  # начальное тело змейки
direction = "RIGHT"  # начальное направление движения

# Параметры фрукта
fruit_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
fruit_spawn = True

# Параметры игры
clock = pygame.time.Clock()
score = 0

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = "RIGHT"
            if event.key == pygame.K_LEFT:
                direction = "LEFT"
            if event.key == pygame.K_UP:
                direction = "UP"
            if event.key == pygame.K_DOWN:
                direction = "DOWN"

    # Движение змейки
    if direction == "RIGHT":
        snake_pos[0] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10

    # Проверка на столкновение с фруктом
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop(0)

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
        fruit_spawn = True

    # Добавление новой части к змейке
    snake_body.append(list(snake_pos))

    # Отрисовка игрового поля
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, red, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    # Проверка на столкновение с собой
    if snake_pos[0] < 0 or snake_pos[0] > width - 10 or snake_pos[1] < 0 or snake_pos[1] > height - 10:
        pygame.quit()
        quit()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            pygame.quit()
            quit()

    # Обновление игрового экрана
    pygame.display.update()
    clock.tick(15)