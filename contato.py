# Linguagem de Programação II
# Atividade Contínua 05 - Atividade final
# Arquivo: contato.py
# Prof. Rafael Maximo
#
# e-mail: ricardo.antunes@aluno.faculdadeimpacta.com.br

# Faça também a importação dos módulos da atividade necessários
# Não importe módulos a mais pois isso pode causar erros de
# importação cíclica.
# use a forma: from modulo import Classe

from telefone import Telefone
from email_ import Email


class DeleteError(Exception):
    """
    Erro criado para indicar que não foi possível deletar o valor
    ou item pedido. Não é preciso implementar nada nesta classe
    - Não deve ser modificada -
    """
    pass


class CreateContactError(Exception):
    """
    Erro criado para indicar que não foi possível criar o contato.
    Não é preciso implementar nada nesta classe
    - Não deve ser modificada -
    """
    pass


class Contato:
    """ (4,0 pontos)
    Classe para representar um contato

    Deve receber na criação:
        nome: str
        telefone: str
        email: str

    Devem ser criados os atributos PROTEGIDOS: nome, telefones e emails
        nome:
            se não for uma string, levanta um TypeError, e se
            for uma string vazia, levanta um CreateContactError

        telefones:
            um dicionário iniciado com um par chave-valor,
            chave -> 'principal'; valor -> uma instância de Telefone

        emails:
            um dicionário iniciado com um par chave-valor,
            chave -> 'principal'; valor -> uma instância de Email

        (Deve ser instânciado um objeto de Telefone/Email com o valor recebido
        na string para telefone/email e esse objeto adicionado ao dicionário)
        Ex: {'principal': <instância de Telefone/Email aqui>}
    """

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.__telefones = {'principal': Telefone(telefone)}
        self.__emails = {'principal': Email(email)}

    @property
    def nome(self):
        """
        Retorna o valor do atributo protegido referente ao nome
        """
        return self.__nome

    @nome.setter
    def nome(self, nome):
        """
        Verifica as condições definidas para validação do nome e
        atribui o valor ao atributo protegido referente ao nome
        se estiverem OK

        Parâmetros:
        -----------
            nome: str

        Retorno:
        --------
            não possui retorno
        """
        if not isinstance(nome, str):
            raise TypeError
        if nome == "":
            raise CreateContactError
        self.__nome = nome

    def adiciona_telefone(self, telefone, tipo='principal'):
        """
        Atualiza o dicionário com um novo número de telefone, adicionado na chave
        dada em `tipo`. (Notem que o uso de crase ` indica que é a variável e não
        uma string). Da mesma forma que na criação, o telefone deve ser uma instância
        de Telefone criada a partir da string recebida em telefone.
        Se o tipo não for passado, deve ser por padrão tipo 'principal'.

        Parâmetros:
        -----------
            telefone: str
            tipo: str (opcional)

        Retorno:
        --------
            não possui retorno
        """
        self.__telefones.update({tipo: Telefone(telefone)})

    def adiciona_email(self, email, tipo='principal'):
        """
        Atualiza o dicionário com um novo endereço de email, adicionado na chave
        dada em `tipo`. (Notem que o uso de crase ` indica que é a variável e não
        uma string). Da mesma forma que na criação, o email deve ser uma instância
        de Email criada a partir da string recebida em email.
        Se o tipo não for passado, por padrão o tipo 'principal' é atualizado.

        Parâmetros:
        -----------
            email: str
            tipo: str (opcional)

        Retorno:
        --------
            não possui retorno
        """
        self.__emails.update({tipo: Email(email)})

    def apaga_telefone(self, tipo):
        """
        Exclui o telefone dado em `tipo` do dicionário de emails, mas não deve permitir a
        exclusão do tipo 'principal', levantando um DeleteError nesse caso. Se o tipo
        não existir no dicionário, não deve fazer nada

        Parâmetros:
        -----------
            tipo: str

        Retorno:
        --------
            não possui retorno
        """
        if tipo == 'principal':
            raise DeleteError
        del self.__telefones[tipo]

    def apaga_email(self, tipo):
        """
        Exclui o email dado em `tipo` do dicionário de emails, mas não deve permitir a
        exclusão do tipo 'principal', levantando um DeleteError nesse caso. Se o tipo
        não existir no dicionário, não deve fazer nada

        Parâmetros:
        -----------
            tipo: str

        Retorno:
        --------
            não possui retorno
        """
        if tipo == 'principal':
            raise DeleteError
        del self.__emails[tipo]

    @property
    def telefones(self):
        """
        Retorna o dicionário de telefones
        """
        return self.__telefones

    @property
    def emails(self):
        """
        Retorna o dicionário de emails
        """
        return self.__emails

    def lista_telefones(self):
        """
        Retorna o dicionário de telefones convertido para uma lista de tuplas,
        cada tupla com um par de valores (chave, valor) referentes às entradas
        do dicionário.
        Ex: [('principal', objeto_telefone01), ('casa', objeto_telefone02)]

        DICA: usem o método items() de dicionários e convertam o resultado
        para uma lista com list().

        Parâmetros:
        -----------
            -

        Retorno:
        --------
            retorna o dicionário pedido
        """
        tupla_tel = tuple(self.__telefones.items())
        lista_tel = list(tupla_tel)
        return lista_tel

    def lista_emails(self):
        """
        Retorna o dicionário de emails convertido para uma lista de tuplas,
        cada tupla com um par de valores (chave, valor) referentes às entradas
        do dicionário.
        Ex: [('principal', objeto_email01), ('casa', objeto_email02)]

        DICA: usem o método items() de dicionários e convertam o resultado
        para uma lista com list().

        Parâmetros:
        -----------
            -

        Retorno:
        --------
            retorna o dicionário pedido
        """
        tupla_mail = tuple(self.__emails.items())
        lista_mail = list(tupla_mail)
        return lista_mail

    def buscar(self, valor_busca):
        """
        Função para determinar se o contato atual (o self) corresponde ao
        valor buscado, retorna True em caso afirmativo e False caso contrário

        Regras para correspondências:
        - o valor buscado está contido no nome do contato
        - o valor buscado está contido em um dos telefones do contato
        - o valor buscado está contido em um dos emails do contato
        Se qualquer uma das condições acima forem verdadeiras, retornar True.
        Caso contrário, retornar False.
        Ex: Se o valor buscado for 'Ana' deve retornar True caso o self
            tenha 'Ana' em qualquer atributo:
                Ana Julia', 'Mariana', 'marcos@bananas.com.br'
            E se o valor buscado for '345' deve retornar True caso o self
            tenha '345' em qualquer atributo:
                '11999888345', 'João do 345', 'joao345@exemplo.com'

        Parâmetros:
        -----------
            valor_busca: str

        Retorno:
        --------
            True se o valor foi encontrado no contato,
            False caso contrário
        """
        self.valor_busca = valor_busca
        conta_res_tel = 0
        conta_res_mail = 0

        if self.valor_busca in self.__nome:
            return True

        for tel in self.__telefones.values():
            tel = str(tel)
            if valor_busca in tel:
                conta_res_tel += 1

        if conta_res_tel > 0:
            return True

        for e_mail in self.__emails.values():
            e_mail = str(e_mail)
            if valor_busca in e_mail:
                conta_res_mail += 1
        if conta_res_mail > 0:
            return True

        return False

    def create_dump(self):
        """
        Retorna um dicionário com os dados do contato:
        Pares chave-valor:
            'nome': nome do contato,
            'telefones': dicionário de telefones do contato
            'emails': dicionário de emails do contato.

        Parâmetros:
        -----------
            -

        Retorno:
        --------
            retorna o dicionário pedido
        """
        return {'nome': self.__nome, 'telefones': self.__telefones, 'emails': self.__emails}

    def __repr__(self):
        """
        Retorna a string de representação de um contato, use o padrão:
        '<Contato: nome-do-contato-aqui>'
        """
        return f'<Contato: {self.nome}>'
