# crappy code to delete welcome message:
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "anything really lol"



# import the pygame module 
import pygame 


# Variable to keep our game loop running 
running = True
screen = None
background_colour = (159, 189, 237)

def init():
    global screen

# Define the background colour 
# using RGB color coding. 
     
  
# Define the dimensions of 
# screen object(width,height) 
    screen = pygame.display.set_mode((300, 300)) 
  
# Set the caption of the screen 
    pygame.display.set_caption('eScapeSquare') 
  

    mainloop()

def draw():
    # Fill the background colour to the screen 
    screen.fill(background_colour) 
  
# Update the display using flip 
    pygame.display.flip() 

def mainloop():
    global running
    running = True
    # game loop 
    while running: 
        draw() 
# for loop through the event queue   
        for event in pygame.event.get(): 
      
            # Check for QUIT event       
            if event.type == pygame.QUIT: 
                running = False

            if event.type == pygame.KEYDOWN:
                keydown_event(event)

def keydown_event(event):
    global running
    if event.key == pygame.K_ESCAPE:
        running = False

init()
