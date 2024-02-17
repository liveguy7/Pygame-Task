import pygame
import sys
import time

pygame.init()

icon = pygame.image.load('pizza.jpg')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Jello')
clock = pygame.time.Clock()
running = True
dt = 0

pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
  
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill("blue")
  pygame.draw.circle(screen, "cyan", pos, 20)

  keys = pygame.key.get_pressed()

  if(keys[pygame.K_w]):
    pos.y -= 300 * dt
  if(keys[pygame.K_s]):
    pos.y += 300 * dt
  if(keys[pygame.K_a]):
    pos.x -= 300 * dt
  if(keys[pygame.K_d]):
    pos.x += 300 * dt

  pygame.display.flip()    

  dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()











