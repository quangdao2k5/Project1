def get_targets(player_x, player_y, blink_x, blink_y, ink_x, ink_y, 
                pink_x, pink_y, clyd_x, clyd_y, powerup, 
                blinky_dead, inky_dead, pinky_dead, clyde_dead, eaten_ghost,
                player_direction):
    
    # Vị trí chạy trốn khi powerup
    if player_x < 450:
        runaway_x = 900
    else:
        runaway_x = 0
    if player_y < 450:
        runaway_y = 900
    else:
        runaway_y = 0
    
    return_target = (380, 400)  # Vị trí spawn ghost
    
    if powerup:
        
        # BLINKY - chạy về góc xa nhất
        if not blinky_dead and not eaten_ghost[0]:
            blink_target = (runaway_x, runaway_y)
        elif not blinky_dead and eaten_ghost[0]:
            if 340 < blink_x < 560 and 340 < blink_y < 500:
                blink_target = (400, 100)
            else:
                blink_target = (player_x, player_y)
        else:
            blink_target = return_target
        
        # INKY - chạy theo hàng ngang
        if not inky_dead and not eaten_ghost[1]:
            ink_target = (runaway_x, player_y)
        elif not inky_dead and eaten_ghost[1]:
            if 340 < ink_x < 560 and 340 < ink_y < 500:
                ink_target = (400, 100)
            else:
                ink_target = (player_x, player_y)
        else:
            ink_target = return_target
        
        # PINKY - chạy theo hàng dọc
        if not pinky_dead and not eaten_ghost[2]:
            pink_target = (player_x, runaway_y)
        elif not pinky_dead and eaten_ghost[2]:
            if 340 < pink_x < 560 and 340 < pink_y < 500:
                pink_target = (400, 100)
            else:
                pink_target = (player_x, player_y)
        else:
            pink_target = return_target
        
        # CLYDE - đi về giữa
        if not clyde_dead and not eaten_ghost[3]:
            clyd_target = (450, 450)
        elif not clyde_dead and eaten_ghost[3]:
            if 340 < clyd_x < 560 and 340 < clyd_y < 500:
                clyd_target = (400, 100)
            else:
                clyd_target = (player_x, player_y)
        else:
            clyd_target = return_target
            
    else:
        
        if not blinky_dead:
            if 340 < blink_x < 560 and 340 < blink_y < 500:
                blink_target = (400, 100)  # Ra khỏi box
            else:
                blink_target = (player_x, player_y)  # Đuổi thẳng
        else:
            blink_target = return_target
        
        if not pinky_dead:
            if 340 < pink_x < 560 and 340 < pink_y < 500:
                pink_target = (400, 100)  # Ra khỏi box
            else:
                # Dự đoán vị trí player sau 4 ô
                ahead_distance = 120
                if player_direction == 0:  # RIGHT
                    pink_target = (player_x + ahead_distance, player_y)
                elif player_direction == 1:  # LEFT
                    pink_target = (player_x - ahead_distance, player_y)
                elif player_direction == 2:  # UP
                    pink_target = (player_x, player_y - ahead_distance)
                elif player_direction == 3:  # DOWN
                    pink_target = (player_x, player_y + ahead_distance)
                else:
                    pink_target = (player_x, player_y)
                
                # Giới hạn trong bản đồ
                pink_target = (max(50, min(850, pink_target[0])), 
                              max(50, min(900, pink_target[1])))
        else:
            pink_target = return_target
        
        if not inky_dead:
            if 340 < ink_x < 560 and 340 < ink_y < 500:
                ink_target = (400, 100)  # Ra khỏi box
            else:
                # Tính vector từ Blinky đến điểm trước player 2 ô
                ahead_distance = 60
                if player_direction == 0:  # RIGHT
                    ref_point = (player_x + ahead_distance, player_y)
                elif player_direction == 1:  # LEFT
                    ref_point = (player_x - ahead_distance, player_y)
                elif player_direction == 2:  # UP
                    ref_point = (player_x, player_y - ahead_distance)
                elif player_direction == 3:  # DOWN
                    ref_point = (player_x, player_y + ahead_distance)
                else:
                    ref_point = (player_x, player_y)
                
                # Vector từ Blinky đến ref_point, nhân đôi
                vector_x = ref_point[0] - blink_x
                vector_y = ref_point[1] - blink_y
                
                ink_target = (blink_x + vector_x * 2, blink_y + vector_y * 2)
                
                # Giới hạn trong bản đồ
                ink_target = (max(50, min(850, ink_target[0])), 
                             max(50, min(900, ink_target[1])))
        else:
            ink_target = return_target

        if not clyde_dead:
            if 340 < clyd_x < 560 and 340 < clyd_y < 500:
                clyd_target = (400, 100)  # Ra khỏi box
            else:
                # Tính khoảng cách đến player
                distance_to_player = ((clyd_x - player_x)**2 + (clyd_y - player_y)**2)**0.5
                
                if distance_to_player > 240:  # Xa (> 8 ô)
                    clyd_target = (player_x, player_y)  # Đuổi theo
                else:  # Gần
                    clyd_target = (50, 900)  # Chạy về góc dưới trái
        else:
            clyd_target = return_target
    
    return [blink_target, ink_target, pink_target, clyd_target]
