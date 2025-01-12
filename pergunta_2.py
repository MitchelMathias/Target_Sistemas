def pertence_a_fibonacci(n):
    a, b = 0, 1
    print("Cálculo da sequência de Fibonacci:")
    while a <= n:
        print(a, end=" ")
        if a == n:
            print()
            return f"O número {n} pertence à sequência de Fibonacci."
        a, b = b, a + b
    print()
    return f"O número {n} não pertence à sequência de Fibonacci."

# Teste
numero = int(input("Informe um número: "))
print(pertence_a_fibonacci(numero))
