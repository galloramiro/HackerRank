# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ar):
    sameColor = {}                  # Establezco un dic para poder vincular las claves a los valores
    count = 0                       # Establezco el contador para a futuro contar
    for key in ar:                  # Tomo cada variable en el array
        if key in sameColor:        # Tomo los valores y compruebo si están en sameColor
            sameColor[key] += 1     # Si no están los sumo más un uno, y si está le sumo un uno. 
        else:
            sameColor[key] = 1      # Si no está, osea si no se repite, lo sumo una sola vez. 
    for key in sameColor:           # Ahora tomo los valores que están en el dict para iterarlos
        count += sameColor[key]//2  # Sumo los valores únicos y divido las repeticiones por //(flor) 2 lo que los dividie individualmente y lo redondea para abajo. 
    return count


print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))
