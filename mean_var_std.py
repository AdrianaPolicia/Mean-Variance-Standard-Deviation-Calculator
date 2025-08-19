import numpy as np

def calculate(lista):
    if len(lista) != 9: #verifica se a lista tem 9 elementos
        raise ValueError("List must contain nine numbers.") # 
    lista = np.array(lista).reshape (3, 3) #muda a lista em uma matiz 3 por 3 
    print(lista)
    calculations = { #cria um dicionário com todas as listas pedidas
  'mean': [lista.mean(axis=0).tolist(), lista.mean(axis=1).tolist(), lista.mean().tolist()], #máximo por coluna, média por linha, média de todos os elementos
  'variance': [lista.var(axis=0).tolist(), lista.var(axis=1).tolist(), lista.var().tolist()],
  'standard deviation': [lista.std(axis=0).tolist(), lista.std(axis=1).tolist(), lista.std().tolist()],
  'max': [lista.max(axis=0).tolist(), lista.max(axis=1).tolist(), lista.max().tolist()],
  'min': [lista.min(axis=0).tolist(), lista.min(axis=1).tolist(), lista.min().tolist()],
  'sum': [lista.sum(axis=0).tolist(), lista.sum(axis=1).tolist(), lista.sum().tolist()]
}

    return calculations # retorna o dicionário com as estatísticas