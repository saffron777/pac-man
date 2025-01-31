    
from tkinter import font
import pygame
import sys
import math
import random
from datetime import datetime, timedelta
# constantes del laberinto
WALL = 1
GALLETA = 2
SUPER_GALLETA = 3
WAY = 0

GHOST_RED = 4
GHOST_CYAN = 5
GHOST_MAGENTA = 6
GHOST_GREEN = 7

# Configuración del laberinto
LABERINTO = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 3, 1, 0, 0, 1, 2, 1, 0, 0, 0, 1, 2, 1, 1, 2, 1, 0, 0, 0, 1, 2, 1, 0, 0, 1, 3, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 3, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 1],
    [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Tamaño de la celda y dimensiones de la pantalla
CELL_SIZE = 20
WIDTH = len(LABERINTO[0]) * CELL_SIZE
HEIGHT = len(LABERINTO) * CELL_SIZE

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0) # Color de los fantasmas
CYAN = (0, 255, 255) # Color de los fantasmas
MAGENTA = (255, 0, 255) # Color de los fantasmas
GREEN = (0, 255, 0) # Color de los fantasmas
# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

# Fuente para el mensaje de "Game Over"
font = pygame.font.Font(None, 74)

# Función para reiniciar el juego
def reset_game():
    global pacman_pos, pacman_direction, pacman_mouth_open, ghost_update_counter, ghosts, game_over, you_win, LABERINTO
    # Reiniciar posición de Pacman
    pacman_pos = [14, 13]
    pacman_direction = [0, 0]
    pacman_mouth_open = True
    ghost_update_counter = 0
    # Reiniciar posición de los fantasmas
    ghosts = {
        "red": {"pos": [10, 9], "color": RED, "target": None, "speed": 0.5},
        "green": {"pos": [10, 10], "color": GREEN, "target": None, "speed": 0.5},
        "cyan": {"pos": [10, 11], "color": CYAN, "target": None, "speed": 0.5},
        "magenta": {"pos": [10, 12], "color": MAGENTA, "target": None, "speed": 0.5}
    }

    # Reiniciar el laberinto (restaurar galletas y supergalletas)
    LABERINTO = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
        [1, 3, 1, 0, 0, 1, 2, 1, 0, 0, 0, 1, 2, 1, 1, 2, 1, 0, 0, 0, 1, 2, 1, 0, 0, 1, 3, 1],
        [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
        [1, 3, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 1],
        [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    # Reiniciar estado del juego
    game_over = False
    you_win = False

# Posición inicial de Pacman
pacman_pos = [14, 13]
pacman_direction = [0, 0]
pacman_mouth_open = True

# Posiciones iniciales de los fantasmas
ghosts = {
    "red": {"pos": [10, 9], "color": RED, "target": None},
    "green": {"pos": [10, 10], "color": GREEN, "target": None},
    "cyan": {"pos": [10, 11], "color": CYAN, "target": None},
    "magenta": {"pos": [10, 12], "color": MAGENTA, "target": None}
}

# Contador de actualización para los fantasmas
ghost_update_counter = 0

# Estado del juego
game_over = False
you_win = False
# Función para dibujar el laberinto
def draw_maze():
    for y, row in enumerate(LABERINTO):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == 2:
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 2)
            elif cell == 3:
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 5)

# Función para dibujar a Pacman
def draw_pacman():
    x, y = pacman_pos
    if pacman_mouth_open:
        pygame.draw.circle(screen, YELLOW, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)
    else:
        pygame.draw.circle(screen, YELLOW, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)
        pygame.draw.polygon(screen, BLACK, [
            (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2),
            (x * CELL_SIZE + CELL_SIZE, y * CELL_SIZE),
            (x * CELL_SIZE + CELL_SIZE, y * CELL_SIZE + CELL_SIZE)
        ])

