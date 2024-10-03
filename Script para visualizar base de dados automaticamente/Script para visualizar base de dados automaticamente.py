import pandas as pd
import matplotlib.pyplot as plt
import os

import sys

print('Quantidade de argumentos:', len(sys.argv), 'argumentos.')
print('Lista de argumentos:', sys.argv)
print('Argumento 0 sys.argv[0]:', sys.argv[0])
print('Argumento 1 sys.argv[1]:', sys.argv[1])
print('Argumento 1 sys.argv[1]:', sys.argv[2])
print('Argumento 1 sys.argv[1]:', sys.argv[3])
print('Argumento 1 sys.argv[1]:', sys.argv[4])
print('Argumento 1 sys.argv[1]:', sys.argv[5])


def plota_pivot_table(sinasc, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(sinasc, values=value, index=index,
                       aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(sinasc, values=value, index=index,
                       aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(sinasc, values=value, index=index,
                       aggfunc=func).unstack().plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return None


meses = sys.argv[1:]

for mes in meses:
    sinasc = pd.read_csv('./input/SINASC_RO_2019_'+mes+'.csv')
    print('Data minima: ', sinasc.DTNASC.min())
    print('Data máxima: ', sinasc.DTNASC.max())

    max_data = sinasc.DTNASC.max()[:7]
    print(max_data)

    os.makedirs('./output/figs/'+max_data, exist_ok=True)

    plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'count',
                      'quantidade de nascimento', 'data de nascimento')
    plt.savefig('./output/figs/'+max_data+'/quantidade de nascimento.png')

    plota_pivot_table(sinasc, 'IDADEMAE', [
                      'DTNASC', 'SEXO'], 'mean', 'media idade mae', 'data de nascimento', 'unstack')
    plt.savefig('./output/figs/'+max_data+'/media idade mae por sexo.png')

    plota_pivot_table(sinasc, 'PESO', [
                      'DTNASC', 'SEXO'], 'mean', 'media peso bebe', 'data de nascimento', 'unstack')
    plt.savefig('./output/figs/'+max_data+'/media peso bebe por sexo.png')

    plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median',
                      'apgar1 medio', 'gestacao', 'sort')
    plt.savefig('./output/figs/'+max_data +
                '/media apgar1 por escolaridade mae.png')

    plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean',
                      'apgar1 medio', 'gestacao', 'sort')
    plt.savefig('./output/figs/'+max_data+'/media apgar1 por gestacao.png')

    plota_pivot_table(sinasc, 'APGAR5', 'GESTACAO', 'mean',
                      'apgar5 medio', 'gestacao', 'sort')
    plt.savefig('./output/figs/'+max_data+'/media apgar5 por gestacao.png')
