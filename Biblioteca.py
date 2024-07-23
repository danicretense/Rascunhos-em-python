#----Objeto Livro
class Livro:
    def __init__(self, titulo, autor, n_copias):
        self.titulo = titulo
        self.autor = autor
        self.n_copias = n_copias

#----Classe que gerencia livros
class Biblioteca:
    def __init__(self):
        self.lista_livros = []

    def adiciona_livros(self, livro):
        self.lista_livros.append(livro)
        
    def ver_lista(self):
        for livro in self.lista_livros:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Número de Cópias: {livro.n_copias}")
    
    def remover_livro(self, livro):
        if livro in self.lista_livros:
            self.lista_livros.remove(livro)
        else:
            print("Livro não encontrado na biblioteca.")
        
    def emprestar_livro(self, livro):
        if livro in self.lista_livros and livro.n_copias > 0:
            livro.n_copias -= 1
            print(f"Livro '{livro.titulo}' emprestado. Cópias restantes: {livro.n_copias}")
        else:
            print("Livro não disponível para empréstimo.")
        
    def devolver_livro(self, livro):
        
        if livro in self.lista_livros:
            livro.n_copias += 1
            print(f"Livro '{livro.titulo}' devolvido. Cópias disponíveis: {livro.n_copias}")
        else:
            print("Este livro não pertence à biblioteca.")

# Criação dos objetos Livro
l1 = Livro('O pequeno príncipe', 'João Fernandes', 30)
l2 = Livro('Eu nos declaro marido e marido', 'Gael', 50)
l3 = Livro('O menino no espelho', 'Fernando Sabino', 20)
l4 = Livro('Minha história', 'Daniela Silva', 10)

# Criação do objeto Biblioteca e adição dos livros
biblioteca = Biblioteca()
biblioteca.adiciona_livros(l1)
biblioteca.adiciona_livros(l2)
biblioteca.adiciona_livros(l3)
biblioteca.adiciona_livros(l4)

# Empréstimo de um livro
biblioteca.emprestar_livro(l3)
biblioteca.devolver_livro(l3)
# Visualização da lista de livros
biblioteca.ver_lista()
