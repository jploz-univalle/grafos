from  graphs_1.graph import Graph
from graphs_1.adjacencyList import AdjacencyList
from graphs_1.GUI import Graphic as Window
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
                grafo.show_nodes()
                waitConfirm()
            case 2:
                print("Nodos disponibles: " + grafo.getNodesStr())
                op = input(">")
                grafo.degreeOut(op)
                waitConfirm()
            case 3:
                print("Nodos disponibles: " + grafo.getNodesStr())
                op = input(">")
                grafo.degreeIn(op)
                waitConfirm()
            case 4:
                grafo.IsAMultigraph()
                waitConfirm()
            case 5:
                grafo.IsACompleteGraph()
                waitConfirm()
            case 6:
                def load_window():
                    Window(grafo=grafo)
                
                t = threading.Thread(target=load_window, daemon=True)
                t.start()

            case 7:
                if grafo.isTree():
                    print("Si, el grafo es un arbol porque es conexo y m = n - 1.")
                else:
                    print("No es un arbol.")
                waitConfirm()
            case 8:
                startNode = input("Ingrese el nodo de inicio: ")
                endNode = input("Ingrese el nodo final: ")
                weigth, route = grafo.dijkstra(startNode, endNode)
                if weigth != "inf":
                    print(f"La ruta entre {startNode} y {endNode} tiene el peso: {weigth} y la ruta: {route}")
                else:
                    print("Los nodos seleccionados no son validos para el algoritmo dijkstra")
                waitConfirm()
            case 9:
                if grafo.has_eulerian_path():
                    print("Sí, el grafo tiene al menos un camino de Euler.")
                else:
                    print("No, el grafo no contiene ningún camino de Euler.")
                waitConfirm()
            case 10:
                if grafo.has_eulerian_circuit():
                    print("Sí, el grafo tiene un circuito de Euler.")
                else:
                    print("No, el grafo no contiene ningún circuito de Euler.")
                waitConfirm()
            case 11:
                print("Saliendo...")
                break
            case _:
                print("Instrucción incorrecta, elige nuevamente.")

        print("-"*80)

def waitConfirm():
    input("Presiona Enter para continuar...")