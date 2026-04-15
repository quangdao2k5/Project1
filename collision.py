def handle_ghost_collision(game_state, ghost_name):
    """Xử lý va chạm với ghost (mất mạng)"""
    if game_state.lives > 0:
        game_state.lives -= 1
        game_state.reset_positions()
    else:
        game_state.game_over = True
        game_state.moving = False
        game_state.startup_counter = 0

def handle_ghost_eaten(game_state, ghost_id):
    """Xử lý khi ăn được ghost"""
    # Đánh dấu ghost đã bị ăn
    if ghost_id == 0:
        game_state.blinky_dead = True
        game_state.eaten_ghost[0] = True
    elif ghost_id == 1:
        game_state.inky_dead = True
        game_state.eaten_ghost[1] = True
    elif ghost_id == 2:
        game_state.pinky_dead = True
        game_state.eaten_ghost[2] = True
    elif ghost_id == 3:
        game_state.clyde_dead = True
        game_state.eaten_ghost[3] = True
    
    # Tính điểm (nhân đôi cho mỗi ghost)
    game_state.score += (2 ** game_state.eaten_ghost.count(True)) * 100

def check_ghost_collisions(game_state, player_circle, blinky, inky, pinky, clyde):
    """Kiểm tra va chạm giữa player và các ghost"""
    # Không powerup - va chạm = mất mạng
    if not game_state.powerup:
        if (player_circle.colliderect(blinky.rect) and not blinky.dead) or \
           (player_circle.colliderect(inky.rect) and not inky.dead) or \
           (player_circle.colliderect(pinky.rect) and not pinky.dead) or \
           (player_circle.colliderect(clyde.rect) and not clyde.dead):
            handle_ghost_collision(game_state, 'any')
    
    # Có powerup
    if game_state.powerup:
        # Va chạm với ghost đã bị ăn = mất mạng
        if player_circle.colliderect(blinky.rect) and game_state.eaten_ghost[0] and not blinky.dead:
            handle_ghost_collision(game_state, 'blinky')
        elif player_circle.colliderect(inky.rect) and game_state.eaten_ghost[1] and not inky.dead:
            handle_ghost_collision(game_state, 'inky')
        elif player_circle.colliderect(pinky.rect) and game_state.eaten_ghost[2] and not pinky.dead:
            handle_ghost_collision(game_state, 'pinky')
        elif player_circle.colliderect(clyde.rect) and game_state.eaten_ghost[3] and not clyde.dead:
            handle_ghost_collision(game_state, 'clyde')
        
        # Ăn ghost chưa bị ăn
        if player_circle.colliderect(blinky.rect) and not blinky.dead and not game_state.eaten_ghost[0]:
            handle_ghost_eaten(game_state, 0)
        if player_circle.colliderect(inky.rect) and not inky.dead and not game_state.eaten_ghost[1]:
            handle_ghost_eaten(game_state, 1)
        if player_circle.colliderect(pinky.rect) and not pinky.dead and not game_state.eaten_ghost[2]:
            handle_ghost_eaten(game_state, 2)
        if player_circle.colliderect(clyde.rect) and not clyde.dead and not game_state.eaten_ghost[3]:
            handle_ghost_eaten(game_state, 3)

def revive_ghosts(game_state, blinky, inky, pinky, clyde):
    """Hồi sinh ghost khi về box"""
    if blinky.in_box and game_state.blinky_dead:
        game_state.blinky_dead = False
    if inky.in_box and game_state.inky_dead:
        game_state.inky_dead = False
    if pinky.in_box and game_state.pinky_dead:
        game_state.pinky_dead = False
    if clyde.in_box and game_state.clyde_dead:
        game_state.clyde_dead = False