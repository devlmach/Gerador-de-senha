import random
senha = []

letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '1234567890'
especiais = '!@#$%¨&*()?~'
algarismos = letras + numeros + especiais

for i in range(10):
    c = random.choice(algarismos)
    senha.append(c)
    
print(''.join(senha))