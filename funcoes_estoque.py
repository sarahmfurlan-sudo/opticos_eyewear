# Guarda funções como: cadastrar, listar produtos, buscar produto,
# remover produto, salvar em arquivo e carregar do arquivo

from produto import Produto


def cadastrar_produto(lista_produtos):
    try:
        nome = input("Digite o nome do produto: ")
        codigo = input("Digite o código do produto: ")
        categoria = input("Digite a categoria: ")
        quantidade = int(input("Digite a quantidade em estoque: "))
        preco = float(input("Digite o preço do produto: "))
        fornecedor = input("Digite o fornecedor: ")
        descricao = input("Digite a descrição do produto: ")

        if quantidade < 0 or preco < 0:
            print("Erro: quantidade e preço devem ser maiores ou iguais a zero.")
            return

        produto_existente = buscar_produto(lista_produtos, codigo)
        if produto_existente is not None:
            print("Erro: já existe um produto com esse código.")
            return

        novo_produto = Produto(
            nome, codigo, categoria, quantidade, preco, fornecedor, descricao
        )
        lista_produtos.append(novo_produto)
        print("Produto cadastrado com sucesso!")

    except ValueError:
        print("Erro: quantidade ou preço inválido. Tente novamente.")


def listar_produtos(lista_produtos):
    if len(lista_produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\n===== LISTA DE PRODUTOS =====")
        for produto in lista_produtos:
            produto.exibir_dados()


def buscar_produto(lista_produtos, codigo):
    for produto in lista_produtos:
        if produto.codigo == codigo:
            return produto
    return None


def atualizar_estoque(lista_produtos):
    codigo = input("Digite o código do produto: ")
    produto = buscar_produto(lista_produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    print("1 - Adicionar ao estoque")
    print("2 - Remover do estoque")

    try:
        opcao = int(input("Escolha uma opção: "))
        quantidade = int(input("Digite a quantidade: "))

        if quantidade < 0:
            print("Erro: a quantidade não pode ser negativa.")
            return

        if opcao == 1:
            produto.adicionar_estoque(quantidade)
            print("Estoque atualizado com sucesso!")

        elif opcao == 2:
            if produto.remover_estoque(quantidade):
                print("Estoque atualizado com sucesso!")
            else:
                print("Erro: quantidade insuficiente em estoque.")

        else:
            print("Opção inválida.")

    except ValueError:
        print("Erro: digite valores numéricos válidos.")


def remover_produto(lista_produtos):
    codigo = input("Digite o código do produto que deseja remover: ")
    produto = buscar_produto(lista_produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
    else:
        lista_produtos.remove(produto)
        print("Produto removido com sucesso!")


def verificar_estoque_baixo(lista_produtos):
    encontrou = False

    for produto in lista_produtos:
        if produto.quantidade <= 3:
            if not encontrou:
                print("\n===== ALERTA DE ESTOQUE BAIXO =====")
            produto.exibir_dados()
            encontrou = True

    if not encontrou:
        print("Nenhum produto com estoque baixo.")


def salvar_produtos(lista_produtos, nome_arquivo):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for produto in lista_produtos:
                arquivo.write(produto.to_string_arquivo())
        print("Produtos salvos com sucesso no arquivo.")
    except Exception as erro:
        print(f"Erro ao salvar produtos: {erro}")


def carregar_produtos(nome_arquivo):
    lista_produtos = []

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")

                if len(dados) == 7:
                    nome = dados[0]
                    codigo = dados[1]
                    categoria = dados[2]
                    quantidade = int(dados[3])
                    preco = float(dados[4])
                    fornecedor = dados[5]
                    descricao = dados[6]

                    produto = Produto(
                        nome, codigo, categoria, quantidade, preco, fornecedor, descricao
                    )
                    lista_produtos.append(produto)

    except FileNotFoundError:
        print("Arquivo de produtos ainda não existe. O sistema começará com estoque vazio.")

    return lista_produtos


def buscar_produto_codigo(lista_produtos):
    codigo = input("Digite o código do produto: ")
    produto = buscar_produto(lista_produtos, codigo)

    if produto is not None:
        print("\n===== PRODUTO ENCONTRADO =====")
        produto.exibir_dados()
    else:
        print("Produto não encontrado.")


def gerar_relatorio(lista_produtos):
    print("\n===== RELATÓRIO OPTICOS EYEWEAR =====")

    if not lista_produtos:
        print("Nenhum produto cadastrado.")
        return

    total_produtos = len(lista_produtos)
    valor_total = 0
    produto_mais_caro = lista_produtos[0]
    estoque_baixo = 0

    for produto in lista_produtos:
        valor_em_estoque = produto.preco * produto.quantidade
        valor_total += valor_em_estoque

        if produto.preco > produto_mais_caro.preco:
            produto_mais_caro = produto

        if produto.quantidade < 5:
            estoque_baixo += 1

        print(f"\nProduto: {produto.nome}")
        print(f"Quantidade: {produto.quantidade}")
        print(f"Valor em estoque: R$ {valor_em_estoque:.2f}")

    print("\n===== RESUMO =====")
    print(f"Total de produtos cadastrados: {total_produtos}")
    print(f"Valor total do estoque: R$ {valor_total:.2f}")
    print(f"Produto mais caro: {produto_mais_caro.nome}")
    print(f"Preço do produto mais caro: R$ {produto_mais_caro.preco:.2f}")
    print(f"Produtos com estoque baixo: {estoque_baixo}")