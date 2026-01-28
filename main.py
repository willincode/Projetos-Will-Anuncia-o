
print('Menu')

nomes = []

while True:

    Opções = input("1-Cadastrar, 2-Listar, 3-Sair, 4-Remover: ")

    if Opções == '1':
        print('Cadastrar')
    elif Opções == '2':
        print('Listar')
    elif Opções == '3':
        print('Você saiu do sistema')
        break
    elif Opções == '4':
        print('Qual código deseja remover?')
    else:
        print("Escolha uma opção válida")

       
    if Opções == "1":
        produto = input('Nome Produto: ').strip()
        if produto == "":
            print("O nome digitado não foi aceito")
            continue
        try:
            valor = (input('Valor Produto: '))
            valor_txt = valor.replace(",",".")
            valor_txt = float(valor_txt)
            nomes.append({"nome": produto, "Valor": valor_txt})
        except ValueError:
            print('Você digiotu um número inválido, tente novamente')
            continue
    
    if Opções == "2":
        if len(nomes) == 0:
            print("Nenhum produto cadastrado!")
        
    if Opções == "4":
        if len(nomes) == 0:
            print('Você não digitou nenhuma informação')
            continue

        for numero, produto in enumerate(nomes, start=1):
            print(f'{numero}) {produto["nome"]} - R$ {produto["Valor"]:.2f}')

        numero = input('Informe o código do produto: ')

        if not numero.isdigit():
            print('Opção inválida, digite um número!')
            continue

        numero = int(numero)
        
            
        if numero < 1 or numero > len(nomes):
                print("Opção inválida: número fora da lista")
                
        else: 
             removido = nomes.pop(numero - 1)
             print(f'Removido: {removido["nome"]}')
             continue
    else:
        for nome in nomes:
            print(f' Nome Produto: {nome["nome"]}, Valor R$ {nome["Valor"]:.2f}')
    
        




