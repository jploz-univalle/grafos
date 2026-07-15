from  graphs_2.graph import Graph
from graphs_2.adjacencyList import AdjacencyList
from graphs_2.GUI import Graphic as Window
import threading

def main() -> None:
    """Metodo para inicializar la consola
    """    

    print("El archivo (.txt o .csv) debe estar en la carpeta ./data")
    file_name = input("Por favor ingrese el nombre del archivo: ")
    
    #Inicializar la lista de adyacencia con lectura de un archivo o csv
    adjacency_list = AdjacencyList(file_name) 

    #Inicializar el grafo con la lista de adyacencia cargada
    grafo = Graph(adjacency_list)

    def show_node_info():
        grafo.show_nodes()
        waitConfirm()
    
    def show_entry_degree():
        print("Nodos disponibles: " + grafo.getNodesStr())
        op = input(">")
        grafo.degreeOut(op)
        waitConfirm()
    
    def show_exit_degree():
        print("Nodos disponibles: " + grafo.getNodesStr())
        op = input(">")
        grafo.degreeIn(op)
        waitConfirm()

    def isMultigraphOrSimplegraph(): 
        grafo.IsAMultigraph()
        waitConfirm()

    def isFullGraph():
        grafo.IsACompleteGraph()
        waitConfirm()
    
    def visualizeGraph():
        def load_window():
            Window(grafo=grafo)
        
        t = threading.Thread(target=load_window, daemon=True)
        t.start()
    
    def isGraphTree():
        if grafo.isTree():
            print("Si, el grafo es un arbol porque es conexo y m = n - 1.")
        else:
            print("No es un arbol.")
        waitConfirm()

    def dijkstraAlgorithm():
        startNode = input("Ingrese el nodo de inicio: ")
        endNode = input("Ingrese el nodo final: ")
        weigth, route = grafo.dijkstra(startNode, endNode)
        if weigth != "inf":
            print(f"La ruta entre {startNode} y {endNode} tiene el peso: {weigth} y la ruta: {route}")
        else:
            print("Los nodos seleccionados no son validos para el algoritmo dijkstra")
        waitConfirm()

    def hasEulerPath():
        if grafo.has_eulerian_path():
            print("Sí, el grafo tiene al menos un camino de Euler.")
        else:
            print("No, el grafo no contiene ningún camino de Euler.")
        waitConfirm()
    
    def hasEulerCircuit():
        if grafo.has_eulerian_circuit():
            print("Sí, el grafo tiene un circuito de Euler.")
        else:
            print("No, el grafo no contiene ningún circuito de Euler.")
        waitConfirm()

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
7.\tEs el grafo un arbol?
8.\tAlgoritmo de dijkstra.
9.\t¿Tiene un camino de Euler?
10.\t¿Tiene un circuito de Euler?
11.\tSalir.""")
        option = int(input("> "))

        match option:
            case 1:
                show_node_info()
            case 2:
                show_entry_degree()
            case 3:
                show_exit_degree()
            case 4:
                isMultigraphOrSimplegraph()
            case 5:
                isFullGraph()
            case 6:
                visualizeGraph()
            case 7:
                isGraphTree()
            case 8:
                dijkstraAlgorithm()
            case 9:
                hasEulerPath()
            case 10:
                hasEulerCircuit()
            case 11:
                print("Saliendo...")
                break
            case _:
                print("Instrucción incorrecta, elige nuevamente.")

        print("-"*80)

def waitConfirm():
    input("Presiona Enter para continuar...")