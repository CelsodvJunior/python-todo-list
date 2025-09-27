import uteis

lista_de_tarefas = uteis.carregar_tarefas()
print(uteis.titulo("To-Do List").upper)
opcao = 0
while opcao != 5:
    print(
        """
    Escolha uma opção:
    1 - Adicionar tarefa
    2 - Visualisar tarefas
    3 - Marcar tarefa como lida
    4 - Sair
    """
    )
    opcao = int(input("Entre com a opção desejada: "))

    if opcao == 1:
        print(uteis.linhas())
        msg = uteis.add_tarefa(lista_de_tarefas)
        uteis.salvar_tarefas(lista_de_tarefas)
        print(msg)
        print(uteis.linhas())

    elif opcao == 2:
        print(uteis.linhas())
        print(uteis.visualisar_tarefas(lista_de_tarefas))
        print(uteis.linhas())

    elif opcao == 3:
        print(uteis.linhas())
        print(uteis.marcar_como_lida(lista_de_tarefas))
        print(uteis.linhas())
    elif opcao == 4:
        print(uteis.linhas())
        print(uteis.sair())
        print(uteis.linhas())
    else:
        print("Opção inválida...")
