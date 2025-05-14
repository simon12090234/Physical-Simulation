import pymunk
import pymunk.pygame_util
import pygame

# Inicializar Pygame y la ventana
pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Movimiento tipo juego")
clock = pygame.time.Clock()

# Crear espacio
space = pymunk.Space()
space.gravity = (0, 981)

# Crear plataforma
def add_ramp(space, start_pos, end_pos):
    static_body = space.static_body
    ramp = pymunk.Segment(static_body, start_pos, end_pos, 5)
    ramp.elasticity = 0.5
    ramp.friction = 0.7
    ramp.color = (150, 100, 200, 100)
    space.add(ramp)

def add_boloncho(space, position, radius=30):
    mass = 8
    inertia = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, inertia)  # cuerpo dinámico
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.friction = 1.0
    shape.color = (100, 150, 50, 255)
    space.add(body, shape)
    return body, shape

def add_elastic_ball(space, position, radius=20):
    mass = 1
    inertia = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, inertia)
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.friction = 0.0               # Sin fricción
    shape.elasticity = 0.95
    shape.color = (128, 191, 255, 255)          # Alta elasticidad
    space.add(body, shape)
    return body

# Crear bola
def add_ball(space, position, radius=20):
    mass = 1
    inertia = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, inertia)
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.friction = 1.0
    shape.elasticity = 0.6
    space.add(body, shape)
    return body

# Agregar objetos
add_ramp(space, (450, 300), (600, 300))
add_ramp(space, (450, 300), (200, 190))
add_ramp(space, (200, 190), (100, 190))
add_ramp(space, (10, 190), (10, 400))  # Pared izquierda
add_ramp(space, (100, 190), (100, 400))  # Pared derecha

# Rampa inferior inclinada donde cae el boloncho
add_ramp(space, (10, 450), (160, 530))  # Piso inclinado hacia la derecha
add_ramp(space, (160,530), (450,530)) # Piso donde cae el boloncho luego de la rampa
add_ramp(space, (310, 470), (390, 470)) 

add_ramp(space, (660, 40), (660, 400))  # Pared izquierda del recipiente
add_ramp(space, (780, 40), (780, 400))  # Pared derecha del recipiente
add_ramp(space, (660, 400), (780, 400))  # Fondo del recipiente

boloncho_body, boloncho_shape = add_boloncho(space, (150, 180))
ball_body = add_ball(space, (500, 260))

# Agregar 5 bolas elásticas en el suelo luego de la rampa
start_x = 200
y_pos = 510  # ligeramente por encima del suelo
for i in range(5):
    add_elastic_ball(space, (start_x + i * 50, y_pos))


for i in range(3):  # 3 filas
    for j in range(3):  # 3 columnas
        x = 720 + j * 25  # Separación horizontal
        y = 60 - i * 25  # Separación vertical
        add_ball(space, (x, y), radius=15)


# Opciones de dibujo
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Velocidad de movimiento
HORIZONTAL_SPEED = 100

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Detectar teclas
    keys = pygame.key.get_pressed()
    velocity = ball_body.velocity

    if keys[pygame.K_LEFT]:
        ball_body.velocity = (-HORIZONTAL_SPEED, velocity.y)
    elif keys[pygame.K_RIGHT]:
        ball_body.velocity = (HORIZONTAL_SPEED, velocity.y)
    else:
        ball_body.velocity = (0, velocity.y)  # Detener en X si no se pulsa nada

    # Dibujar
    screen.fill((40, 40, 40))
    space.debug_draw(draw_options)

    space.step(1 / 60.0)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
