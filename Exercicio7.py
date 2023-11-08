# Crie um programa que receba um número e imprima "fizz" se o numero for multiplo de 3,
# "buzz" se for multiplo de 5 e "fizzbuzz" se for multiplo de 3 e 5

numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("fizzbuzz")
elif numero % 3 == 0:
    print("fizz")
elif numero % 5 == 0:
    print("buzz")
else:
    print(numero)

