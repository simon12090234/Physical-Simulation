import pygame, pymunk, sys
import random

def crear_obj_dinamico(space, pos):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    shape.collision_type = 1
    space.add(body, shape)
    body.color = (0,0,0)
    shape.collision_ocurred = False
    return shape

def crear_obj_statico(space, posicion):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = posicion
    shape = pymunk.Circle(body, 50)
    shape.collision_type = 2
    space.add(body, shape)
    return shape
def agregar_obj_dinamico(objs_dinamicos):
    for obj_dinamico in objs_dinamicos:
        pygame.draw.circle(screen, obj_dinamico.body.color, obj_dinamico.body.position, 50)

def agregar_objs_estaticos(objs_estaticos):
    for obj_estatico in objs_estaticos:
        pygame.draw.circle(screen, (0,0,0), obj_estatico.body.position, 50)

def ocurrio_colision(arbiter, space, data):
    obj_dinamico_shape, obj_estatico_shape = arbiter.shapes
    if obj_dinamico_shape.collision_ocurred is False:
        obj_dinamico_shape.body.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #cambio de color
        obj_dinamico_shape.collision_ocurred = True
    return True

pygame.init()
screen = pygame.display.set_mode((800, 800)) #crear el display
clock = pygame.time.Clock() #Para controlar el fps
space = pymunk.Space()
space.gravity = (0, 200) #gravedad que se mide en pixeles.

objs_dinamicos = []

objs_estaticos = []
objs_estaticos.append(crear_obj_statico(space, posicion = (270, 450)))
objs_estaticos.append(crear_obj_statico(space, posicion = (500, 250)))
objs_estaticos.append(crear_obj_statico(space, posicion = (400, 350)))


handler = space.add_collision_handler(1, 2)
handler.begin = ocurrio_colision

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            objs_dinamicos.append(crear_obj_dinamico(space, event.pos))


    screen.fill((200, 200, 200))# Color de la pantalla
    agregar_obj_dinamico(objs_dinamicos)
    agregar_objs_estaticos(objs_estaticos)
    space.step(1/50)
    pygame.display.update()
    clock.tick(150)
