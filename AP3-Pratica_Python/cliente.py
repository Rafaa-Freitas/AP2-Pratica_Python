class Cliente:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def telefone(self):
        return self.__telefone

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
