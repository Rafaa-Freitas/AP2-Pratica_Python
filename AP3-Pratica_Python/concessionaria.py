from cliente import Cliente
from motocicletas import Motocicletas

def __main__():
    carrega_mensagem_inicial();

    primeira_escolha = int(input('\n1 - Clientes \n2 - Motos \n3 - Vendas\n4 - Encerrar\n\nO que deseja: '))
    print('\n')
    if (primeira_escolha == 1):
        print(f'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n'+12*' '+'Clientes\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        segunda_escolha = int(input('\n1 - Cadastrar Cliente \n2 - Buscar por Cliente \n3 - Atualizar dados do Cliente \n4 - Deletar Cliente\n\nDigite o que deseja: '))
        if(segunda_escolha == 1):
            nome = input('\nDigite um nome: ')
            endereco = input('\nDigite um endereço: ')
            telefone = input('\nDigite um telefone: ')
            criar_cliente(nome, endereco, telefone)

            recarregar()
        elif(segunda_escolha == 2):
            nome = input('Digite o nome do cliente para buscar os dados: ')
            buscar_cliente(nome)

            recomecar = (input('Deseja recomeçar? (S/N) ')).upper()
            if recomecar == 'S':
                recarregar()
            elif recomecar == 'N':
                carrega_mensagem_final()
            else:
                print('Valor incorreto!')
                recomecar = input('Deseja recomeçar? (S/N)')

        elif(segunda_escolha == 3):
            nome_antigo = input('Digite o nome do cliente que deve ser alterado: ')

            nome_novo = input('\nDigite um novo nome: ')
            endereco_novo = input('Digite um novo endereço: ')
            telefone_novo = input('Digite um novo telefone: ')
            alterar_cliente(nome_novo, endereco_novo, telefone_novo, nome_antigo)

            recarregar()
        elif(segunda_escolha == 4):
            nome = input('Digite o nome do cliente que deseja deletar: ')
            deletar_cliente(nome)

            recarregar()

    elif(primeira_escolha == 2):
        print(f'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n' + 10 * ' ' + 'Motocicletas\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        segunda_escolha = int(input('\n1 - Cadastrar Moto \n2 - Buscar por Moto \n3 - Atualizar dados da moto \n4 - Deletar Moto\n\nDigite o que deseja: '))
        if (segunda_escolha == 1):
            modelo = input('\nDigite um modelo: ')
            marca = input('Digite um marca: ')
            ano = input('Digite um ano: ')
            criar_moto(modelo, marca, ano)

            recarregar()
        elif (segunda_escolha == 2):
            modelo = input('Digite o modelo da moto para buscar os dados: ')
            buscar_moto(modelo)

            recomecar = (input('Deseja recomeçar? (S/N) ')).upper()
            if recomecar == 'S':
                recarregar()
            elif recomecar == 'N':
                carrega_mensagem_final()
            else:
                print('Valor incorreto!')
                recomecar = input('Deseja recomeçar? (S/N)')

        elif (segunda_escolha == 3):
            modelo_antigo = input('Digite o modelo da moto para alterar os dados: ')
            modelo_novo = input('Digite um novo modelo: ')
            marca_novo = input('Digite uma nova marca: ')
            ano_novo = input('Digite um novo ano: ')

            alterar_moto(modelo_novo, marca_novo, ano_novo, modelo_antigo)

            recarregar()
        elif (segunda_escolha == 4):
            modelo = input('Digite o modelo da moto que deseja deletar: ')
            deletar_moto(modelo)

            recarregar()

    elif(primeira_escolha == 3):
        print(f'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n' + 10 * ' ' + 'Vendas\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        escolha_vendas = int(input('\n1 - Vender moto \n2 - Buscar venda \n3 - Listar vendas \n4 - Sair\n\nDigite o que deseja: '))
        if (escolha_vendas == 1):
            cliente = input('Digite o nome do(a) cliente que irá comprar a moto: ')
            moto = input(f'Digite o modelo da moto que será vendida para o(a) cliente {cliente}: ')
            criar_venda(cliente, moto)


        if (escolha_vendas == 2):
            cliente = input('Digite o nome do(a) cliente que realizou a compra desejada: ')
            moto = input(f'Digite o modelo da moto que foi vendida para o cliente {cliente}: ')
            print('\n\n')
            buscar_venda(cliente, moto)

        if (escolha_vendas == 3):
            listar_vendas()

        if (escolha_vendas == 4):
            carrega_mensagem_final()

    elif((primeira_escolha == 4) or (segunda_escolha == 5)):
        carrega_mensagem_final()
    else:
        print('Opção inválida, recomece o sistema.')


            ############ CRUD DE CLIENTES ############

def criar_cliente(nome, endereco, telefone):
    cliente = Cliente(nome, endereco, telefone)

    arquivo = open("clientes.txt", "a", encoding="utf-8")
    arquivo.write(f'Nome: {cliente.nome}, Endereço: {cliente.endereco}, Telefone: {cliente.telefone}\n')
    arquivo.close()


def buscar_cliente(nome):
    arquivo = open("clientes.txt", "r", encoding="utf-8")
    for linha in arquivo:
        if nome in linha:
            print(linha)

def alterar_cliente(nome_novo, endereco_novo, telefone_novo, valor_antigo):
    with open("clientes.txt", 'r', encoding="utf-8") as f:
        texto = f.readlines()
    for i in texto:
        if valor_antigo in i:
            index_linha = texto.index(i)
            texto[index_linha] = (f'Nome: {nome_novo}, Endereço: {endereco_novo}, Telefone: {telefone_novo}\n')
        else:
            continue

    with open("clientes.txt", 'w+', encoding="utf-8") as f:
        f.writelines(texto)

def deletar_cliente(nome):
    with open("clientes.txt", 'r', encoding="utf-8") as f:
        texto = f.readlines()
    for i in texto:
        if nome in i:
            index_linha = texto.index(i)
            texto[index_linha] = ''
        else:
            continue

    with open("clientes.txt", 'w+', encoding="utf-8") as f:
        f.writelines(texto)


############ CRUD DE MOTOS ############

def criar_moto(nome, endereco, telefone):
    moto = Motocicletas(nome, endereco, telefone)

    arquivo = open("motos.txt", "a", encoding="utf-8")
    arquivo.write(f'Modelo: {moto.modelo}, Marca: {moto.marca}, Ano: {moto.ano}\n')
    arquivo.close()


def buscar_moto(modelo):
    arquivo = open("motos.txt", "r", encoding="utf-8")
    for linha in arquivo:
        if modelo in linha:
            print(linha)

def alterar_moto(modelo, marca, ano, valor_antigo):
    with open("motos.txt", 'r', encoding="utf-8") as f:
        texto = f.readlines()
    for i in texto:
        if valor_antigo in i:
            index_linha = texto.index(i)
            texto[index_linha] = (f'Nome: {modelo}, Endereço: {marca}, Telefone: {ano}\n')
        else:
            continue

    with open("motos.txt", 'w+', encoding="utf-8") as f:
        f.writelines(texto)

def deletar_moto(modelo):
    with open("motos.txt", 'r', encoding="utf-8") as f:
        texto = f.readlines()
    for i in texto:
        if modelo in i:
            index_linha = texto.index(i)
            texto[index_linha] = ''
        else:
            continue

    with open("motos.txt", 'w+', encoding="utf-8") as f:
        f.writelines(texto)

############ VENDAS ###############

def criar_venda(cliente, moto):
    arquivo_cliente = open("clientes.txt", "r", encoding="utf-8")
    if cliente not in arquivo_cliente:
        print("\nEsse cliente não existe na concessionaria")
        return

    arquivo_moto = open("motos.txt", "r", encoding="utf-8")
    if moto not in arquivo_moto:
        print("\n Essa moto não existe na concessionaria")
        return

    arquivo = open("vendas.txt", "a", encoding="utf-8")

    arquivo.write(f'Venda - O(A) cliente de nome: {cliente} comprou a moto: {moto}\n')
    arquivo.close()

def buscar_venda(cliente, venda):
    arquivo = open("vendas.txt", "r", encoding="utf-8")
    for linha in arquivo:
        if (cliente and venda) in linha:
            print(linha)
            return
    print('Nenhuma venda encontrada.')

def listar_vendas():
    arquivo = open("vendas.txt", "r", encoding="utf-8")
    for linha in arquivo:
        print(linha)

############ MANIPULAÇÃO DE ARQUIVOS ############

def carrega_mensagem_inicial():
    arquivo = open("mensagem_inicial.txt", "r", encoding="utf-8")

    for linha in arquivo:
        print(linha)

    arquivo.close()

def carrega_mensagem_final():
    arquivo = open("mensagem_final.txt", "r", encoding="utf-8")

    for linha in arquivo:
        print(linha)

    arquivo.close()

def recarregar():
    __main__()

if(__name__ == "__main__"):
    __main__()
