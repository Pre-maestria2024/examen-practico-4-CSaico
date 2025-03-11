def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    # Leer valores de entrada
    m, n = map(int, data[0].split())  # m = salud máxima, n = cantidad de alimentos
    H = list(map(int, data[1].split()))  # Valores de salud que otorgan los alimentos
    D = list(map(int, data[2].split()))  # Costos de los alimentos

    # Crear lista de alimentos con (costo, salud) y ordenarlos por eficiencia (costo menor primero)
    alimentos = sorted(zip(D, H))

    salud_actual = sum(H)  # Salud inicial de Major Muffin
    salud_necesaria = m - salud_actual  # Cuánta salud falta para llegar a m
    total_dolares = 0

    if salud_necesaria <= 0:
        print(0)  # Ya tiene salud máxima, no necesita gastar nada
        return

    # Consumir los alimentos más baratos primero hasta alcanzar la salud máxima
    for costo, salud in alimentos:
        if salud_necesaria <= 0:
            break  # Ya alcanzó la salud máxima
        cantidad = min(salud_necesaria, salud)  # Tomamos la cantidad necesaria
        total_dolares += (costo * (cantidad // salud))  # Multiplicamos costo por unidades
        salud_necesaria -= cantidad  # Reducimos la salud necesaria

    print(total_dolares)  # Imprimir el costo total mínimo

if __name__ == '__main__':
    main()

