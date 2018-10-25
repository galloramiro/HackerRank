numero_casos = int(input())             # Capturo el primer input que va a dar la máquina

for n in range(numero_casos):
    s = input()                         # Capturo el segundo
    even = ''
    odd = ''
    for x in range(len(s)):
        if x % 2 == 0:
            even += s[x]
        else:
            odd += s[x]
    print(even +' '+odd)

print(evenOddIndex('Hacker'))
print(evenOddIndex('Rank'))