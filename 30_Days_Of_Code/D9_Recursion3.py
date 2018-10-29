def factorial(n):
    if n <= 1:                              # Entrando en el loop, le digo que siempre que si es igual a uno que simplemente devuelva uno
        return 1
    else:
        return n * factorial(n-1)           # Sino que multiplique n por la funcion con n -1 y esto vuelve un bucle hasta el último elemento

print(factorial(3))             # 3 * 2 * 1 = 6
print(factorial(5))             # 5 * 4 * 3 * 2 * 1 = 120


