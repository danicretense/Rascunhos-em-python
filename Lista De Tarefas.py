from datetime import datetime

class Tarefa:
    def __init__(self, titulo, descricao, data_vencimento, status='pendente'):
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.status = status

    def __str__(self):
        return (f"Título: {self.titulo}\n"
                f"Descrição: {self.descricao}\n"
                f"Data de Vencimento: {self.data_vencimento.strftime('%d/%m/%Y')}\n"
                f"Status: {self.status}\n")

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, titulo):
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.titulo != titulo]

    def atualizar_tarefa(self, titulo, novo_titulo=None, nova_descricao=None, nova_data_vencimento=None, novo_status=None):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                if novo_titulo:
                    tarefa.titulo = novo_titulo
                if nova_descricao:
                    tarefa.descricao = nova_descricao
                if nova_data_vencimento:
                    tarefa.data_vencimento = nova_data_vencimento
                if novo_status:
                    tarefa.status = novo_status

    def listar_tarefas(self):
        for tarefa in self.tarefas:
            print(tarefa)

    def listar_tarefas_por_status(self, status):
        for tarefa in self.tarefas:
            if tarefa.status == status:
                print(tarefa)

# Exemplo de uso
tarefa1 = Tarefa("Comprar leite", "Comprar leite no mercado", datetime(2023, 7, 20), "pendente")
tarefa2 = Tarefa("Estudar Python", "Fazer exercícios de Python", datetime(2023, 7, 21), "em andamento")
tarefa3 = Tarefa("Limpar a casa", "Fazer a limpeza geral da casa", datetime(2023, 7, 22), "concluída")

lista = ListaDeTarefas()
lista.adicionar_tarefa(tarefa1)
lista.adicionar_tarefa(tarefa2)
lista.adicionar_tarefa(tarefa3)

#print("Todas as tarefas:")
#lista.listar_tarefas()

print("Tarefas pendentes:")
lista.listar_tarefas_por_status("pendente")
