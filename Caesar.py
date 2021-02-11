"""
Práctica 1 - Fundamentos de Criptografía
Script del Cifrado de Sustitución César
Cipher Caesar
@author: Rafael Contín
"""

import string

texto_original = input("Digite la palabra o frase que quiere cifrar: ").lower()

while True:
    try:
        desplazamiento = int(input("Digite el número de posiciones a desplazar la palabra o frase: "))
        break
    except ValueError:
        print("Digite solo números enteros")

alfabeto = list(string.ascii_lowercase)

def cifradoCesar(original,desplazo,alfabeto):
    texto_cifrado = ''
    for i in original:
        while True:
            try:
                posicion = (alfabeto.index(i) + desplazo) % 26
                texto_cifrado += alfabeto[posicion]
                break
            except ValueError:
                texto_cifrado += i
                break

    return texto_cifrado

texto_cifrado = cifradoCesar(texto_original,desplazamiento,alfabeto)
print('La palabra o frase cifrada es:',texto_cifrado)
