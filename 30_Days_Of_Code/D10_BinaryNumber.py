actual = 0
maximo = 0
while n > 0:                    # Mientras que el valor de 'n' sea mayor a 0
    restante = n % 2            # Busco el valor que sobra de dividrlo por 2
    n = n // 2                  # Cambio el valor actual de 'n' a 'n' divido 2
    if restante == 1:           
        actual += 1             # Si el restante es 1 se lo sumo a actual
        if actual > maximo:     # Si actual es mayor a máximo actualizo el valor
            maximo = actual
    else:
        actual = 0              # Si el restante es 0 simplemente vuelvo actual a 0

print(maximo)