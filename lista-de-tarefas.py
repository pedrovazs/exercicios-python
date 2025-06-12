listaTarefas = []

def menu():
    print('===== MENU =====')
    print('1. Adicionar Tarefa')
    print('2. Listar Tarefas')
    print('3. Remover Tarefa')
    print('4. Sair')
    print('===============\n')

while True:
    menu()
    try:
        opcao = int(input('Digite a opção desejada: '))
    except ValueError:
        print("Por favor, digite um número válido.\n")
        continue

    if opcao == 1:
        tarefa = input("\nDigite sua tarefa: ")
        listaTarefas.append(tarefa)
        print("Tarefa adicionada!\n")

    elif opcao == 2:
        if not listaTarefas:
            print("\nNenhuma tarefa cadastrada.\n")
        else:
            print("\nTarefas:")
            for i, tarefa in enumerate(listaTarefas):
                print(f'{i}. {tarefa}')
            print()

    elif opcao == 3:
        if not listaTarefas:
            print("\nNenhuma tarefa para remover.\n")
            continue

        print("\nTarefas:")
        for i, tarefa in enumerate(listaTarefas):
            print(f'{i}. {tarefa}')
        print()

        try:
            remover = int(input('Digite o índice da tarefa a ser removida: '))
            if 0 <= remover < len(listaTarefas):
                tarefa_removida = listaTarefas.pop(remover)
                print(f'Tarefa "{tarefa_removida}" removida!\n')
            else:
                print("Índice inválido.\n")
        except ValueError:
            print("Digite um número válido.\n")

    elif opcao == 4:
        print("Programa Finalizado! Obrigado!")
        break

    else:
        print("Opção inválida. Tente novamente.\n")
