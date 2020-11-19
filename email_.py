# Linguagem de Programação II
# Atividade Contínua 05 - Atividade final
# Arquivo: email_.py
# Prof. Rafael Maximo
#
# e-mail: ricardo.antunes@aluno.faculdadeimpacta.com.br

# Caso decida usar o módulo de regex, lembre de importá-lo


class Email:
    """ (3,5 pontos)
    Classe para representar um Email, responsável por realizar a validação
    do email recebido. As instruções e regras de validação estão descritas
    nas docstrings de cada método a seguir.
    """

    def __init__(self, email):
        """
        Inicializador de Email - deve usar a property para atribuir o email,
        isto é, deve ser usado o atributo público `self.email`, da mesma
        forma que foi feito no construtor de Telefone.
        """
        self.email = email

    @property
    def email(self):
        """
        Retorna o endereço de email (o atributo protegido -> apenas um _ )
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Verifica se o email recebido é válido, usando o método estático
        valida_email() e em caso afirmativo, define o atributo protegido
        para email (apenas um _).
        DICA: Se o email for válido, defina também mais outros dois atributos
              protegidos (auxiliares) para guardar o usuario e o dominio do email,
              isso não é necessário, mas pode simplificar as outras verificações

        Parâmetros:
        -----------
            email: str

        Retorno:
        --------
            não possui retorno
        """
        if self.valida_email(email):
            self._email = email
            self._user = self._email.split("@")[0]
            self._dom = self._email.split("@")[1]

    @staticmethod
    def valida_email(email):
        """
        Recebe um email e retorna True caso seja válido, levanta um erro
        caso contrário.

        Este método estático é responsável por conter as regras de validação
        de um endereço de email, qualquer objeto da classe pode acessá-lo
        (chamá-lo), mas notem que ele não recebe o self como primeiro
        parâmetro, portanto ele não tem conhecimento sobre o objeto (não
        sabe quais informações o objeto guarda).

        Regras de validação:
        - Deve ser uma string, senão levanta um TypeError
        - Deve conter exatamente 1 símbolo @, senão levanta um ValueError
        - Deve conter apenas letras, números e pontos, senão levanta um
          ValueError.

        DICAS:
        - As mensagens de erro não importam;
        - A validação de caracteres pode ser feita como preferirem,
          uma forma de descobrir se os caracteres são alfanuméricos
          (apenas letras e números) é usar o método de strings isalnum():
              Ex: 'abc123'.isalnum() -> True
                  '#@123'.isalnum() -> False
          Vocês podem quebrar (split) a string no '.' e verificar se cada
          string da lista resultante retorna True para isalnum(), ou
          usar um replace para trocar os pontos por uma string vazia e
          em seguida verificar se isalnum() é True.
          Qualquer outra forma de validação que use apenas módulos da
          biblioteca padrao do python pode ser usada. (Se foi necessário
          fazer um pip install do módulo, então ele não está na biblioteca
          padrão e não será considerado para a nota - eu não irei instalar
          o módulo e isso irá gerar um erro de execução, resultando em nota
          zero. Caso alguém esteja na dúvida, o módulo de regex faz parte
          da biblioteca padrão e pode ser usado se assim desejarem, apenas
          lembrem de importá-lo no ínicio do arquivo)

        Parâmetros:
        -----------
            email: str

        Retorno:
        --------
            True caso a string recebida seja um email válido de acordo
            com as regras aqui definidas
        """
        if not isinstance(email, str):
            raise TypeError

        if email.count("@") < 1 or email.count("@") > 1:
            raise ValueError

        email_sem_ponto = email.replace('.', '')
        email_al_num = email_sem_ponto.replace('@', '')

        if not email_al_num.isalnum():
            raise ValueError

        return True

    @property
    def eh_aluno_impacta(self):
        """
        Retorna True se o dominio completo do email (parte depois do @)
        for igual à 'aluno.faculdadeimpacta.com.br', False caso contrário
        """
        if self._dom == 'aluno.faculdadeimpacta.com.br':
            return True
        else:
            return False

    @property
    def eh_impacta(self):
        """
        Retorna True se a string 'faculdadeimpacta.com.br' estiver
        contida no dominio do email (parte depois do @), False caso contrário
        """
        if 'faculdadeimpacta.com.br' in self._email:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        Reescrevendo o método de comparação de igualdade para os objetos de
        email. Este é um método especial do python que será chamado quando
        fizermos a comparação `email1 == email2`. email1 será o `self` e email2
        será o `other`. Caso tenhamos uma lista de emails e fizermos a
        verificação de pertencimento `email1 in [e1, e2, e3, e4, ...]`
        o python irá automaticamente percorrer a lista chamando para cada
        elemento dessa lista o método __eq__ de email1 passando os elementos
        da lista como other, isto é:
            email1.__eq__(e1), email1.__eq__(e2), email1.__eq__(e3), ...
        e no primeiro resultado True, ele retorna True. Se chegar ao final da
        lista e não tiver nenhum True, então retorna False.

        Não modificar este método, já está implementado
        """
        if not isinstance(other, Email):
            raise TypeError('Não é possível comparar um email com '
                            'objetos de outro tipo')
        return self.email == other.email

    def to_json(self):
        """
        Retorna o endereço de email para ser a representação serializada
        de email no arquivo json.
        """
        return self.email

    def __repr__(self):
        """
        Retorna uma string representando o objeto do tipo email,
        siga o padrão usado para a representação de Telefone
        """
        return f'<Email: {self.email}>'
