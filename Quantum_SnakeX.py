import math
import pygame
import sys
import random
from collections import deque
import time
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Game constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.body = deque([(GRID_WIDTH // 2, GRID_HEIGHT // 2)])
        self.direction = (1, 0)  # Start moving right
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)

        self.body.appendleft(new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        # Prevent 180-degree turns
        dx, dy = self.direction
        new_dx, new_dy = new_direction
        if (dx, dy) != (-new_dx, -new_dy):
            self.direction = new_direction

    def check_collision(self):
        # Check if snake collides with itself
        head = self.body[0]
        return head in list(self.body)[1:]

    def get_head(self):
        return self.body[0]

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)

        # Load sounds
        self.load_sounds()

        self.reset()

    def load_sounds(self):
        # Create sounds directory if it doesn't exist
        if not os.path.exists('sounds'):
            os.makedirs('sounds')

        # Define sound file paths
        self.eat_sound_path = 'sounds/eat.wav'
        self.game_over_sound_path = 'sounds/game_over.wav'
        self.move_sound_path = 'sounds/move.wav'

        # Create default sounds if files don't exist
        self.create_default_sounds()

        # Load sounds
        self.eat_sound = pygame.mixer.Sound(self.eat_sound_path)
        self.game_over_sound = pygame.mixer.Sound(self.game_over_sound_path)
        self.move_sound = pygame.mixer.Sound(self.move_sound_path)

        # Adjust volumes
        self.eat_sound.set_volume(0.9)
        self.game_over_sound.set_volume(0.9)
        self.move_sound.set_volume(0.7)

    def create_default_sounds(self):
        # This creates very basic sounds if the files don't exist
        # In a real game, you'd use actual sound files

        if not os.path.exists(self.eat_sound_path):
            self.create_beep_sound(self.eat_sound_path, 440, 100)  # A4 note

        if not os.path.exists(self.game_over_sound_path):
            self.create_beep_sound(self.game_over_sound_path, 220, 500)  # A3 note

        if not os.path.exists(self.move_sound_path):
            self.create_beep_sound(self.move_sound_path, 330, 50)  # E4 note

    def create_beep_sound(self, filename, frequency, duration):
        # Create a simple beep sound as a placeholder
        sample_rate = 44100
        bits = 16

        pygame.mixer.pre_init(sample_rate, -bits, 2)

        # Generate a simple sine wave
        buf = bytearray(int(duration * sample_rate * 2))
        for i in range(0, len(buf), 2):
            t = i / sample_rate
            val = int(32767 * 0.5 * math.sin(2 * 3.14159 * frequency * t))
            buf[i] = val & 0xFF
            buf[i+1] = (val >> 8) & 0xFF

        with open(filename, 'wb') as f:
            f.write(buf)

    def reset(self):
        self.snake = Snake()
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False

    def generate_food(self):
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake.body:
                return food

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_r:
                        self.reset()
                else:
                    direction_changed = False
                    if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                        self.snake.change_direction((0, -1))
                        direction_changed = True
                    elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                        self.snake.change_direction((0, 1))
                        direction_changed = True
                    elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                        self.snake.change_direction((-1, 0))
                        direction_changed = True
                    elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                        self.snake.change_direction((1, 0))
                        direction_changed = True

                    if direction_changed:
                        self.move_sound.play()

    def update(self):
        if not self.game_over:
            self.snake.move()

            # Check if snake eats food
            if self.snake.get_head() == self.food:
                self.snake.grow = True
                self.food = self.generate_food()
                self.score += 1
                self.eat_sound.play()

            # Check for collision
            if self.snake.check_collision():
                self.game_over = True
                self.game_over_sound.play()

    def draw(self):
        self.screen.fill(BLACK)

        # Draw snake
        for i, segment in enumerate(self.snake.body):
            x, y = segment
            # Make head a slightly different color
            color = (0, 255, 0) if i > 0 else (0, 200, 0)
            pygame.draw.rect(self.screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw food
        x, y = self.food
        pygame.draw.rect(self.screen, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render("Game Over! Press R to restart", True, WHITE)
            self.screen.blit(game_over_text, (WIDTH // 2 - 180, HEIGHT // 2))

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()