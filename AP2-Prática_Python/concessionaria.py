from cliente import Cliente
from motocicletas import Motocicletas

clientes = []
motos = []

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
            criar_cliente(nome, endereco, telefone, clientes)
            print(f'\nCliente {nome} criado com sucesso!')

            print(clientes)

            recarregar()
        elif(segunda_escolha == 2):
            nome = input('Digite o nome do cliente para buscar os dados: ')
            buscar_cliente(nome)
            recarregar()
        elif(segunda_escolha == 3):
            nome_antigo = input('Digite o nome do cliente que deve ser alterado: ')
            terceira_escolha = int(input('1 - Nome, 2 - Endereço, 3 - Telefone\nO que deseja alterar: '))
            if (terceira_escolha == 1):
                nome = input('\nDigite um novo nome: ')
                alterar_cliente(nome, 0, nome_antigo)
            elif (terceira_escolha == 2):
                endereco = input('\nDigite um novo endereço: ')
                alterar_cliente(endereco, 1, nome_antigo)
            elif (terceira_escolha == 3):
                telefone = input('\nDigite um novo telefone: ')
                alterar_cliente(telefone, 2, nome_antigo)

            print(clientes)
            recarregar()
        elif(segunda_escolha == 4):
            nome = input('Digite o nome do cliente que deseja deletar: ')
            deletar_cliente(nome)
            print(clientes)

            recarregar()

    elif(primeira_escolha == 2):
        print(f'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n' + 10 * ' ' + 'Motocicletas\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        segunda_escolha = int(input('\n1 - Cadastrar Moto \n2 - Buscar por Moto \n3 - Atualizar dados da moto \n4 - Deletar Moto\n\nDigite o que deseja: '))
        if (segunda_escolha == 1):
            modelo = input('Digite um modelo: ')
            marca = input('Digite um marca: ')
            ano = input('Digite um ano: ')
            criar_moto(modelo, marca, ano, motos)
            print(f'Moto {modelo} criada com sucesso!')

            print(motos)

            recarregar()
        elif (segunda_escolha == 2):
            modelo = input('Digite o modelo da moto para buscar os dados: ')
            buscar_moto(modelo)
            recarregar()

        elif (segunda_escolha == 3):
            modelo_antigo = input('Digite o modelo da moto para alterar os dados: ')
            terceira_escolha = int(input('1 - Modelo, 2 - Marca, 3 - Ano\nO que deseja alterar: '))
            if (terceira_escolha == 1):
                modelo = input('Digite um novo modelo: ')
                alterar_moto(modelo, 0, modelo_antigo)
            elif (terceira_escolha == 2):
                marca = input('Digite uma nova marca: ')
                alterar_moto(marca, 1, modelo_antigo)
            elif (terceira_escolha == 3):
                ano = input('Digite um novo ano: ')
                alterar_moto(ano, 2, modelo_antigo)

            print(motos)
            recarregar()
        elif (segunda_escolha == 4):
            modelo = input('Digite o modelo da moto que deseja deletar: ')
            deletar_moto(modelo)
            print(motos)
            recarregar()

    elif(primeira_escolha == 3):
        print('Você escolheu vendas')

    elif((primeira_escolha == 4) or (segunda_escolha == 5)):
        carrega_mensagem_final()
    else:
        print('Opção inválida, recomece o sistema.')


            ############ CRUD DE CLIENTES ############

def criar_cliente(nome, endereco, telefone, array):
    cliente = Cliente(nome, endereco, telefone)
    return array.append([cliente.nome, cliente.endereco, cliente.telefone])

def buscar_cliente(nome):
    for cliente in clientes:
        print(cliente)
        if(cliente[0] == nome):
            print(f'Nome do Cliente: {cliente[0]}\nEndereço do Cliente: {cliente[1]}\nTelefone do Cliente: {cliente[2]}')

def alterar_cliente(valor, index, valor_antigo):
    for cliente in clientes:
        if(valor_antigo == cliente[index]):
            cliente[index] = valor

def deletar_cliente(nome):
    for cliente in clientes:
        if (cliente[0] == nome):
            clientes.remove(cliente)


def deletar_cliente(nome):
    for cliente in clientes:
        if (cliente[0] == nome):
            clientes.remove(cliente)


############ CRUD DE MOTOS ############

def criar_moto(modelo, marca, ano, array):
    moto = Motocicletas(modelo, marca, ano)
    return array.append(([moto.modelo, moto.marca, moto.ano]))

def buscar_moto(modelo):
    for moto in motos:
        if(moto[0] == modelo):
            print(f'Modelo da Moto: {moto[0]}\nMarca da Moto: {moto[1]}\nAno da Moto: {moto[2]}')

def alterar_moto(valor, index, valor_antigo):
    for moto in motos:
        if (valor_antigo == moto[index]):
            moto[index] = valor

def deletar_moto(modelo):
    for moto in motos:
        if (moto[0] == modelo):
            motos.remove(moto)


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
