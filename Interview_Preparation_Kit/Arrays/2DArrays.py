def _get_hourglass_sum(matrix,row,col):                                     # tomo el resultado de hourglassSum que en este caso sería arr[1][1]
    sum = 0                                                                 
    ### superior
    sum += matrix[row-1][col-1]                                             # arr[1-1][1-1] = arr[0][0] tomo el primer valor del reloj de arena
    sum += matrix[row-1][col]                                               # arr[1-1][1] = arr[0][1] tomo el valor que sigue del reloj de arena
    sum += matrix[row-1][col+1]                                             # arr[1-1][1+1] = arr[0][2] tomo el último valor de la parte superior
    #   centro
    sum += matrix[row][col]                                                 # arr[1][1] = tomo el valor central del reloj de arena
    ### inferior
    sum += matrix[row+1][col-1]                                             # arr[1+1][1-1] = arr[0][0] tomo el primer valor del reloj de arena
    sum += matrix[row+1][col]                                               # arr[1+1][1] = arr[0][1] tomo el valor que sigue del reloj de arena
    sum += matrix[row+1][col+1]                                             # arr[1+1][1+1] = arr[0][2] tomo el último valor de la parte superior
    return sum

def hourglassSum(arr):
    max_hourglass_sum = -63                                                 # Establezco la suma mínima que sería -63 que sería un reloj lleno de -9
    for row in range(1,5):                                                  # Le pido que recorra de 1 a 5 ya que los costados no pueden tener relojes completos
        for col in range(1,5):                                              # Entonces al ir del uno al 5 centro el número en el medio y siempre tendrá techo y piso. 
            current_hourglass_sum = _get_hourglass_sum(arr,row, col)        # llamo a la función brindando los números a recorrer
            if current_hourglass_sum > max_hourglass_sum:                   # Le pregunto si es mayor al que actualmente tenemos guardado
                max_hourglass_sum = current_hourglass_sum                   # si no coloco el nuevo. 

    return(max_hourglass_sum)






print(hourglassSum([[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]))
#     19
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0