# Función para dibujar los fantasmas
def draw_ghosts():
    for ghost in ghosts.values():
        x, y = ghost["pos"]
        pygame.draw.circle(screen, ghost["color"], (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

# Función para mover a Pacman
def move_pacman():
    global pacman_pos, pacman_mouth_open
    new_x = pacman_pos[0] + pacman_direction[0]
    new_y = pacman_pos[1] + pacman_direction[1]

    # Verificar colisiones con las paredes
    if 0 <= new_x < (len(LABERINTO[0])) and 0 <= new_y < (len(LABERINTO)):
        if LABERINTO[new_y][new_x] != 1:
            pacman_pos = [new_x, new_y]
            pacman_mouth_open = not pacman_mouth_open

    # Pasadizo en la fila 15
    if ((pacman_pos[0] == 0 or pacman_pos[0] == 27) and pacman_pos[1] == 11) or ((pacman_pos[0] == 0 or pacman_pos[0] == 27) and pacman_pos[1] == 10):
        if pacman_pos[0] <= 0:
            pacman_pos[0] = len(LABERINTO[0]) - 1
        elif pacman_pos[0] >= (len(LABERINTO[0]) - 1):
            pacman_pos[0] = 0

    # Comer galletas
    if LABERINTO[pacman_pos[1]][pacman_pos[0]] == 2 or LABERINTO[pacman_pos[1]][pacman_pos[0]] == 3:
        LABERINTO[pacman_pos[1]][pacman_pos[0]] = 0

# Función para calcular la distancia entre dos puntos
def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Función para mover los fantasmas
def move_ghosts():
    global ghost_update_counter
    ghost_update_counter += 1
    
    # Los fantasmas se mueven cada 2 iteraciones (mitad de velocidad de Pacman)
    if ghost_update_counter >= 3:
        ghost_update_counter = 0
        for ghost in ghosts.values():
            x, y = ghost["pos"]
            possible_moves = []

            # Movimientos posibles (arriba, abajo, izquierda, derecha)
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < len(LABERINTO[0]) and 0 <= new_y < len(LABERINTO):
                    if LABERINTO[new_y][new_x] != 1:
                        possible_moves.append((new_x, new_y))

            # Elegir el movimiento según el comportamiento del fantasma
            if ghost["color"] == RED:
                # Fantasma rojo: ruta más corta hacia Pacman
                ghost["target"] = pacman_pos
            elif ghost["color"] == GREEN:
                # Fantasma verde: ruta corta hacia 4 posiciones delante de Pacman
                target_x = pacman_pos[0] + pacman_direction[0] * 4
                target_y = pacman_pos[1] + pacman_direction[1] * 4
                ghost["target"] = [target_x, target_y]
            elif ghost["color"] == CYAN:
                # Fantasma cyan: radio de 8 posiciones detrás de Pacman
                target_x = pacman_pos[0] - pacman_direction[0] * 8
                target_y = pacman_pos[1] - pacman_direction[1] * 8
                ghost["target"] = [target_x, target_y]
            elif ghost["color"] == MAGENTA:
                # Fantasma magenta: posición de Pacman a dos cuadros delante y 180 grados contrario al fantasma rojo
                target_x = pacman_pos[0] + pacman_direction[0] * 2
                target_y = pacman_pos[1] + pacman_direction[1] * 2
                ghost["target"] = [target_x, target_y]

            # Elegir el movimiento más cercano al objetivo
            if ghost["target"]:
                best_move = min(possible_moves, key=lambda move: distance(move, ghost["target"]))
                ghost["pos"] = list(best_move)

# Función para verificar si no quedan galletas
def check_win():
    for row in LABERINTO:
        if 2 in row or 3 in row:
            return False
    return True

# Función para mostrar "Game Over"
def show_game_over():
    text = font.render("GAME OVER", True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
 
# Función para mostrar "You Win!"
def show_you_win():
    text = font.render("YOU WIN!", True, GREEN)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    
# Bucle principal del juego
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman_direction = [0, -1]
            elif event.key == pygame.K_DOWN:
                pacman_direction = [0, 1]
            elif event.key == pygame.K_LEFT:
                pacman_direction = [-1, 0]
            elif event.key == pygame.K_RIGHT:
                pacman_direction = [1, 0]
            elif (event.key == pygame.K_SPACE or event.key == pygame.MOUSEBUTTONUP) and (game_over or you_win):
                # Reiniciar el juego si se presiona la barra espaciadora
                reset_game()
                
    if not game_over and not you_win:
        screen.fill(BLACK)
        draw_maze()
        move_pacman()
        move_ghosts()
        draw_pacman()
        draw_ghosts()  
        
        # Verificar si el jugador ganó
        if check_win():            
            you_win = True
            
            
        # Verificar colisiones entre Pacman y los fantasmas
        for ghost in ghosts.values():
            if ghost["pos"] == pacman_pos:
                game_over = True
  
        pygame.display.flip()
        clock.tick(10)
        
    else:
        # Mostrar "Game Over" y esperar a que el usuario cierre la ventana
        screen.fill(BLACK)
        if game_over:
            show_game_over()
        elif you_win:
            show_you_win()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()
sys.exit()
    