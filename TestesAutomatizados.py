# Importações
from BFSDemo import BFS
from DFSDemo import DFS
from dijkstraMaze import dijkstra
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit
import pandas as pd
import matplotlib.pyplot as plt

# Formatação Resultados.csv
df = pd.DataFrame(columns=['Teste', 'Maze', 'Tipo', 'Passos', 'Tamanho da Busca - Custo', 'Tempo'])

# Testes realizados
dimensionsList = [(5,5),(10,10),(15,15),(20,20),(25,25),(30,30),(35,35),(40,40),(45,45),(50,50)]

for teste in range(len(dimensionsList)):
    linhas = dimensionsList[teste][0]
    colunas = dimensionsList[teste][1]
    # Cria o labirinto
    m=maze(linhas,colunas) #Dimensões
    m.CreateMaze() #(Destino, Maximiza os caminhos, carrega o labirinto)

        
    # Algoritmo - Busca DFS
    searchPath,dfsPath,fwdDFSPath=DFS(m)
    # Algoritmo - Busca BFS
    bSearch,bfsPath,fwdBFSPath=BFS(m)
    # Algoritmo - Busca Dijkstra
    fwdDijPath,cDij=dijkstra(m)

    # Labels legenda (resultados linha superior)
    textLabel(m,'DFS - Passos',len(fwdDFSPath)+1)
    textLabel(m,'BFS - Passos',len(fwdBFSPath)+1)
    textLabel(m,'Dijkstra - Passos',len(fwdDijPath)+1)
    textLabel(m,'DFS - Tamanho da Busca',len(searchPath)+1)
    textLabel(m,'BFS - Tamanho da Busca',len(bSearch)+1)
    textLabel(m,'Dijkstra - Custo Total',cDij)

    # Definição dos agentes (que objetos que percorrem)
    a=agent(m,footprints=True,color=COLOR.cyan,shape='arrow')
    b=agent(m,footprints=True,color=COLOR.yellow,shape='arrow')
    c=agent(m,footprints=True,color=COLOR.green,shape='arrow')

    # Execução das buscas {agente:algoritmo da busca}
    m.tracePath({a:fwdBFSPath},delay=50,kill=True)
    m.tracePath({b:fwdDFSPath},delay=50,kill=True)
    m.tracePath({c:fwdDijPath},delay=50,kill=True)

    # Definição do timer de cada busca
    t1=timeit(stmt='DFS(m)',number=1000,globals=globals())
    t2=timeit(stmt='BFS(m)',number=1000,globals=globals())
    t3=timeit(stmt='dijkstra(m)',number=1000,globals=globals())

    # Labels legenda (resultados linha superior)
    textLabel(m,'DFS - Tempo:',t1)
    textLabel(m,'BFS - Tempo:',t2)
    textLabel(m,'Dijkstra - Tempo:',t3)

    dimensions = '('+str(linhas)+','+str(colunas)+')'
    linha1 = pd.Series({'Teste': teste, 'Maze': dimensions, 'Tipo': 'DFS', 'Passos': len(fwdDFSPath)+1, 'Tamanho da Busca - Custo': len(searchPath)+1, 'Tempo': t1})
    linha2 = pd.Series({'Teste': teste, 'Maze': dimensions, 'Tipo': 'BFS', 'Passos': len(fwdBFSPath)+1, 'Tamanho da Busca - Custo': len(bSearch)+1, 'Tempo': t2})
    linha3 = pd.Series({'Teste': teste, 'Maze': dimensions, 'Tipo': 'Dijkstra', 'Passos': len(fwdDijPath)+1, 'Tamanho da Busca - Custo': cDij, 'Tempo': t3})

    df = df._append(linha1, ignore_index=True)
    df = df._append(linha2, ignore_index=True)
    df = df._append(linha3, ignore_index=True)


df_Passos = pd.DataFrame({
   'DFS': df.loc[df['Tipo'] == 'DFS', 'Passos'].values,
   'BFS': df.loc[df['Tipo'] == 'BFS', 'Passos'].values,
   'Dijkstra': df.loc[df['Tipo'] == 'Dijkstra', 'Passos'].values
   }, index=df.Maze.unique())

df_Custo = pd.DataFrame({
   'DFS': df.loc[df['Tipo'] == 'DFS', 'Tamanho da Busca - Custo'].values,
   'BFS': df.loc[df['Tipo'] == 'BFS', 'Tamanho da Busca - Custo'].values,
   'Dijkstra': df.loc[df['Tipo'] == 'Dijkstra', 'Tamanho da Busca - Custo'].values
   }, index=df.Maze.unique())

df_Tempo = pd.DataFrame({
   'DFS': df.loc[df['Tipo'] == 'DFS', 'Tempo'].values,
   'BFS': df.loc[df['Tipo'] == 'BFS', 'Tempo'].values,
   'Dijkstra': df.loc[df['Tipo'] == 'Dijkstra', 'Tempo'].values
   }, index=df.Maze.unique())

fig, axes = plt.subplots(nrows=2, ncols=2)

df_Passos.plot(ax=axes[0,0], title = 'Passos')
df_Custo.plot(ax=axes[0,1], title = 'Custo')
df_Tempo.plot(ax=axes[1,0], title = 'Tempo')

fig.suptitle('Resultados', fontsize=15)
plt.subplots_adjust(wspace=0.25, 
                    hspace=0.5)
plt.figure(figsize=(60,100))
fig.savefig('resultados.png')

# Salva o arquivo de resultados
df.to_csv('Resultados.csv', index=False)