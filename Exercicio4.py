#4) Faça um programa em que o usuário digite números quaisquer e encerrará no momento em que o valor 0 seja digitado.
#Ao final diga qual foi o maior número digitado.

maior_numero = None

while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))

    if numero == 0:
        break

    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

if maior_numero is not None:
    print(f"O maior número digitado foi: {maior_numero}")
else:
    print("Nenhum número foi digitado.")
