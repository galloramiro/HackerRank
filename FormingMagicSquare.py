def formingMagicSquare(arr):
    suma1 = 0
    suma2 = 0
    suma3 = 0
    v = 0 
    for a in arr:
        for a in ar:
            suma1 += a
        for a in ar:
            suma2 += r
        return suma1, suma2


# Para sumar todos los elementos del primer array
#    for ar in arr:
#        for a in ar:
#            suma1 += a
#        return suma1





print(formingMagicSquare([[5,3,4],[1,5,8],[6,4,2]]))
#       [5-8] + [8-9] + [4-7] = 7
# 5 3 4  --> 12          8 3 4  --> 15
# 1 5 8  --> 14          1 5 9  --> 15
# 6 4 2  --> 12          6 7 2  --> 15
print(formingMagicSquare([[4,9,2],[3,5,7],[8,1,5]]))
#              [6-5] = 1
# 4 9 2  --> 15          4 9 2  --> 15 
# 3 5 7  --> 15          3 5 7  --> 15 
# 8 1 5  --> 14          8 1 5  --> 15
print(formingMagicSquare([[4,8,2],[4,5,7],[6,1,6]]))
#          [9-8] + [3-4] + [8-6]
# 4 8 2  --> 14          4 9 2  --> 15 
# 4 5 7  --> 16          3 5 7  --> 15 
# 6 1 6  --> 13          8 1 6  --> 15 