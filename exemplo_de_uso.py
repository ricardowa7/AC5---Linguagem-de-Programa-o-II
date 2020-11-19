from agenda import Agenda

ag1 = Agenda('Rafael', '11999888777', 'rafael@exemplo.com')

ag1.novo_contato('Ana Maria', '999111000', 'ana@email.com')
ag1.novo_contato('João Paulo', '111222333', 'joaopl@email2.com')
ag1.novo_contato('Julia Matos', '16123123123', 'julia@impacta.com.br')
ag1.novo_contato('Pedro Matos', '1623234545', 'pedro@impacta.com.br')

lista = ag1.busca_contatos('23')
print(lista)
