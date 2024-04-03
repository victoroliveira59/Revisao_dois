# def verificar_maioridade():
#     idade = int(input('Qual é a sua idade: '))
#     if idade >= 18:
#         print("Maior de idade")
#     else:
#         print("Menor de idade")
#
# verificar_maioridade()
#
#
# def par_ou_impar():
#     numero = int(input('Digite um número:'))
#     if numero % 2 == 0:
#              print("Este número é par")
#     else:
#              print("Este número é impar")
#
#
# par_ou_impar()

def nota_aprovacao():
        try:
            nota1 = float(input('Digite a nota: '))
        except ValueError:
            print("Valor inválido. Digite um número entre 0 e 10.")
            return

        if 0 <= nota1 <= 10:
            if nota1 >= 7:
                print("Approvado")
            else:
                print("Reprovado")
        else:
            print("Valor não estar entre 0 e 10.")

nota_aprovacao()
