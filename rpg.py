from abc import ABC, abstractmethod

#--------PERSONAGENS BONS
class Personagem(ABC):
    def __init__(self, nome):
        self._nome = nome
        self._vida = 100
        self._moedas = 0
        self._ataque = 10
        self._nivel = 1

    def esquivar(self):
        print(f"{self._nome} esquivou!")

    def subir_nivel(self):
        self._nivel += 1
        self._ataque += 5
        print(f"{self._nome} subiu de nível!\nNível atual: {self._nivel}")

    @abstractmethod
    def acao_especial(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)

    def usar_espada(self):
        print(f"{self._nome} usou a espada!")

    def acao_especial(self):
        self.usar_espada()
     
class Curandeiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)

    def curar(self, alvo):
        alvo._vida += 10
        print(f"{self._nome} curou {alvo._nome}!")

    def acao_especial(self):
        print(f"{self._nome} usou cura especial!")
        self._vida += 20

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)

    def atirar_flecha(self):
        self._moedas += 40
        print(f'{self._nome} O Arqueiro atirou uma flecha e ganhou {self._moedas} moedas')

    def acao_especial(self):
        self.atirar_flecha()

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)

    def soltar_poder(self, personagem):
        personagem._moedas += 12
        print(f'{self._nome} soltou um poder e {personagem._nome} ganhou {personagem._moedas} moedas')

    def acao_especial(self):
        print(f"{self._nome} usou magia especial!")
        self._ataque += 10

#--------VILÕES
class Inimigo(ABC):
    def __init__(self, nome, forca):
        self._nome = nome
        self._forca = forca

    def atacar(self, personagem):
        personagem._moedas -= 15
        print(f'{self._nome} atacou e {personagem._nome} perdeu 15 moedas')

    @abstractmethod
    def acao_especial(self):
        pass

class Caveira(Inimigo):
    def __init__(self, nome, forca):
        super().__init__(nome, forca)

    def matar(self, personagem):
        personagem._vida -= 30
        self._forca += 30
        print(f'{self._nome} matou {personagem._nome} e agora está com {self._forca} de força e {personagem._vida} de vida')

    def acao_especial(self):
        print(f'{self._nome} usou ataque mortal!')
        self._forca += 50

class Clow(Inimigo):
    def __init__(self, nome, forca):
        super().__init__(nome, forca)

    def cuspir_fogo(self, personagem):
        personagem._vida -= 5
        print(f'{self._nome} cuspiu fogo e {personagem._nome} perdeu 5 de vida')

    def acao_especial(self):
        print(f'{self._nome} cuspiu fogo especial!')
        self._forca += 20

# CRIAÇÃO DOS OBJETOS------------------------------------->
kain = Guerreiro("Kain")
mei = Curandeiro("Mei")
arq1 = Arqueiro('Pedro')
kain._vida -= 20
mig1 = Caveira('Mig1', 300)
clow = Clow('Gloob', 100)
guto = Mago('Guto')
def ataque_duplo(guerreiro,arqueiro):
    mig1._forca-=100
    clow._forca-=50
    guerreiro._nivel+=2
    arqueiro._nivel+=2
    print(f"Que ataque incrivel!!!! agora {guerreiro._nome} esta no nível:{guerreiro._nivel} e o arqueiro esta no nível: {arqueiro._nivel}")
# EXEMPLO DE USO-------------------------------------->
arq1.atirar_flecha()
clow.atacar(arq1)
guto.soltar_poder(arq1)
clow.cuspir_fogo(kain)
mig1.matar(kain)
print(kain._vida)
print(f'guto está no nivel: {guto._nivel}')

# Usando acao_especial para demonstrar polimorfismo
personagens = [kain, mei, arq1, guto]
inimigos = [mig1, clow]

for personagem in personagens:
    personagem.acao_especial()

for inimigo in inimigos:
    inimigo.acao_especial()

ataque_duplo(kain,arq1)

