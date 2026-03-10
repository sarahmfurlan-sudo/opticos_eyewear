from funcoes_estoque import (
    cadastrar_produto,
    listar_produtos,
    atualizar_estoque,
    remover_produto,
    verificar_estoque_baixo,
    salvar_produtos,
    carregar_produtos,
    buscar_produto_codigo,
    gerar_relatorio
)

NOME_ARQUIVO = "produtos.txt"


def exibir_menu():
    print("\n==============================")
    print("      OPTICOS EYEWEAR")
    print(" SISTEMA DE GESTÃO DE ESTOQUE")
    print("==============================")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar estoque")
    print("4 - Remover produto")
    print("5 - Verificar estoque baixo")
    print("6 - Buscar produto")
    print("7 - Gerar relatório")
    print("8 - Salvar produtos")
    print("9 - Sair")


def main():
    lista_produtos = carregar_produtos(NOME_ARQUIVO)

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                cadastrar_produto(lista_produtos)

            elif opcao == 2:
                listar_produtos(lista_produtos)

            elif opcao == 3:
                atualizar_estoque(lista_produtos)

            elif opcao == 4:
                remover_produto(lista_produtos)

            elif opcao == 5:
                verificar_estoque_baixo(lista_produtos)

            elif opcao == 6:
                buscar_produto_codigo(lista_produtos)

            elif opcao == 7:
                gerar_relatorio(lista_produtos)

            elif opcao == 8:
                salvar_produtos(lista_produtos, NOME_ARQUIVO)

            elif opcao == 9:
                salvar_produtos(lista_produtos, NOME_ARQUIVO)
                print("Sistema encerrado.")
                break

            else:
                print("Opção inválida.")

        except ValueError:
            print("Erro: digite um número válido.")


if __name__ == "__main__":
    main()