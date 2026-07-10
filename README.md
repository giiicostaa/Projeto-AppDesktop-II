# VetCare — Sistema de Clínica Veterinária (Nível 2)

## Descrição

O **VetCare** é um sistema de gerenciamento de clínica veterinária desenvolvido em Python utilizando os princípios da Programação Orientada a Objetos (POO).

Esta versão corresponde ao **Nível 2** da atividade, implementando os principais conceitos de orientação a objetos, além do gerenciamento de clientes, veterinários, animais e consultas por meio de um menu em modo texto.

---

## Funcionalidades

O sistema permite:

- Cadastrar clientes;
- Cadastrar veterinários;
- Cadastrar animais;
- Associar animais aos seus tutores;
- Agendar consultas;
- Listar clientes;
- Listar veterinários;
- Listar animais;
- Listar consultas;
- Concluir consultas;
- Testar o polimorfismo dos animais;
- Gerar um relatório geral da clínica.

---

## Conceitos de Programação Orientada a Objetos

### Classe Abstrata

O sistema utiliza duas classes abstratas:

- `Pessoa`
- `Animal`

Essas classes definem comportamentos que obrigatoriamente são implementados pelas subclasses.

### Herança

- `Cliente` herda de `Pessoa`;
- `Veterinario` herda de `Pessoa`;
- `Cachorro` herda de `Animal`;
- `Gato` herda de `Animal`.

### Polimorfismo

Cada animal implementa o método `emitir_som()` de maneira diferente.

Exemplos:

- Cachorro → "Au Au!"
- Gato → "Miau!"

### Associação

A classe `Consulta` relaciona:

- Cliente
- Animal
- Veterinário

### Composição

A classe `Clinica` é responsável por gerenciar as coleções de:

- clientes;
- veterinários;
- consultas.

### Dependência

A classe `Clinica` cria e utiliza objetos das demais classes para realizar todas as operações do sistema.

---

## Estrutura das classes

```text
Pessoa (Classe Abstrata)
├── Cliente
└── Veterinario

Animal (Classe Abstrata)
├── Cachorro
└── Gato

Consulta

Clinica
```

---

## Menu do sistema

```
1 - Cadastrar Cliente
2 - Cadastrar Veterinário
3 - Cadastrar Animal
4 - Agendar Consulta
5 - Listar Clientes
6 - Listar Veterinários
7 - Listar Animais
8 - Listar Consultas
9 - Concluir Consulta
10 - Testar Sons dos Animais
11 - Relatório Geral
0 - Sair
```

---

## Fluxo recomendado

1. Cadastre um cliente.
2. Cadastre um veterinário.
3. Cadastre um animal para um cliente.
4. Agende uma consulta.
5. Liste os dados cadastrados.
6. Conclua uma consulta.
7. Gere o relatório.
8. Teste o polimorfismo.

---

## Limitações da versão Nível 2

- Os dados são armazenados apenas em memória.
- Ao fechar o programa, todas as informações são perdidas.
- Não utiliza banco de dados nem interface gráfica.

---

## Autor

Projeto acadêmico desenvolvido para demonstrar os conceitos de Programação Orientada a Objetos em Python realizado pelas alunas: Giovanna da Costa Santos (251021303)
e Geovana Duarte de Carvalho (251021241).
