#ler arquivo TXT
class Texto(object): 
  def __init__(self, conteudo): 
    self.__conteudo = conteudo

  @property 
  def conteudo(self): 
    return self.__conteudo

  @nome.setter 
  def nome(self, conteudo): 
    self.__conteudo = conteudo

  def __repr__(self): 
    return "%s" % (self.__conteudo)

  def ler_produtos(arquivo):
    arquivo = 'arquivos/code.txt'

  def ler_produtos(arquivo):
    arquivo_aberto = open(arquivo, 'rb')



