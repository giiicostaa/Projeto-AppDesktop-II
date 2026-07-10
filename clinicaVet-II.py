from abc import ABC, abstractmethod


# ==========================================
# CLASSE ABSTRATA PESSOA
# ==========================================

class Pessoa(ABC):

    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    @abstractmethod
    def mostrar_dados(self):
        pass


# ==========================================
# CLIENTE
# ==========================================

class Cliente(Pessoa):

    def __init__(self, nome, cpf, telefone, endereco):
        super().__init__(nome, cpf, telefone)
        self.endereco = endereco
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def remover_animal(self, animal):
        if animal in self.animais:
            self.animais.remove(animal)

    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

        if self.animais:
            print("Animais:")
            for animal in self.animais:
                print(f" - {animal.nome}")
        else:
            print("Animais: Nenhum")


# ==========================================
# VETERINÁRIO
# ==========================================

class Veterinario(Pessoa):

    def __init__(self, nome, cpf, telefone, crmv, especialidade):
        super().__init__(nome, cpf, telefone)
        self.crmv = crmv
        self.especialidade = especialidade

    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
        print(f"CRMV: {self.crmv}")
        print(f"Especialidade: {self.especialidade}")


# ==========================================
# CLASSE ABSTRATA ANIMAL
# ==========================================

class Animal(ABC):

    def __init__(self, nome, idade, peso, raca):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.raca = raca

    @abstractmethod
    def emitir_som(self):
        pass

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Raça: {self.raca}")


# ==========================================
# CACHORRO
# ==========================================

class Cachorro(Animal):

    def emitir_som(self):
        print(f"{self.nome}: Au Au!")


# ==========================================
# GATO
# ==========================================

class Gato(Animal):

    def emitir_som(self):
        print(f"{self.nome}: Miau!")

# ==========================================
# CONSULTA (ASSOCIAÇÃO)
# ==========================================

class Consulta:

    def __init__(self, cliente, animal, veterinario, data, motivo):
        self.cliente = cliente
        self.animal = animal
        self.veterinario = veterinario
        self.data = data
        self.motivo = motivo
        self.status = "Agendada"

    def concluir(self):
        self.status = "Concluída"

    def cancelar(self):
        self.status = "Cancelada"

    def mostrar_dados(self):

        print("\n----------------------------")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Animal: {self.animal.nome}")
        print(f"Veterinário: {self.veterinario.nome}")
        print(f"Data: {self.data}")
        print(f"Motivo: {self.motivo}")
        print(f"Status: {self.status}")


# ==========================================
# CLÍNICA (COMPOSIÇÃO)
# ==========================================

