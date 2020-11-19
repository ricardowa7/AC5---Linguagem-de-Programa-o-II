# Linguagem de Programação II
# Atividade Contínua 05 - Atividade final
# Arquivo: agenda.py
# Prof. Rafael Maximo
#
# e-mail: ricardo.antunes@aluno.faculdadeimpacta.com.br

# Importação do módulo json para exportar/importar contatos
import json

# Faça também a importação dos módulos da atividade necessários
# Não importe módulos a mais pois isso pode causar erros de
# importação cíclica.
# use a forma: from modulo import Classe

from contato import Contato


def dumper(obj):
    """
    Função auxiliar para ser usada no momento de serializar
    os objetos para json.
    - Não deve ser modificada -
    """
    try:
        return obj.to_json()
    except AttributeError:
        return obj.__dict__


class Agenda:
    lst_busca = []
    """ (3,5 pontos)

    No mometo de criação, a agenda recebe um titular (nome), um número de
    telefone e um email do titular, criando um atributo público
    meu_contato que irá guardar uma instância de Contato criada com os
    dados do titular.
    O inicializador deve ainda criar um atributo público contatos, que deverá
    ser inicializado como uma lista vazia.
    """

    def __init__(self, titular, meu_numero, meu_email):
        self.meu_contato = Contato(titular, meu_numero, meu_email)
        self.contatos = []

    def novo_contato(self, nome, telefone, email):
        """
        Instancia um novo Contato e insere-o na agenda,
        adicionando-o à lista de contatos

        Parâmetros:
        -----------
            nome: str
            telefone: str
            email: str

        Retorno:
        --------
            não possui retorno
        """
        novo_contato = Contato(nome, telefone, email)
        self.contatos.append(novo_contato)

    def busca_contatos(self, valor_busca):
        """
        Retorna uma lista com todos os contatos que correspondam ao valor
        buscado. Se nenhum contato for encontrado, retorna uma lista vazia

        DICA: Itere sobre a lista de contatos e use o método de
        correspondência (buscar) de cada contato para ver se ele deve ou não
        ser adicionado à lista

        Parâmetros:
        -----------
            valor_busca: str

        Retorno:
        --------
            retorna a lista pedida
        """
        for em_contatos in self.contatos:
            busca_em_contato = str(em_contatos)
            if busca_em_contato.count(valor_busca) > 0:
                self.lst_busca.append(em_contatos)
        return self.lst_busca

    def ligar(self, valor_busca, tipo='principal'):
        """
        Busca a lista de contato que correspondam ao valor buscado e liga
        para o primeiro contato da lista que possuir o telefone do tipo dado
        retornando uma string com a mensagem:
        'Ligando para <nome_contato>: <telefone>'
        Se nenhum contato da lista possuir o tipo dado, retorna a mensagem:
        'Nenhum contato possui o tipo de telefone dado!'

        DICA: Após buscar os contatos com o método busca_contatos, percorram
        a lista retorna e para cada contato dessa lista, verifiquem se o contato
        possui um telefone do tipo pedido

        Parâmetros:
        -----------
            valor_busca: str
            tipo: str (opcional)

        Retorno:
        --------
            retorna a string pedida
        """
        pass

    def apagar_contato(self, email_busca):
        """
        Busca um contato por email e exclui o contato da agenda.
        retornando a mensagem:
        '<representação do contato> excluído com sucesso!'
        Ex: '<Contato: João do 345> excluído com sucesso!'

        Se nenhum contato for encontrado, retorna a mensagem:
        'Nenhum contato corresponde ao email dado.'

        Parâmetros:
        -----------
            email_busca: str

        Retorno:
        --------
            retorna a string pedida
        """
        pass

    def exportar_contatos(self, nome_arquivo):
        """
        Exporta um arquivo json com a agenda de contatos.
        Verificar se o nome do arquivo termina em '.json'.
        Em caso afirmativo, deve ser usadado como dado para criação
        do arquivo. Caso o nome do arquivo não termine em '.json',
        a extensão deve ser adicionada ao nome para criação do arquivo
        em disco, garantindo que será sempre escrito um arquivo json.

        DICAS:
            - Crie uma nova lista vazia e percorra a lista de contatos
              adicionando à nova lista o dicionário retornado pelo método
              create_dump para cada contato da lista de contatos.
            - Usem o gerenciador de contexto --> with
            - Os objetos de Telefone e Email não são serializáveis,
              por isso criei o método to_json() e a função dumper.
              Então passe a função dumper por parâmetro nomeado para o
              parâmetro `default` do método dump() de json.
            - Para deixar o arquivo json mais legível por humanos, passe
              como parâmetro nomeado `indent` um valor inteiro positivo.
              Valores comuns são 2 ou 4.

        Parâmetros:
        -----------
            nome_arquivo: str

        Retorno:
        --------
            não possui retorno
        """
        pass

    def carregar_contatos(self, nome_arquivo):
        """
        Método bônus - não será considerado para a correção
        Ler um arquivo json exportado pelo método anterior e
        carregar os contatos na agenda.

        Parâmetros:
        -----------
            nome_arquivo: str

        Retorno:
        --------
            não possui retorno
        """
        pass

"""
a1 = Agenda('Rafael', '11999887766', 'rafael@email.com')
a1.novo_contato('Ana', '11999888563', 'ana@email.com')
a1.novo_contato('Pedro', '1955552222', 'pedro@email.com')
a1.novo_contato('Mariana', '21145145145', 'mariana@email.com')
a1.novo_contato('João', '1152525252', 'joao@email.com')
lista01 = a1.busca_contatos('ana')
lista02 = a1.busca_contatos('9888')
lista03 = a1.busca_contatos('52')
lista04 = a1.busca_contatos('email.com')
"""
