import datetime
import random

class ListaDeTarefas:
    '''Classe que vai conter várias tarefas'''
    def __init__(self, id):
        self.id = id
        self.tarefas = []
        
        print('Crie aqui sua Lista de Tarefas!')
        self.titulo = input('Qual o título da sua lista de tarefas? ')
    
    def adicionar_tarefa(self):
        id_tarefa = random.randint(1000, 9999)
        
        while id_tarefa in self.ids_tarefas:
            id_tarefa = random.randint(1000, 9999)
        
        print('Crie aqui sua Tarefa!')
        
        titulo = input('Qual o título da sua tarefa? ')
        print()
        
        nota = input('Você tem alguma nota sobre a sua tarefa? \n')
        print()
        
        dia, mes, ano = input('Digite o dia, mês e ano para a conclusão da tarefa no formato dd/mm/aaaa:').split('/')
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
        
        valores_possiveis_repeticao = ["nenhuma", "diária", "semanal", "mensal", "anual"]
        while True:
            repeticao = input('Qual a frequência de repetição dessa tarefa? Valores possíveis: "Nenhuma", "Diária", "Semanal", "Mensal" e "Anual". \n').lower()
            
            if repeticao in valores_possiveis_repeticao:
                break
            
            print('O valor digitado é inválido! Tente novamente.')
            print()
        
        self.tarefas.append(Tarefa(id_tarefa, self, titulo, nota, data_conclusao, tags, prioridade, repeticao))
    
    def concluir_tarefa(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                tarefa.concluida = True
                
                if tarefa.repeticao == 'nenhuma':
                    print(f'Tarefa {tarefa.titulo} concluída!') 
                    return
                elif tarefa.repeticao == 'diária':
                    dias = 1
                elif tarefa.repeticao == 'semanal':
                    dias = 7
                elif tarefa.repeticao == 'mensal':
                    dias = 30
                else:
                    dias = 365
                    
                id_tarefa = random.randint(1000, 9999)
                while id_tarefa in self.ids_tarefas:
                    id_tarefa = random.randint(1000, 9999)
                nova_tarefa = Tarefa(id_tarefa, self.id, tarefa.titulo, tarefa.nota, datetime.datetime.now() + datetime.timedelta(days=dias), tarefa.tags, tarefa.prioridade, tarefa.repeticao)
                self.tarefas.append(nova_tarefa)
                print(f'Tarefa {tarefa.titulo} concluída! Uma nova tarefa igual foi criada, mas com a data de conclusão atualizada para {nova_tarefa.data_conclusao.strftime("%d/%m/%Y")}.')
                    
        
        print('Tarefa não encontrada! Verifique o ID e tente novamente.')

class Tarefa:
    '''Classe que vai definir cada uma das tarefas'''
    def __init__(self, id:int, lista:ListaDeTarefas, titulo:str, nota:str, data_conclusao:datetime.datetime, tags:list, prioridade:str, repeticao:str):
        self.id = id
        self.lista = lista
        self.concluida = False
        self.titulo = titulo
        self.nota = nota
        self.data_conclusao = data_conclusao
        self.tags = tags
        self.prioridade = prioridade
        self.repeticao = repeticao
    
    def __str__(self):
        print(f'ID da Tarefa: {self.id}')
        print(f'Título: {self.titulo}')
        print(f'Lista: {self.lista.titulo}')
        print(f'Nota: {self.nota}')
        print(f'Data de Conclusão: {self.data_conclusao.strftime("%d/%m/%Y")}')
        if len(self.tags) > 0:
            print(f'Tags: {", ".join(self.tags)}')
        print(f'Prioridade: {self.prioridade}')
        print(f'Repetição: {self.repeticao}')
        print(f'Concluída: {"Sim" if self.concluida else "Não"}')
    
    def editar_tarefa(self):
        campo_editar = input('Qual campo você gostaria de editar? (título, nota, data de conclusão, tags, prioridade, repetição) ').lower()
        
        if campo_editar == 'título':
            self.titulo = input('Digite o novo título: ')
        elif campo_editar == 'nota':
            self.nota = input('Digite a nova nota: ')
        elif campo_editar == 'data de conclusão':
            dia, mes, ano = input('Digite a nova data de conclusão no formato dd/mm/aaaa: ')
            self.data_conclusao = datetime.datetime(ano, mes, dia)
        elif campo_editar == 'tags':
            self.tags = []
            print('Adicione tags à sua tarefa. Quando quiser parar, não digite nada e pressione ENTER.')
            while True:
                tag = input()
                
                if tag == '':
                    break
                
                self.tags.append(tag)
                
        elif campo_editar == 'prioridade':
            valores_possiveis_prioridades = ["sem prioridade", "baixa", "média", "alta"]
            while True:
                prioridade = input('Qual a nova prioridade? Valores possíveis: "Sem prioridade", "Baixa", "Média" e "Alta". \n').lower()
                
                if prioridade in valores_possiveis_prioridades:
                    self.prioridade = prioridade
                    break
                
                print('O valor digitado é inválido! Tente novamente.')
                print()
        
        elif campo_editar == 'repetição':
            valores_possiveis_repeticao = ["nenhuma", "diária", "semanal", "mensal", "anual"]
            while True:
                repeticao = input('Qual a nova frequência de repetição? Valores possíveis: "Nenhuma", "Diária", "Semanal", "Mensal" e "Anual". \n').lower()
                
                if repeticao in valores_possiveis_repeticao:
                    self.repeticao = repeticao
                    break
                
                print('O valor digitado é inválido! Tente novamente.')
                print()
        
        else:
            print('Campo inválido! Tente novamente.')
            self.editar_tarefa()
            
