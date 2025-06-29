import os
from classes import ListaDeTarefas, Tarefa
from gerenciador import Gerenciador
import json
import datetime

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add_tarefa(entrada:list, tarefa:Tarefa):
    '''Adiciona todos os parametros de tarefa no final de lista'''

    lista = []

    lista.append(tarefa.id)
    lista.append(tarefa.lista_tarefas)
    lista.append(tarefa.concluida)
    lista.append(tarefa.titulo)
    lista.append(tarefa.nota)
    lista.append(tarefa.data_conclusao.isoformat())
    lista.append(tarefa.tags)
    lista.append(tarefa.prioridade)
    lista.append(tarefa.repeticao)

    entrada.append(lista)

def add_listadetarefas(entrada:list, listadetarefas:ListaDeTarefas):
    '''Adiciona os parametros de uma lista de tarefas em lista'''

    lista = []

    lista.append(listadetarefas.id)
    lista.append(listadetarefas.titulo)
    lista.append(listadetarefas.tarefas)

    entrada.append(lista)

def salvar(gerenciador:Gerenciador):
    '''Salva as informações em dois arquivos json'''


    listas_arquivo = []
    tarefas_arquivo = []

    for x in gerenciador.listas:
        add_listadetarefas(listas_arquivo, x)
    
    arquivo = open('listas.json', 'w')

    json.dump(listas_arquivo, arquivo)
    arquivo.close()            

    for x in gerenciador.tarefas:
        add_tarefa(tarefas_arquivo, x)

    arquivo = open('tarefas.json', 'w')
    json.dump(tarefas_arquivo, arquivo)
    arquivo.close()

def carregar():
    '''Carrega as informações dos aquivos json para o código'''
    listas = []
    tarefas = []

    arquivo = open('listas.json', 'r')
    listas_arquivo = json.load(arquivo)
    arquivo.close()

    arquivo = open('tarefas.json', 'r')
    tarefas_arquivo = json.load(arquivo)
    arquivo.close()

    for x in listas_arquivo:
        listas.append(ListaDeTarefas(x[0], x[1], x[2]))

    for x in tarefas_arquivo:
        tarefas.append(Tarefa(x[0], x[1], x[2], x[3], x[4], datetime.datetime.fromisoformat(x[5]), x[6], x[7], x[8]))

    return Gerenciador(listas, tarefas)