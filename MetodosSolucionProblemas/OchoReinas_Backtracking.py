
TAM_TABLERO = 8
contadorSoluciones = 0

def es_seguro(tablero, fila, columna): # int[][] tablero, int fila, int columna
    
    # Verificar si hay una reina en la misma fila a la izquierda
    for i in range(columna):
        if tablero[fila][i] == 1:
            return False
    
    # Veritifar la diagonal superior izquierda
    i, j = fila, columna
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Verificar la diagonal inferior izquierda
    i, j = fila, columna
    while i < TAM_TABLERO and j >= 0:
        if tablero[i][j] == 1:
            return False
        i += 1
        j -= 1
    
    return True  # Si se cumplen todas las condiciones, es seguro colocar la reina en esa posición



def imprimir_solucion(tablero): # Muestra gráficamente el tablero con las reinas colocadas
    global contadorSoluciones
    contadorSoluciones += 1
    print(f"\nSolución #{contadorSoluciones}")
    print("   A B C D E F G H")
    print("  -----------------")
    for i in range(TAM_TABLERO):
        print(f"{i+1}| ", end="")
        for j in range(TAM_TABLERO):
            print("Q " if tablero[i][j] == 1 else "- ", end="")
        print(f"|{i+1}")
    print("  -----------------")
    print("   A B C D E F G H")
    

    
def resolver_todas(tablero, col):
    if col == TAM_TABLERO:
        imprimir_solucion(tablero)
        return

    for i in range(TAM_TABLERO):
        if es_seguro(tablero, i, col):
            tablero[i][col] = 1
            resolver_todas(tablero, col + 1) # Backtracking: intentar colocar la siguiente reina llamando la función recursivamente
            tablero[i][col] = 0 
            
            

def main():
    tablero = [[0 for _ in range(TAM_TABLERO)] for _ in range(TAM_TABLERO)]
    resolver_todas(tablero, 0)

    if contadorSoluciones == 0:
        print("No se encontró ninguna solución.")
    else:
        print(f"Se encontraron {contadorSoluciones} soluciones en total.")


if __name__ == "__main__":
    main()