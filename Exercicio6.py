#6) Faça uma calculadora. O usuário deve inserir qual a operação matemática ele deseja realizar e logo em seguida os dois números.
#O programa deve finalizar apenas quando o usuário digitar a opção "sair" no momento de escolha da operação matemática.

while True:
    operacao = input("Escolha a operação (soma(+), subtracao(-), multiplicacao(*), divisao(/)) ou 'sair' para encerrar: ").lower()

    if operacao == 'sair':
        break

    if operacao not in ['soma', 'subtracao', 'multiplicacao', 'divisao', '+', '-', '*', '/']:
        print("Operação inválida. Tente novamente.")
        continue

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if operacao == 'soma' or operacao == '+':
        resultado = numero1 + numero2
    elif operacao == 'subtracao' or operacao == '-':
        resultado = numero1 - numero2
    elif operacao == 'multiplicacao' or operacao == '*':
        resultado = numero1 * numero2
    elif operacao == 'divisao' or operacao == '/':
        if numero2 == 0:
            print("Erro: divisão por zero.")
            continue
        resultado = numero1 / numero2

    print(f"Resultado da {operacao}: {resultado:.2f}")
