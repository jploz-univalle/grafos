from  graphs_1.graph import Graph
from graphs_1.adjacencyList import AdjacencyList
from graphs_1.GUI import Graphic as Window

def main() -> None:
    """Metodo para inicializar la consola
    """    

    print("El archivo (.txt o .csv) debe estar en la carpeta ./data")
    file_name = input("Por favor ingrese el nombre del archivo: ")
    
    #Inicializar la lista de adyacencia con lectura de un archivo o csv
    adjacency_list = AdjacencyList(file_name)

    #Inicializar el grafo con la lista de adyacencia cargada
    grafo = Graph(adjacency_list)

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