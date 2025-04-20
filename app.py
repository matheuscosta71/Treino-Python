import os

restaurantes = ['Pizza', 'Sushi']


def exibir_nome_do_programa():
      print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      
            
            """)


def exibir_opcoes():
      print ('1. Cadastrar Restaurante')
      print ('2. Listar Restaurante')
      print ('3. Ativar Restaurante')
      print ('4. Sair')

def exibir_subtitulo(texto):
      os.system ('cls')
      print(texto)

def voltar_ao_menu_principal():
      input('\nDigite uma tecla para voltar ao programa principal ')
      main()

def opcao_invalida():
      print ('Opcao inválida \n')
      voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
      exibir_subtitulo('Cadastro de novos restaurantes')
      nome_do_restaurante = input ('Digite o nome do restaurante: ')
      restaurantes.append (nome_do_restaurante)
      print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
      voltar_ao_menu_principal()

def listar_restaurantes():
      exibir_subtitulo('Listando os Restaurantes\n')
      
      for restaurante in restaurantes:
            print (f'.{restaurante}')
      
      voltar_ao_menu_principal()


def escolher_opcoes():
      try :
            opcao_escolhida =int(input('Escolha uma opção: '))
            #print (f'Você escolheu a opção {opcao_escolhida}') mesclando texto com variáveis
            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:
                  print('Ativar Restaurantes')
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except opcao_escolhida:
            opcao_invalida()

def finalizar_app():
      exibir_subtitulo('Finalizando o app')

def main():
      os.system ('cls')
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcoes()

if __name__ == '__main__':
      main()