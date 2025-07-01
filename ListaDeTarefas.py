from gerenciador import Gerenciador
from utils import clear_screen, add_tarefa, add_listadetarefas, salvar, carregar
from classes import ListaDeTarefas, Tarefa
import datetime
import time
import random

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

        if tarefa.repeticao != "nenhuma":
            tempo_atual = datetime.datetime.now()

            if tarefa.repeticao == "diária":
                novo = tempo_atual + datetime.timedelta(days = 1)
            elif tarefa.repeticao == "semanal":
                novo = tempo_atual + datetime.timedelta(days = 7)
            elif tarefa.repeticao == "mensal":
                novo = tempo_atual + datetime.timedelta(days = 30)
            elif tarefa.repeticao == "anual":
                novo = tempo_atual + datetime.timedelta(days = 365)

        while True:
            id_tarefa = random.randint(1000, 9999)
            if all(tarefa.id != id_tarefa for tarefa in gerenciador.tarefas):
                break

        nova_tarefa = Tarefa(id_tarefa, tarefa.lista_tarefas, False, tarefa.titulo+'*', tarefa.nota, novo, tarefa.tags, tarefa.prioridade, tarefa.repeticao)



        gerenciador.tarefas.append(nova_tarefa)
        for lista in gerenciador.listas:
            if lista.id == nova_tarefa.lista_tarefas:
                lista.tarefas.append(nova_tarefa.id)


        input('Pressione ENTER para voltar...')
        tarefa_selecionada(tarefa)
    
    elif opcao == '4':
        minhalista = tarefa.lista_tarefas

        for lista in gerenciador.listas:
            if lista.id == minhalista:
                lista.tarefas.remove(tarefa.id)
        
        gerenciador.tarefas.remove(tarefa)

        print(f"A tarefa {tarefa} foi apagada com sucesso!")

        time.sleep(2)
    
    elif opcao == '5':
        clear_screen()

        for x in gerenciador.listas:
            if x.id == tarefa.lista_tarefas:
                lista = x

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
        
        if tarefa != None and tarefa.lista_tarefas == lista.id:
            tarefa_selecionada(tarefa)
        else:
            print('Tarefa não encontrada ou não pertence a esta lista. Tente novamente.')
            time.sleep(2)
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
        titulo = input('Digite o título da lista de tarefas para a selecionar: ').strip()
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
        
def visualizacao_tarefas():
    """Função para visualizar as tarefas de todas as listas com filtros"""
    clear_screen()
    print('Qual filtro você gostaria de aplicar?')
    print('1. Listar todas as tarefas')
    print('2. Filtrar por tags')
    print('3. Filtrar por tarefas para hoje (incluindo tarefas atrasadas)')
    print('4. Filtrar por tarefas para esta semana')
    print('5. Filtrar por não concluídas')
    print('6. Ordenar por prioridade')
    print('7. Ordenar por data de conclusão')
    print('8. Voltar ao menu principal')
    
    opcao = input('Escolha uma opção: ').strip()
    clear_screen()

    if opcao == '1':
        gerenciador.listar_tarefas()
        input('Pressione ENTER para voltar...')
        visualizacao_tarefas()
    
    elif opcao == '2':
        tag = input('Digite a tag que deseja filtrar: ').strip()
        tarefas_filtradas = gerenciador.filtrar_tarefas_tags(tag)
        
        if not tarefas_filtradas:
            print(f'Nenhuma tarefa encontrada com a tag "{tag}". Tente novamente.')
            time.sleep(1)
            visualizacao_tarefas()
        
        for tarefa in tarefas_filtradas:
            print('-'*20)
            print(tarefa)
            print('-'*20)
            
            selecionar_tarefa = input('Você gostaria de selecionar essa tarefa? (s/n) ').strip().lower()
            
            if selecionar_tarefa == 's':
                tarefa_selecionada(tarefa)
                break
            
            clear_screen()
    
    elif opcao == '3':
        tarefas_hoje = gerenciador.filtrar_tarefas_hoje()
        
        if not tarefas_hoje:
            print('Nenhuma tarefa encontrada para hoje.')
            input('Pressione ENTER para voltar...')
            visualizacao_tarefas()
        
        for tarefa in tarefas_hoje:
            print('-'*20)
            print(tarefa)
            print('-'*20)
            
            selecionar_tarefa = input('Você gostaria de selecionar essa tarefa? (s/n) ').strip().lower()
            
            if selecionar_tarefa == 's':
                tarefa_selecionada(tarefa)
                break
            
            clear_screen()
    
    elif opcao == '4':
        tarefas_semana = gerenciador.filtrar_tarefas_semana()
        
        if not tarefas_semana:
            print('Nenhuma tarefa encontrada para esta semana.')
            input('Pressione ENTER para voltar...')
            visualizacao_tarefas()
        
        for tarefa in tarefas_semana:
            print('-'*20)
            print(tarefa)
            print('-'*20)
            
            selecionar_tarefa = input('Você gostaria de selecionar essa tarefa? (s/n) ').strip().lower()
            
            if selecionar_tarefa == 's':
                tarefa_selecionada(tarefa)
                break
            
            clear_screen()
    
    elif opcao == '5':
        tarefas_nao_concluidas = gerenciador.filtrar_nao_concluidas()
        
        if not tarefas_nao_concluidas:
            print('Nenhuma tarefa não concluída encontrada.')
            input('Pressione ENTER para voltar...')
            visualizacao_tarefas()
        
        for tarefa in tarefas_nao_concluidas:
            print('-'*20)
            print(tarefa)
            print('-'*20)
            
            selecionar_tarefa = input('Você gostaria de selecionar essa tarefa? (s/n) ').strip().lower()
            
            if selecionar_tarefa == 's':
                tarefa_selecionada(tarefa)
                break
            
            clear_screen()
    
    elif opcao == '6':
        gerenciador.ordenar_tarefas_prioridade()
        gerenciador.listar_tarefas()
        input('Pressione ENTER para voltar...')
        visualizacao_tarefas()
    
    elif opcao == '7':
        gerenciador.ordenar_tarefas_data()
        gerenciador.listar_tarefas()
        input('Pressione ENTER para voltar...')
        visualizacao_tarefas()
    
    elif opcao == '8':
        return
    
    else:
        print('Opção inválida. Tente novamente.')
        time.sleep(0.5)
        visualizacao_tarefas()
        
            

def main():
    global gerenciador
    gerenciador = carregar()
    
    while True:
        clear_screen()
        print("Menu:")
        print("1. Criar nova lista de tarefas")
        print("2. Adicionar tarefa")
        print("3. Listas de Tarefas")
        print('4. Visualização de Tarefas')
        print("5. Sair")

        salvar(gerenciador)
        
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
            clear_screen()
            visualizacao_tarefas()
                        
        elif opcao == '5':
            salvar(gerenciador)

            time.sleep(1)
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()