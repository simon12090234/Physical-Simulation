import pygame
import pymunk
import pymunk.pygame_util
import math
import time

ESCALA = 0.75


#-------------------------------------------------------------------------------------------
def obj_estatico(space, x, y, ancho, alto, inclinacion):
    cuerpo = pymunk.Body(body_type=pymunk.Body.STATIC)
    cuerpo.position = (x * ESCALA, y * ESCALA)
    cuerpo.angle = math.radians(inclinacion)

    ancho_e = ancho * ESCALA
    alto_e = alto * ESCALA
    vertices = [(-ancho_e/2, -alto_e/2),
                (-ancho_e/2, alto_e/2),
                (ancho_e/2, alto_e/2),
                (ancho_e/2, -alto_e/2)]

    forma = pymunk.Poly(cuerpo, vertices)
    forma.friction = 0.5
    forma.elasticity = 0.0
    forma.color = (0, 0, 255, 255)
    forma.collision_type = 2
    space.add(cuerpo, forma)
    return cuerpo, forma

    
#------------------------------------------------------------------------------
def carro(space, x, y, radio=50, masa=24 ):
    radio_escalado = radio * ESCALA
    momento = pymunk.moment_for_circle(masa, 0, radio_escalado)
    cuerpo = pymunk.Body(masa, momento)
    cuerpo.position = (x * ESCALA, y * ESCALA)
    forma = pymunk.Circle(cuerpo, radio_escalado)
    forma.elasticity = 5.0
    forma.friction = 0.01
    forma.color = (85, 85, 85, 255)
    forma.collision_type = 1
    forma.collison_ocurred = False
    cuerpo.angular_damping = 0.4
    space.add(cuerpo, forma)
    return cuerpo, forma
#-------------------------------------------------------------------------------
def crear_bola_dinamica(space, x, y, radio=20, masa=5):
    radio_escalado = radio * ESCALA
    momento = pymunk.moment_for_circle(masa, 0, radio_escalado)
    cuerpo = pymunk.Body(masa, momento)
    cuerpo.position = (x * ESCALA, y * ESCALA)
    forma = pymunk.Circle(cuerpo, radio_escalado)
    forma.elasticity = 0.3
    forma.friction = 0.2
    forma.color = (128, 191, 255, 255)
    cuerpo.angular_damping = 0.4
    space.add(cuerpo, forma)
    return cuerpo, forma
#--------------------------------------------------------------------------------
def superficie_carro(space, x, y, ancho, alto, angulo_grados):
    cuerpo = pymunk.Body(body_type=pymunk.Body.STATIC)
    cuerpo.position = (x * ESCALA, y * ESCALA)
    cuerpo.angle = math.radians(angulo_grados)
    ancho_e = ancho * ESCALA
    alto_e = alto * ESCALA
    vertices = [(-ancho_e/2, -alto_e/2),
                (-ancho_e/2, alto_e/2),
                (ancho_e/2, alto_e/2),
                (ancho_e/2, -alto_e/2)]

    forma = pymunk.Poly(cuerpo, vertices)
    forma.friction = 0.01
    forma.elasticity =0.000000001
    forma.color = (0, 0, 255, 255)
    space.add(cuerpo, forma)
    return cuerpo, forma

#-------------------------------------------------------------------------------
def crear_rectangulo_estatico(space, x, y, ancho, alto, angulo_grados, color):
    cuerpo = pymunk.Body(body_type=pymunk.Body.STATIC)
    cuerpo.position = (x * ESCALA, y * ESCALA)
    cuerpo.angle = math.radians(angulo_grados)
    ancho_e = ancho * ESCALA
    alto_e = alto * ESCALA
    vertices = [(-ancho_e/2, -alto_e/2),
                (-ancho_e/2, alto_e/2),
                (ancho_e/2, alto_e/2),
                (ancho_e/2, -alto_e/2)]

    forma = pymunk.Poly(cuerpo, vertices)
    forma.friction = 0.5
    forma.color = color
    space.add(cuerpo, forma)
    return cuerpo, forma
#--------------------------------------------------------------------------------


# Inicializar pygame    
pygame.init()
width, height = 900, 790
screen = pygame.display.set_mode((width, height))
#---------------------------------------------------------
fondo = pygame.image.load("imagenes/gris.jpg").convert()
fondo = pygame.transform.scale(fondo, (width, height))
#---------------------------------------------------------
globo = pygame.image.load("imagenes/globo.png").convert_alpha()
imagen_escalada = pygame.transform.scale(globo, (190, 190))
globo_coordenadas = (500, 420)
#---------------------------------------------------------
globo_explotado = pygame.image.load("imagenes/globoexplotado.png").convert_alpha()
globo_escalado = pygame.transform.scale(globo_explotado, (250, 250))
explotado_coordenadas = (500, 420)
#---------------------------------------------------------
imagen_carro = pygame.image.load("imagenes/carro.png").convert_alpha()
radio_carro = 50 * ESCALA
imagen_carro = pygame.transform.scale(imagen_carro, (int(radio_carro*2), int(radio_carro*2)))
#----------------------------------------------------------
pygame.display.set_caption("Ingenieria del caos: Cuando la cauda encuentra su efecto")
clock = pygame.time.Clock()

