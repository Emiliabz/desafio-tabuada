"""
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.

Exemplo de funcionamento:
- Usuário digita 5 -> Mostra tabuada do 5.
- Usuário digita 8 -> Mostra tabuada do 8.
- Usuário digita -1 -> Programa encerra.
-------------------------------------------------------------------------
"""
print('-=-' * 22)
print(f'\033[34mCalculadora de Tabuada - Para encerrar, digite um número \033[31mnegativo.\033[m')
print('-=-' * 22)
while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 30)

    if n < 0:
        break


    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')

print('\033[34mPROGRAMA TABUADA ENCERRADO.\033[m Volte sempre!')