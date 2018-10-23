def minimumBribes(q):
    sobornos = 0                                  

    for i in range(len(q)-1,-1,-1):                        # Largo de "q-1" decreciendo por -1 hasta -1, siempre se cruza el valor que debería tener originalmente
        if q[i] - (i + 1) > 2:                             # Comrpuebo si el valor de "q[i]" - (i + 1) este más uno es el que le da su lugar.  Ej2: 5 - (1 + 1) == 3
            print('Too chaotic')                           # En donde está el 5 debería estar el dos y le restamos dos. 
            return
        for j in range(max(0, q[i] - 2),i):                # devuelve un rango del maximo entre 0 y q[i]-1 hasta i. Ej 1: max(0, 4-2) == range(2,4) 
            if q[j] > q[i]:                                # Acá comprueba si 5 > 4 y luego si 3 es mayor a 4 
                sobornos+=1                                # Entonces suma un solo soborno, ya que el otro paso lo dio 5
    print(sobornos)



minimumBribes([2,1,5,3,4])               # 3
minimumBribes([2,5,1,3,4])               # Too chaotic
minimumBribes([5,1,2,3,7,8,6,4])         # Too chaotic
minimumBribes([1,2,3,4,5,6,7,10,9,8])    # 2
minimumBribes([1,2,5,3,7,8,6,4])         # 7





# PRIMER INTENTO FALLIDO, no acierta el último ejemplo. 
#def minimumBribes(this_queue):
#    lugar = 1                          # Establezco la cuenta en 1, esto hace que desde el primer momento los reste con el valor que debería haber en su puesto.
#    pasos = 0                          # Establezco variable que va a sumar los pasos. 

#    for x in this_queue:               # Para cada elemento en la lista
#        if x-lugar > 2:                # "x - lugar" resta el valor de x con el valor que debería tener en la fila, si es negativo 
#            return 'Too chaotic'       # Si el valor es mayor a dos, entonces devuelve que es muy caótico
#        elif x-lugar > 0:
#            pasos += x-lugar           # En caso de que sea mayor a 0 simplemente suma la cantidad de pasos dados a pasos
#            lugar += 1                 # Suma uno al lugar
#        else: 
#            lugar += 1                 # En caso de que sea otro valor simplemente lo sumo. 
#    return pasos
