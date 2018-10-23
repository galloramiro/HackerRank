# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def countingValleys(n, s):
    lvl = 0                             # Marco el nivel actual y lo comienzo en 0
    valleys = 0                         # Numero de valles 0
    for step in s:                      # Le pido que para cada paso que de en la lista de pasos
        if step == 'U':                 # Si el paso es Up le sume uno al nivel actual
            lvl += 1                    
        else:                           # Si el paso no es Up
            if lvl == 0:                # Compruevo como está el nivel actual, si es 0
                valleys += 1            # Sumo uno al valley, ya que estaría descendiendo 
            lvl -= 1                    # y le resto uno al nivel actual, si no es 0 simplemente solo le resto uno al nivel actual. 
    return valleys                      #

print(countingValleys(8,'UDDDUDUU'))

