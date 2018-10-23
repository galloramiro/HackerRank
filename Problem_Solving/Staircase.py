def staircase(n):
    
    for v in range(1,n+1):              # Hago una lista que comience desde el uno y hasta el número brindado, por eso se pone más uno al número porque range no lo incluye
        escalon = '#'*v                 # Multiplico el '#' por el valor de v (por eso lo hago empezar por uno)
        espacio = ' '*(n-(v+1))         # Multiplico el espacio por n - v y le sumo uno porque necesito que quede tome en cuenta el '#' 
        if v == n:                      
            print(escalon)              # Le digo que si 'v' es igual a 'n' solo imprima el escalon ya que sería el número completo y no necesitamos agregar espacios
        else:                           
            print(espacio,escalon)      # Sino que imprima el escalon y la cantidad de espacios restantes para completar el largo. 
    






print(staircase(6))
     #
    ##
   ###
  ####
 #####
######

def staircase(n):
    esc = '#'
    
    for v in range(1,n+1):
        escalon = esc*v
        espacio = ' '*(n-(v+1))
        if v == n:
            print(escalon)
        else:
            print(espacio,escalon)