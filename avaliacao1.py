"""5 - Uma livraria quer controlar seu estoque usando um dicionário onde as chaves são os títulos dos livros e os valores são a quantidade 
disponível em estoque. Implemente um programa com as seguintes funcionalidades:
1. Adicionar um livro ao estoque: o usuário informa o título e a quantidade (se o livro já existir, some a quantidade nova à existente).
2. Remover unidades de um livro: o usuário informa o título e a quantidade a remover; o programa deve atualizar o estoque e avisar se o estoque 
ficar zerado ou se o livro não existir.
3. Consultar quantidade de um livro: o usuário digita o título e o programa mostra a quantidade disponível ou informa que o livro não está no estoque.
4. Mostrar todos os livros com suas quantidades ordenados alfabeticamente.
5. Sair

Avaliação 1

Neidiman e Sara
"""
#Função responsável por localizar um livro
def buscar_livro(estoque, titulo): #def serve para criar ou declarar uma função (Função é um bloco de código reutilizável)
    titulo_normalizado = titulo.casefold() #É um método usado em textos/strings para converter todas as letras em minúsculas de forma mais agressiva que o .lower()

    for livro in estoque: #Serve para passar por cada item de uma lista ou grupo de itens chamado estoque, guardando cada item temporariamente na variável
        if livro.casefold() == titulo_normalizado: #Para ignorar a diferença entre letras maiúsculas e minúsculas
            return livro

    return None

#Função responsável por adicionar livros ao estoque
def adicionar_livro(estoque):
    titulo = input("Digite o título do livro: ").strip() #Remover espaços/quebra de linha extras do início e do final de um texto

    if titulo == "":
        print("O título não pode ficar vazio.")
        return

    while True: #Loop (Será repetido até o comando para parar)
        try:
            quantidade = int(input("Digite a quantidade a adicionar: "))

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
            else:
                break

        except ValueError:
            print("Quantidade inválida. Digite um número inteiro.")

    livro_encontrado = buscar_livro(estoque, titulo)

    if livro_encontrado:
        estoque[livro_encontrado] += quantidade
    else:
        estoque[titulo] = quantidade

    print("Livro adicionado ao estoque com sucesso.")

#Função responsável por remover unidades de um livro
def remover_livro(estoque):
    titulo = input("Digite o título do livro: ").strip()

    if titulo == "":
        print("O título não pode ficar vazio.")
        return

    livro_encontrado = buscar_livro(estoque, titulo)

    if livro_encontrado is None:
        print("Livro não encontrado no estoque.")
        return

    while True:
        try:
            quantidade = int(input("Digite a quantidade a remover: "))

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")

            elif quantidade > estoque[livro_encontrado]:
                print("Quantidade maior que o estoque disponível.")

            else:
                break

        except ValueError:
            print("Quantidade inválida. Digite um número inteiro.")

    estoque[livro_encontrado] -= quantidade

    if estoque[livro_encontrado] == 0:
        print("O estoque deste livro ficou zerado.")
    else:
        print("Quantidade removida com sucesso.")

#Função responsável por consultar um livro
def consultar_livro(estoque):
    titulo = input("Digite o título do livro: ").strip()

    if titulo == "":
        print("O título não pode ficar vazio.")
        return

    livro_encontrado = buscar_livro(estoque, titulo)

    if livro_encontrado is None:
        print("Livro não encontrado no estoque.")
    else:
        print(
            f"{livro_encontrado}: "
            f"{estoque[livro_encontrado]} unidade(s)"
        )

#Função responsável por mostrar todo o estoque
def mostrar_estoque(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return

    print("\nEstoque da Livraria")

    for livro in sorted(estoque, key=str.lower): #Para ignorar a diferença entre letras maiúsculas e minúsculas
        print(f"{livro}: {estoque[livro]} unidade(s)")

#Função responsável por exibir o menu
def exibir_menu():
    print("\nLivraria Raposo's")
    print("1 - Adicionar Livro")
    print("2 - Remover Unidades")
    print("3 - Consultar Quantidade")
    print("4 - Mostrar todos os livros")
    print("5 - Sair")

#Dicionário que armazena o estoque
estoque = {}

#Menu principal
while True: 
    exibir_menu()
    opcao = input("Escolha uma Opção: ")

    if opcao == "1":
        adicionar_livro(estoque)

    elif opcao == "2":
        remover_livro(estoque)

    elif opcao == "3":
        consultar_livro(estoque)

    elif opcao == "4":
        mostrar_estoque(estoque)

    elif opcao == "5":
        print("Consulta Encerrada.")
        break

    else:
        print("Opção Inválida. Escolha uma opção de 1 a 5.")