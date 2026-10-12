import pygame
import random
import sys

pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 600
CELL = 20  # Размер шага и квадрата змейки

# Создаем окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake — Skins Edition (No Images)")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# Стартовая змейка (координаты блоков)
snake_pos = [[100, 100], [80, 100], [60, 100]]

# ---------------------------------------------
# цвета игры
# ---------------------------------------------
GRASS_COLOR_1 = (50, 160, 50)     # Трава — светлая клетка
GRASS_COLOR_2 = (40, 150, 40)     # Трава — тёмная клетка
SNAKE_COLOR = (0, 255, 0)         # Скин змейки
APPLE_COLOR = (255, 50, 50)       # Скин яблока
# ---------------------------------------------
main = pygame.image.load('freakyasssnake.png')
dead = pygame.image.load('freakysnakedead.png')
texture = main
HEAD = pygame.transform.rotate(texture, 90)
texturepos = texture.get_rect(topleft=(snake_pos[0][0],snake_pos[0][1]))

# Направление движения
dx, dy = CELL, 0
direction = 'RIGHT'

# Создаем еду
food = [random.randrange(0, WIDTH - CELL, CELL),
        random.randrange(0, HEIGHT - CELL, CELL)]

score = 0
gameover = False

# ------------------------------------------------------------
# Функция: рисуем клетчатую траву (как поле Minecraft)
# ------------------------------------------------------------
def draw_grass():
    """Фон в стиле «травяного поля» с шахматным узором."""
    for y in range(0, HEIGHT, CELL):
        for x in range(0, WIDTH, CELL):
            # Клетки чередуются
            if (x // CELL + y // CELL) % 2 == 0:
                color = GRASS_COLOR_1
            else:
                color = GRASS_COLOR_2
            pygame.draw.rect(screen, color, (x, y, CELL, CELL))


# ------------------------------------------------------------
# Функция: отрисовка змейки
# ------------------------------------------------------------
def draw_snake():
    """Рисуем каждый блок змейки."""
    texturepos = texture.get_rect(topleft=(snake_pos[0][0], snake_pos[0][1]))
    if snake_pos[0]:
        screen.blit(HEAD, texturepos)
    if not gameover:
        for x, y in snake_pos[1:]:
            pygame.draw.rect(screen, SNAKE_COLOR, (x, y, CELL, CELL))


# ------------------------------------------------------------
# Функция: яблоко
# ------------------------------------------------------------
def draw_food():
    """Рисуем яблоко."""
    pygame.draw.rect(screen, APPLE_COLOR, (food[0], food[1], CELL, CELL))


# ------------------------------------------------------------
# Экран поражения
# ------------------------------------------------------------
def game_over():
    """Показать текст после проигрыша."""
    global gameover,texture,HEAD,texturepos
    gameover = True
    texture = dead
    texturepos = texture.get_rect(topleft=(snake_pos[0][0],snake_pos[0][1]))
    draw_snake()
    text = font.render("GAME OVER (press R to restart)", True, (255, 255, 255))
    screen.blit(text, (50, HEIGHT // 2))
    pygame.display.update()


# =========================== ИГРОВОЙ ЦИКЛ ================================
while True:

    # --- Обработка кнопок и выхода ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Управление направлениями
        if event.type == pygame.KEYDOWN:
            # Нельзя повернуть в противоположную сторону
            if not gameover:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and dy == 0 and direction != 'DOWN':
                    dx, dy = 0, -CELL
                    direction = 'UP'
                    HEAD = pygame.transform.rotate(texture, 180)
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and dy == 0 and direction != 'UP':
                    dx, dy = 0, CELL
                    direction = 'DOWN'
                    HEAD = pygame.transform.rotate(texture, 0)
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and dx == 0 and direction != 'RIGHT':
                    dx, dy = -CELL, 0
                    direction = 'LEFT'
                    HEAD = pygame.transform.rotate(texture, 270)
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and dx == 0 and direction != 'LEFT':
                    dx, dy = CELL, 0
                    direction = 'RIGHT'
                    HEAD = pygame.transform.rotate(texture, 90)
            # Перезапуск
            if event.key == pygame.K_r and gameover:
                snake_pos = [[100, 100], [80, 100], [60, 100]]
                texture = main
                HEAD = pygame.transform.rotate(texture, 90)
                dx, dy = CELL, 0
                score = 0
                gameover = False
                food = [random.randrange(0, WIDTH - CELL, CELL),
                        random.randrange(0, HEIGHT - CELL, CELL)]

    # --- Движение змейки ---
    if not gameover:
        head = [snake_pos[0][0] + dx, snake_pos[0][1] + dy]
        snake_pos.insert(0, head)

        # Проверка — съела ли змейка яблоко, если сьела счет увеличивается
        if head == food:
            score += 1
            # через функцию рандома делаем для змейки новые яблоки на поле
            food = [random.randrange(0, WIDTH - CELL, CELL),
                    random.randrange(0, HEIGHT - CELL, CELL)]
        else:
            texture = main
            snake_pos.pop()  # Удаляем хвост (анимация движения змейки)

    # --- Проверка на столкновения ---
    if (
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT or
        head in snake_pos[1:]):
        game_over()
        continue

    # --- Отрисовка всего ---
    draw_grass()
    draw_snake()
    draw_food()

    # Кол-во очков
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(8)  # скорость игры