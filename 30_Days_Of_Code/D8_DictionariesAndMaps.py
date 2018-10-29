import sys                                                  # Importo la librería del sistema

n = int(sys.stdin.readline().strip())                       # Creo una variable que lea la cantidad de pares que nos van a enviar. 
agenda = dict()                                             # Inicializo el diccionario donde voy a almacenar los datos

for i in range(0, n):                                       # Le pido que para cada uno entre 0 y n
    entrada = sys.stdin.readline().strip().split(' ')       # Agarre la entrada y la divida separándola con comas. 
    agenda[entrada[0]] = entrada[1]                         # Asigno el 0 que sería el primer valor a la key del diccionario y la 1 a la clave del diccionario

query = sys.stdin.readline().strip()                        # Le pido que toma las "Query´s" que nos mandan
while query:                                                # Mientras existan "Query´s" que siga haciendo
    telefono = agenda.get(query)                            # Le pido que busque la clave de la query
    if telefono:                                          
        print(query + '=' + telefono)                       # Si está en el diccionario, lo tiene que imprimir con el formato solicitado
    else:                                                   
        print('Not found')                                  # Sino imprime NotFound
    query = sys.stdin.readline().strip()                    # Cuando termina esto vuelve a leer si hay query



