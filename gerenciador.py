from classes import ListaDeTarefas, Tarefa
import random
import datetime

class Gerenciador:
    def __init__(self):
        self.listas = []
        self.tarefas = []

    def criar_lista(self):
        titulo = input('Qual o título da sua lista de tarefas? ').strip()
        
        #Cria um ID único para a nova lista de tarefas
        while True:
            id_lista = random.randint(1000, 9999)
            if all(lista.id != id_lista for lista in self.listas):
                break
        
        nova_lista = ListaDeTarefas(id_lista, titulo)
        self.listas.append(nova_lista)
        print(f'Lista "{titulo}" criada com sucesso!')
    
    def adicionar_tarefa(self):
        
        #Cria um ID para a nova tarefa
        while True:
            id_tarefa = random.randint(1000, 9999)
            if all(tarefa.id != id_tarefa for tarefa in self.tarefas):
                break
        
        print('Crie aqui sua Tarefa!')
        
        #Pergunta ao usuário em qual lista de tarefas ele quer adicionar a tarefa
        print('Você gostaria de adicionar essa tarefa a qual lista de tarefas?')
        print('Essas são as listas disponíveis:')
        
        #Printa as listas disponíveis
        for lista in self.listas:
            print('- ', lista)
        
        #Solicita o título da lista de tarefas e busca a lista correspondente
        lista_titulo = input('Digite o título da lista de tarefas: ').lower().strip()
        lista = self.buscar_lista(lista_titulo)
        lista_tarefas = lista.id
        
        titulo = input('Qual o título da sua tarefa? ')
        print()
        
        nota = input('Você tem alguma nota sobre a sua tarefa? \n')
        print()
        
        dia, mes, ano = map(int, input('Digite o dia, mês e ano para a conclusão da tarefa no formato dd/mm/aaaa: ').split('/'))
        data_conclusao = datetime.datetime(ano, mes, dia)
        print()
        
        tags = []
        print('Você gostaria de adicionar tags à sua tarefa? Caso não queira, não digite nada e pressione ENTER.')
        while True:
            tag = input()
            
            if tag == '':
                break
            
            tags.append(tag)
        print()
        
        valores_possiveis_prioridades = ["sem prioridade", "baixa", "média", "alta"]
        while True:
            prioridade = input('Qual a prioridade dessa tarefa? Valores possíveis: "Sem prioridade", "Baixa", "Média" e "Alta". \n').lower()
            
            if prioridade in valores_possiveis_prioridades:
                break
            
            print('O valor digitado é inváldio! Tente novamente.')
            print()
        print()
        
        valores_possiveis_repeticao = ["nenhuma", "diária", "semanal", "mensal", "anual"]
        while True:
            repeticao = input('Qual a frequência de repetição dessa tarefa? Valores possíveis: "Nenhuma", "Diária", "Semanal", "Mensal" e "Anual". \n').lower()
            
            if repeticao in valores_possiveis_repeticao:
                break
            
            print('O valor digitado é inválido! Tente novamente.')
            print()
        print()
        
        self.tarefas.append(Tarefa(id_tarefa, lista_tarefas, titulo, nota, data_conclusao, tags, prioridade, repeticao))
        
        print(f'Tarefa "{titulo}" adicionada com sucesso à lista "{lista.titulo}"!')

    def listar_listas(self):
        if not self.listas:
            print('Nenhuma lista criada.')
            return
        print('Listas de Tarefas:')
        for lista in self.listas:
            print(f'- {lista.titulo}')
    
    def listar_tarefas(self):
        if not self.tarefas:
            print('Nenhuma tarefa criada.')
            return
        print('Tarefas:')
        for tarefa in self.tarefas:
            print('-'*20)
            print(f'{tarefa.str_resumo()}')
        print('-'*20)
        
        print()
        input('Pressione ENTER para voltar...')
    
    def listar_listas(self):
        if not self.listas:
            print('Nenhuma lista criada.')
            return
        print('Listas de Tarefas:')
        for lista in self.listas:
            print(f'- {lista.titulo}')
        
        print()
        input('Pressione ENTER para voltar...')

    def buscar_lista(self, titulo):
        for lista in self.listas:
            if lista.titulo.lower() == titulo.lower():
                return lista
        print(f'Lista "{titulo}" não encontrada.')
        return None