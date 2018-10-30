def twoStrings(s1, s2):
    count = sum([+1 for x in list(s1) if x in list(s2)])             # Sumo los valores de la lista coloco por cada repetición un uno. 
    if count >= 1: return('YES')                                     # Si esto es igual o mayor a 1 quiere decir que comparten
    return('NO')



print(twoStrings('hello', 'world'))            # YES
print(twoStrings('hi', 'world'))               # NO


