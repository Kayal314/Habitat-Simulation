import pygame

pygame.init()

screen = pygame.display.set_mode((1800, 1012))
pygame.display.set_caption('Habitat Simulation')
pygame.display.set_icon(pygame.image.load('Sprites/icon.png'))
background = pygame.image.load('map.png')
rabbit = pygame.image.load('Sprites/rabbit.png')
fox = pygame.image.load('Sprites/fox.png')
if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))
        #TODO: screen.blit(rabbit,(different x,y)) and calculate the positions of centres of landforms
        pygame.display.update()
