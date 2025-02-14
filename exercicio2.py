"""
2) Cadastro de Filmes

Objetivo:
Crie uma função chamada cadastrar_filmes() que simule um pequeno sistema de cadastro de filmes. Essa função deve:
- Utilizar uma tupla fixa chamada generos (por exemplo, ("Ação", "Comédia", "Drama", "Fantasia", "Terror")).
- Pedir ao usuário o título de 3 filmes e o índice do gênero (com base na tupla).
- Armazenar os dados em um dicionário, onde a chave é o título e o valor é o gênero (string).
- Ao final, exibir quantos filmes de cada gênero foram cadastrados.

Observação:
- Você pode usar uma lista para armazenar títulos antes de inseri-los no dicionário, mas não é obrigatório.
- A contagem de filmes por gênero pode ser feita percorrendo o dicionário ou usando outro dicionário auxiliar.

Exemplo de Chamada:
    cadastrar_filmes()
    # Durante a execução:
    # - O programa pede 3 filmes + índice do gênero
    # - Depois exibe quantos filmes de cada gênero foram cadastrados

Requisitos:
- Utilize ao menos uma tupla para gêneros.
- Armazene os filmes cadastrados em um dicionário.
- Exiba ao final um resumo da quantidade de filmes por gênero.
"""
# Solution:

def cadastrar_filmes():
    try:
        gen = ('Ação', 'Comédia', 'Drama', 'Fantasia', 'Terror')
        for i in range(len(gen)):
            print(f"{i} - {gen[i]}")
        dic_movies = {input("Digite o nome do filme: "): gen[int(input("Digite o Gênero do filme: "))] for _ in range(3)}
        print(dic_movies)
        result = list(dic_movies.values())
        for i in range(len(gen)):
            print(f"{gen[i]} - Quantidade de filmes: {result.count(gen[i])}")
    except Exception as e:
        print(e)

cadastrar_filmes()