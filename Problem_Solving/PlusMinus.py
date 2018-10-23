# https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def plusMinus(arr):
    positivo = 0                                    # Declaro las variables para sumar la cantidad de números positivos
    negativo = 0                                    # Igual en negativos
    cero = 0                                        # Igual en ceros

    for a in arr:                                   # Le pido que para cada valor del array compruebe
        if a == 0:                                  # Si a es 0
            cero += 1                               # Suma uno a cero
        elif a > 0:                                 # si a es mayor a 0 
            positivo += 1                           # sumale uno a positivo
        else:                                       # Todo lo que resta es negativo así que se le suma uno a negativo
            negativo += 1                           # 
#    print('{:.6f}'.format(positivo/len(arr)))
#    print('{:.6f}'.format(negativo/len(arr)))        El ejercicio en la página exige que se haga el print así, encuentro mejor hacerlo de la otra forma pero sino no te aprueba. 
#    print('{:.6f}'.format(cero/len(arr)))
    return '{:.6f}\n{:.6f}\n{:.6f}'.format(positivo/len(arr), negativo/len(arr), cero/len(arr))      # acá divido la suma total por el largo del string y lo formateo como pide.




print(plusMinus([-4, 3, -9, 0, 4, 1]))  
# 0.500000
# 0.333333
# 0.166667
print(plusMinus([1, 1, 0, -1, -1]))  
# 0.500000
# 0.333333
# 0.166667
print(plusMinus([1, 2, 3, -1, -2, -3, 0, 0]))  
# 0.375000
# 0.375000
#0.250000