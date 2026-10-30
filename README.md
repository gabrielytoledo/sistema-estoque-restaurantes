# Sistema de Estoque para Restaurantes

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-7C3AED?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-7C3AED?style=for-the-badge&logo=python&logoColor=white)

## Sobre o projeto

Programa de terminal em Python para controlar o estoque de um restaurante: cadastrar produtos, consultar quantidades, registrar o que foi consumido e receber avisos quando algum item atinge o estoque mínimo.

Projeto em desenvolvimento. Estou construindo por etapas e utilizando o histórico de commits para registrar minha evolução.

## Por que fiz este projeto?

Venho da biomedicina e sempre quis trabalhar com tecnologia. Gosto de computadores desde criança e o que mais me atrai é poder criar programas que resolvam problemas do dia a dia e eliminem tarefas repetitivas.

Escolhi desenvolver um sistema de estoque para restaurantes depois de conhecer uma situação em que um estabelecimento enfrentava dificuldades no gerenciamento de seus produtos.

Vi nessa situação uma oportunidade de desenvolver meus conhecimentos e colocar em prática meu aprendizado.

## Funcionalidades atuais

- Cadastro de produtos com nome, quantidade e estoque mínimo.
- Listagem dos produtos cadastrados.
- Registro de consumo e atualização automática das quantidades.
- Impedimento de consumo superior à quantidade disponível.
- Avisos quando um produto atinge ou fica abaixo do estoque mínimo.
- Validação de entradas inválidas, como letras no lugar de números, valores zero ou negativos, produtos inexistentes, nomes vazios e nomes duplicados.

## Como executar

**Pré-requisito:** Python 3 instalado.

Clone o repositório:

```bash
git clone https://github.com/gabrielytoledo/sistema-estoque-restaurantes.git
```

Entre na pasta:

```bash
cd sistema-estoque-restaurantes
```

Execute o programa:

```bash
python estoque.py
```

## Exemplo de uso

O programa inicia com dois produtos cadastrados: Arroz e Feijão, ambos com 10 unidades e estoque mínimo de 5.

Ao registrar o consumo de 6 unidades de Arroz, o sistema apresenta:

```text
===== SISTEMA DE ESTOQUE =====
1 - Cadastrar produto
2 - Listar produtos
3 - Registrar consumo
4 - Sair

Escolha uma opção: 3

1 - Arroz
2 - Feijão

Qual produto deseja selecionar? 1

Arroz

Qual a quantidade de produto que foi consumida? 6

Consumo registrado!

Arroz está no estoque mínimo ou abaixo dele.
Quantidade atual: 4
```

## Limitações atuais

Atualmente, os dados ficam armazenados apenas na memória. Quando o programa é encerrado, o estoque volta aos valores iniciais.

Essa limitação será resolvida futuramente com a implementação de um banco de dados SQLite.

## Próximas implementações

- [ ] Histórico de movimentações (entradas, saídas e ajustes, com data e motivo).
- [ ] Testes automatizados com pytest.
- [ ] Reorganização do código utilizando classes.
- [ ] Controle de lotes e validade, utilizando a regra FEFO (First Expire, First Out).
- [ ] Persistência dos dados utilizando SQLite.

## Contato

**Gabriely Toledo**

- E-mail: [gabrielytoledo98@gmail.com](mailto:gabrielytoledo98@gmail.com)
- GitHub: [github.com/gabrielytoledo](https://github.com/gabrielytoledo)

---

*Projeto desenvolvido como parte da minha jornada de aprendizado em programação.* 💜
