# Complete the evenForest function below.

from re import A


def evenForest(t_nodes, t_edges, t_from, t_to):
    
    nRemovedEdges = 0
    arregloNodos = []
    nodoSolo = []
    vsolo = 0
    
    for i in range(t_nodes):
        arregloNodos.append([])
        # Crea un arreglo con la cantidad total de puntos (nodos)
    cordenadas = list(zip(t_from, t_to))
    # Junta los puntos para hacerlos 2D, matriz t_nodesx2
    for valorFrom, valorTo in cordenadas:
        arregloNodos[valorFrom-1].append(valorTo)
        arregloNodos[valorTo-1].append(valorFrom)
        # Realiza el conteo de nodos, si se tiene (1,2),(1,3) = [[2,3],[1],[1]]

    for j in range(0, len(arregloNodos[:])):
        if len(arregloNodos[j]) == 1:
            nodoSolo.append(arregloNodos[j])
    print(arregloNodos[:])
    print(nodoSolo[:])

    for k in nodoSolo[:]:
        vsolo = k
        print(vsolo)
        #TODO
    
    return nRemovedEdges