class Clinica:

    def __init__(self):

        self.clientes = []
        self.veterinarios = []
        self.consultas = []

    # ======================================
    # MÉTODOS AUXILIARES
    # ======================================

    def selecionar_cliente(self):

        if not self.clientes:
            print("\nNenhum cliente cadastrado.")
            return None

        print("\nClientes:")

        for i, cliente in enumerate(self.clientes):
            print(f"{i+1} - {cliente.nome}")

        try:
            indice = int(input("Escolha: ")) - 1
            return self.clientes[indice]
        except:
            print("Opção inválida.")
            return None

    def selecionar_veterinario(self):

        if not self.veterinarios:
            print("\nNenhum veterinário cadastrado.")
            return None

        print("\nVeterinários:")

        for i, veterinario in enumerate(self.veterinarios):
            print(f"{i+1} - {veterinario.nome}")

        try:
            indice = int(input("Escolha: ")) - 1
            return self.veterinarios[indice]
        except:
            print("Opção inválida.")
            return None

    # ======================================
    # CLIENTES
    # ======================================

    def cadastrar_cliente(self):

        print("\n=== Cadastro de Cliente ===")

        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")

        self.clientes.append(
            Cliente(nome, cpf, telefone, endereco)
        )

        print("\nCliente cadastrado com sucesso!")

    def listar_clientes(self):

        if not self.clientes:
            print("\nNenhum cliente cadastrado.")
            return

        for cliente in self.clientes:
            cliente.mostrar_dados()

    # ======================================
    # VETERINÁRIOS
    # ======================================

    def cadastrar_veterinario(self):

        print("\n=== Cadastro de Veterinário ===")

        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        crmv = input("CRMV: ")
        especialidade = input("Especialidade: ")

        self.veterinarios.append(
            Veterinario(
                nome,
                cpf,
                telefone,
                crmv,
                especialidade
            )
        )

        print("\nVeterinário cadastrado com sucesso!")

    def listar_veterinarios(self):

        if not self.veterinarios:
            print("\nNenhum veterinário cadastrado.")
            return

        for veterinario in self.veterinarios:
            veterinario.mostrar_dados()

    # ======================================
    # ANIMAIS
    # ======================================

    def cadastrar_animal(self):

        cliente = self.selecionar_cliente()

        if cliente is None:
            return

        print("\n=== Cadastro do Animal ===")

        nome = input("Nome: ")

        try:
            idade = int(input("Idade: "))
            peso = float(input("Peso: "))
        except ValueError:
            print("Valores inválidos.")
            return

        raca = input("Raça: ")

        print("\n1 - Cachorro")
        print("2 - Gato")

        tipo = input("Escolha: ")

        if tipo == "1":
            animal = Cachorro(nome, idade, peso, raca)

        elif tipo == "2":
            animal = Gato(nome, idade, peso, raca)

        else:
            print("Tipo inválido.")
            return

        cliente.adicionar_animal(animal)

        print("\nAnimal cadastrado com sucesso!")

    def listar_animais(self):

        existe = False

        for cliente in self.clientes:

            for animal in cliente.animais:

                existe = True

                print(f"\nTutor: {cliente.nome}")
                animal.mostrar_dados()

        if not existe:
            print("\nNenhum animal cadastrado.")

    # ======================================
    # EDITAR CLIENTE
    # ======================================

    def editar_cliente(self):

        cliente = self.selecionar_cliente()

        if cliente is None:
            return

        print("\nDeixe em branco para manter o valor.")

        nome = input(f"Nome ({cliente.nome}): ")
        telefone = input(f"Telefone ({cliente.telefone}): ")
        endereco = input(f"Endereço ({cliente.endereco}): ")

        if nome:
            cliente.nome = nome

        if telefone:
            cliente.telefone = telefone

        if endereco:
            cliente.endereco = endereco

        print("\nCliente atualizado!")

    # ======================================
    # EXCLUIR CLIENTE
    # ======================================

    def excluir_cliente(self):

        cliente = self.selecionar_cliente()

        if cliente is None:
            return

        self.consultas = [
            c for c in self.consultas
            if c.cliente != cliente
        ]

        self.clientes.remove(cliente)

        print("\nCliente removido!")

    # ======================================
    # EDITAR VETERINÁRIO
    # ======================================

    def editar_veterinario(self):

        veterinario = self.selecionar_veterinario()

        if veterinario is None:
            return

        print("\nDeixe em branco para manter o valor.")

        nome = input(f"Nome ({veterinario.nome}): ")
        telefone = input(f"Telefone ({veterinario.telefone}): ")
        especialidade = input(
            f"Especialidade ({veterinario.especialidade}): "
        )

        if nome:
            veterinario.nome = nome

        if telefone:
            veterinario.telefone = telefone

        if especialidade:
            veterinario.especialidade = especialidade

        print("\nVeterinário atualizado!")

    # ======================================
    # EXCLUIR VETERINÁRIO
    # ======================================

    def excluir_veterinario(self):

        veterinario = self.selecionar_veterinario()

        if veterinario is None:
            return

        self.consultas = [
            c for c in self.consultas
            if c.veterinario != veterinario
        ]

        self.veterinarios.remove(veterinario)

        print("\nVeterinário removido!")

    # ======================================
    # SELECIONAR ANIMAL
    # ======================================

    def selecionar_animal(self):

        cliente = self.selecionar_cliente()

        if cliente is None:
            return None, None

        if not cliente.animais:

            print("\nEste cliente não possui animais.")
            return None, None

        print()

        for i, animal in enumerate(cliente.animais):

            print(f"{i+1} - {animal.nome}")

        try:

            indice = int(input("Escolha: ")) - 1

            return cliente, cliente.animais[indice]

        except:

            print("Animal inválido.")
            return None, None

    # ======================================
    # EDITAR ANIMAL
    # ======================================

    def editar_animal(self):

        cliente, animal = self.selecionar_animal()

        if animal is None:
            return

        print("\nDeixe vazio para manter.")

        nome = input(f"Nome ({animal.nome}): ")
        idade = input(f"Idade ({animal.idade}): ")
        peso = input(f"Peso ({animal.peso}): ")
        raca = input(f"Raça ({animal.raca}): ")

        if nome:
            animal.nome = nome

        if idade:
            animal.idade = int(idade)

        if peso:
            animal.peso = float(peso)

        if raca:
            animal.raca = raca

        print("\nAnimal atualizado!")

    # ======================================
    # EXCLUIR ANIMAL
    # ======================================

    def excluir_animal(self):

        cliente, animal = self.selecionar_animal()

        if animal is None:
            return

        self.consultas = [
            c for c in self.consultas
            if c.animal != animal
        ]

        cliente.remover_animal(animal)

        print("\nAnimal removido!")

