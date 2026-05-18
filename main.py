from  graph import Graph
from adjacencyList import AdjacencyList

def main():
    #Inicializar la lista de adyacencia con lectura de un archivo txt
    adjacency_list = AdjacencyList()

    #Inicializar el grafo con la lista de adyacencia cargada
    grafo = Graph(adjacency_list)

    grafo.show_nodes()

    grafo.degreeOut("A")
    grafo.degreeIn("A")
    grafo.IsAMultigraph()
    grafo.IsACompleteGraph()

if __name__ == "__main__":
    main()