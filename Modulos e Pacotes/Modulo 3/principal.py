class ListaDeTarefas:
    def _init_(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append({"tarefa": tarefa, "concluida": False})

    def remover_tarefa(self, indice):
        try:
            del self.tarefas[indice]
        except IndexError:
            print("Índice inválido!")

    def concluir_tarefa(self, indice):
        try:
            self.tarefas[indice]["concluida"] = True
        except IndexError:
            print("Índice inválido!")

    def imprimir_tarefas(self):
        print("Lista de Tarefas:")
        for indice, tarefa in enumerate(self.tarefas):
            status = "Concluída" if tarefa["concluida"] else "Não Concluída"
            print(f"{indice + 1}. {tarefa['tarefa']} - {status}")

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

def calculadora(lista_de_tarefas):
    while True:
        print("\nOpções:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Voltar")

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
            resultado = somar(a, b)
            print(f"{a} + {b} = {resultado}")
            lista_de_tarefas.adicionar_tarefa(f"Calcular {a} + {b} = {resultado}")
        elif opcao == "2":
            resultado = subtrair(a, b)
            print(f"{a} - {b} = {resultado}")
            lista_de_tarefas.adicionar_tarefa(f"Calcular {a} - {b} = {resultado}")
        elif opcao == "3":
            resultado = multiplicar(a, b)
            print(f"{a} * {b} = {resultado}")
            lista_de_tarefas.adicionar_tarefa(f"Calcular {a} * {b} = {resultado}")
        elif opcao == "4":
            resultado = dividir(a, b)
            print(f"{a} / {b} = {resultado}")
            lista_de_tarefas.adicionar_tarefa(f"Calcular {a} / {b} = {resultado}")

def main():
    lista_de_tarefas = ListaDeTarefas()

    while True:
        print("\nOpções:")
        print("1. Gerenciar Tarefas")
        print("2. Calculadora")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                print("\nOpções:")
                print("1. Adicionar Tarefa")
                print("2. Remover Tarefa")
                print("3. Concluir Tarefa")
                print("4. Imprimir Tarefas")
                print("5. Voltar")

                opcao_tarefa = input("Escolha uma opção: ")

                if opcao_tarefa == "5":
                    break
                elif opcao_tarefa == "1":
                    tarefa = input("Digite a tarefa: ")
                    lista_de_tarefas.adicionar_tarefa(tarefa)
                elif opcao_tarefa == "2":
                    indice = int(input("Digite o número da tarefa a remover: ")) - 1
                    lista_de_tarefas.remover_tarefa(indice)
                elif opcao_tarefa == "3":
                    indice = int(input("Digite o número da tarefa a concluir: ")) - 1
                    lista_de_tarefas.concluir_tarefa(indice)
                elif opcao_tarefa == "4":
                    lista_de_tarefas.imprimir_tarefas()
                else:
                    print("Opção inválida!")

        elif opcao == "2":
            calculadora(lista_de_tarefas)

        elif opcao == "3":
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()