# ==========================================
# SUBMENU DE CLIENTES
# ==========================================

def menu_clientes(clinica):

    while True:

        print("\n===== CLIENTES =====")
        print("1 - Cadastrar")
        print("2 - Editar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            clinica.cadastrar_cliente()

        elif opcao == "2":
            clinica.editar_cliente()

        elif opcao == "3":
            clinica.excluir_cliente()

        elif opcao == "4":
            clinica.listar_clientes()

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida.")


# ==========================================
# SUBMENU DE VETERINÁRIOS
# ==========================================

def menu_veterinarios(clinica):

    while True:

        print("\n===== VETERINÁRIOS =====")
        print("1 - Cadastrar")
        print("2 - Editar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            clinica.cadastrar_veterinario()

        elif opcao == "2":
            clinica.editar_veterinario()

        elif opcao == "3":
            clinica.excluir_veterinario()

        elif opcao == "4":
            clinica.listar_veterinarios()

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida.")


# ==========================================
# SUBMENU DE ANIMAIS
# ==========================================

def menu_animais(clinica):

    while True:

        print("\n===== ANIMAIS =====")
        print("1 - Cadastrar")
        print("2 - Editar")
        print("3 - Excluir")
        print("4 - Listar")
        print("5 - Testar sons")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            clinica.cadastrar_animal()

        elif opcao == "2":
            clinica.editar_animal()

        elif opcao == "3":
            clinica.excluir_animal()

        elif opcao == "4":
            clinica.listar_animais()

        elif opcao == "5":
            clinica.testar_polimorfismo()

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida.")


# ==========================================
# SUBMENU DE CONSULTAS
# ==========================================

def menu_consultas(clinica):

    while True:

        print("\n===== CONSULTAS =====")
        print("1 - Agendar")
        print("2 - Editar")
        print("3 - Cancelar")
        print("4 - Concluir")
        print("5 - Listar")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            clinica.agendar_consulta()

        elif opcao == "2":
            clinica.editar_consulta()

        elif opcao == "3":
            clinica.cancelar_consulta()

        elif opcao == "4":
            clinica.concluir_consulta()

        elif opcao == "5":
            clinica.listar_consultas()

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida.")


# ==========================================
# MENU PRINCIPAL
# ==========================================

def exibir_menu():

    print("\n")
    print("=" * 40)
    print("              VETCARE")
    print("   Sistema de Clínica Veterinária")
    print("=" * 40)

    print("1 - Clientes")
    print("2 - Veterinários")
    print("3 - Animais")
    print("4 - Consultas")
    print("5 - Relatório geral")
    print("0 - Sair")

    print("=" * 40)


# ==========================================
# FUNÇÃO PRINCIPAL
# ==========================================

def main():

    clinica = Clinica()

    while True:

        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes(clinica)

        elif opcao == "2":
            menu_veterinarios(clinica)

        elif opcao == "3":
            menu_animais(clinica)

        elif opcao == "4":
            menu_consultas(clinica)

        elif opcao == "5":
            clinica.relatorio()

        elif opcao == "0":
            print("\nObrigado por utilizar o VetCare!")
            print("Sistema encerrado.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


# ==========================================
# EXECUÇÃO
# ==========================================

if __name__ == "__main__":
    main()