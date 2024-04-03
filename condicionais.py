def verificar_maioridade():
    idade = int(input('Qual é a sua idade: '))
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

verificar_maioridade()


def par_ou_impar():
    numero = int(input('Digite um número:'))
    if numero % 2 == 0:
             print("Este número é par")
    else:
             print("Este número é impar")


par_ou_impar()

