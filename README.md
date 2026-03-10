# OPTICOS EYEWEAR

## Sistema de Gestão de Estoque

Este projeto foi desenvolvido com o objetivo de criar um sistema simples de gestão de estoque para uma ótica em processo de migração para o ambiente online. O sistema permite cadastrar, listar, buscar, atualizar e remover produtos, além de gerar relatórios e salvar os dados em arquivo.

## Objetivo do projeto

O sistema foi criado para facilitar o controle de produtos de uma loja, permitindo uma organização mais prática do estoque e auxiliando no gerenciamento das informações dos itens cadastrados.

## Funcionalidades

- Cadastrar novos produtos
- Listar todos os produtos cadastrados
- Buscar produto pelo código
- Atualizar quantidade em estoque
- Remover produtos
- Verificar produtos com estoque baixo
- Gerar relatório do estoque
- Salvar os dados em arquivo
- Carregar automaticamente os produtos salvos ao iniciar o sistema

## Estrutura do projeto

### `main.py`
Arquivo principal do sistema. É responsável por exibir o menu, receber as opções do usuário e chamar as funções do sistema.

### `produto.py`
Arquivo que contém a classe `Produto`, com os atributos e métodos necessários para representar cada produto cadastrado.

### `funcoes_estoque.py`
Arquivo responsável pelas funções do sistema, como cadastro, listagem, busca, atualização de estoque, remoção, salvamento em arquivo e geração de relatório.

### `produtos.txt`
Arquivo usado para armazenar os dados dos produtos cadastrados no sistema.

## Dados de cada produto

Cada produto possui as seguintes informações:

- Nome do produto
- Código do produto
- Categoria
- Quantidade em estoque
- Preço
- Fornecedor
- Descrição

## Tecnologias e conceitos utilizados

- Python
- Variáveis
- Listas
- Estruturas condicionais
- Laços de repetição
- Funções
- Programação Orientada a Objetos
- Manipulação de arquivos
- Tratamento de exceções

## Como executar o projeto

1. Abra a pasta do projeto no terminal
2. Execute o arquivo principal com o comando:

```bash
python main.py

## Integrantes do grupo

Claudio Alves - RM:568565 Sara Furlan - RM: 556764 Rodrigo Wolkoff - RM: 856980 Luna Rousseau - RM: 564215 Turma: 1TIAPR

