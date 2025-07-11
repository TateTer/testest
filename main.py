import pygame
import random

print("")

cool = 1
#integer is an integer
name: int = 4
#float is like a double
archer: float = 2.0
#string is anything
tate: str = "aersghj jmgvm 3497845##@%^#^*)"
#boolean is true/false
hello: bool = True
square = pygame.Rect(0, 0, 30, 40)

WIDTH = 600
HEIGHT = 900

surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()

def apple():
    global cool
    print(tate)
    if(cool == 1):
        print("cool is 1")
        cool -= 3
    else:
        print("cool is not 1")
        cool += 1

def main():
    run = True
    apple()
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    width, height = 10, 11
                    circle = pygame.Rect(random.randint(0, WIDTH - width), random.randint(0, HEIGHT - height), width, height)
                    pygame.draw.rect(surface, random_color_rgb(), circle)
                    pygame.display.update()

def random_color_rgb():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


main()