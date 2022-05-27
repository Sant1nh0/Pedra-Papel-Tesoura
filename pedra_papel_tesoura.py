import random

ppt = input('pedra, papel ou tesoura?\n')
list = ['pedra', 'papel', 'tesoura']
r = random.choice(list)
print(r)

if r == ppt:
    print('empate!')

elif ppt == 'pedra' and r == 'tesoura':
    print('ganhou!')

elif ppt == 'papel' and r == 'pedra':
    print('ganhou!')

elif ppt == 'tesoura' and r == 'papel':
    print('ganhou!')

else:
    print('perdeu!')