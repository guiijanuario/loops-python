#1) Escreva um programa que solicite um número inteiro e imprima na tela todos os números de 1 até o número digitado, separado por espaços.
#_Exemplo_
#número digitado: 5
#resultado esperado: 1 2 3 4 5


numero = int(input("Digite um número inteiro: "))

print(f"Número digitado: {numero}")
print("Resultado:", end=' ')

for i in range(1, numero + 1):
    print(i, end=' ')

print()