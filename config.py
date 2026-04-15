import pygame
import math

# Khởi tạo pygame
pygame.init()

# Cấu hình màn hình
WIDTH = 900
HEIGHT = 950
FPS = 60

# Màu sắc
COLOR = 'blue'
PI = math.pi

# Tốc độ
PLAYER_SPEED = 2
GHOST_SPEEDS_NORMAL = [2, 2, 2, 2]
GHOST_SPEEDS_POWERUP = [1, 1, 1, 1]
GHOST_SPEED_EATEN = 2
GHOST_SPEED_DEAD = 4

# Thời gian
POWERUP_DURATION = 600
STARTUP_TIME = 180

# Điểm số
SCORE_DOT = 10
SCORE_POWERUP = 50

# Vị trí ban đầu
PLAYER_START_X = 450
PLAYER_START_Y = 663

BLINKY_START_X = 56
BLINKY_START_Y = 58

INKY_START_X = 440
INKY_START_Y = 388

PINKY_START_X = 440
PINKY_START_Y = 438

CLYDE_START_X = 390
CLYDE_START_Y = 438

# Font
FONT = pygame.font.Font('freesansbold.ttf', 20)