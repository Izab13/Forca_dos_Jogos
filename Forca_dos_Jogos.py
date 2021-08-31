import random

lista_palavras = ["final fantasy","fortnite","assassins creed","infamous","god of war","the last of us","watch dogs","resident evil","unravel","the witcher","detroit become human","hitman","uncharted","minecraft"]

def escolher_palavra():

  palavra = random.choice(lista_palavras)

  return palavra.upper()

def mostrar_palavra(palavra):

  palavra_listrada = "_" * len(palavra)
  adivinhou = False
  tentou_letras = []
  tentou_palavras = []
  tentativas = 6

  print("A Forca dos Jogos")
  print("Espaço tambem é válido")
  print("Você tem",tentativas,"tentativas")
  print(palavra_listrada)
  print("\n")

  while not adivinhou and tentativas > 0:

    letra = input("Digite uma letra: ").upper()

    if len(letra) == 1 :

      if letra in tentou_letras:

        print("Você já digitou a letra",letra)

      elif letra not in palavra:

        print(letra,"não está na palavra!")

        tentativas -= 1
        tentou_letras.append(letra)

      else:

        print(letra,"está na palavra!")

        tentou_letras.append(letra)
        palavra_em_lista = list(palavra_listrada)
        indices = [i for i, letter in enumerate(palavra) if letter == letra]

        for posicao in indices:

          palavra_em_lista[posicao] = letra
        palavra_listrada = "".join(palavra_em_lista)

        if "_"not in palavra_listrada:

          adivinhou = True
    else:

      print("Não é válido. Digite uma LETRA.")
    print("Você tem",tentativas,"tentativas")
    print(palavra_listrada)
    print("\n")

  if adivinhou:

    print("Voce acertou qual é o jogo!")

  else:

    print("Você perdeu!")

def iniciar_jogo():

  palavra = escolher_palavra()
  mostrar_palavra(palavra)

  while input("Jogar novamente? (S/N) ").upper() == "S":

    palavra = escolher_palavra()
    mostrar_palavra(palavra)

iniciar_jogo()
