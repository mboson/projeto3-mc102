from gerenciador import Gerenciador
from utils import clear_screen
from classes import ListaDeTarefas, Tarefa
import time

def tarefa_selecionada(tarefa: Tarefa):
    '''Função que será chamada quando o usuário selecionar uma tarefa específica'''
    clear_screen()
    print('Menu:')
    print('1. Ver detalhes da tarefa')
    print('2. Editar tarefa')
    print('3. Concluir tarefa')
    print('4. Remover tarefa')
    print('5. Voltar ao menu de listas de tarefas')
    
    opcao = input('Escolha uma opção: ').strip()
    clear_screen()
    
    if opcao == '1':
        print(tarefa)
        input('Pressione ENTER para voltar...')
        tarefa_selecionada(tarefa)
    
    elif opcao == '2':
        tarefa.editar_tarefa()
        input('Pressione ENTER para voltar...')
        tarefa_selecionada(tarefa)
    
    elif opcao == '3':
        tarefa.concluida = True
        print(f'Tarefa "{tarefa.titulo}" concluída!')
        input('Pressione ENTER para voltar...')
        tarefa_selecionada(tarefa)
    
    elif opcao == '4':
        #Falta implementar a remoção de tarefas
        print()
    
    elif opcao == '5':
        clear_screen()
        lista = gerenciador.buscar_lista(tarefa.lista_tarefas)
        lista_de_tarefas_selecionada(lista)

def lista_de_tarefas_selecionada(lista: ListaDeTarefas):
    '''Função que será chamada quando o usuário selecionar uma lista de tarefas específica'''
    clear_screen()
    print('Menu:')
    print('1. Listar todas as tarefas')
    print('2. Listar as tarefas concluídas')
    print('3. Selecionar tarefa')
    print('4. Voltar ao menu de listas de tarefas')
    
    opcao = input('Escolha uma opção: ').strip()
    clear_screen()
    
    if opcao == '1':
        gerenciador.tarefas_in_lista(lista.id)
        input('Pressione ENTER para voltar...')
        lista_de_tarefas_selecionada(lista)
    
    elif opcao == '2':
        gerenciador.tarefas_concluidas_in_lista(lista.id)
        input('Pressione ENTER para voltar...')
        lista_de_tarefas_selecionada(lista)
    
    elif opcao == '3':
        titulo_tarefa = input('Digite o título da tarefa que deseja selecionar: ').strip()
        tarefa = gerenciador.buscar_tarefa(titulo_tarefa)
        
        if tarefa and tarefa.lista_tarefas == lista.id:
            tarefa_selecionada(tarefa)
        else:
            print('Tarefa não encontrada ou não pertence a esta lista. Tente novamente.')
            lista_de_tarefas_selecionada(lista)
    
    elif opcao == '4':
        clear_screen()
        opcao_3()
    
    else:
        print('Opção inválida. Tente novamente.')
        lista_de_tarefas_selecionada(lista)
    
def opcao_3():
    """Função que será chamada quando o usuário selecionar a opção 3 do menu"""
    clear_screen()
    print('Menu:')
    print('1. Listar todas as listas de tarefas')
    print('2. Editar lista de tarefas')
    print('3. Selecionar lista de tarefas')
    print('4. Remover lista de tarefas')
    print('5. Voltar ao menu principal')
    
    opcao = input('Escolha uma opção: ').strip()
    clear_screen()
    
    if opcao == '1':
        gerenciador.listar_listas()
        input('Pressione ENTER para voltar...')
        opcao_3()
    
    elif opcao == '2':
        titulo = input('Digite o título da lista de tarefas que deseja editar: ').strip()
        lista = gerenciador.buscar_lista(titulo)
        
        if lista:
            lista.editar_lista()
        else:
            print('Lista não encontrada. Tente novamente.')
            opcao_3()
    
    elif opcao == '3':
        titulo = input('Digite o título da lista de tarefas para selecionar: ').strip()
        lista = gerenciador.buscar_lista(titulo)
        
        if lista:
            lista_de_tarefas_selecionada(lista)
        else:
            print('Lista não encontrada. Tente novamente.')
            opcao_3()
    
    elif opcao == '4':
        #Falta implementar a remoção de listas
        print()
    
    elif opcao == '5':
        return
    
    else:
        print('Opção inválida. Tente novamente.')
        time.sleep(1)
        opcao_3()

def main():
    global gerenciador
    gerenciador = Gerenciador()
    
    while True:
        clear_screen()
        print("Menu:")
        print("1. Criar nova lista de tarefas")
        print("2. Adicionar tarefa")
        print("3. Listas de Tarefas")
        print("4. Sair")
        
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
            opcao_3()
            
        elif opcao == '4':
            time.sleep(1)
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()