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

def main():
    lista_de_tarefas = ListaDeTarefas()

    while True:
        print("\nOpções:")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Concluir Tarefa")
        print("4. Imprimir Tarefas")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            lista_de_tarefas.adicionar_tarefa(tarefa)
        elif opcao == "2":
            indice = int(input("Digite o número da tarefa a remover: ")) - 1
            lista_de_tarefas.remover_tarefa(indice)
        elif opcao == "3":
            indice = int(input("Digite o número da tarefa a concluir: ")) - 1
            lista_de_tarefas.concluir_tarefa(indice)
        elif opcao == "4":
            lista_de_tarefas.imprimir_tarefas()
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()