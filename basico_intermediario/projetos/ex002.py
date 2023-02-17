#Dissecando uma variável:

a = input('Digite algo: ')
print(f'O tipo primitivo dessa informação é: {type(a)}')
print(f'A informação é alfabética? {a.isalpha()}')
print(f'A informação é alfanumérica? {a.isalnum()}')
print(f'A informação é numérica? {a.isnumeric()}')
print(f'A informação é decimal? {a.isdecimal()}')
print(f'A informação está apenas em maiúscula? {a.isupper()}')
print(f'A informação está apenas em minúsculo? {a.islower()}')
print(f'A informação possuí apenas espaços? {a.isspace()}')
print(f'A informação capitalizada? {a.istitle()}')

