def reversedArray(arr):
    return ' '.join([str(x) for x in arr[::-1] ])       # Le pido que para cada elemento de arr dado vuelta[::-1] lo convierta en string y lo agregue y luego lo junte.


print(reversedArray([1,4,3,2]))         # 3 2 4 1

# ESTA ES LA RESPUETA QUE QUIERE LA PÁGINA
print(' '.join([str(x) for x in arr[::-1] ]))
