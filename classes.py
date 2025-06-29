import datetime
import random

class ListaDeTarefas:
    '''Classe que vai conter várias tarefas'''
    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo
        self.tarefas = []
        
    def __str__(self):
        return self.titulo
    
    def editar_lista(self):
        novo_titulo = input('Digite o novo título da lista: ').strip()
        
        if novo_titulo == self.titulo or novo_titulo == '':
            print('O título digitado é igual ao atual! Tente novamente.')
            self.editar_lista()
        else:
            self.titulo = novo_titulo
            print(f'Título da lista alterado para: {self.titulo}')

class Tarefa:
    '''Classe que vai definir cada uma das tarefas'''
    def __init__(self, id:int, lista_tarefas:int , titulo:str, nota:str, data_conclusao:datetime.datetime, tags:list, prioridade:int, repeticao:str):
        self.id = id
        self.lista_tarefas = lista_tarefas
        self.concluida = False
        self.titulo = titulo
        self.nota = nota
        self.data_conclusao = data_conclusao
        self.tags = tags
        self.prioridade = prioridade
        self.repeticao = repeticao
    
    def __str__(self):
        dict_prioridades = {
            3: "sem prioridade",
            2: "baixa",
            1: "média",
            0: "alta"
        }
        
        return f'ID da Tarefa: {self.id}\nTítulo: {self.titulo}\nLista: {self.lista_tarefas}\nNota: {self.nota}\nData de Conclusão: {self.data_conclusao.strftime("%d/%m/%Y")}\nTags: {", ".join(self.tags) if self.tags else "Nenhuma"}\nPrioridade: {dict_prioridades[self.prioridade]}\nRepetição: {self.repeticao}\nConcluída: {"Sim" if self.concluida else "Não"}'
    
    def str_resumo(self):
        return f'Título: {self.titulo}\nData de Conclusão: {self.data_conclusao.strftime("%d/%m/%Y")}\nConcluída: {"Sim" if self.concluida else "Não"}'
    
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