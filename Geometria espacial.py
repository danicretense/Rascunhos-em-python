class Cilindro:
    def __init__(self,r,h) :
        self.r=r
        self.h=h
    def calcula_volume(self,cilindro):
        quadrado=pow(cilindro.r,2)
        v=quadrado*cilindro.h
        print(f'{v}π')
    def area_total(self,cilindro) :
        dobro_raio= 2*cilindro.r
        at=dobro_raio*(cilindro.r+cilindro.h)  
        print(at)
    
class Esfera:
    def __init__(self,r):
          self.r=r
    def calcular_volume(self,esfera):
      passo1=pow(esfera.r,3)
      passo2=4*passo1
      passo3=passo2/3
      print(f'{passo3}π')
    def area_total(self,esfera):
        passo1=pow(esfera.r,2)
        passo2=4*passo1        
        print(f'{passo2}π')

ask=int(input("Qual forma você quer calcular?: \n1-Clindro\n2-Esfera"))
if ask==1:
    raio=int(input("Digite o valor do raio: "))
    altura=int(input("Digite o valor da altura: "))
    c1=Cilindro(raio,altura)
    p1=input("digite 'a' para area total ou 'v' para volume: " )
    if p1=="a":
        c1.area_total(c1)
    else:
        c1.calcula_volume(c1)
else:
    raio=int(input("Digite o valor do raio: "))
    e1=Esfera(raio)
    p2=input("Digite 'a' para calcular a area total ou 'v' para calcular o volume: ")
    if p2:
        e1.area_total(e1)
    else:
        e1.calcular_volume(e1)
