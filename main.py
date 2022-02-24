from random import randrange
import pygame

WIDTH, HEIGHT = 1000, 1000
PIECEWIDTH = 50
PIECEHEIGHT = 50

BGCOLOR = (20, 20, 20)
WHITE = (50, 50, 50)

snake_position = [2, 9]
snake_length = 1
SNAKE_COLOR = (102, 227, 34)
snake_direction = "right"

prev_positions = []
is_apple = False
apple_position = [0, 0]
APPLE_COLOR = (227, 69, 34)

FPS = 15

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake | Robin Aerts")


# DRAW

def draw_snake():
    global prev_positions, snake_position
    snake = pygame.Rect(
        snake_position[0] * PIECEWIDTH, snake_position[1] * PIECEHEIGHT, PIECEWIDTH, PIECEHEIGHT)
    pygame.draw.rect(WIN, SNAKE_COLOR, snake)
    if snake_direction == "right":
        snake_position[0] += 1
        if snake_position[0] >= 20:
            snake_position[0] = 0
    elif snake_direction == "down":
        snake_position[1] += 1
        if snake_position[1] >= 20:
            snake_position[1] = 0
    elif snake_direction == "left":
        snake_position[0] -= 1
        if snake_position[0] < 0:
            snake_position[0] = 20
    elif snake_direction == "up":
        snake_position[1] -= 1
        if snake_position[1] < 0:
            snake_position[1] = 20
    prev_positions.append(snake_position)
    if snake_length <= len(prev_positions):
        prev_positions.pop(0)
        print(prev_positions)
    if snake_length > 1:
        for x in range(1, snake_length):
            print(-x)
            position_x = prev_positions[-x][0]
            position_y = prev_positions[-x][1]
            segment = pygame.Rect(position_x * PIECEWIDTH, position_y * PIECEHEIGHT,
                                  PIECEWIDTH, PIECEHEIGHT)
            pygame.draw.rect(WIN, SNAKE_COLOR, segment)


def draw_apple():
    global is_apple
    global apple_position
    if not is_apple:
        apple_position = [randrange(0, 20), randrange(0, 20)]
    apple = pygame.Rect(
        apple_position[0] * PIECEWIDTH, apple_position[1] * PIECEHEIGHT, PIECEWIDTH, PIECEHEIGHT)
    pygame.draw.rect(WIN, APPLE_COLOR, apple)
    is_apple = True


def draw_grid():
    for x in range(WIDTH // PIECEWIDTH):
        for y in range(HEIGHT // PIECEHEIGHT):
            rect = pygame.Rect(x*PIECEWIDTH, y * PIECEHEIGHT,
                               PIECEHEIGHT, PIECEWIDTH)
            pygame.draw.rect(WIN, WHITE, rect, 1)


def draw_canvas():
    WIN.fill(BGCOLOR)
    draw_grid()
    draw_snake()
    draw_apple()
    pygame.display.update()


def snake_movement(keys_pressed):
    global snake_direction
    if keys_pressed[pygame.K_LEFT]:
        snake_direction = "left"
    elif keys_pressed[pygame.K_DOWN]:
        snake_direction = "down"
    elif keys_pressed[pygame.K_RIGHT]:
        snake_direction = "right"
    elif keys_pressed[pygame.K_UP]:
        snake_direction = "up"


def check_apple_snake():
    global snake_length, is_apple
    if (apple_position == snake_position):
        snake_length += 1
        is_apple = False


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        snake_movement(keys_pressed)
        draw_canvas()
        check_apple_snake()
    pygame.quit()


if __name__ == "__main__":
    main()
