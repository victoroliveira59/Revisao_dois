def calculadora(num1, num2, operador):
    try:
        if not 1 <= operador <= 5:
            raise ValueError("Operador inválido.")
        match operador:
            case 1:
                print("Soma =", num1 + num2)
            case 2:
                print("Subtract =", num1 - num2)
            case 3:
                print("Multiplication =", num1 * num2)
            case 4:
                print("Division =", num1 / num2)
            case 5:
                print("Saindo...")
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
    except ValueError as e:
        print(f"Erro:{e}")



num1 = float(input(f'Difgite o primeiro número: '))
num2 = float(input(f'Digite o segundo número: '))
operador = int(input(f'Escolha um operador para realizar sua operação(1: soma, 2: subtração, 3: multiplicação, 4: divisão, 5: sair): '))

calculadora(num1,num2,operador)