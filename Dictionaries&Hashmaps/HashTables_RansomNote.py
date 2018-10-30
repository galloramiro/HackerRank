from collections import Counter

def checkMagazine(magazine, note):                          
        l1 = len(note)                                  # Tomo el largo de note y magazine, que fueron convertidos en lista
        l2 = len(magazine)                              
        magazine.sort()                                 # Organizo ambas listas, por lo que quedarán alfabeticamente ordenadas. 
        note.sort()                                     
        i = 0                                           # Establezco dos cuentas distintas para ir sumando hasta encontrar los respectivos
        j = 0                                           
        count = 0                                       # Establezco la cuenta final para comparar con el largo y ver si se puede armar la lista
        while i<l1 and j<l2:                            # Mientras que las sumas no superen los largos prosigo
                if note[i] == magazine[j]:              # Si la primera palabra es igual a la primera palabra
                        count += 1                      # Sumo uno a count
                        i += 1                          # Sumo uno a i (osea que avanzo sobre la nota)
                j += 1                                  # Caso contrario sumo uno a j (osea avanzo sobre la el magazine en el próximo turno y vuelvo a comparar)
        if count == l1:                                 
                print ('Yes')                           # Si cuando termino todo el largo de la nota me da igual al count quiere decir que se puede armar. 
        else:                                           
                print('No')                             # Sino quiere decir que no se puede armar. 




# Las palabras las paso en lista para simular como las pasa HackerRank que las convierte en lista con la función __main__
checkMagazine(['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts'],['ive', 'got', 'some', 'coconuts'])      # No
checkMagazine(['two', 'times', 'three', 'is', 'not', 'four'],['two', 'times', 'two', 'is', 'four'])             # No
checkMagazine(['give', 'me', 'one', 'grand', 'today', 'night'],['give', 'one', 'grand', 'today'])               # Yes