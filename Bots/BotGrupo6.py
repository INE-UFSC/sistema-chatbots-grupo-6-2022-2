from Bots.Bot import Bot


class BotGrupo6(Bot):

  def __init__(self, nome):
    super().__init__(nome)

    boas_vindas = """Oi, tudo bem?
Bem-vindo ao chat!"""
    apresentacao = """Eu sou um bot personalizado do grupo 06, prazer em te conhecer!
Meu nome? Sou %s""" % self.nome
    despedida = "BBBBBBB"

    self.adicionar_comando(apresentacao, "apresentacao")
    self.adicionar_comando(boas_vindas, "boas-vindas")
    self.adicionar_comando(despedida, "despedida")

  def executa_comando(self, cmd):
    return self.comandos[cmd].executar()
