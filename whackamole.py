import pygame

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            draw_grid(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

#Draw 20x16 grid with 32x32 blocks
def draw_grid(screen):
    block = 32
    for x in range(0, 20, block):
        for y in range(0, 16, block):
            rect = pygame.Rect(x, y, block, block)
            pygame.draw.rect(screen, "light green", rect, 1)


if __name__ == "__main__":
    main()
