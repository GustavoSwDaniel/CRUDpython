import os
import time
import pickle

from validações import ValidaCpf

cadastros = []

resgistros = open('registros.txt','rb')
cadastros = pickle.load(resgistros)
resgistros.close()

def menu_principa():
    
    while True:
        layout()

        print('1 - Cadastrar novo usuario')
        print('2 - Atualizar Cadastro')
        print('3 - Pesquisar Cadastro')
        print('4 - Excluir Cadastro')
        print('5 - Sair')

        print()

        try:
            opcao = int(input('Escolha a opção'))    

        except ValueError:  
            print('Opção invalida')
            time.sleep(1.5)

        else:
          
            if opcao == 1:
                cadastrar_usuario()
                break
            elif opcao == 2:
                atulizar_cadastro()
                break
            elif opcao == 3:
                pesquisar_cadastro()
                break
            elif opcao == 4:
                excluir_usuario()
                break
            elif opcao == 5:
                sair()
            

def cadastrar_usuario():
    layout()
    

    global cadastros

    
    
    id_user = 0
    id_user = len(cadastros) + 1
    nome_user = input('Nome completo: ')
    print(cadastros)
    idade_user = input('Data de Nascimento: ')
    cpf_user = input('CPF: ')
    new_cpf_user = remove_caracteres_especiais(cpf_user)

    if validar_cpf(new_cpf_user) == False:
        cadastrar_usuario()
    
    cadastro = ler_arquivo()

    verifica_se_cfp_existe_arquivo(cadastro,new_cpf_user)

    if verifica_se_cfp_existe_arquivo(cadastro,new_cpf_user) == True:
        cadastrar_usuario()

    endereco_user = input('Endereço:')
    
    print(id_user)
    
    
    cadastros = carregar_na_matriz(
                        id_user,
                        nome_user,
                        idade_user,
                        new_cpf_user,
                        endereco_user)


    escreve_no_arquivo(cadastros)

    
    while True:
        resp = input('Deseja fazer um novo cadastro S/N: ')

        if resp == 'S':
            cadastrar_usuario()
            break
        elif resp == 'N':
            menu_principa()
            os.system('clear')
            break
        else:
            print('Opação invalidada! Tente novamente!')


def pesquisar_cadastro():
    layout()

    cadastro = ler_arquivo()

    pesquisar = input('Entre um cadastro para ser pesquisado: ')

    for cadastro_user in cadastro:
        if pesquisar in cadastro_user.values():
            nome, idade = cadastro_user.get('nome'),cadastro_user.get('idade')
            cpf , endereco = cadastro_user.get('cpf'),cadastro_user.get('endereco')
            index = cadastro.index(cadastro_user)
            

            print(f'Nome: {nome} ')
            print(f'Idade: {idade}')
            print(f'CPF: {cpf}')
            print(f'Endereco: {endereco}')
            print(index)
            print()
    
    
    resp = input('Deseja fazer uma nova pesquisa? S/N: ')
    if resp == 'S':
        pesquisar_cadastro()
    elif resp == 'N':
        menu_principa()
        os.system('clear')


def atulizar_cadastro():
    layout()

    cadastros = ler_arquivo()

    pesquisar = input('Entre o CPF do usuario que desenha cadastrar: ')

    for cadastro_user in cadastros:
        if pesquisar in cadastro_user.values():
            nome, idade = cadastro_user.get('nome'),cadastro_user.get('idade')
            cpf , endereco = cadastro_user.get('cpf'),cadastro_user.get('endereco')
            index = cadastro.index(cadastro_user)
            
            apresentacao(nome,idade,cpf,endereco)
            
            opcao = int(input('Qual informação deseja atualizar'))

            if opcao == 1:
                nome_atualizado = input(f'Nome: ')
                cadastro[index].update({'nome': nome_atualizado})
                escreve_no_arquivo(cadastro)
            elif opcao == 2:
                data_de_nacimento_atualizado = input(f'Data de Nacimento:')
                cadastro[index].update({'idade': data_de_nacimento_atualizado})
                escreve_no_arquivo(cadastro)
            elif opcao == 3:
                cpf_atualizado = input(f'CPF: {cpf}')
                cpf_verificado = atualizar_cpf(cpf_atualizado)
                cadastro[index].update({'cpf':cpf_verificado})
                escreve_no_arquivo(cadastro)
                
            elif opcao == 4:
                endereco_atualizado= input(f'Endereco: ')
                cadastro[index].update({'endereco': endereco_atualizado})
                escreve_no_arquivo(cadastro)

    
    
    resp = input('Deseja fazer uma nova alteração? S/N: ')
    if resp == 'S':
        pesquisar_cadastro()
    elif resp == 'N':
        menu_principa()
        os.system('clear')

            
            



