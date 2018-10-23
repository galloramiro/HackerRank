def conditional(n):
    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0 and n in range(2,5):
        print('Not Weird')
    elif n % 2 == 0 and n in range(6,20):
        print('Weird')
    elif n % 2 == 0 and n > 20:
        print('Not Weird')

conditional(1)
conditional(5)
conditional(4)
conditional(6)
conditional(8)
conditional(20)
conditional(22)
conditional(21)