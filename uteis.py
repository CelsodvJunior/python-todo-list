import json
import os


def titulo(msg):
    """Retorna o título formatado em maiúsculas e com sinais de igual ao redor."""
    msg = f"======={msg}=====".upper()
    return msg


def linhas():
    """Retorna uma linha de separação."""
    return "-" * 20


arquivo_json = "tarefas.json"


def carregar_tarefas():
    try:
        if not os.path.exists(arquivo_json):
            return []
        with open(arquivo_json, "r") as tarefas:
            return json.load(tarefas)
    except FileNotFoundError as error:
        return f"Arquivo não encontrado! Error: {error}"


def salvar_tarefas(lista_de_tarefa):
    with open(arquivo_json, "w") as tarefas:
        json.dump(lista_de_tarefa, tarefas, indent=4)


def add_tarefa(lista_de_tarefa):
    """Adiciona uma nova tarefa à lista de tarefas."""
    descricao = input("Entre com sua tarefa: ")
    if descricao.strip() != "":
        nova_tarefa = {"descrição": descricao, "status": False}
        lista_de_tarefa.append(nova_tarefa)
        msg = "Tarefa adicionada com sucesso!!!"
    else:
        msg = "O campo de tarefa não pode ser vazio..."

    salvar_tarefas(lista_de_tarefa)

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
    """Marca uma tarefa como lida na lista de tarefas."""
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
    """Sai do programa."""
    print("Saindo do programa...")
    sys.exit()
    pass
