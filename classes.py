import datetime
import random

class ListaDeTarefas:
    '''Classe que vai conter várias tarefas'''
    def __init__(self, id, titulo):
        self.id = id
        self.tarefas = []
        self.titulo = titulo
        
    def __str__(self):
        return self.titulo
    
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
    
    def tarefas_concluidas(self):
        tarefas_concluidas = [tarefa for tarefa in self.tarefas if tarefa.concluida]
        
        if len(tarefas_concluidas) == 0:
            print('Nenhuma tarefa concluída.')
            return
        
        print('Tarefas concluídas:')
        for tarefa in tarefas_concluidas:
            print('-' * 20)
            print(tarefa.str_resumo())

    def remover_tarefa(self, tarefa):
        self.tarefas.remove(tarefa)
        print(f"Tarefa removida: {tarefa}")
    
    def editar_lista(self):
        novo_titulo = input('Digite o novo título da lista: ').strip()
        
        if novo_titulo == self.titulo or novo_titulo == '':
            print('O título digitado é igual ao atual! Tente novamente.')
            self.editar_lista()
        else:
            self.titulo = novo_titulo
            print(f'Título da lista alterado para: {self.titulo}')

    def busca_tarefa(self, tarefa): #incompleto
        if tarefa in self.tarefas:
            print(tarefa) #?Todas as tarefas que contém esse texto no título, nota, ou tags deverão ser mostradas
        else:
            print("Tarefa não encontrada")
class Tarefa:
    '''Classe que vai definir cada uma das tarefas'''
    def __init__(self, id:int, lista_tarefas:int , titulo:str, nota:str, data_conclusao:datetime.datetime, tags:list, prioridade:str, repeticao:str):
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
        return f'ID da Tarefa: {self.id}\nTítulo: {self.titulo}\nLista: {self.lista_tarefas}\nNota: {self.nota}\nData de Conclusão: {self.data_conclusao.strftime("%d/%m/%Y")}\nTags: {", ".join(self.tags) if self.tags else "Nenhuma"}\nPrioridade: {self.prioridade}\nRepetição: {self.repeticao}\nConcluída: {"Sim" if self.concluida else "Não"}'
    
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