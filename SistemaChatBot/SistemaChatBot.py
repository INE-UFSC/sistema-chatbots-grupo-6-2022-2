from Bots.Bot import Bot
from Bots import Bot

class SistemaChatBot:
    def __init__(self, nomeEmpresa: str, lista_bots: list):
        self.__empresa=nomeEmpresa
        self.__lista_bots = lista_bots
        self.__bot = None
    
    def boas_vindas_sistema(self):
        print (f"""AOBA! Seja bem-vindo ao melhor sistema de chatbots, segundo a própria empresa {self.__empresa}""")

    def mostra_menu(self):
        print('---------------------------')
        print('Os bots disponíveis são:')
        for i in range (len(self.__lista_bots)):
          print(f'{i+1} - {self.__lista_bots[i].nome}:', end = ' ')
          print(f'{self.__lista_bots[i].executa_comando(0)}')
          
      ##mostra o menu de escolha de bots
 
    def escolhe_bot(self):
      
      while True:
        escolha_do_usuario = int(input("Digite o número do chatbot desejado:"))
        
        if 0 < escolha_do_usuario <= len(self.__lista_bots):
          self.__bot = self.__lista_bots[escolha_do_usuario - 1]
          break
  
        else:
          print('Opção inválida!')
      
    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())
        ##mostra os comandos disponíveis no bot escolhido
    
    def le_envia_comando(self, comando):
        print(self.__bot.executa_comando(comando))
      
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        self.boas_vindas_sistema()
      
        ##mostra o menu ao usuário
        self.mostra_menu()
      
        ##escolha do bot
        self.escolhe_bot()
      
        #BoasVindas
        self.le_envia_comando(1)
      
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        while True:
          self.mostra_comandos_bot()
          comando = int(input("Digite o número do comando (ou -1 para sair): "))

          if comando == -1:
            break

          if self.__bot.numero_comandos - 3 < comando or comando < 1:
            print("O número digitado não correponde a nenhum comando do bot")
          else:
            self.le_envia_comando(comando+2)

        #Despedida
        self.le_envia_comando(2)
        
        
