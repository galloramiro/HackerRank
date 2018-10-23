def rotLeft(a, d):                                  # 'a' es un array con los números y 'd' es la cantidad de rotaciones a hacer
    normal = []                                     # Establezco una lista vacía para colocar la nueva lista
    for x in range(len(a)):                         # le pido que para cada valor en el largo de la lista sume ese valor a la nueva lista
        normal.append(str(a[x]))
    for i in range(d):                              # Acá le pido que para cada valor en la lista
        normal.insert(len(a),normal[0])             # inserte en el final de la misma (el final es el largo del la lista), el valor de indice 0
        normal.pop(0)                               # Con esto elimino el valor de indice 0 que ahora también estaría en el final de la lista. 
    return normal



print(rotLeft([1,2,3,4,5],4))
# 5 1 2 3 4
print(rotLeft([1,2,3,4,5,6,7,8,9],3))
# 4 5 6 7 8 9 1 2 3
print(rotLeft([41,73,89,7,10,1,59,58,84,77,77,97,58,1,86,58,26,10,86,51],10))
# 77 97 58 1 86 58 26 10 86 51 41 73 89 7 10 1 59 58 84 77
print(rotLeft([33,47,70,37,8,53,13,93,71,72,51,100,60,87,97],13))
# 87 97 33 47 70 37 8 53 13 93 71 72 51 100 60
