import pymunk
import pymunk.pygame_util
import pygame


# Configurar la ventana
pygame.init()
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Maquina De Goldberg")
clock = pygame.time.Clock()

# Crear espacio
space = pymunk.Space()
space.gravity = (0, 981)

# Función para agregar una rampa inclinada
def add_ramp(space, start_pos, end_pos):
    static_body = space.static_body
    ramp = pymunk.Segment(static_body, start_pos, end_pos, 5)
    ramp.elasticity = 0.5
    ramp.friction = 0.7
    ramp.color = (0, 200, 0, 255)
    space.add(ramp)

def add_ball(space, position, radius=15):
    mass = 5
    inertia = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, inertia)
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.7  # Rebota más
    shape.friction = 0.2     # Algo más de fricción
    shape.density = 8.83572934      # Añadimos densidad
    body.angular_damping = 0.3  # Amortigua rotación
    shape.collision_type = 1
    space.add(body, shape)
    return body, shape


# Crear varias rampas (puedes ajustar las posiciones según necesites)
add_ramp(space, (600, 10), (200, 80)) # Rampa 1
add_ramp(space, (400, 200), (10, 150))  # Rampa 2
add_ramp(space, (300, 320), (590, 250))  # Rampa 3
add_ramp(space, (10, 350), (300, 400))  # Rampa 4
add_ramp(space, (300, 500), (590, 470))  # Rampa 5
add_ramp(space, (10, 500), (400, 580))
# add_ramp(space, ()) #Rampa 6


# Crear paredes laterales para cada rampa
add_ramp(space, (10, 350), (10, 300))
add_ramp(space, (590, 470), (590, 420))
add_ramp(space, (590, 250), (590, 200))
add_ramp(space, (10, 150), (10, 100 ))
add_ramp(space, (420, 590),(420, 700))
add_ramp(space, (500,550 ),(500,700) )



# Crear varias canicas arriba del todo
add_ball(space, (570, 10))
add_ball(space, (550, 10))
add_ball(space, (520, 10))
add_ball(space, (500, 10))
add_ball(space, (480, 10))
add_ball(space, (460, 10))
add_ball(space, (440, 10))
add_ball(space, (420, 10))
add_ball(space, (400, 10))




# Opciones de dibujo
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((85, 85, 85))  # Fondo blanco

    # Dibujar rampas en verde (opcional para mejor visual)
    for shape in space.shapes:
        if isinstance(shape, pymunk.Segment):
            pygame.draw.line(
                screen,
                (0, 0, 255, 255),  # Verde
                shape.a,
                shape.b,
                5
            )

    # Dibujar y avanzar la simulación
    space.debug_draw(draw_options)
    space.step(1 / 60.0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()