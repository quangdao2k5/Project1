import pygame

def load_assets():
    """Tải tất cả hình ảnh của game"""
    # Hình ảnh player
    player_images = []
    for i in range(1, 5):
        img = pygame.image.load(f'images/player_images/{i}.png')
        player_images.append(pygame.transform.scale(img, (45, 45)))
    
    # Hình ảnh ghost
    blinky_img = pygame.transform.scale(
        pygame.image.load('images/ghost_images/red.png'), (45, 45))
    pinky_img = pygame.transform.scale(
        pygame.image.load('images/ghost_images/pink.png'), (45, 45))
    inky_img = pygame.transform.scale(
        pygame.image.load('images/ghost_images/blue.png'), (45, 45))
    clyde_img = pygame.transform.scale(
        pygame.image.load('images/ghost_images/orange.png'), (45, 45))
    spooked_img = pygame.transform.scale(
        pygame.image.load('images/ghost_images/powerup.png'), (45, 45))
    dead_img = pygame.transform.scale(
        pygame.image.load('images/ghost_images/dead.png'), (45, 45))
    
    return {
        'player': player_images,
        'blinky': blinky_img,
        'pinky': pinky_img,
        'inky': inky_img,
        'clyde': clyde_img,
        'spooked': spooked_img,
        'dead': dead_img
    }