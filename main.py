#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste
from Bots.BotGrupo6 import BotGrupo6

lista_bots = [BotFeliz("feliz"), BotZangado("zangado"), BotTriste("triste"), BotGrupo6("personalizado")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()

