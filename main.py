import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'computador', 'jogo', 'desenvolvimento']
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = []
    letras_erradas = []
    tentativas = 6
    
    while True:
        palavra_escondida = ''.join(letra if letra in letras_certas else '_' for letra in palavra)
        print(f'Palavra: {palavra_escondida}')
        print(f'Tentativas restantes: {tentativas}')
        print(f'Letras erradas: {", ".join(letras_erradas)}')
        
        if palavra_escondida == palavra:
            print('Parabéns! Você ganhou!')
            break
        
        if tentativas == 0:
            print(f'Game over! A palavra era "{palavra}".')
            break
        
        letra = input('Digite uma letra: ').lower()
        
        if letra in letras_certas or letra in letras_erradas:
            print('Você já tentou esta letra. Tente novamente.')
            continue
        
        if letra in palavra:
            print('Letra correta!')
            letras_certas.append(letra)
        else:
            print('Letra errada!')
            letras_erradas.append(letra)
            tentativas -= 1

jogar_forca()
