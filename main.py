import pygame
import time

# -------------------------------
# 1️⃣ Configuración de Pygame
# -------------------------------
pygame.init()
ANCHO, ALTO = 540, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sudoku Solver")
FUENTE_NUM = pygame.font.SysFont("Arial", 40)
FPS = 60

# -------------------------------
# 2️⃣ Colores
# -------------------------------
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)

# -------------------------------
# 3️⃣ Tablero inicial
# -------------------------------
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

numeros_iniciales = [[bool(num) for num in fila] for fila in tablero]

# -------------------------------
# 4️⃣ Funciones para dibujar
# -------------------------------
def dibujar_tablero():
    VENTANA.fill(BLANCO)
    for i in range(9):
        for j in range(9):
            num = tablero[i][j]
            if num != 0:
                color = NEGRO if numeros_iniciales[i][j] else VERDE
                texto = FUENTE_NUM.render(str(num), True, color)
                VENTANA.blit(texto, (j * 60 + 20, i * 60 + 10))
    for i in range(10):
        grosor = 4 if i % 3 == 0 else 1
        pygame.draw.line(VENTANA, NEGRO, (0, i*60), (540, i*60), grosor)
        pygame.draw.line(VENTANA, NEGRO, (i*60, 0), (i*60, 540), grosor)
    pygame.display.update()

# -------------------------------
# 5️⃣ Funciones del solver
# -------------------------------
def es_valido(num, fila, col):
    if num in tablero[fila]:
        return False
    for i in range(9):
        if tablero[i][col] == num:
            return False
    start_fila, start_col = 3 * (fila // 3), 3 * (col // 3)
    for i in range(start_fila, start_fila + 3):
        for j in range(start_col, start_col + 3):
            if tablero[i][j] == num:
                return False
    return True

def encontrar_vacio():
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return (i, j)
    return None

# -------------------------------
# 6️⃣ Solver tradicional rápido
# -------------------------------
def resolver():
    encontrado = encontrar_vacio()
    if not encontrado:
        return True
    fila, col = encontrado
    for num in range(1, 10):
        if es_valido(num, fila, col):
            tablero[fila][col] = num
            # Si quieres animación, descomenta la línea siguiente
            # dibujar_tablero(); pygame.time.delay(20)
            if resolver():
                return True
            tablero[fila][col] = 0
    return False

# -------------------------------
# 7️⃣ Loop principal
# -------------------------------
def main():
    correr = True
    clock = pygame.time.Clock()
    solucion_iniciada = False

    while correr:
        clock.tick(FPS)
        dibujar_tablero()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not solucion_iniciada:
                    solucion_iniciada = True
                    resolver()  # Resuelve instantáneamente
                    dibujar_tablero()  # Muestra el resultado final

    pygame.quit()

if __name__ == "__main__":
    main()
