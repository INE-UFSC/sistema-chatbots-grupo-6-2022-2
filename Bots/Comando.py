class Comando:  
  def __init__(self, texto: str, chave: str):
    self.__texto = texto
    
  def getTexto(self):
    return self.__texto

  def setTexto(self, texto):
    self.__texto = texto

  def executar(self):
    return self.__texto
    