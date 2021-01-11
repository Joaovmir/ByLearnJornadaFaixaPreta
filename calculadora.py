print("------------------------ Calculadora ------------------------")
print("\n")
sair = "0"

while sair != "s":
    print("Escolha uma operação para continuar:\n")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Exponenciação")
    
    print("\n")
    
    op = int(input("Digite uma opção válida: 1/2/3/4/5: "))
    
    if op in [1,2,3,4,5]:
        print("\n")
        valor1 = float(input("Digite o primeiro valor: "))
        print("\n")
        valor2 = float(input("Digite o segundo valor: "))
        print("\n")

        if op == 1:
            res = valor1 + valor2
            print(f"{valor1} + {valor2} = {res}")
        elif op == 2:
            res = valor1 - valor2
            print(f"{valor1} - {valor2} = {res}")
        elif op == 3:
            res = valor1 * valor2
            print(f"{valor1} * {valor2} = {res}")
        elif op == 4:
            if valor2 == 0:
                print("Denominador deve ser diferente de 0.")
            else:
                res = valor1 / valor2
                print(f"{valor1} / {valor2} = {res}")
        elif op == 5:
            res = valor1 ** valor2
            print(f"{valor1} ^ {valor2} = {res}")
    else:
        print("\n")
        print("Operação escolhida é inválida")
    print("\n")
    sair = input("Digite 's' para sair, digite outra tecla para continuar na calculadora: ")
    print("\n")
    print("\n")
