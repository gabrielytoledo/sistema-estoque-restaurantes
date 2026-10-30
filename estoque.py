estoque = [
    {
        'nome': 'Arroz',
        'quantidade': 10,
        'estoque_minimo': 5,
    },
    {
        'nome': 'Feijão',
        'quantidade': 10,
        'estoque_minimo': 5,
    },
]


while True:
    print('===== SISTEMA DE ESTOQUE =====')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Registrar consumo')
    print('4 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '2':
        for produto in estoque:
            print(f'Nome: {produto["nome"]}')
            print(f'Quantidade: {produto["quantidade"]}')
            print(f'Estoque mínimo: {produto["estoque_minimo"]}')
            print()

    
    elif opcao == '3':
        for indice, produto in enumerate(estoque, start=1):
            print(indice, produto['nome'])
        escolha = int(input('Qual produto deseja selecionar? '))
        escolha = escolha - 1
        produto = estoque[escolha]
        print(produto['nome'])

        quantidade_produto_consumida = int(input('Qual a quantidade de produto que foi consumida? '))
    
        if quantidade_produto_consumida > produto["quantidade"]:
            print('Estoque insuficiente')
        else:
            produto["quantidade"] = produto["quantidade"] - quantidade_produto_consumida
            print('Consumo registrado!')
            if produto["quantidade"] <= produto["estoque_minimo"]:
                print(f'{produto["nome"]} está no estoque mínimo ou abaixo dele. Quantidade atual: {produto["quantidade"]}')
            
        

    elif opcao == '4':
        print('Saindo do sistema...')
        break