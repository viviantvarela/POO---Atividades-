# Aluno(a): Vivian Thaís Varela Oliveira
# Professor: Higor Morais
# Turma: TSI 2026.2

# Lista 01 - Exercícios (POO) 

# Aplicação - Aluno
# Etapa 1 - Definição da classe Aluno

class Aluno:
    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def lancar_nota(self, valor: float):
        self.notas.append(valor)

    def media(self) -> float:
        if len(self.notas) == 0:
            return 0.0
        else:
            return(sum(self.notas) / len(self.notas))
        
    def aprovado(self) -> bool:
        if self.media() >= 6.0:
            return True
        else:
            return False

    def __str__(self):
        return f"Nome: {self.nome} ({self.matricula}) - Média: {self.media():.1f}"

# Etapa 2 - Aplicação e Teste 

aluno1 = Aluno("Ana", "20261234")
aluno1.lancar_nota(7.5)
aluno1.lancar_nota(7.5)

aluno2 = Aluno("Helena", "20261235")
aluno2.lancar_nota(5.0)
aluno2.lancar_nota(9.5)

aluno3 = Aluno("Rafael", "20261236")
aluno3.lancar_nota(6.0)
aluno3.lancar_nota(10.0)

print("Alunos Aprovados:")
for aluno in [aluno1, aluno2, aluno3]:
    if aluno.aprovado():
        print(aluno)

# Aplicação - Retangulo e Data 
# Etapa 1 - Definição da classe Retangulo

class Retangulo:
    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("A base e a altura precisam ser valores positivos (maiores que zero)!")
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return ((self.base * 2) + (self.altura * 2))

    def __eq__(self, outro) -> bool:
        if not isinstance(outro, Retangulo):
            return False
        else:
            return self.base == outro.base and self.altura == outro.altura

# Exemplos:
        
r1 = Retangulo(6, 10)
r2 = Retangulo(6, 10)
r3 = Retangulo(5, 16)

print(r1 == r2)
print(r1 == r3)

# Etapa 2 - Classe Data(dia, mes ano)

class Data:
    def __init__(self, dia: int, mes: int, ano: int):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def de_texto(cls, texto: str) -> "Data":
        dia, mes, ano = map(int, texto.split("/"))
        return cls(dia, mes, ano)

    @staticmethod
    def bissexto(ano: int) -> bool:
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    def __str__(self) -> str:
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"

# Exemplos 

d1 = Data(9, 8, 2026)
print(d1)

d2 = Data.de_texto("09/08/2026")
print(d2)

print(Data.bissexto(2024))
print(Data.bissexto(2026))
