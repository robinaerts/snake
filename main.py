from random import randrange
import pygame

pygame.init()

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

game_over = False
font = pygame.font.Font('freesansbold.ttf', 32)

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
    # if prev_positions[-1] != snake_position:
    prev_positions.append(snake_position.copy())
    if snake_length <= len(prev_positions):
        del prev_positions[0]
    # print(prev_positions)
    if snake_length > 1:
        for x in range(1, snake_length):
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


def game_over_screen():
    WIN.fill(BGCOLOR)
    text = font.render("Game Over: Score " + str(snake_length), False, WHITE)
    textRect = text.get_rect()
    textRect.center = (WIDTH//2, HEIGHT//2)
    WIN.blit(text, textRect)
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
    global snake_length, is_apple, game_over
    if apple_position == snake_position:
        snake_length += 1
        is_apple = False
    prev_positions_copy = prev_positions.copy()
    if (len(prev_positions) > 1):
        del prev_positions_copy[-1]
        if (snake_position in prev_positions_copy):
            game_over = True


def restart_game():
    global snake_position, snake_length, snake_direction, prev_positions, is_apple, apple_position, game_over
    snake_position = [2, 9]
    snake_length = 1
    snake_direction = "right"
    prev_positions = []
    is_apple = False
    apple_position = [0, 0]
    game_over = False


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_r]:
                restart_game()
        if not game_over:
            snake_movement(keys_pressed)
            draw_canvas()
            check_apple_snake()
        else:
            game_over_screen()
    pygame.quit()


if __name__ == "__main__":
    main()
