"""
3) Gerar Relatório (parâmetros opcionais e *args)

Objetivo:
Crie uma função chamada gerar_relatorio(*valores, titulo="Relatório Geral", subtitulo="Valores") que receba:
- Uma quantidade variável de números em *valores.
- Dois parâmetros opcionais titulo e subtitulo, com valores-padrão fornecidos.

A função deve:
1. Exibir o titulo e o subtitulo.
2. Calcular e exibir:
   - A soma de todos os valores.
   - A média dos valores.
   - O valor máximo e o valor mínimo.

Observação:
- Utilize funções built-in como sum(), max() e min().
- Se não houver valores em *valores, trate esse caso (por exemplo, exiba mensagem que não há valores).

Exemplo de Chamada:
    gerar_relatorio(10, 20, 30)
    gerar_relatorio(1.5, 2.5, 3.5, 4.5, titulo="Relatório Personalizado", subtitulo="Métricas Financeiras")

    # Exemplo de saída:
    # ====== Relatório Geral ======
    # Subtítulo: Valores
    # Soma: 60
    # Média: 20.0
    # Máximo: 30
    # Mínimo: 10
    # ----------------------------

Requisitos:
- Use parâmetros opcionais (titulo, subtitulo) e *args.
- Faça uso de funções built-in para facilitar a soma e a busca de maior/menor valor.
- Mostre os resultados de forma organizada.
"""
# Solution:

def gerar_relatorio(*args, titulo="Relatório Geral", subtitulo="Valores"):
    try:
        if not args:
            print("Não foi passado valores!")
        else:
            print(f"Bem vindo ao {titulo} e {subtitulo}")
            print("\n====== Relatório Geral ======")
            print(f"Subtítulo: {subtitulo}")
            print(f"Soma: {sum(args)}")
            print(f"Média: {round(sum(args) / len(args))}")
            print(f"Máximo: {max(args)}")
            print(f"Mínimo: {min(args)}")
            print("----------------------------")
    except Exception as e:
        print(e)

gerar_relatorio()