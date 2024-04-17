import random

def carregar_palavras():
    with open("palavras.txt", "r") as arquivo:
        return arquivo.read().splitlines()

def escolher_palavra(palavras):
    return random.choice(palavras)

def exibir_forca(erros):
    desenhos = [
        """
           _______
          |       |
          |       
          |       
          |       
          |       
        __|__
        """,
        """
           _______
          |       |
          |       O
          |       
          |       
          |       
        __|__
        """,
        """
           _______
          |       |
          |       O
          |       |
          |       
          |       
        __|__
        """,
        """
           _______
          |       |
          |       O
          |      /|
          |       
          |       
        __|__
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |       
          |       
        __|__
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |      / 
          |       
        __|__
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |      / \\
          |       
        __|__
        """
    ]
    print(desenhos[erros])

def jogar_forca():
    print("Bem-vindo ao jogo da forca!")
    palavras = carregar_palavras()
    palavra = escolher_palavra(palavras)
    letras_certas = []
    letras_erradas = []
    tentativas = 6
    
    while True:
        exibir_forca(len(letras_erradas))
        palavra_escondida = ''.join(letra if letra in letras_certas else '_' for letra in palavra)
        print(f'Palavra: {palavra_escondida}')
        print(f'Tentativas restantes: {tentativas}')
        print(f'Letras erradas: {", ".join(letras_erradas)}')
        
        if palavra_escondida == palavra:
            print('Parabéns! Você ganhou!')
            break
        
        if len(letras_erradas) == len(exibir_forca(0)):
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
