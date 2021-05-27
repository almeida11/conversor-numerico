num = int(input('Digite um número qualquer: '))
print('[1] para binário')
print('[2] para octal')
print('[3] para hexadecimal')
conv = int(input('Opção: '))
if conv == 1:
    print('O número {} em binário é {}'.format(num, bin(num)[2:]))
elif conv == 2:
    print('O número {} em octal é {}'.format(num, oct(num)[2:]))
elif conv == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Valor inválido, tente novamente!')
