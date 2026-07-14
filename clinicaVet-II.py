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
        for i, cliente in enumerate(self.clientes, start=1):
            print(f"{i} - {cliente.nome}")

        try:
            indice = int(input("Escolha: ")) - 1
        except ValueError:
            print("Digite apenas números.")
            return None

        if indice < 0 or indice >= len(self.clientes):
            print("Cliente inválido.")
            return None

        return self.clientes[indice]

    def selecionar_veterinario(self):
        if not self.veterinarios:
            print("\nNenhum veterinário cadastrado.")
            return None

        print("\nVeterinários:")
        for i, veterinario in enumerate(self.veterinarios, start=1):
            print(f"{i} - {veterinario.nome}")

        try:
            indice = int(input("Escolha: ")) - 1
        except ValueError:
            print("Digite apenas números.")
            return None

        if indice < 0 or indice >= len(self.veterinarios):
            print("Veterinário inválido.")
            return None

        return self.veterinarios[indice]

    def selecionar_animal(self):
        cliente = self.selecionar_cliente()

        if cliente is None:
            return None, None

        if not cliente.animais:
            print("\nEste cliente não possui animais.")
            return None, None

        print("\nAnimais:")
        for i, animal in enumerate(cliente.animais, start=1):
            print(f"{i} - {animal.nome}")

        try:
            indice = int(input("Escolha: ")) - 1
        except ValueError:
            print("Digite apenas números.")
            return None, None

        if indice < 0 or indice >= len(cliente.animais):
            print("Animal inválido.")
            return None, None

        return cliente, cliente.animais[indice]

    def selecionar_consulta(self):
        if not self.consultas:
            print("\nNenhuma consulta cadastrada.")
            return None

        print("\nConsultas:")
        for i, consulta in enumerate(self.consultas, start=1):
            print(
                f"{i} - {consulta.animal.nome} | "
                f"{consulta.data} | {consulta.status}"
            )

        try:
            indice = int(input("Escolha: ")) - 1
        except ValueError:
            print("Digite apenas números.")
            return None

        if indice < 0 or indice >= len(self.consultas):
            print("Consulta inválida.")
            return None

        return self.consultas[indice]

    # ======================================
    # CLIENTES
    # ======================================

    def cadastrar_cliente(self):
        print("\n=== Cadastro de Cliente ===")
        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        telefone = input("Telefone: ").strip()
        endereco = input("Endereço: ").strip()

        if not nome or not cpf:
            print("\nNome e CPF são obrigatórios.")
            return

        if any(cliente.cpf == cpf for cliente in self.clientes):
            print("\nJá existe um cliente com esse CPF.")
            return

        self.clientes.append(Cliente(nome, cpf, telefone, endereco))
        print("\nCliente cadastrado com sucesso!")

    def listar_clientes(self):
        if not self.clientes:
            print("\nNenhum cliente cadastrado.")
            return

        for cliente in self.clientes:
            print("\n----------------------------")
            cliente.mostrar_dados()

    def editar_cliente(self):
        cliente = self.selecionar_cliente()

        if cliente is None:
            return

        print("\nDeixe em branco para manter o valor.")
        nome = input(f"Nome ({cliente.nome}): ").strip()
        telefone = input(f"Telefone ({cliente.telefone}): ").strip()
        endereco = input(f"Endereço ({cliente.endereco}): ").strip()

        if nome:
            cliente.nome = nome
        if telefone:
            cliente.telefone = telefone
        if endereco:
            cliente.endereco = endereco

        print("\nCliente atualizado!")

    def excluir_cliente(self):
        cliente = self.selecionar_cliente()

        if cliente is None:
            return

        self.consultas = [
            consulta for consulta in self.consultas
            if consulta.cliente != cliente
        ]
        self.clientes.remove(cliente)
        print("\nCliente e consultas relacionadas removidos!")

    # ======================================
    # VETERINÁRIOS
    # ======================================

    def cadastrar_veterinario(self):
        print("\n=== Cadastro de Veterinário ===")
        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        telefone = input("Telefone: ").strip()
        crmv = input("CRMV: ").strip()
        especialidade = input("Especialidade: ").strip()

        if not nome or not crmv:
            print("\nNome e CRMV são obrigatórios.")
            return

        if any(veterinario.crmv == crmv for veterinario in self.veterinarios):
            print("\nJá existe um veterinário com esse CRMV.")
            return

        self.veterinarios.append(
            Veterinario(nome, cpf, telefone, crmv, especialidade)
        )
        print("\nVeterinário cadastrado com sucesso!")

    def listar_veterinarios(self):
        if not self.veterinarios:
            print("\nNenhum veterinário cadastrado.")
            return

        for veterinario in self.veterinarios:
            print("\n----------------------------")
            veterinario.mostrar_dados()

    def editar_veterinario(self):
        veterinario = self.selecionar_veterinario()

        if veterinario is None:
            return

        print("\nDeixe em branco para manter o valor.")
        nome = input(f"Nome ({veterinario.nome}): ").strip()
        telefone = input(f"Telefone ({veterinario.telefone}): ").strip()
        especialidade = input(
            f"Especialidade ({veterinario.especialidade}): "
        ).strip()

        if nome:
            veterinario.nome = nome
        if telefone:
            veterinario.telefone = telefone
        if especialidade:
            veterinario.especialidade = especialidade

        print("\nVeterinário atualizado!")

    def excluir_veterinario(self):
        veterinario = self.selecionar_veterinario()

        if veterinario is None:
            return

        self.consultas = [
            consulta for consulta in self.consultas
            if consulta.veterinario != veterinario
        ]
        self.veterinarios.remove(veterinario)
        print("\nVeterinário e consultas relacionadas removidos!")

    # ======================================
    # ANIMAIS
    # ======================================

    def cadastrar_animal(self):
        cliente = self.selecionar_cliente()

        if cliente is None:
            return

        print("\n=== Cadastro do Animal ===")
        nome = input("Nome: ").strip()

        try:
            idade = int(input("Idade: "))
            peso = float(input("Peso: ").replace(",", "."))
        except ValueError:
            print("Idade e peso devem ser números válidos.")
            return

        if idade < 0 or peso <= 0:
            print("Idade não pode ser negativa e peso deve ser maior que zero.")
            return

        raca = input("Raça: ").strip()

        print("\n1 - Cachorro")
        print("2 - Gato")
        tipo = input("Escolha: ").strip()

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
                print("\n----------------------------")
                print(f"Tutor: {cliente.nome}")
                animal.mostrar_dados()

        if not existe:
            print("\nNenhum animal cadastrado.")

    def editar_animal(self):
        _, animal = self.selecionar_animal()

        if animal is None:
            return

        print("\nDeixe em branco para manter o valor.")
        nome = input(f"Nome ({animal.nome}): ").strip()
        idade = input(f"Idade ({animal.idade}): ").strip()
        peso = input(f"Peso ({animal.peso}): ").strip()
        raca = input(f"Raça ({animal.raca}): ").strip()

        if nome:
            animal.nome = nome

        if idade:
            try:
                nova_idade = int(idade)
                if nova_idade < 0:
                    raise ValueError
                animal.idade = nova_idade
            except ValueError:
                print("Idade inválida. Alteração de idade ignorada.")

        if peso:
            try:
                novo_peso = float(peso.replace(",", "."))
                if novo_peso <= 0:
                    raise ValueError
                animal.peso = novo_peso
            except ValueError:
                print("Peso inválido. Alteração de peso ignorada.")

        if raca:
            animal.raca = raca

        print("\nAnimal atualizado!")

    def excluir_animal(self):
        cliente, animal = self.selecionar_animal()

        if animal is None:
            return

        self.consultas = [
            consulta for consulta in self.consultas
            if consulta.animal != animal
        ]
        cliente.remover_animal(animal)
        print("\nAnimal e consultas relacionadas removidos!")

    def testar_polimorfismo(self):
        existe = False
        print("\n=== Sons dos Animais ===")

        for cliente in self.clientes:
            for animal in cliente.animais:
                existe = True
                animal.emitir_som()

        if not existe:
            print("Nenhum animal cadastrado.")

    # ======================================
    # CONSULTAS
    # ======================================

    def agendar_consulta(self):
        cliente, animal = self.selecionar_animal()

        if animal is None:
            return

        veterinario = self.selecionar_veterinario()

        if veterinario is None:
            return

        print("\n=== Agendamento ===")
        data = input("Data: ").strip()
        motivo = input("Motivo: ").strip()

        if not data or not motivo:
            print("Data e motivo são obrigatórios.")
            return

        self.consultas.append(
            Consulta(cliente, animal, veterinario, data, motivo)
        )
        print("\nConsulta agendada com sucesso!")

    def listar_consultas(self):
        if not self.consultas:
            print("\nNenhuma consulta cadastrada.")
            return

        for i, consulta in enumerate(self.consultas, start=1):
            print(f"\nConsulta {i}")
            consulta.mostrar_dados()

    def editar_consulta(self):
        consulta = self.selecionar_consulta()

        if consulta is None:
            return

        print("\nDeixe em branco para manter o valor.")
        data = input(f"Data ({consulta.data}): ").strip()
        motivo = input(f"Motivo ({consulta.motivo}): ").strip()

        if data:
            consulta.data = data
        if motivo:
            consulta.motivo = motivo

        print("\nConsulta atualizada!")

    def cancelar_consulta(self):
        consulta = self.selecionar_consulta()

        if consulta is None:
            return

        consulta.cancelar()
        print("\nConsulta cancelada!")

    def concluir_consulta(self):
        consulta = self.selecionar_consulta()

        if consulta is None:
            return

        consulta.concluir()
        print("\nConsulta concluída!")

    # ======================================
    # RELATÓRIO GERAL
    # ======================================

    def relatorio(self):
        total_animais = sum(
            len(cliente.animais) for cliente in self.clientes
        )

        print("\n" + "=" * 50)
        print("RELATÓRIO GERAL DA CLÍNICA")
        print("=" * 50)
        print(f"\nClientes cadastrados: {len(self.clientes)}")
        print(f"Veterinários cadastrados: {len(self.veterinarios)}")
        print(f"Animais cadastrados: {total_animais}")
        print(f"Consultas cadastradas: {len(self.consultas)}")

        print("\n================ CLIENTES ================")
        if self.clientes:
            for cliente in self.clientes:
                print("\n----------------------------")
                cliente.mostrar_dados()
        else:
            print("Nenhum cliente cadastrado.")

        print("\n============== VETERINÁRIOS ==============")
        if self.veterinarios:
            for veterinario in self.veterinarios:
                print("\n----------------------------")
                veterinario.mostrar_dados()
        else:
            print("Nenhum veterinário cadastrado.")

        print("\n================ ANIMAIS =================")
        existe_animal = False
        for cliente in self.clientes:
            for animal in cliente.animais:
                existe_animal = True
                print("\n----------------------------")
                print(f"Tutor: {cliente.nome}")
                animal.mostrar_dados()

        if not existe_animal:
            print("Nenhum animal cadastrado.")

        print("\n=============== CONSULTAS ================")
        if self.consultas:
            for consulta in self.consultas:
                consulta.mostrar_dados()
        else:
            print("Nenhuma consulta cadastrada.")

        print("\n==========================================")
        print("Resumo Final")
        print("-" * 30)
        print(f"Clientes: {len(self.clientes)}")
        print(f"Veterinários: {len(self.veterinarios)}")
        print(f"Animais: {total_animais}")
        print(f"Consultas: {len(self.consultas)}")


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

        opcao = input("Escolha: ").strip()

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

        opcao = input("Escolha: ").strip()

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

        opcao = input("Escolha: ").strip()

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

        opcao = input("Escolha: ").strip()

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
    print("\n" + "=" * 45)
    print("            VETCARE")
    print(" Sistema de Clínica Veterinária")
    print("=" * 45)
    print("1 - Clientes")
    print("2 - Veterinários")
    print("3 - Animais")
    print("4 - Consultas")
    print("5 - Relatório Geral")
    print("0 - Sair")
    print("=" * 45)


# ==========================================
# FUNÇÃO PRINCIPAL
# ==========================================

def main():
    clinica = Clinica()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

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
