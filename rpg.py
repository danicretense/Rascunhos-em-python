
#--------PERSONAGENS BONS
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.moedas = 0
        self.ataque = 10
        self.nivel = 1
        
    def esquivar(self):
        print(f"{self.nome} esquivou!")
    
    def subir_nivel(self):
        self.nivel += 1
        self.ataque += 5
        print(f"{self.nome} subiu de nível!\nNível atual: {self.nivel}")
 
class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
    
    def usar_espada(self):
        print(f"{self.nome} usou a espada!")


class Curandeiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
    
    def curar(self, alvo:Personagem):
        alvo.vida += 10
        print(f"{self.nome} curou {alvo.nome}!")
class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome) 
    def atirar_flecha(self):
        self.moedas+=40
        print( f'{self.nome} O Arqueiro Atirou uma flecha! e ganhou {self.moedas} moedas') 
class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
    def soltar_poder(self,personagem):
        personagem.moedas+=12   
        
        
   #-------- VILÕES                        
class Inimigo:
    def __init__(self,nome,forca):
        self.nome=nome
        self.forca=forca
    def atacar(self,personagem):
        personagem.moedas-=15
class Caveira(Inimigo):
    def __init__(self, nome, forca):
        super().__init__(nome, forca)
    def matar(self,personagem) :
      personagem.vida-=30
      self.forca+=30
      print(f'{self.nome} matou: {personagem.nome} e ele agora está com {personagem.vida} vidas!!!')   
class Clow(Inimigo):
    def __init__(self, nome, forca):
        super().__init__(nome, forca)
    def cuspir_fogo(self,personagem):
        personagem.vida-=5 
        
        
#CRIAÇÃO DOS OBJETOS------------------------------------->                
kain = Guerreiro("Kain")
mei = Curandeiro("Mei")
arq1=Arqueiro('Pedro')
kain.vida -= 20
mig1=Caveira('Mig1',300)
clow=Clow('Gloob',100)
guto=Mago('Guto')

#EXEMPLO DE USO-------------------------------------->
arq1.atirar_flecha()
clow.atacar(arq1)
#print(arq1.moedas)
guto.soltar_poder(arq1)
clow.cuspir_fogo(kain)
mig1.matar(kain)
print(kain.vida)
print(f'guto está mo nivel: {guto.nivel}')