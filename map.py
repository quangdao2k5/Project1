import pygame
from config import WIDTH, HEIGHT, COLOR, PI

def draw_board(screen, level, flicker):
    """Vẽ bản đồ game"""
    num1 = (HEIGHT - 50) // 32
    num2 = WIDTH // 30
    
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                # Vẽ chấm nhỏ
                pygame.draw.circle(screen, 'white', 
                    (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            
            if level[i][j] == 2 and not flicker:
                # Vẽ power pellet
                pygame.draw.circle(screen, 'white', 
                    (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            
            if level[i][j] == 3:
                # Vẽ đường dọc
                pygame.draw.line(screen, COLOR, 
                    (j * num2 + (0.5 * num2), i * num1),
                    (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            
            if level[i][j] == 4:
                # Vẽ đường ngang
                pygame.draw.line(screen, COLOR, 
                    (j * num2, i * num1 + (0.5 * num1)),
                    (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            
            if level[i][j] == 5:
                # Vẽ góc dưới phải
                pygame.draw.arc(screen, COLOR, 
                    [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                    0, PI / 2, 3)
            
            if level[i][j] == 6:
                # Vẽ góc dưới trái
                pygame.draw.arc(screen, COLOR,
                    [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], 
                    PI / 2, PI, 3)
            
            if level[i][j] == 7:
                # Vẽ góc trên trái
                pygame.draw.arc(screen, COLOR, 
                    [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], 
                    PI, 3 * PI / 2, 3)
            
            if level[i][j] == 8:
                # Vẽ góc trên phải
                pygame.draw.arc(screen, COLOR,
                    [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 
                    3 * PI / 2, 2 * PI, 3)
            
            if level[i][j] == 9:
                # Vẽ cổng ghost
                pygame.draw.line(screen, 'white', 
                    (j * num2, i * num1 + (0.5 * num1)),
                    (j * num2 + num2, i * num1 + (0.5 * num1)), 3)