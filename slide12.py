class Animal:
    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._posicao = 0

    def mover_se(self) -> None:
        self._posicao += 1

class Gato(Animal):
    def mover_se(self):
        print(f"{self.nome} caminhando...")
        self._posicao += 1 