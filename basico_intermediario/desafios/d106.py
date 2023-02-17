def isprime(n):
    if n == 2: return True
    if n % 2 == 0 or n <= 1: return False
    for x in range (3, n):
        if n % x == 0: return False
        x += 2
    return True
n = int(input('Qual intervalo pra verificar os números primos: '))
for c in range (0, n+1):
    if isprime(c) == True:
        print(f'{c} => ', end='')
print('FIM')

