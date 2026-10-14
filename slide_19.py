class Funcionario:
    def __init__(self, nome: str, matricula: str) -> None:
        self._nome = nome
        self._matricula = matricula 

    def autenticar(self, senha: str) -> None:
        self._senha = senha

    def cadastrar_senha(self, senha: str):
        self._senha = senha

    