import sys


def titulo(msg):
    msg = f"======={msg}=====".upper()
    return msg


def linhas():
    return "-" * 20


def add_tarefa(lista_de_tarefa):
    descricao = input("Entre com sua tarefa: ")
    if descricao.strip() != "":
        nova_tarefa = {"descrição": descricao, "status": False}
        lista_de_tarefa.append(nova_tarefa)
        msg = "Tarefa adicionada com sucesso!!!"
    else:
        msg = "O campo de tarefa não pode ser vazio..."

    return msg


def visualisar_tarefas(lista_de_tarefa):
    if len(lista_de_tarefa) != 0:
        mensagens = []
        for item in lista_de_tarefa:
            linha = item["descrição"]
            if item["status"] is True:
                linha += "  [x]"
            else:
                linha += "  [ ]"
            mensagens.append(linha)
        msg = "\n".join(mensagens)
    else:
        msg = "Não há tarefas"

    return msg


def marcar_como_lida(lista_de_tarefa):
    if len(lista_de_tarefa) == 0:
        return "Não há tarefas"

    # Exibe tarefas numeradas
    tarefas = []
    for item in lista_de_tarefa:
        linha = item["descrição"]
        if item["status"] is True:
            linha += "  [x]"
        else:
            linha += "  [ ]"
        tarefas.append(linha)
    print("Tarefas:")
    print("\n".join([f"{i + 1}. {tarefa}" for i, tarefa in enumerate(tarefas)]))

    try:
        opcao = int(input("Escolha o número da tarefa para marcar como concluída: "))
    except ValueError:
        return "Opção inválida. Digite um número."

    if 1 <= opcao <= len(lista_de_tarefa):
        lista_de_tarefa[opcao - 1]["status"] = True
        # Exibe lista atualizada
        tarefas = []
        for item in lista_de_tarefa:
            linha = item["descrição"]
            if item["status"] is True:
                linha += "  [x]"
            else:
                linha += "  [ ]"
            tarefas.append(linha)
        print("\nLista atualizada:")
        print("\n".join([f"{i + 1}. {tarefa}" for i, tarefa in enumerate(tarefas)]))
        return f'Tarefa "{lista_de_tarefa[opcao - 1]["descrição"]}" marcada como concluída.'
    else:
        return "Opção inválida."


def sair():
    print("Saindo do programa...")
    sys.exit()
    pass
