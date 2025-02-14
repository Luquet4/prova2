"""
5) Fibonacci Recursivo

Objetivo:
Crie uma função chamada fibonacci_recursivo(n) que calcule o n-ésimo termo da sequência de Fibonacci
de forma recursiva. Em seguida, crie outra função (por exemplo, mostrar_fibonacci(n)) que:
- Chame fibonacci_recursivo para obter o valor do n-ésimo termo.
- Exiba os termos de Fibonacci de 0 até n (ou seja, mostre o valor da função para cada índice, de 0 até n).

Observação:
- A sequência de Fibonacci é definida da seguinte forma:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2), para n >= 2
- Utilize um caso base na função recursiva (quando n < 2).
- Se desejar otimizar, você pode usar memoization, mas não é obrigatório.

Exemplo de Chamada:
    mostrar_fibonacci(5)
    # Saída esperada:
    # Fibonacci de 0 = 0
    # Fibonacci de 1 = 1
    # Fibonacci de 2 = 1
    # Fibonacci de 3 = 2
    # Fibonacci de 4 = 3
    # Fibonacci de 5 = 5

Requisitos:
- A função fibonacci_recursivo(n) deve utilizar recursão (sem laços).
- A função mostrar_fibonacci(n) deve exibir a sequência de termos de 0 até n.
- Utilize funções built-in onde necessário (por exemplo, conversão de entrada do usuário).
"""
    