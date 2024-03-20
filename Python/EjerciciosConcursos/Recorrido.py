import copy
def llenar_Grafo(m):
    graph = {}
    renewalRoads = []
    
    for i in range(int(m)):
        u, v, l = input().split()
        rn = u, v
        renewalRoads.append(rn)
        if u in graph:
            nodes = graph[u]
            nodes[v] = int(l)
            graph[u] = nodes
        else:
            graph[u] = {v: int(l)}
            
        if v in graph:        
            nodes = graph[v]
            nodes[u] = int(l)
            graph[v] = nodes
        else:
            graph[v] = {u: int(l)}
    
    return graph, renewalRoads

def encontrar_camino(graph, road, n):
    bestPath = -1

    neighbors = list(graph[road[0]].keys())
    if road[1] in neighbors: neighbors.remove(road[1])
    
    if road[0] == '2': print(neighbors)
    
    for node in neighbors:
        totalWeight = graph[road[0]][node]
        visited = [road[0], node]
        result = recorrer_camino(graph, visited, road, totalWeight ,n)
        if bestPath == -1: bestPath = result
        elif result < bestPath and result != -1: bestPath = result
    
    return bestPath

def recorrer_camino(graph, visited, road, totalWeight, n):
    
    origNode = visited[-1]
    neighbors = list(graph[origNode].keys())
    if road[0] == '2': print(origNode,"\n",neighbors, "\n", visited, "\n", visited[-2])
    if road[1] == origNode:
        return totalWeight
    else:
        if(n <= 0): 
            return -1
        else:
            bestPath = -1
            for node in neighbors:
                print(f"Deberia ser opcion el nodo: {node}")
                isVisited = node in visited
                print(isVisited)
                if isVisited == False:
                    print(f"{node} si es opcion")
                    totalWeight += graph[origNode][node]
                    vis = copy.copy(visited)
                    vis.append(node)
                    print(vis, visited)
                    result = recorrer_camino(graph, vis, road, totalWeight, n-1)
                    if bestPath == -1: bestPath = result
                    elif result < bestPath and result != -1: bestPath = result
    return bestPath

    return 


if __name__ == '__main__':
    n, m = input().split()
    graph = {}
    
    print('nodes')
    graph, renewalRoads  = llenar_Grafo(m)
    for road in renewalRoads:
        print(f'-----------------------------------\nPeso para camino: {road}')
        print(f'resultado: ', encontrar_camino(graph, road, int(n)))

        
    