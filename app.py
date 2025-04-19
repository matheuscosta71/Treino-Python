import os
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

def escolher_opcoes():
      opcao_escolhida =int(input('Escolha uma opção: '))
      #print (f'Você escolheu a opção {opcao_escolhida}') mesclando texto com variáveis
      if opcao_escolhida == 1:
            print('Cadastrar Restaurantes')
      elif opcao_escolhida == 2:
            print('Listar Restaurantes')
      elif opcao_escolhida == 3:
            print('Ativar Restaurantes')
      else :
            finalizar_app()

def finalizar_app():
      os.system('cls')
      print ('Finalizando o app')

def main():
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcoes()

if __name__ == '__main__':
      main()