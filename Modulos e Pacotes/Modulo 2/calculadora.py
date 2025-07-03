def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

def calculadora():
    while True:
        print("\nOpções:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            break
        elif opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida!")
            continue

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Valor inválido!")
            continue

        if opcao == "1":
            print(f"{a} + {b} = {somar(a, b)}")
        elif opcao == "2":
            print(f"{a} - {b} = {subtrair(a, b)}")
        elif opcao == "3":
            print(f"{a} * {b} = {multiplicar(a, b)}")
        elif opcao == "4":
            print(f"{a} / {b} = {dividir(a, b)}")

if __name__ == "__main__":
    calculadora()