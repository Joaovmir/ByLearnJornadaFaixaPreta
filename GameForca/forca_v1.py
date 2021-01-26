import random

tabuleiro = ["""
 +---+
 |   |
     |
     |
     |
     |
 =========
""","""
 +---+
 |   |
 o   |
     |
     |
     |
 =========
""","""
 +---+
 |   |
 o   |
 |   |
     |
     |
 =========
""","""
 +---+
 |   |
 o   |
/|   |
     |
     |
 =========
""","""
 +---+
 |   |
 o   |
/|\  |
     |
     |
 =========
""","""
 +---+
 |   |
 o   |
/|\  |
/    |
     |
 =========
""","""
 +---+
 |   |
 o   |
/|\  |
/ \  |
     |
 =========
"""]

class Forca():

    def __init__(self, word):
        self.word = word
        self.escondida = '_' * len(self.word)
        self.erros = 0
        self.erradas = []
        self.certas = []

    def guess(self, letter):
        if letter in self.word:
            self.certas.append(letter)
        else:
            self.erradas.append(letter)
            self.erros += 1

    def hangman_over(self):
        if self.erros == 6 or self.hangman_won():
            return True
        return False

    def hangman_won(self):
        if '_' not in self.escondida:
            return True
        return False

    def hide_word(self):
        lista = []
        for letra in self.escondida:
            lista.append(letra)
        for letra in self.certas:
            for i in range(len(self.word)):
                if letra == self.word[i]:
                    lista[i] = letra
        self.escondida = ''.join(lista)
        return self.escondida

    def print_game_status(self):

        print(tabuleiro[self.erros])
        print(f'\nPalavra: {self.hide_word()}')
        print(f'\nLetras erradas:')
        for letra in self.erradas:
            print(letra)
        print(f'\nLetras certas:')
        for letra in self.certas:
            print(letra)



def rand_word():
    with open("palavras.txt","rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

def main():

    game = Forca(rand_word())

    while game.hangman_over() == False:
        game.print_game_status()
        print()
        letter = input("Digite uma letra: ")
        game.guess(letter)

    if game.hangman_won():
            print('\nParabéns, você venceu!!')
    else:
        print('\nGame Over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você!')


if __name__ == "__main__":
    main()
