def aVeryBigSum(ar):
    suma = 0
    for a in ar:
        suma += a
    return suma

print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))