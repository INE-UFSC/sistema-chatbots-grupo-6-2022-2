from Bots.Bot import Bot


class BotFeliz(Bot):
# testa esse bot agr, por favor
  def __init__(self, nome):
    super().__init__(nome)

    boas_vindas = """Bem-vindo ao chat!!!
Sobre o que quer conversar nesse maravilhoso dia???"""
    apresentacao = """Oi! Eu sou o bot feliz %s!
Estou animado hoje e pronto pra me divertir! ;)""" % self.nome
    despedida = """Tchau tchau!
Aproveite o resto do seu dia! Se divirta!"""
    
    self.adicionar_comando(apresentacao, "apresentacao")
    self.adicionar_comando(boas_vindas, "boas-vindas")
    self.adicionar_comando(despedida, "despedida")

  def executa_comando(self, cmd):
    return self.comandos[cmd].executar()

  # def incrementar_numero_comandos(self):
  #   self.__numero_comandos += 1
  
  # @property
  # def comandos(self):
  #   return self.__comandos
  
  # @property
  # def comandos_string(self):
  #   return self.__comandos_string

  # @property
  # def nome(self):
  #   return self.__nome