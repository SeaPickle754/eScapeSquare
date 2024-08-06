# crappy code to delete welcome message:
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "anything really lol"


# import the pygame module 
import pygame 
import player


class Game:
    # Variable to keep our game loop running 
    

    def __init__(self):
        self.running = True
        self.screen = None
        # random blue color i found
        self.background_colour = (159, 189, 237)
        # Define the dimensions of 
        # screen object(width,height) 
        self.screen = pygame.display.set_mode((600, 600)) 
        self.player = player.Player()
        # Set the caption of the screen 
        pygame.display.set_caption('eScapeSquare')
        # hide the mouse
        pygame.mouse.set_visible(False)
        self.mainloop()

    def draw(self):
        # Fill the background colour to the screen 
        self.screen.fill(self.background_colour) 
        self.player.draw(self.screen)
        # Update the display using flip 
        pygame.display.flip() 

    def mainloop(self):
        # game loop 
        while self.running: 
            self.draw()   
            self.do_events()
    def do_events(self):
        for event in pygame.event.get(): 
            # Check for QUIT event       
            if event.type == pygame.QUIT: 
                self.running = False
            if event.type == pygame.MOUSEMOTION:
                self.player.move(pygame.mouse.get_pos()[0], \
                            pygame.mouse.get_pos()[1])
            if event.type == pygame.KEYDOWN:
                self.keydown_event(event)
        
    def keydown_event(self, event):
        if event.key == pygame.K_ESCAPE:
            self.running = False


game = Game()
