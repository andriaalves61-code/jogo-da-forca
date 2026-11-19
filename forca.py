import randon

class JogoDaForca:
  def __init__(selff):
    self.palavras = ["python", "computador", "programacao", "algoritimo", "github", "teclado"]
    self.palavra_secreta = random.choice(self.palavras)
    self.letras_certas = []
    self.letras_erradas = []
    self.tentativas = 6

def mostrar_palavras(self):
  resultado = ""
  for letra in self.palavra_secreta:
    if letra in felf.letras_certas:
      resultado += letra + " "
    else:
      resultado += "_ "
  return resultado

def jogar(self):
  print("=== JOGO DA FORCA ===") 
  while self.tentativas > 0:
    print(f"\nPalavras: {self.mostrar_palavras()}")
    print(f"Tentativas: {self.tentativas}")
    print(f"Erradas: {self.letras_erradas}")
    letra = input("Digite uma letra: ").lower()
    if letra in self.palavra_secreta:
      self.letras_certas.append(letra)
    else:
      self.letras_erradas.append(letra)
      self.temtativas -= 1
    ganhou = True
    for 1 in self.palavra_secreta:
      if 1 not in self.letras_certas:
        ganhou = False
    if ganhou:
      print(f"Parabens! Palavra: {self.palavra_secreta}")
      return
  print(f"Voce perdeu! Palavra era: {sel.palavra_secreta}")

jogo = JogoDaForca()
jogo.jogar()
    
