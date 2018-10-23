def compareTriplets(a, b):
    alice = 0
    bob = 0 

    for n in range(len(a)):
        if a[n] > b[n]:
            alice += 1
        elif a[n] == b[n]:
            pass
        else:
            bob += 1
    return alice, bob


print(compareTriplets((5, 6, 7),(3, 6, 10)))                # 1 1
print(compareTriplets((17, 28, 30),(99, 16, 8)))            # 2 1
