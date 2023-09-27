import pygame
from math import ceil

pygame.init

WHITE = (233,237,204)
GREEN = (110,141,77)

sizeOfSquare = 120

ScreenSize = (sizeOfSquare*8,sizeOfSquare*8)


screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption("Chess")

class Peice:
    def __init__(self,peice = None,color = None):
        self.peice = peice[0].upper()
        self.color = color[0].lower()
        if peice and color:
            self.image = pygame.image.load(f"images/{peice}{color}.png")
        #self.image = pygame.image.load("images/Chess_blt45.png")
        self.image = pygame.transform.scale(self.image, (sizeOfSquare*0.7,sizeOfSquare*0.7))
        #pygame.image.save(self.image,"1.png")

class Square:

    def __init__(self,x,y,peice):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x*sizeOfSquare,y*sizeOfSquare,sizeOfSquare,sizeOfSquare)
        #self.rect.center = (x*sizeOfSquare,y*sizeOfSquare)
        self.color = GREEN if (x+y)%2 else WHITE
        self.peice = peice



    def draw(self):
        
        pygame.draw.rect(screen,self.color,self.rect)
        r = pygame.Rect(1,1,10,10)
        r.center = self.rect.center
        pygame.draw.rect(screen,(225,0,0),r)
        peice_rect = self.peice.image.get_rect(center = self.rect.center)
        screen.blit(self.peice.image,peice_rect)
       #pygame.draw.rect(screen,(0,255,0),peice_rect)


# create board
board=[]
for i in range(8):
    row=[]
    for j in range(8):
        row.append(Square(i,j,Peice("P","w")))
    board.append(row)

def DrawBoard():
    for row in board:
        for square in row:
            square.draw()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run = False
            

    DrawBoard()
    #screen.fill(GREEN)


    pygame.display.flip()


pygame.quit()
