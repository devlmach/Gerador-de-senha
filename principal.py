import random
senha = []

letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '1234567890'
especiais = '!@#$%¨&*()?~'
algarismos = letras + numeros + especiais

for i in range(10):
    i = random.choice(algarismos)
    senha.append(i)
    
print(''.join(senha))