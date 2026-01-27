
print('Menu')

nomes = []

while True:

    Opções = input("1-Cadastrar, 2-Listar, 3-Sair: ")

    if Opções == '1':
        print('Cadastrar')
    elif Opções == '2':
        print('Listar')
    elif Opções == '3':
        print('Você saiu do sistema')
        break
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
        else:
            for nome in nomes:
                print(f' Nome Produto: {nome["nome"]}, Valor R$ {nome["Valor"]:.2f}')
    
        




