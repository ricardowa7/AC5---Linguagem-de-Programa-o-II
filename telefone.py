# Linguagem de Programação II
# Atividade Contínua 05 - Atividade final
# Arquivo: telefone.py
# Prof. Rafael Maximo
#
# e-mail: ricardo.antunes@aluno.faculdadeimpacta.com.br

# Não precisa de nenhum import


class Telefone:
    """
    Classe para gerar objetos do tipo telefone, responsável por
    realizar a validação do valor recebido.
    - Não deve ser modificada -

    Regras consideradas para os números:
    - ter obrigatoriamente 8 ou 9 dígitos, fixo ou celular, respectivamente;
    - podem vir ou não precedidos de dois dígitos da área (11, 19, 21, etc.)
      levando o número de dígitos para 10 ou 11.
    - podem contér hífens para separar os números (apenas hífens, não espaços
      nem outros caracteres)
    Exemplos: '11-995-868-587', '11-4567-4879', '19123456789', '65498754'
    """

    def __init__(self, telefone):
        self.telefone = telefone

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        if self.valida_telefone(telefone):
            self._telefone = telefone
            self._digitos = telefone.replace('-', '')
            self._numero_de_digitos = len(self._digitos)

    @staticmethod
    def valida_telefone(telefone):
        if not isinstance(telefone, str):
            raise TypeError('O telefone deve ser uma string')
        digitos = telefone.replace('-', '')
        if not digitos.isdigit():
            raise ValueError('O telefone pode conter apenas dígitos e hífens')
        if len(digitos) not in [8, 9, 10, 11]:
            raise ValueError('Número incorreto de dígitos para um telefone')
        return True

    @property
    def digitos(self):
        return self._digitos

    @property
    def eh_celular(self):
        return self._numero_de_digitos in [9, 11]

    @property
    def eh_fixo(self):
        return self._numero_de_digitos in [8, 10]

    @property
    def possui_ddd(self):
        return self._numero_de_digitos in [10, 11]

    @property
    def ddd(self):
        if self.possui_ddd:
            return self._digitos[:1]
        return ''

    def to_json(self):
        return self._telefone

    def __eq__(self, other):
        if not isinstance(other, Telefone):
            raise TypeError('Não é possível comparar um Telefone com '
                            'objetos de outro tipo')
        return self.digitos == other.digitos

    def __repr__(self):
        return f'<Telefone: {self._telefone}>'
