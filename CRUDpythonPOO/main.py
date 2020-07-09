from crudPOO import *
import time


def menu_principa():
    
    while True:
        #layout()

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
                pass
                break
            


if __name__ == "__main__":
    menu_principa()