# Crear espacio de física
space = pymunk.Space()
space.gravity = (0, 980)

# Dibujador de pymunk en pygame
draw_options = pymunk.pygame_util.DrawOptions(screen)

#---------------------------------------------------------------------------------------------------------------
# Tramo N°1
crear_rectangulo_estatico(space, x=640, y=100, ancho=350, alto=70, angulo_grados=-25.0, color=(255, 130, 0, 255))  
crear_rectangulo_estatico(space, x=380, y=190, ancho=300, alto=70, angulo_grados=-10.0, color=(255, 130, 0, 255))
#----------------------------------------------------------------------------------------------------------------

# Tramo N°2
crear_rectangulo_estatico(space, x=140, y=350, ancho=260, alto=70, angulo_grados=10.0, color=(255, 130, 0, 255))
crear_rectangulo_estatico(space, x=345, y=430, ancho=250, alto=70, angulo_grados=10.0, color=(255, 130, 0, 255))
crear_rectangulo_estatico(space, x=455, y=400, ancho=50, alto=40, angulo_grados=11.0, color=(0, 0, 0, 255))
#----------------------------------------------------------------------------------------------------------------

# Tramo N°3
crear_rectangulo_estatico(space, x=670, y=530, ancho=250, alto=70, angulo_grados=-12.0, color=(255, 130, 0, 255))
crear_rectangulo_estatico(space, x=475, y=610, ancho=250, alto=70, angulo_grados=-12.0, color=(255, 130, 0, 255))
crear_rectangulo_estatico(space, x=365, y=580, ancho=50, alto=40, angulo_grados=-11.0, color=(0, 0, 0, 255))
#----------------------------------------------------------------------------------------------------------------

#Tramo N°4
crear_rectangulo_estatico(space, x=210, y=770, ancho=250, alto=70, angulo_grados=42.0, color=(255, 0, 0, 255))
#----------------------------------------------------------------------------------------------------------------

#Tramo N°5
superficie_carro(space, x=570, y=812, ancho=500, alto=40, angulo_grados=0.01)
#---------------------------------------------------------------------------------------------------------------


# Bolas
crear_bola_dinamica(space, x=710, y=1 )
crear_bola_dinamica(space, x=700, y=1 )
crear_bola_dinamica(space, x=720, y=1 )
crear_bola_dinamica(space, x=760, y=1 )
crear_bola_dinamica(space, x=690, y=1 )

crear_bola_dinamica(space, x=360, y=225 )#fija_primertramo
crear_bola_dinamica(space, x=380, y=230 )#fija_primertramo
crear_bola_dinamica(space, x=400, y=570)#fija_segundotramo
crear_bola_dinamica(space, x=420, y=570)#fija_segundotramo

cuerpo_carro, forma_carro = carro(space, x=325, y=745)
#----------------------------------------------------------------------------------------------------------------

# Bordes
crear_rectangulo_estatico(space, x=20, y=260, ancho=20, alto=90, angulo_grados=4.0, color=(167, 107, 33, 0.8))
obj_estatico(space, x=800, y=800, ancho=40, alto = 60, inclinacion = 0.0  )
#----------------------------------------------------------------------------------------------------------------


globo_visible = True  # Para controlar si se dibuja el globo o no

def al_colisionar_carro_y_obj_estatico(arbiter, space, data):
    global globo_visible
    globo_visible = False
    return True  # continuar con la simulación normal

# Crear manejador de colisiones entre carro (1) y objeto estático (2)
handler = space.add_collision_handler(1, 2)
handler.begin = al_colisionar_carro_y_obj_estatico


# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(fondo, (0, 0))
    space.debug_draw(draw_options)
    if globo_visible is False:
        screen.blit(globo_escalado, explotado_coordenadas)
        running = False
    else:
        screen.blit(imagen_escalada, globo_coordenadas)
    # Dibujar la imagen del carro sobre su cuerpo
    x, y = cuerpo_carro.position
    rect = imagen_carro.get_rect(center=(int(x), int(y)))
    screen.blit(imagen_carro, rect)
    space.step(1/60.0)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
