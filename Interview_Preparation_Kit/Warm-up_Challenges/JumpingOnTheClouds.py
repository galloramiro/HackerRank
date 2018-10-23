# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def jumpingOnClouds(c):
    actual = 0 
    saltos = 0
    fin = len(c)-1                                       # Acá establezco que siempre me falte uno para el final cosa de poder dar el último paso,
                                                         # si le saco el -1 el último paso ya estaría dado. 

    while actual < fin:                                  # Acá le digo que mientras que actual sea menor que final siga iterando. 
        if actual +2 <= fin and c[actual + 2] == 0:      # Si salto y no caigo al vacio y, además, la nube en la que caigo no tiene truenos
            actual += 2                                  # Le sume dos pasos al actual (osea esquivo una nube) y sume un salto
            saltos += 1                                  
        else:                                            # Caso contrario sumame un paso y un salto. 
            actual += 1                                 
            saltos += 1
    return saltos

print(jumpingOnClouds([0, 0, 1, 0, 0, 1,0]))
print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))
