##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r
from Bots.Comando import Comando


class Bot(ABC):
  
  def __init__(self, nome,):
    self.__nome = nome
    self.__primeiro_cmd = True
    self.__numero_comandos = 0
    self.__comandos = []
    self.__comandos_string = ""
  
  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  def mostra_comandos(self):
    return self.__comandos_string
    
  def adicionar_comando(self, texto, chave):
    cmd = Comando(texto, chave)
    self.__comandos.append(cmd)
    self.__numero_comandos += 1
    if self.__numero_comandos < 4:
      pass
    else:
      if self.__primeiro_cmd:
        self.__comandos_string += "%d - %s" % (self.__numero_comandos - 3, chave)
        self.__primeiro_cmd = False
      else:
        self.__comandos_string += """\n%d - %s""" % (self.__numero_comandos,
                                                     chave)

  @abstractmethod
  def executa_comando(self, cmd):
    pass

  @property
  def comandos(self):
    return self.__comandos

  @property
  def numero_comandos(self):
    return self.__numero_comandos
  