# 🍽️ Sistema de Estoque para Restaurantes

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-7C3AED?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-7C3AED?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-8B5CF6?style=for-the-badge&logo=sqlite&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-A78BFA?style=for-the-badge&logo=pytest&logoColor=white)

Sistema de controle de estoque para restaurantes, feito em Python, com cadastro de produtos, histórico de movimentações, controle de lotes e validade e regra **FEFO** (primeiro que vence, primeiro que sai).

> 🚧 **Projeto em desenvolvimento.** Estou construindo em etapas e o histórico de commits mostra a evolução. As funcionalidades abaixo estão marcadas conforme o andamento.

---

## 💜 Por que este projeto existe

Venho da **biomedicina**, onde lote, validade e rastreabilidade fazem parte da rotina do laboratório: saber o que entrou, o que saiu, quando vence e quem foi o responsável. Ao migrar para a área de tecnologia, quis transformar esse olhar em código. Um estoque de restaurante tem os mesmos problemas, e por isso escolhi esse tema para aprender Python, SQL e boas práticas de desenvolvimento.

---

## ✅ Funcionalidades

**Em andamento**
- [ ] Cadastro e listagem de produtos
- [ ] Registro de consumo sem deixar o estoque ficar negativo
- [ ] Aviso de estoque mínimo

**Planejadas**
- [ ] Entradas, saídas e ajustes com data, quantidade, motivo e responsável
- [ ] Testes automatizados com pytest
- [ ] Refatoração para programação orientada a objetos (`Produto`, `Lote`, `Movimentacao`, `Estoque`)
- [ ] Fornecedores, recebimentos e controle de lotes com validade
- [ ] Regra FEFO na saída de produtos
- [ ] Lista de lotes vencidos e próximos do vencimento
- [ ] Persistência de dados com SQLite
- [ ] Relatório de consumo com pandas

---

## 🗺️ Roadmap

| Etapa | O que será feito | Status |
|-------|------------------|--------|
| 1 | Lógica básica do estoque (listas, dicionários, funções) | 🔄 Em andamento |
| 2 | Regras, histórico de movimentações e testes | ⏳ Planejada |
| 3 | Refatoração para POO | ⏳ Planejada |
| 4 | Compras, lotes, validade e FEFO | ⏳ Planejada |
| 5 | Banco de dados SQLite | ⏳ Planejada |
| 6 | Relatórios e fechamento do projeto | ⏳ Planejada |

---

## 🚀 Como rodar

> Os comandos abaixo valem para a versão atual. Vou atualizá-los conforme a estrutura do projeto evoluir.

**Pré-requisitos:** [Python 3.10+](https://www.python.org/downloads/) e [Git](https://git-scm.com/).

```bash
# 1. Clonar o repositório
git clone COLE-AQUI-O-LINK-DO-REPOSITORIO
cd estoque-restaurante

# 2. Executar o programa
python estoque.py
```

---

## 🖥️ Exemplo de uso

> Substitua este trecho por um print ou pela saída real do seu terminal.

```text
=== ESTOQUE ===
1 - Cadastrar produto
2 - Listar produtos
3 - Sair

Escolha uma opção: 2

Arroz | quantidade: 10 | mínimo: 5
Feijão | quantidade: 4 | mínimo: 5
⚠️  Atenção: Feijão está abaixo do estoque mínimo!
```

---

## 🧪 Como rodar os testes

Os testes entram na Etapa 2. Quando estiverem prontos:

```bash
pip install pytest
pytest
```

---

## 📁 Estrutura planejada

```text
estoque-restaurante/
├── README.md
├── requirements.txt
├── src/
│   ├── modelos.py     # classes Produto, Lote, Movimentacao
│   ├── estoque.py     # regras de negócio
│   ├── banco.py       # acesso ao SQLite
│   └── main.py        # menu no terminal
├── tests/
│   └── test_estoque.py
└── .gitignore
```

A lógica fica separada do banco e da interface para que seja possível trocar o menu de terminal por uma API ou uma janela sem reescrever as regras.

---

## 📚 Decisões e aprendizados

*(Vou preencher conforme avançar. Exemplos do que registrar: o que foi mais difícil, o que mudaria, por que escolhi SQLite.)*

- ...

---

## 🔭 Próximos passos

Depois que o núcleo estiver estável, ideias para uma segunda versão:

- API de backend com FastAPI
- Alertas de estoque baixo e de validade por e-mail
- Interface visual

---

## 📫 Contato

**Gabriely Toledo**
[E-mail](mailto:gabrielytoledo98@gmail.com) · [GitHub](https://github.com/gabrielytoledo)

💜 Feito com carinho e muito aprendizado.
