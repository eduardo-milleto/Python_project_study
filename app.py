import os

resturantes = [{'nome':'Sushito', 'categoria':'Japaonesa', 'ativo':True}, {'nome':'Nono Ludovico', 'categoria':'Pizza', 'ativo':False}, 
               
]

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')  # Isso ajuda a garantir compatibilidade entre diferentes sistemas operacionais

def clear_mensagem(mensagem):
    os.system('clear' if os.name == 'posix' else 'cls')  # Isso ajuda a garantir compatibilidade entre diferentes sistemas operacionais
    print(mensagem)
    print()

def voltar_ao_menu():
    print()
    input("Digite uma tecla para voltar ao menu principal")
    main()

def exibir_nome_do_programa():
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    clear_mensagem('Finalizando o app')

def opcao_invalida():
    clear_mensagem('Opcao inválida!')
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    clear_mensagem('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    resturantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')

    voltar_ao_menu()

def listar_restaurantes():
    clear_mensagem('Listando os restaurantes')

    for restaurante in resturantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo} ')

    voltar_ao_menu()

def alternar_estado_restaurante():
    clear_mensagem('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in resturantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    clear()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
