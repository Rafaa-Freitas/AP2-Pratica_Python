class Motocicletas:
    def __init__(self, modelo, marca, ano):
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano

    @property
    def modelo(self):
        return self.__modelo

    @property
    def marca(self):
        return self.__marca

    @property
    def ano(self):
        return self.__ano

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @ano.setter
    def ano(self, ano):
        self.__ano = ano
