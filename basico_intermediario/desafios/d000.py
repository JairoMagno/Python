#Verificando tipo primitivo e suas possíveis informações:

a = input('Digite algo: ')
print(type(a))
print('The information is alphabetic?', a.isalpha())
print('The information is alphanumeric?', a.isalnum())
print('The information is numeric?', a.isnumeric())
print('The information is decimal?', a.isdecimal())
print('The information is upper?', a.isupper())