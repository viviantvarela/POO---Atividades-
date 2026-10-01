class Motorista:
    def __init__(self, nome: str, veiculo: str) -> None:
        self.nome = nome
        self.veiculo = veiculo.lower()

    def dirigir(self) -> None:
        if self.veiculo == "carro":
            return f"Motorista '{self.nome}' está dirigindo seu {self.veiculo}!"
        elif self.veiculo == "moto":
            return f"Motorista '{self.nome}' está pilotando sua {self.veiculo}!"

m1 = Motorista("Nancy", "moto")
print(m1.dirigir())