# Escreva uma função que recebe uma lista de números e devolve o maior número.

def solution(lista):
    maior_numero = None
    for numero_atual in lista:

        if maior_numero is None:
            maior_numero = numero_atual
            continue 
    
        if numero_atual > maior_numero:
            maior_numero = numero_atual
    return maior_numero


lista = [4, 17, 52, 97, 24, 102,53, 48, 24, 91, 12]
resultado = solution(lista)
print(resultado)