def excluir_usuario():
    layout()

    cadastros = ler_arquivo()


    cpf_para_pesquisa = input('Entre o CPF do usuario que deseja excluir: ')
    new_cpf_user_pesquisa = remove_caracteres_especiais(cpf_para_pesquisa)

    if validar_cpf(new_cpf_user_pesquisa) == False:
        excluir_usuario()


    for cadastro_user in cadastros:
        if cpf_para_pesquisa in cadastro_user.values():
            index = cadastros.index(cadastro_user)
            nome = cadastro_user.get('nome')
            ##cpf = cadastro_user.get('cpf')

            resposta = input(f'Tem certe que deseja excluir o usuario {nome}?? S/N')

            if resposta == 'S':
                cadastros.pop(index)
            else:
                resposta_u = input('Deseja faz uma nova consulta ou voltar para o menu principa??')
                print('1 - Menu Principa \n 2 - Nova Exclusão')
                if resposta_u  == 1:
                    menu_principa()
                elif resposta_u == 2:
                    pesquisar_cadastro()


    resp = input('Deseja faz uma nova exclusão? S/N: ')
    if resp == 'S':
        pesquisar_cadastro()
    elif resp == 'N':
        menu_principa()
        os.system('clear')


def sair():
    resp = input('Deseja sair ? Sim/Nao ')
            
    if resp == 'Sim' or 'S' or 'SIM':
        quit()
    else:
        menu_principa()


# Funções de vadidações 

def validar_cpf(cpf):
    cpfVerificado = ValidaCpf(cpf)
    if not cpfVerificado.valida():
        print('CPF inválido')	
        time.sleep(2)
        return False


def verifica_se_cfp_existe_arquivo(cadastro,new_cpf):
    cpf_existente = False
    for cadastros_cpfs in cadastro:
        if new_cpf in cadastros_cpfs.values():
            cpf_existente = True
    
    if cpf_existente == True:
        print('CPF ja existe no cadastros')
        time.sleep(2)
        return True
    else:
        return


def remove_caracteres_especiais(cpf):
    remove=".-/,"
    new_cpf = cpf

    for caracter in remove:
        new_cpf = new_cpf.replace(caracter, '')
    return new_cpf


def atualizar_cpf(cpf):
    
    cpf_limpo = remove_caracteres_especiais(cpf)
    validacao = validar_cpf(cpf_limpo)

    if validacao == False:
        print(f'O essa {cpf} não é valido')
        time.sleep(2)
        atulizar_cadastro()
    else:
        return cpf_limpo



# Manupulação do arquivo 
def ler_arquivo():


    global cadastro

    resgistro = open('registros.txt','rb')
    cadastro = pickle.load(resgistro)
    resgistro.close()

    return cadastro


def carregar_na_matriz(id_u,nome, idade, cpf, endereco):
    
    global cadastros
    cadastros.append({
                    'id':id_u,
                    'nome': nome, 
                    'idade': idade,
                    'cpf': cpf, 
                    'endereco': endereco})

    return cadastros


def escreve_no_arquivo(cadastros):
    

    resgistros = open('registros.txt','wb')
    pickle.dump(cadastros,resgistros) 
    resgistros.close() 


#Designer

def layout(): 
    os.system('clear')
    print('---------------------------------------')
    print('#'*6 + ' Sistemas de Cadastro ' + '#'*6)
    print('---------------------------------------')
        
def apresentacao(nome,idade,cpf,endereco):
    print('---------------------------------------')
    print('#'*6 + ' INFORMAÇÕES ' + '#'*6)
    print('---------------------------------------')
    print(f'1 - Nome: {nome}')
    print(f'2 - Data de Nacimento: {idade}')
    print(f'3 - CPF: {cpf}')
    print(f'4 - Endereço: {endereco}')
    print()



menu_principa()