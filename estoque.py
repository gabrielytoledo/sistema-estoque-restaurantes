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

    if opcao == '1':
        nome = input('Nome do produto: ').strip()
        if nome == '':
            print('Escreva um nome válido')
            continue

        produto_ja_existe = False
        for item in estoque:
            if item['nome'].lower() == nome.lower():
                produto_ja_existe = True

        if produto_ja_existe:
            print('Esse poduto já esta cadastrado')
            continue

        try:
            quantidade = int(input('Quantidade: '))
            if quantidade <= 0:
                print('Digite apenas numeros maiores que 0')
                continue
            estoque_minimo = int(input('Qual estoque minimo desejado? '))
            if estoque_minimo <= 0:
                print('Digite apenas numeros maiores que 0')
                continue
        except ValueError:
            print('Escreva apenas numeros válidos')  
            continue


        novo_produto = {
            'nome': nome,
            'quantidade': quantidade,
            'estoque_minimo': estoque_minimo,
        }
        estoque.append(novo_produto)
        print('Produto cadastrado!')

    elif opcao == '2':
        for produto in estoque:
            print(f'Nome: {produto["nome"]}')
            print(f'Quantidade: {produto["quantidade"]}')
            print(f'Estoque mínimo: {produto["estoque_minimo"]}')
            print()

    
    elif opcao == '3':
        for indice, produto in enumerate(estoque, start=1):
            print(indice, produto['nome'])

        try:
            escolha = int(input('Qual produto deseja selecionar? '))
        except ValueError:
            print('Selecione apenas numeros existentes na lista')
            continue
        escolha = escolha - 1

        if escolha < 0 or escolha >= len(estoque):
            print('Produto inexistente')
            continue
        produto = estoque[escolha]
        print(produto['nome'])

        try:
            quantidade_produto_consumida = int(input('Qual a quantidade de produto que foi consumida? '))
        except ValueError:
            print('Digite apenas numeros válidos')
            continue

        if quantidade_produto_consumida <= 0: 
            print('Digite apenas numeros maiores que 0')
            continue
        
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

    else:
        print('Opção inválida!')