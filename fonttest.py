import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False

font = pygame.font.Font("resources/oldschool_pc_font_pack_v2.2_linux/ttf - Px (pixel outline)/Px437_IBM_CGA.ttf", 28)
image = pygame.image.load("resources/bild_jstrebel.png")

text = font.render("Hello, World", True, (0, 128, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((0, 0, 0))
    screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
    screen.blit(image,(60, 60))

    pygame.display.flip()
    clock.tick(60)
