# here graph is a dictionary with keys and multiple values 
# We use queue concept for bfs
graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
    }
visited=[] # list for visited nodes
queue=[] #Intilialize a queu
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue : # creating loop to visit each node
        m=queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(visited,graph,'5') #function call