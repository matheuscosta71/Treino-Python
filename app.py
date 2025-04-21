import os

restaurantes = [{'nome':'Praca', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False},]


def exibir_nome_do_programa():
      print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      
            
            """)


def exibir_opcoes():
      print ('1. Cadastrar Restaurante')
      print ('2. Listar Restaurante')
      print ('3. Alternar estado do Restaurante')
      print ('4. Sair')

def exibir_subtitulo(texto):
      os.system ('cls')
      linha ='*' * (len(texto) + 4)
      print (linha)
      print(texto)
      print(linha)

def voltar_ao_menu_principal():
      input('\nDigite uma tecla para voltar ao programa principal ')
      main()

def opcao_invalida():
      print ('Opcao inválida \n')
      voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
      '''Essa função é responsável por cadastrar novo restaurante
      
      Inputs: nome do restaurante e categoria

      Output: adiciona um novo restaurante a lista restaurantes
      
      '''
      exibir_subtitulo('Cadastro de novos restaurantes')
      nome_do_restaurante = input ('Digite o nome do restaurante: ')
      categoria = input (f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}

      restaurantes.append(dados_do_restaurante)
      print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
      
      voltar_ao_menu_principal()

def listar_restaurantes():
      exibir_subtitulo('Listando os Restaurantes\n')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f' - {nome_restaurante.ljust(20)} | {categoria. ljust(20)} | {ativo}')
      
      voltar_ao_menu_principal()


def alternar_estado_restaurante():
      exibir_subtitulo("Alterando estado do restaurante")
      nome_restaurante=input ("Digite o nome do restaurante que deseja alterar o estado: ")
      restaurante_encontrado = False

      for restaurante in restaurantes: 
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado= True
                  restaurante['ativo'] = not restaurante ['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
                  print(mensagem)

            if not restaurante_encontrado:
                  print ('O restaurante não foi encontrado')


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
                  alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
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