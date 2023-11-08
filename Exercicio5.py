#5) Faça um script que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas digitadas sejam válidas.

#a. Idade: entre 0 e 150
#b. Salário: maior que 0
#c. Gênero: M, F ou Outro

#Por último imprima os dados recebidos do usuário.

while True:
    idade = int(input("Digite a idade (entre 0 e 150): "))
    if 0 <= idade <= 150:
        break
    else:
        print("Idade fora do intervalo válido. Tente novamente.")

while True:
    salario = float(input("Digite o salário (maior que 0): "))
    if salario > 0:
        break
    else:
        print("Salário deve ser maior que 0. Tente novamente.")

while True:
    genero = input("Digite o gênero (M, F ou Outro): ").strip().upper()
    if genero in ["M", "F", "OUTRO"]:
        break
    else:
        print("Gênero inválido. Tente novamente.")

print("Dados do usuário:")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Gênero: {genero}")
