import pygame
from config import FONT

def draw_ui(screen, score, lives, powerup, game_over, game_won, player_images):
    """Vẽ giao diện người dùng (điểm, mạng, thông báo)"""
    # Hiển thị điểm
    score_text = FONT.render(f'Score: {score}', True, 'white')
    screen.blit(score_text, (10, 920))
    
    # Hiển thị powerup
    if powerup:
        pygame.draw.circle(screen, 'blue', (140, 930), 15)
    
    # Hiển thị số mạng
    for i in range(lives):
        screen.blit(pygame.transform.scale(player_images[0], (30, 30)), 
                   (650 + i * 40, 915))
    
    # Hiển thị game over
    if game_over:
        pygame.draw.rect(screen, 'white', [50, 200, 800, 300], 0, 10)
        pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        
        # Font lớn cho game over
        big_font = pygame.font.Font('freesansbold.ttf', 60)
        small_font = pygame.font.Font('freesansbold.ttf', 30)
        
        # Dòng 1: GAME OVER
        gameover_text = big_font.render('GAME OVER', True, 'red')
        text_rect = gameover_text.get_rect(center=(450, 280))
        screen.blit(gameover_text, text_rect)
        
        # Dòng 2: Score
        score_display = small_font.render(f'Final Score: {score}', True, 'white')
        score_rect = score_display.get_rect(center=(450, 350))
        screen.blit(score_display, score_rect)
        
        # Dòng 3: Restart
        restart_text = small_font.render('Press SPACE to restart', True, 'yellow')
        restart_rect = restart_text.get_rect(center=(450, 400))
        screen.blit(restart_text, restart_rect)
    
    # Hiển thị thắng game
    if game_won:
        pygame.draw.rect(screen, 'white', [50, 200, 800, 300], 0, 10)
        pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        
        # Font lớn cho victory
        big_font = pygame.font.Font('freesansbold.ttf', 60)
        small_font = pygame.font.Font('freesansbold.ttf', 30)
        
        # Dòng 1: VICTORY
        victory_text = big_font.render('VICTORY!', True, 'green')
        text_rect = victory_text.get_rect(center=(450, 280))
        screen.blit(victory_text, text_rect)
        
        # Dòng 2: Score
        score_display = small_font.render(f'Final Score: {score}', True, 'white')
        score_rect = score_display.get_rect(center=(450, 350))
        screen.blit(score_display, score_rect)
        
        # Dòng 3: Restart
        restart_text = small_font.render('Press SPACE to restart', True, 'yellow')
        restart_rect = restart_text.get_rect(center=(450, 400))
        screen.blit(restart_text, restart_rect)