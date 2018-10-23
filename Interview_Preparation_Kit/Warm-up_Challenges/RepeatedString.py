def repeatedString(s, n):                   # s = string a repetir      n = numero de valores a contar
    a_count = s.count('a')                  # Cuento las 'a' que hay en el string
    a_count *= (n//len(s))                  # Divido el número de repeteiciones por el largo del string y lo multiplico por la cuenta. 
    a_count += s[:n%len(s)].count('a')      # No lo entendí... 
    return a_count



    #return(s.count('a')*(n//len(s))+s[:n%len(s)].count('a'))




print(repeatedString('abcac',10))           # Deve devolver 4
print(repeatedString('aba',10))             # Deve devolver 7
#print(repeatedString('a',1000000000000))    # Deve devolver 1000000000000