import copy
from board import boards
from config import *

class GameState:
    """Quản lý toàn bộ trạng thái game"""
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset game về trạng thái ban đầu"""
        # Level
        self.level = copy.deepcopy(boards)
        
        # Player
        self.player_x = PLAYER_START_X
        self.player_y = PLAYER_START_Y
        self.direction = 0
        self.direction_command = 0
        self.turns_allowed = [False, False, False, False]
        
        # Ghosts
        self.blinky_x = BLINKY_START_X
        self.blinky_y = BLINKY_START_Y
        self.blinky_direction = 0
        self.blinky_dead = False
        self.blinky_box = False
        
        self.inky_x = INKY_START_X
        self.inky_y = INKY_START_Y
        self.inky_direction = 2
        self.inky_dead = False
        self.inky_box = False
        
        self.pinky_x = PINKY_START_X
        self.pinky_y = PINKY_START_Y
        self.pinky_direction = 2
        self.pinky_dead = False
        self.pinky_box = False
        
        self.clyde_x = CLYDE_START_X
        self.clyde_y = CLYDE_START_Y
        self.clyde_direction = 2
        self.clyde_dead = False
        self.clyde_box = False
        
        # Game state
        self.score = 0
        self.lives = 3
        self.powerup = False
        self.power_counter = 0
        self.eaten_ghost = [False, False, False, False]
        self.ghost_speeds = list(GHOST_SPEEDS_NORMAL)
        self.targets = [(self.player_x, self.player_y)] * 4
        
        # Counters
        self.counter = 0
        self.flicker = False
        self.startup_counter = 0
        self.moving = False
        
        # Game status
        self.game_over = False
        self.game_won = False
    
    def reset_positions(self):
        """Reset vị trí khi mất mạng"""
        self.powerup = False
        self.power_counter = 0
        self.player_x = PLAYER_START_X
        self.player_y = PLAYER_START_Y
        self.direction = 0
        self.direction_command = 0
        
        self.blinky_x = BLINKY_START_X
        self.blinky_y = BLINKY_START_Y
        self.blinky_direction = 0
        
        self.inky_x = INKY_START_X
        self.inky_y = INKY_START_Y
        self.inky_direction = 2
        
        self.pinky_x = PINKY_START_X
        self.pinky_y = PINKY_START_Y
        self.pinky_direction = 2
        
        self.clyde_x = CLYDE_START_X
        self.clyde_y = CLYDE_START_Y
        self.clyde_direction = 2
        
        self.eaten_ghost = [False, False, False, False]
        self.blinky_dead = False
        self.inky_dead = False
        self.clyde_dead = False
        self.pinky_dead = False
        self.startup_counter = 0
    
    def check_win(self):
        """Kiểm tra xem đã thắng chưa"""
        for row in self.level:
            if 1 in row or 2 in row:
                return False
        return True
    
    def update_ghost_speeds(self):
        """Cập nhật tốc độ ghost dựa trên trạng thái"""
        if self.powerup:
            self.ghost_speeds = list(GHOST_SPEEDS_POWERUP)
        else:
            self.ghost_speeds = list(GHOST_SPEEDS_NORMAL)
        
        # Ghost đã bị ăn
        for i in range(4):
            if self.eaten_ghost[i]:
                self.ghost_speeds[i] = GHOST_SPEED_EATEN
        
        # Ghost đang chết
        if self.blinky_dead:
            self.ghost_speeds[0] = GHOST_SPEED_DEAD
        if self.inky_dead:
            self.ghost_speeds[1] = GHOST_SPEED_DEAD
        if self.pinky_dead:
            self.ghost_speeds[2] = GHOST_SPEED_DEAD
        if self.clyde_dead:
            self.ghost_speeds[3] = GHOST_SPEED_DEAD