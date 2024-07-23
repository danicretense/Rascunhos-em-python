class Curso:
    def __init__(self, nome, desc, aulas=None):
        self.nome = nome
        self.desc = desc
        self.aulas = aulas if aulas is not None else []

    def __repr__(self):
        return f"Curso(nome='{self.nome}')"

class Aula:
    def __init__(self, titulo, desc, duracao):
        self.titulo = titulo
        self.desc = desc
        self.duracao = duracao

    def __repr__(self):
        return f"{self.titulo} - {self.duracao} min"

class Estudante:
    def __init__(self, nome, email, cursos=None):
        self.nome = nome
        self.email = email
        self.cursos = cursos if cursos is not None else []

    def __repr__(self):
        return f"Estudante(nome='{self.nome}', email='{self.email}')"

class Main:
    def listar_aulas(self, curso):
        if curso.nome:
            print(f'Curso: {curso.nome}\nAulas:')
            for aula in curso.aulas:
                print(aula)
    
    def listar_cursos(self, estudante):
        if estudante.email:
            print(f'Aluno: {estudante.nome}\nCursos em que você se inscreveu:')
            for curso in estudante.cursos:
                print(f"- {curso.nome}")

    def inscrever_alunos(self, estudante, curso): 
        estudante.cursos.append(curso)

# Criando aulas
a1 = Aula("Aula 01", "Aprender os tipos de variáveis e como usá-las", 6.30)
a2 = Aula("Aula 02", 'Uso do for e do while', 7.45)
a3 = Aula("Aula 03", "Uso do 'if', 'else' e 'elif'", 8.54)

# Criando cursos
c1 = Curso('Espanhol', "Curso de conversação na língua espanhola", [a1, a2, a3])
c2 = Curso("Power BI", "Curso avançado de Power BI", [Aula("Aula 04", "Descrição da Aula 04", 60), Aula("Aula 05", "Descrição da Aula 05", 75)])
c3 = Curso('Lógica de programação', 'Aprender resolver problemas simples com programação', [Aula("Variáveis", "Descrição da Aula 1", 45), Aula("Estruturas de repetição", "Descrição da Aula 2", 60), Aula("Estruturas condicionais", "Descrição da Aula 3", 50)])
c4 = Curso('HTML&CSS', "Aprender a estilizar páginas web", [Aula("Aula 08", "Descrição da Aula 8", 40), Aula("Aula 15", "Descrição da Aula 15", 50), Aula("Aula 09", "Descrição da Aula 9", 55)])

# Criando estudantes
e1 = Estudante('Tiago', 'tiago@hotmail.com', [c1])
e2 = Estudante('Daniel Lucas', 'dandan@gmail.com', [c1, c3])
e3 = Estudante("Alice Gabriela", 'gabi@yahoo.com', [c3, c2, c1])

# Inicializando a classe principal
principal = Main()

# Listando aulas de um curso
principal.listar_aulas(c3)

# Inscrevendo alunos em cursos
principal.inscrever_alunos(e1, c2)
principal.inscrever_alunos(e1, c4)

# Listando cursos inscritos por um estudante
principal.listar_cursos(e1)
