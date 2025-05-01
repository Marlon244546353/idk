import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 500, 500
GRAVITY = 0.5
FLAP_STRENGTH = -7
PIPE_GAP = 200
PIPE_WIDTH = 70
PIPE_SPEED = 5

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (135, 206, 250)

# Load Assets
plane_img = pygame.image.load("airplane.png")  # Replace with your airplane image
plane_img = pygame.transform.scale(plane_img, (70, 70))

# Setup Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# Airplane Class
class Airplane:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.vel = 0

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel

    def flap(self):
        self.vel = FLAP_STRENGTH

    def draw(self, screen):
        screen.blit(plane_img, (self.x, self.y))


# Pipe Class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP)

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)


# Game Loop
def main():
    running = True
    airplane = Airplane()
    pipes = [Pipe(WIDTH + i * 200) for i in range(3)]
    score = 0

    while running:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                airplane.flap()

        airplane.update()
        airplane.draw(screen)

        for pipe in pipes:
            pipe.update()
            pipe.draw(screen)
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
                pipes.append(Pipe(WIDTH))
                score += 1
            if airplane.y < 0 or airplane.y > HEIGHT:
                running = False
            if pipe.top_rect.colliderect(pygame.Rect(airplane.x, airplane.y, 50, 35)) or \
                    pipe.bottom_rect.colliderect(pygame.Rect(airplane.x, airplane.y, 50, 35)):
                running = False

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()