#  Sistema de Estoque para Restaurantes

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-7C3AED?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-7C3AED?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-8B5CF6?style=for-the-badge&logo=sqlite&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-A78BFA?style=for-the-badge&logo=pytest&logoColor=white)

Sistema de Estoque para Restaurantes

Programa de terminal em Python para controlar o estoque de um restaurante: cadastrar produtos, ver o que tem, registrar o que foi consumido e receber um aviso quando algum item chega no mínimo.

Projeto em desenvolvimento. Estou construindo por etapas e usando o histórico de commits para registrar a evolução.

Por que fiz

Venho da biomedicina e sempre quis trabalhar com tecnologia. Gosto de computador desde criança e o que mais me atrai é poder criar um programa que resolva um problema do dia a dia e tire o trabalho repetitivo das mãos de alguém. Escolhi estoque de restaurante porque me deparei com uma situação onde um conhecido teve problemas no gerenciamento do estoque do seu estabelecimento. Vi essa situação como uma oportunidade para desenvolver meu conhecimento e pôr em prática meu aprenndizado. 

O que ele faz hoje
Cadastra produtos com nome, quantidade e estoque mínimo
Lista os produtos cadastrados
Registra o consumo de um produto e atualiza a quantidade
Impede consumir mais do que existe em estoque
Avisa quando a quantidade chega no estoque mínimo ou fica abaixo dele
Valida as entradas: letras no lugar de números, valores zero ou negativos, produto que não existe na lista, nome vazio e nome repetido
Como rodar

Precisa do Python 3 instalado.

bash
git clone https://github.com/gabrielytoledo/sistema-estoque-restaurantes.git
cd sistema-estoque-restaurantes
python estoque.py
Exemplo de uso

O programa já começa com Arroz e Feijão cadastrados, 10 unidades de cada e mínimo de 5. Registrando o consumo de 6 de Arroz:

text
===== SISTEMA DE ESTOQUE =====
1 - Cadastrar produto
2 - Listar produtos
3 - Registrar consumo
4 - Sair
Escolha uma opção: 3
1 Arroz
2 Feijão
Qual produto deseja selecionar? 1
Arroz
Qual a quantidade de produto que foi consumida? 6
Consumo registrado!
Arroz está no estoque mínimo ou abaixo dele. Quantidade atual: 4
Limitações

Os dados ficam só na memória. Quando o programa fecha, o estoque volta ao começo. Isso vai mudar quando eu adicionar o banco de dados.

O que vem a seguir
Histórico de movimentações (entradas, saídas e ajustes, com data e motivo)
Testes automatizados com pytest
Reorganizar o código em classes
Controle de lotes e validade, com a regra FEFO (o lote que vence primeiro sai primeiro)
Salvar os dados em SQLite

##  Contato

**Gabriely Toledo**
[E-mail](mailto:gabrielytoledo98@gmail.com) · [GitHub](https://github.com/gabrielytoledo)

💜 Feito com carinho e muito aprendizado.
