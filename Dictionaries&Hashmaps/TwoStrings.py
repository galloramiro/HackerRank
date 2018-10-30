def twoStrings(s1, s2):
    return 'YES' if set(s1) & set(s2) else 'NO'         # De esta manera comparo directamente si hay valores únicos entre estos dos elementos. 

print(twoStrings('hello', 'world'))            # YES
print(twoStrings('hi', 'world'))               # NO



# V 2           Tira time out error con strings demasiado grandes. 
#def twoStrings(s1, s2):
    #count = sum([+1 for x in list(s1) if x in list(s2)])             # Sumo los valores de la lista coloco por cada repetición un uno. 
    #if count >= 1: return('YES')                                     # Si esto es igual o mayor a 1 quiere decir que comparten
    #return('NO')


# BASE
#def twoStrings(s1, s2):
#    count = 0
#    for x in list(s1):
#        if x in list(s2):
#            count += 1
#    if count > 1:
#        return('YES')
#    else:
#        return('NO')

