from Bots.Bot import Bot


class BotInteligente(Bot):

  def __init__(self, nome):
    super().__init__(nome)

    boas_vindas = "Bem-vindo buscador da chama. Pronto para aprender sobre as maravilhas do universo?"
    apresentacao = "Olá, meu nome é {self.nome}, detentor de todo o conhecimento existente"
    despedida = "Espero que essa conversa tenha sido tão proveitosa para você quanto foi para mim. Adeus, buscador da chama"

    self.adicionar_comando(apresentacao, "apresentacao")
    self.adicionar_comando(boas_vindas, "boas-vindas")
    self.adicionar_comando(despedida, "despedida")

  def executa_comando(self, cmd):
    return self.comandos[cmd].executar()