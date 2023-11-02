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
dimensionsList = [(10,10),(20,20),(30,30),(40,40),(50,50),(60,60),(70,70),(80,80),(90,90),(100,100)]

# 

for teste in range(len(dimensionsList)):
   linhas = dimensionsList[teste][0]
   colunas = dimensionsList[teste][1]
   print('Tamanho: ', linhas, 'x', colunas, '\n')
   
   # Cria o labirinto
   m=maze(linhas,colunas) #Dimensões
   m.CreateMaze(loopPercent=100) #(Destino, Maximiza os caminhos, carrega o labirinto)

   # Algoritmo - Busca DFS
   searchPath,dfsPath,fwdDFSPath=DFS(m)
   # Algoritmo - Busca BFS
   bSearch,bfsPath,fwdBFSPath=BFS(m)
      # Algoritmo - Busca Dijkstra
   fwdDijPath,cDij=dijkstra(m)
   
   # Labels legenda (resultados linha superior)
   # textLabel(m,'DFS - Passos',len(fwdDFSPath)+1)
   # textLabel(m,'BFS - Passos',len(fwdBFSPath)+1)
   # textLabel(m,'Dijkstra - Passos',len(fwdDijPath)+1)
   # textLabel(m,'DFS - Tamanho da Busca',len(searchPath)+1)
   # textLabel(m,'BFS - Tamanho da Busca',len(bSearch)+1)
   # textLabel(m,'Dijkstra - Custo Total',cDij)

   # Definição dos agentes (que objetos que percorrem)
   a=agent(m,footprints=True,color=COLOR.cyan,shape='arrow')
   b=agent(m,footprints=True,color=COLOR.yellow,shape='arrow')
   c=agent(m,footprints=True,color=COLOR.green,shape='arrow')

   # Execução das buscas {agente:algoritmo da busca}
   m.tracePath({a:fwdBFSPath},delay=1,kill=True)
   m.tracePath({b:fwdDFSPath},delay=1,kill=True)
   m.tracePath({c:fwdDijPath},delay=1,kill=True)

   # Definição do timer de cada busca
   t1=timeit(stmt='DFS(m)',number=1000,globals=globals())
   t2=timeit(stmt='BFS(m)',number=1000,globals=globals())
   t3=timeit(stmt='dijkstra(m)',number=1000,globals=globals())

   # Labels legenda (resultados linha superior)
   # textLabel(m,'DFS - Tempo:',t1)
   # textLabel(m,'BFS - Tempo:',t2)
   # textLabel(m,'Dijkstra - Tempo:',t3)

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
   'Dijkstra': df.loc[df['Tipo'] == 'Dijkstra', 'Passos'].values}, index=df.Maze.unique())

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

# fig1, axes = plt.subplots(nrows=2, ncols=2)

# df_Passos.plot(ax=axes[0,0], title = 'Passos')
# df_Custo.plot(ax=axes[0,1], title = 'Custo')
# df_Tempo.plot(ax=axes[1,0], title = 'Tempo')

# fig1.suptitle('Resultados', fontsize=15)
# plt.subplots_adjust(wspace=0.25, 
#                      hspace=0.5)
# plt.figure(figsize=(120,200))
# fig1.savefig('Resultados.png')

# Plot e salve o gráfico de 'Passos'
fig1, ax1 = plt.subplots()
df_Passos.plot(ax=ax1, title='Passos')
fig1.suptitle('Resultados - Passos', fontsize=15)
fig1.savefig('Passos.png')
plt.close(fig1)  # Fecha a figura para liberar memória

# Plot e salve o gráfico de 'Custo'
fig2, ax2 = plt.subplots()
df_Custo.plot(ax=ax2, title='Custo')
fig2.suptitle('Resultados - Custo', fontsize=15)
fig2.savefig('Custo.png')
plt.close(fig2)  # Fecha a figura para liberar memória

# Plot e salve o gráfico de 'Tempo'
fig3, ax3 = plt.subplots()
df_Tempo.plot(ax=ax3, title='Tempo')
fig3.suptitle('Resultados - Tempo', fontsize=15)
fig3.savefig('Tempo.png')
plt.close(fig3)  # Fecha a figura para liberar memória

# Salva o arquivo de resultados
df.to_csv('Resultados.csv', index=False)