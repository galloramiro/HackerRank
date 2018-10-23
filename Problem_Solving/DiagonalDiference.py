# https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen

def diagonalDifference(arr):
    v = 0                               # Para recorrer en diagonal un array sabemos que el valor inicial será 0,0 el valor siguien será 1,1 etc. Por eso empezamos setando 0
    nv = -1                             # Para hacer la diagonal contraria es lo mismo, solo que empieza de -1
    suma1 = 0                           # Seteo las distintas sumas
    suma2 = 0                           
    for a in arr:                       # Hago que recorra cada uno de los array dentro del array 2d, osea que un valor ya lo tengo asegurado siempre
        suma1 += a[v]                   # Sumo el valor del primer array con el indice de 'v' que es 0, osea el 0,0
        v +=1                           # Le sumo uno a 'v' para que el proximo sea 1,1
        suma2 += a[nv]                  # Lo mismo pero con 'nv' osea que empezamos en 0,-1 como debe ser
        nv -= 1                         # y ahora le resto uno para que el próximo sea 1,-2
    return abs(suma1 - suma2)           # Resto el valor absoluto de los números. 
        


print(diagonalDifference([[11, 2, 4],[4, 5, 6],[10, 8, -12]]))