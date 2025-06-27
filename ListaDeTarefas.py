from gerenciador import Gerenciador
from utils import clear_screen
import time

def main():
    gerenciador = Gerenciador()
    
    while True:
        clear_screen()
        print("Menu:")
        print("1. Criar nova lista de tarefas")
        print("2. Adicionar tarefa")
        print("3. Mostrar todas as Listas de Tarefas")
        print("4. Mostrar todas as Tarefas")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        time.sleep(0.5)
        
        if opcao == '1':
            clear_screen()
            gerenciador.criar_lista()
            time.sleep(1)
        elif opcao == '2':
            clear_screen()
            gerenciador.adicionar_tarefa()
            time.sleep(1)
        elif opcao == '3':
            clear_screen()
            gerenciador.listar_listas()
            time.sleep(1)
        elif opcao == '4':
            clear_screen()
            gerenciador.listar_tarefas()
            time.sleep(1)
        elif opcao == '5':
            time.sleep(1)
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()