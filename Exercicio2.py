#2) Faça um programa que mostre o fatorial de um número digitado.
#_Exemplo_
#número digitado: 5
#resultado esperado: 120



numero = int(input("Digite um número inteiro: "))

fatorial = 1
if numero < 0:
    print("O fatorial não está definido para números negativos.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial}")
