import pygame
import random

#initialize pygame
pygame.init()

#gets the user's display information
displayInfo = pygame.display.Info()

#setting window size to be user's display resolution
window = pygame.display.set_mode([displayInfo.current_w, displayInfo.current_h])

#setting score variable
score = 0

#target recentering
back_to_center = True

#function to render the score of our user at top of window
font_name = pygame.font.match_font('arial')
def draw_score(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)

#runs till exited
running = True
while running:

    #if user clicks window close or presses the escape key, exits program
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if target.collidepoint(x, y):
                score += 1

    #sets background color to be white
    window.fill((200,200,200))

    #draws/renders the user's current score
    draw_score(window, str(score), 40, displayInfo.current_w/2, 10)

    #sets random radius
    randR = random.randint(25, 75)

    if back_to_center:
        x_coord = displayInfo.current_w / 2
        y_coord = displayInfo.current_h / 2
        back_to_center = False
    else:
        #sets random x (within 720 pixels) coordinate for circle location
        x_coord = random.randint(280, displayInfo.current_w- 280)
        #sets random y (within 480 pixels) coordinate for circle location
        y_coord = random.randint(120, displayInfo.current_h - 120)
        back_to_center = True


    #draws our target on window
    target = pygame.draw.circle(window, (0, 168, 0), (displayInfo.current_w - x_coord, displayInfo.current_h - y_coord), randR)

    #updates display on window
    pygame.display.flip()

    pygame.time.wait(750)

pygame.quit()


