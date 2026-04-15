import pygame
from config import WIDTH, HEIGHT, FPS, PLAYER_SPEED, POWERUP_DURATION, STARTUP_TIME
from assets import load_assets
from map import draw_board
from player import draw_player, check_position, move_player, check_collisions
from ghost import Ghost
from game_state import GameState
from ghost_ai import get_targets
from collision import check_ghost_collisions, revive_ghosts
from ui import draw_ui

def main():
    # Khởi tạo pygame
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    timer = pygame.time.Clock()
    
    # Load assets
    assets = load_assets()
    
    # Tạo game state
    game_state = GameState()
    
    # Game loop
    run = True
    while run:
        timer.tick(FPS)
        
        # Cập nhật counter và flicker
        if game_state.counter < 19:
            game_state.counter += 1
            if game_state.counter > 3:
                game_state.flicker = False
        else:
            game_state.counter = 0
            game_state.flicker = True
        
        # Cập nhật powerup
        if game_state.powerup and game_state.power_counter < POWERUP_DURATION:
            game_state.power_counter += 1
        elif game_state.powerup and game_state.power_counter >= POWERUP_DURATION:
            game_state.power_counter = 0
            game_state.powerup = False
            game_state.eaten_ghost = [False, False, False, False]
        
        # Startup counter
        if game_state.startup_counter < STARTUP_TIME and not game_state.game_over and not game_state.game_won:
            game_state.moving = False
            game_state.startup_counter += 1
        else:
            game_state.moving = True
        
        # Vẽ màn hình
        screen.fill('black')
        draw_board(screen, game_state.level, game_state.flicker)
        
        # Tính center
        center_x = game_state.player_x + 23
        center_y = game_state.player_y + 24
        
        # Cập nhật tốc độ ghost
        game_state.update_ghost_speeds()
        
        # Kiểm tra thắng
        game_state.game_won = game_state.check_win()
        
        # Vẽ player
        player_circle = pygame.draw.circle(screen, 'black', (center_x, center_y), 20, 2)
        draw_player(screen, assets['player'], game_state.player_x, 
                   game_state.player_y, game_state.direction, game_state.counter)
        
        # Tạo ghost objects
        blinky = Ghost(game_state.blinky_x, game_state.blinky_y, game_state.targets[0], 
                      game_state.ghost_speeds[0], assets['blinky'], game_state.blinky_direction, 
                      game_state.blinky_dead, game_state.blinky_box, 0, 
                      assets['spooked'], assets['dead'])
        
        inky = Ghost(game_state.inky_x, game_state.inky_y, game_state.targets[1], 
                    game_state.ghost_speeds[1], assets['inky'], game_state.inky_direction, 
                    game_state.inky_dead, game_state.inky_box, 1, 
                    assets['spooked'], assets['dead'])
        
        pinky = Ghost(game_state.pinky_x, game_state.pinky_y, game_state.targets[2], 
                     game_state.ghost_speeds[2], assets['pinky'], game_state.pinky_direction, 
                     game_state.pinky_dead, game_state.pinky_box, 2, 
                     assets['spooked'], assets['dead'])
        
        clyde = Ghost(game_state.clyde_x, game_state.clyde_y, game_state.targets[3], 
                     game_state.ghost_speeds[3], assets['clyde'], game_state.clyde_direction, 
                     game_state.clyde_dead, game_state.clyde_box, 3, 
                     assets['spooked'], assets['dead'])
        
        # Vẽ ghosts
        blinky.check_collisions(game_state.level)
        blinky.draw(screen, game_state.powerup, game_state.eaten_ghost)
        
        inky.check_collisions(game_state.level)
        inky.draw(screen, game_state.powerup, game_state.eaten_ghost)
        
        pinky.check_collisions(game_state.level)
        pinky.draw(screen, game_state.powerup, game_state.eaten_ghost)
        
        clyde.check_collisions(game_state.level)
        clyde.draw(screen, game_state.powerup, game_state.eaten_ghost)
        
        # Vẽ UI
        draw_ui(screen, game_state.score, game_state.lives, game_state.powerup, 
               game_state.game_over, game_state.game_won, assets['player'])
        
        # Cập nhật targets
        game_state.targets = get_targets(
            game_state.player_x, game_state.player_y,
            game_state.blinky_x, game_state.blinky_y,
            game_state.inky_x, game_state.inky_y,
            game_state.pinky_x, game_state.pinky_y,
            game_state.clyde_x, game_state.clyde_y,
            game_state.powerup,
            game_state.blinky_dead, game_state.inky_dead, 
            game_state.pinky_dead, game_state.clyde_dead,
            game_state.eaten_ghost,
            game_state.direction  # ← Thêm player direction
        )
        
        # Kiểm tra hướng có thể đi
        game_state.turns_allowed = check_position(center_x, center_y, 
                                                  game_state.level, game_state.direction)
        
        # Di chuyển
        if game_state.moving:
            game_state.player_x, game_state.player_y = move_player(
                game_state.player_x, game_state.player_y, 
                game_state.direction, game_state.turns_allowed, PLAYER_SPEED)
            
            # Di chuyển ghosts
            if not game_state.blinky_dead and not blinky.in_box:
                game_state.blinky_x, game_state.blinky_y, game_state.blinky_direction = blinky.move_blinky()
            else:
                game_state.blinky_x, game_state.blinky_y, game_state.blinky_direction = blinky.move_clyde()
            
            if not game_state.pinky_dead and not pinky.in_box:
                game_state.pinky_x, game_state.pinky_y, game_state.pinky_direction = pinky.move_pinky()
            else:
                game_state.pinky_x, game_state.pinky_y, game_state.pinky_direction = pinky.move_clyde()
            
            if not game_state.inky_dead and not inky.in_box:
                game_state.inky_x, game_state.inky_y, game_state.inky_direction = inky.move_inky()
            else:
                game_state.inky_x, game_state.inky_y, game_state.inky_direction = inky.move_clyde()
            
            game_state.clyde_x, game_state.clyde_y, game_state.clyde_direction = clyde.move_clyde()
        
        # Kiểm tra va chạm với chấm
        game_state.score, game_state.powerup, game_state.power_counter, game_state.eaten_ghost = \
            check_collisions(game_state.level, center_x, center_y, 
                           game_state.player_x, game_state.score, 
                           game_state.powerup, game_state.power_counter, game_state.eaten_ghost)
        
        # Kiểm tra va chạm với ghost
        check_ghost_collisions(game_state, player_circle, blinky, inky, pinky, clyde)
        
        # Hồi sinh ghost
        revive_ghosts(game_state, blinky, inky, pinky, clyde)
        
        # Xử lý events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game_state.direction_command = 0
                if event.key == pygame.K_LEFT:
                    game_state.direction_command = 1
                if event.key == pygame.K_UP:
                    game_state.direction_command = 2
                if event.key == pygame.K_DOWN:
                    game_state.direction_command = 3
                if event.key == pygame.K_SPACE and (game_state.game_over or game_state.game_won):
                    game_state.reset()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and game_state.direction_command == 0:
                    game_state.direction_command = game_state.direction
                if event.key == pygame.K_LEFT and game_state.direction_command == 1:
                    game_state.direction_command = game_state.direction
                if event.key == pygame.K_UP and game_state.direction_command == 2:
                    game_state.direction_command = game_state.direction
                if event.key == pygame.K_DOWN and game_state.direction_command == 3:
                    game_state.direction_command = game_state.direction
        
        # Cập nhật direction
        if game_state.direction_command == 0 and game_state.turns_allowed[0]:
            game_state.direction = 0
        if game_state.direction_command == 1 and game_state.turns_allowed[1]:
            game_state.direction = 1
        if game_state.direction_command == 2 and game_state.turns_allowed[2]:
            game_state.direction = 2
        if game_state.direction_command == 3 and game_state.turns_allowed[3]:
            game_state.direction = 3
        
        # Xử lý teleport
        if game_state.player_x > 900:
            game_state.player_x = -47
        elif game_state.player_x < -50:
            game_state.player_x = 897
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':
    main()