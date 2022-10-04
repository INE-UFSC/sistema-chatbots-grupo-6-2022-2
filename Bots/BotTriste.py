from Bots.Bot import Bot


class BotTriste(Bot):

  def __init__(self, nome):

    super().__init__(nome)

    boas_vindas = """oi..."""
    apresentacao = """sde"""
    despedida = """adeus"""

    self.adicionar_comando(apresentacao, "apresentacao")
    self.adicionar_comando(boas_vindas, "boas-vindas")
    self.adicionar_comando(despedida, "despedida")

  def executa_comando(self, cmd):
    return self.comandos[cmd].executar()
