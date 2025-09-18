# Escreva uma função que recebe uma lista de palavras e devolve a palavra mais longa.


def solution(lista):
    maior_palavra = None
    for palavra_atual in lista:
        tamanho_palavra_atual = len(palavra_atual)

        if maior_palavra is None:
            maior_palavra = palavra_atual
            continue
        
        if tamanho_palavra_atual > len(maior_palavra):
            maior_palavra = palavra_atual

    return maior_palavra


lista_palavras = ['laranja', 'carro', 'computador', 'casa', 'moto', 'linguagem', 'RPG', 'sapo', 'unicelulares']
maior_palavra = solution(lista_palavras)
print("A maior palavra da lista é:", maior_palavra)