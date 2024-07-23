from datetime import datetime

class Quarto:
    def __init__(self, numero, tipo, disponivel=True):
        self.numero = numero
        self.tipo = tipo
        self.disponivel = disponivel
    
    def __repr__(self):
        return f"Quarto {self.numero} ({self.tipo}) - {'Disponível' if self.disponivel else 'Ocupado'}"

class Reserva:
    def __init__(self, nome_hospede, quarto, check_in, check_out):
        self.nome_hospede = nome_hospede
        self.quarto = quarto
        self.check_in = check_in
        self.check_out = check_out
    
    def __repr__(self):
        return (f"Reserva para {self.nome_hospede} no {self.quarto.numero} de "
                f"{self.check_in.strftime('%d/%m/%Y')} a {self.check_out.strftime('%d/%m/%Y')}")

class Hotel:
    def __init__(self):
        self.quartos = []
        self.reservas = []
    
    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)
    
    def verificar_disponibilidade(self, tipo, check_in, check_out):
        disponiveis = []
        for quarto in self.quartos:
            if quarto.tipo == tipo and quarto.disponivel:
                disponivel = True
                for reserva in self.reservas:
                    if reserva.quarto == quarto:
                        if (check_in < reserva.check_out and check_out > reserva.check_in):
                            disponivel = False
                            break
                if disponivel:
                    disponiveis.append(quarto)
        return disponiveis
    
    def criar_reserva(self, nome_hospede, tipo, check_in, check_out):
        quartos_disponiveis = self.verificar_disponibilidade(tipo, check_in, check_out)
        if quartos_disponiveis:
            quarto = quartos_disponiveis[0]
            reserva = Reserva(nome_hospede, quarto, check_in, check_out)
            self.reservas.append(reserva)
            quarto.disponivel = False
            return reserva
        else:
            return None
    
    def cancelar_reserva(self, nome_hospede, quarto_numero):
        for reserva in self.reservas:
            if reserva.nome_hospede == nome_hospede and reserva.quarto.numero == quarto_numero:
                self.reservas.remove(reserva)
                reserva.quarto.disponivel = True
                return True
        return False

# Exemplos de uso:

# Criação do hotel
hotel = Hotel()

# Adição de quartos
hotel.adicionar_quarto(Quarto(101, 'simples'))
hotel.adicionar_quarto(Quarto(102, 'duplo'))
hotel.adicionar_quarto(Quarto(201, 'suíte'))

# Verificação de disponibilidade
check_in = datetime(2024, 7, 20)
check_out = datetime(2024, 7, 25)
disponiveis = hotel.verificar_disponibilidade('simples', check_in, check_out)
print("Quartos disponíveis:", disponiveis)

# Criação de uma reserva
reserva = hotel.criar_reserva('João Silva', 'simples', check_in, check_out)
print("Reserva criada:", reserva)

# Cancelamento de uma reserva
cancelada = hotel.cancelar_reserva('João Silva', 101)
print("Reserva cancelada:", cancelada)
