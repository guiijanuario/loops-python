#3) Faça um programa que imprima a tabuada do 9 na tela (entre 1 e 10).
#Insira a conta, por exemplo, 9 * 1 = 9, sendo cada um dos valores em uma linha diferente.

numero = 9

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
