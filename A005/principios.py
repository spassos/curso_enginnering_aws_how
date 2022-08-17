import datetime
import math
from typing import List


# class Pessoa:
#     def __init__(self,
#                  nome: str,
#                  sobrenome: str,
#                  data_de_nascimento: datetime.date) -> None:
#         # cargo_atual: str,
#         # experiencias: List[str]
#         # self.cargo_atual = cargo_atual
#         # self.experiencias = experiencias
#         self.data_de_nascimento = data_de_nascimento
#         self.sobrenome = sobrenome
#         self.nome = nome
#
#     @property
#     def idade(self) -> int:
#         return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)
#
#     def __str__(self) -> str:
#         return f"{self.nome} {self.sobrenome} tem {self.idade} anos"
#
#
# class Curriculo:
#     def __init__(self, pessoa: Pessoa, experiencias: List[str]):
#         self.experiencias = experiencias
#         self.pessoa = pessoa
#
#     @property
#     def quantidade_de_experiencias(self) -> int:
#         return len(self.experiencias)
#
#     @property
#     def empresa_atual(self) -> str:
#         return self.experiencias[-1]
#
#     def adiciona_experiencia(self, experiencia: str) -> None:
#         self.experiencias.append(experiencia)
#
#     def __str__(self):
#         return f"{self.pessoa.nome} {self.pessoa.sobrenome} tem {self.pessoa.idade} anos e já " \
#                f"trabalhou em {self.quantidade_de_experiencias} empresas e atualmente trabalha " \
#                f"na empresa {self.empresa_atual}"
#
#
# sergio = Pessoa(nome='Sergio', sobrenome='Passos', data_de_nascimento=datetime.date(1988, 12, 27))
#
# print(sergio)
#
# curriculo_sergio = Curriculo(
#     pessoa=sergio,
#     experiencias=['CDP', 'Pronto Digital', 'Revemar', 'TOTVS', 'DASA'])
#
# print(curriculo_sergio.pessoa.idade)
#
# print(curriculo_sergio)
#
# curriculo_sergio.adiciona_experiencia("Freelancer")
#
# print(curriculo_sergio)


class Vivente:
    def __init__(self, nome: str, data_nascimento: datetime.date) -> None:
        self.nome = nome
        self.data_nascimento = data_nascimento

    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_nascimento).days / 365.2425)

    def emite_ruido(self, ruido: str):
        print(f"{self.nome} fez ruído: {ruido}")


class PessoaHeranca(Vivente):
    def __str__(self) -> str:
        return f"{self.nome} tem {self.idade} anos"

    def fala(self, frase):
        return self.emite_ruido(frase)


class Cachorro(Vivente):
    def __init__(self, nome: str, data_nascimento: datetime.date, raca: str):
        super().__init__(nome, data_nascimento)
        self.raca = raca

    def __str__(self):
        return f"{self.nome} é de raça {self.raca} e tem {self.idade} anos"

    def late(self):
        return self.emite_ruido("Au! Au!")


sergio2 = PessoaHeranca(nome='Sergio', data_nascimento=datetime.date(1988, 12, 27))

print(sergio2)

lucky = Cachorro(nome='Lucky', data_nascimento=datetime.date(2015, 1, 1), raca='Poodle')

print(lucky)

lucky.late()
lucky.late()
lucky.late()
lucky.late()
sergio2.fala("Cala a boca Lucky!")
lucky.late()
