from BFSDemo import BFS
from DFSDemo import DFS
from dijkstraMaze import dijkstra
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

m=maze(20,30)
m.CreateMaze(2,10,loopPercent=100,loadMaze='pathMaze.csv')

searchPath,dfsPath,fwdDFSPath=DFS(m)
bSearch,bfsPath,fwdBFSPath=BFS(m)
fwdDijPath,cDij=dijkstra(m)


textLabel(m,'DFS - Tamanho do Caminho',len(fwdDFSPath)+1)
textLabel(m,'BFS - Tamanho do Caminho',len(fwdBFSPath)+1)
textLabel(m,'Dijkstra - Tamanho do Caminho',len(fwdDijPath)+1)
textLabel(m,'DFS - Tamanho da Busca',len(searchPath)+1)
textLabel(m,'BFS - Tamanho da Busca',len(bSearch)+1)
textLabel(m,'Dijkstra - Custo Total',cDij)

a=agent(m,footprints=True,color=COLOR.cyan,shape='arrow')
b=agent(m,footprints=True,color=COLOR.yellow,shape='arrow')
c=agent(m,footprints=True,color=COLOR.green,shape='arrow')


m.tracePath({a:fwdBFSPath},delay=50)
m.tracePath({b:fwdDFSPath},delay=10)
m.tracePath({c:fwdDijPath},delay=50)

t1=timeit(stmt='DFS(m)',number=1000,globals=globals())
t2=timeit(stmt='BFS(m)',number=1000,globals=globals())
t3=timeit(stmt='dijkstra(m)',number=1000,globals=globals())

textLabel(m,'DFS - Tempo:',t1)
textLabel(m,'BFS - Tempo:',t2)
textLabel(m,'Dijkstra - Tempo:',t3)

m.run()
