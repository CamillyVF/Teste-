def verifLetra(string):
    string_lower = string.lower()  
    contagem = string_lower.count('a') 
    
    if contagem > 0:
        return f"A letra 'a' aparece {contagem} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."

texto = input("Informe uma string: ")
resultado = verifLetra(texto)
print(resultado)
