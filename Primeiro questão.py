def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def verifica_fibonacci(numero):
    if fibonacci(numero):
        return f"O número {numero} pertence à sequência."
    else:
        return f"O número {numero} não pertence à sequência."

numero = int(input("Informe um número: "))
resultado = verifica_fibonacci(numero)
print(resultado)
