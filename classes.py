import datetime
import random

class Tarefa:
    '''Classe que vai definir cada uma das tarefas'''
    def __init__(self, id:int, id_lista:int):
        print('Crie aqui sua Tarefa!')
        
        self.titulo = input('Qual o título da sua tarefa? ')
        print()
        
        self.nota = input('Você tem alguma nota sobre a sua tarefa? \n')
        print()
        
        dia, mes, ano = input('Digite o dia, mês e ano para a conclusão da tarefa no formato dd/mm/aaaa:').split('/')
        self.data_conclusao = datetime.datetime(ano, mes, dia)
        print()
        
        print('Você gostaria de adicionar tags à sua tarefa? Caso não queira, não digite nada e pressione ENTER.')
        while True:
            tag = input()
            
            if tag == '':
                break
            
            self.tags.append(tag)
        print()
        
        valores_possiveis_prioridades = ["sem prioridade", "baixa", "média", "alta"]
        while True:
            prioridade = input('Qual a prioridade dessa tarefa? Valores possíveis: "Sem prioridade", "Baixa", "Média" e "Alta". \n').lower()
            
            if prioridade in valores_possiveis_prioridades:
                self.prioridade = prioridade
                break
            
            print('O valor digitado é inváldio! Tente novamente.')
            print()
        
        valores_possiveis_repeticao = ["nenhuma", "diária", "semanal", "mensal", "anual"]
        while True:
            repeticao = input('Qual a frequência de repetição dessa tarefa? Valores possíveis: "Nenhuma", "Diária", "Semanal", "Mensal" e "Anual". \n').lower()
            
            if repeticao in valores_possiveis_repeticao:
                self.repeticao = repeticao
                break
            
            print('O valor digitado é inválido! Tente novamente.')
            print()
        
        self.id = id
        self.id_lista = id_lista
        self.concluida = False
    

        
        
            


class ListaDeTarefas:
    '''Classe que vai conter várias tarefas'''
    def __init__(self, id):
        self.id = id
        self.tarefas = []
        self.ids_tarefas = []
        
        print('Crie aqui sua Lista de Tarefas!')
        self.titulo = input('Qual o título da sua lista de tarefas? ')
    
    def adicionar_tarefa(self):
        id_tarefa = random.randint(1000, 9999)
        
        while id_tarefa in self.ids_tarefas:
            id_tarefa = random.randint(1000, 9999)
        
        self.tarefas.append(Tarefa(id_tarefa, self.id))