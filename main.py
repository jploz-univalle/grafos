from  graph import Graph
from adjacencyList import AdjacencyList
from GUI import Graphic as Window

def main():
    #Inicializar la lista de adyacencia con lectura de un archivo txt
    adjacency_list = AdjacencyList()

    #Inicializar el grafo con la lista de adyacencia cargada
    grafo = Graph(adjacency_list)

    # grafo.show_nodes()
    # grafo.degreeOut("A")
    # grafo.degreeIn("A")
    # grafo.IsAMultigraph()
    # grafo.IsACompleteGraph()
    #Window(grafo)

    while True: 
        print("\t\tPrograma piloto de grafos")
        print("seleccione una opcion: ")
        print(
"""1.\tMostrar informacion de nodos.
2.\tMostrar grado de salida de un nodo.
3.\tMostrar grado de entrada de un nodo.
4.\tEs un multigrafo o un grafo simple?
5.\tEs un grafo completo?
6.\tVisualizar grafo.
7.\tSalir.""")
        option = int(input("> "))

        match option:
            case 1:
                grafo.show_nodes()
            case 2:
                print("Nodos disponibles: " + grafo.getNodesStr())
                op = input("> ")
                grafo.degreeOut(op)
            case 3:
                print("Nodos disponibles: " + grafo.getNodesStr())
                op = input("> ")
                grafo.degreeIn(op)
            case 4:
                grafo.IsAMultigraph()
            case 5:
                grafo.IsACompleteGraph()
            case 6:
                Window(grafo=grafo)
            case 7:
                print("Saliendo...")
                break
            case _:
                print("Instruccion incorrecta, elige nuevamente.")

        print("-"*80)


if __name__ == "__main__":
    main()