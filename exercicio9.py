#Crie um programa que receba palavras e agregue elas em um texto até que seja escrita a palavra PARE.

texto = ""
print('Digite a palavra PARE para encerrar o programa!')
while True:
    palavra = input("Digite uma palavra: ")
    if palavra.upper() == "PARE":
        break
    texto += palavra + " "

print(f"Texto agregado: {texto}")


