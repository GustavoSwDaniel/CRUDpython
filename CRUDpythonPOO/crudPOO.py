
from api.validacoes import ValidaCpf


class Cadastro:
    def __init__(self, name_user, data_de_nacimento_user, cpf_user, endereco_user):
        
        self.nome_user = name_user.upper()
        
        self.data_de_nacimento_user = data_de_nacimento_user
        
        self.cpf_user = cpf_user
        
        self.endereco_user = endereco_user.upper()
