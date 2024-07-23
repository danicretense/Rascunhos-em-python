
class Curso:
    def __init__(self,nome,desc,aulas=[]):
        self.nome=nome
        self.desc=desc
        self.aulas=aulas
    
class Aulas:
    def __init__(self,titulo,desc,duracao):
        self.titulo=titulo
        self.desc=desc
        self.duracao=duracao
    
class Estudante:
    
    def __init__(self,nome,email,cursos=[]):
        self.nome=nome
        self.email=email
        self.cursos=cursos
          
class Main:
     def listar_aulas(self,curso):
        if curso.nome:
            print(f'Curso: {curso.nome}\nAulas: ')
            for aula in curso.aulas:
                print(aula)
     def listar_cursos(self,estudante):
         if estudante.email:
             print(f'Aluno: {estudante.nome}\nCursos em que você se inscreveu: \n')
             for curso in estudante.cursos:
              print(curso)  
     def inscrever_alunos(self,estudante,curso): 
         nome_curso=[curso.nome]
         estudante.cursos+=nome_curso
         
c1=Curso('Espanhol',"Curso de conversação na lingua espanhola",['Aula 01','Aula 02','Aula 03'])  
c2=Curso("Power BI","Curso avançado de Power BI",["Aula 4,","Aula 5"]) 
c3=Curso('Lógica de programação','Aprender resolver problemas simples com programação ',['Variaveis','estruturas de repetição','estruturas condicionais'])
c4=Curso('HTML&CSS',"Aprender estilizar páginas web",['aula 08','aula 15','aula 09'])
e1=Estudante('Tiago','tiago@hotmail.com',[c1.nome])
e2=Estudante('Daniel Lucas','dandan@gmail.com',[c1.nome,c3.nome])
e3=Estudante("Alice Gabriela",'gabi@yahoo.com',[c3.nome,c2.nome,c1.nome])
a1=Aulas(c1.aulas[0],"Aprender os tipos de variaveis e como usa-las",6.30)
a2=Aulas(c1.aulas[1],'Uso do for e do while',7.45)
a3=Aulas(c1.aulas[2],"Uso do 'if','else' e 'elif' ", 8.54)
principal=Main()
principal.listar_aulas(c3)
principal.inscrever_alunos(e1,c2)
principal.inscrever_alunos(e1,c4)
principal.listar_cursos(e1)
