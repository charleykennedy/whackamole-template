import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole = (0, 0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN: #moves mole to random square when clicked
                    clicked_x, clicked_y = event.pos
                    if clicked_x // 32 == mole[0] and clicked_y // 32 == mole[1]:
                        mole = (random.randrange(0, 20), random.randrange(0, 16))
                        print(mole)

            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft= (mole[0] * 32, mole[1] * 32)))
            pygame.display.flip()
            clock.tick(60)


    finally:
        pygame.quit()

#Draw 20x16 grid with 32x32 blocks
def draw_grid(screen):
    block = 32
    for x in range(0, 641, block):
        for y in range(0, 513, block):
            pygame.draw.line(screen, "black", (x,y), (x, block))
            pygame.draw.line(screen, "black", (x,y), (block, y))

if __name__ == "__main__":
    main()
