import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 360
HEIGHT = 400
STEP = 2
RADIUS = 10

class Ball:
    def __init__(self):
        self.x = random.randint(RADIUS, WIDTH-RADIUS)
        self.y = random.randint(RADIUS, HEIGHT-RADIUS)
        self.x_step = random.choice([-STEP, STEP])
        self.y_step = random.choice([-STEP,STEP])
        self.color = random.choice([WHITE, RED, GREEN, BLUE])

    def move(self):
        self.x += self.x_step
        self.y += self.y_step

        if self.x + RADIUS >= WIDTH:
            self.x_step = -STEP

        if self.x - RADIUS <= 0:
            self.x_step = STEP

        if self.y + RADIUS >= HEIGHT:
            self.y_step = -STEP

        if self.y - RADIUS <= 0:
            self.y_step = STEP

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), RADIUS)
        
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Balls")

clock = pygame.time.Clock()

running = True

balls = []

for i in range(10):
    balls.append(Ball())

while running:
    # Control the speed of the game
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    for ball in balls:
        ball.draw(screen)
        ball.move()

    # Flip the screen
    pygame.display.flip()
pygame.quit()

