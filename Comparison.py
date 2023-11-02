from BFSDemo import BFS
from DFSDemo import DFS
from dijkstraMaze import dijkstra
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit
import pandas as pd

m=maze(20,20)
m.CreateMaze(loopPercent=100, loadMaze='pathMaze.csv')


searchPath,dfsPath,fwdDFSPath=DFS(m)
bSearch,bfsPath,fwdBFSPath=BFS(m)
fwdDijPath,cDij=dijkstra(m)


textLabel(m,'DFS - Passos',len(fwdDFSPath)+1)
textLabel(m,'BFS - Passos',len(fwdBFSPath)+1)
textLabel(m,'Dijkstra - Passos',len(fwdDijPath)+1)
textLabel(m,'DFS - Tamanho da Busca',len(searchPath)+1)
textLabel(m,'BFS - Tamanho da Busca',len(bSearch)+1)
textLabel(m,'Dijkstra - Custo Total',cDij)

a=agent(m,footprints=True,color=COLOR.cyan,shape='arrow')
b=agent(m,footprints=True,color=COLOR.yellow,shape='arrow')
c=agent(m,footprints=True,color=COLOR.green,shape='arrow')

d=agent(m,footprints=True,color=COLOR.cyan,shape='arrow')
e=agent(m,footprints=True,color=COLOR.yellow,shape='arrow')
f=agent(m,footprints=True,color=COLOR.green,shape='arrow')


m.tracePath({a:fwdBFSPath},delay=60,kill=True)
m.tracePath({b:fwdDFSPath},delay=60,kill=True)
m.tracePath({c:fwdDijPath},delay=60,kill=True)

m.tracePath({d:fwdBFSPath},delay=60)
m.tracePath({e:fwdDFSPath},delay=60)
m.tracePath({f:fwdDijPath},delay=60)

t1=timeit(stmt='DFS(m)',number=1000,globals=globals())
t2=timeit(stmt='BFS(m)',number=1000,globals=globals())
t3=timeit(stmt='dijkstra(m)',number=1000,globals=globals())

textLabel(m,'DFS - Tempo:',t1)
textLabel(m,'BFS - Tempo:',t2)
textLabel(m,'Dijkstra - Tempo:',t3)

# Resultados

df = pd.DataFrame(columns=['Tipo', 'Passos', 'Tamanho da Busca - Custo', 'Tempo'])
dfBFSpath = pd.DataFrame()
dfDFSPath = pd.DataFrame()
dfDijkstraPath = pd.DataFrame()

linha1 = pd.Series({'Tipo': 'DFS', 'Passos': len(fwdDFSPath)+1, 'Tamanho da Busca - Custo': len(searchPath)+1, 'Tempo': t1})
linha2 = pd.Series({'Tipo': 'BFS', 'Passos': len(fwdBFSPath)+1, 'Tamanho da Busca - Custo': len(bSearch)+1, 'Tempo': t2})
linha3 = pd.Series({'Tipo': 'Dijkstra', 'Passos': len(fwdDijPath)+1, 'Tamanho da Busca - Custo': cDij, 'Tempo': t3})

BFSpath = pd.Series(fwdBFSPath)
DFSpath = pd.Series(fwdDFSPath)
Dijkstrapath = pd.Series(fwdDijPath)

df = df._append(linha1, ignore_index=True)
df = df._append(linha2, ignore_index=True)
df = df._append(linha3, ignore_index=True)

dfBFSpath = dfBFSpath._append(fwdBFSPath, ignore_index=True)
dfDFSPath = dfDFSPath._append(DFSpath, ignore_index=True)
dfDijkstraPath = dfDijkstraPath._append(Dijkstrapath, ignore_index=True)

df.to_csv('Resultados.csv', index=False, sep=';')
dfBFSpath.to_csv('BFS.csv', index=False, sep=';')
dfDFSPath.to_csv('DFS.csv', index=False, sep=';')
dfDijkstraPath.to_csv('Dijkstra.csv', index=False, sep=';')

m.run()


