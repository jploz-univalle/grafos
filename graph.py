from adjacencyList import AdjacencyList
from node import Node

class Graph:
    def __init__(self, adjacencyList: AdjacencyList):
        self.nodes_list = []
        self.adjacency_list = adjacencyList
        self.constructByAdjacencyList()

    # Carga la lista de adyacencia a la entidad grafo
    def constructByAdjacencyList (self) -> None:
        for node_name in self.adjacency_list.nodesList:
            self.nodes_list.append(Node(source=node_name,
                                   targets=self.adjacency_list.nodesExit.get(node_name, list()),
                                   targeted=self.adjacency_list.nodesEntry.get(node_name, list())
                                   )
                                )


    # Muestra informacion acerca de los nodos
    def show_nodes(self) -> None:
        print("\tShow all")
        for node in self.nodes_list:
            node:Node
            print(f"{node.targeted} => {node.source} => {node.targets}")

        print("\n\tDetails")
        for node in self.nodes_list: 
            for target in node.targets:
                target:tuple
                print(f"Source: {node.source}\tTarget:{target[0]}\tWeight:{target[1]}")

    # Cuenta el grado de salida de un nodo
    def degreeOut(self, node_name: str) -> None:
        print("El grado de salida del nodo: "+node_name+"es :" + len(self.findNodeByName(node_name).targets))

    # Cuenta el grado de entrada de un nodo
    def degreeIn(self, node_name: str) -> None:
        print("El grado de entrada del nodo: "+node_name+"es :" + len(self.findNodeByName(node_name).targeted))
        
    # Encontrar un Nodo por su nombre 
    def findNodeByName(self, node_name): 
        for node in self.nodes_list:
            if node.source == node_name:
                node:Node
                return node

    
    # Definir si es un grafo simple o multigrafo
    def IsAMultigraph(self) -> None:
        relations = []
        for node in self.nodes_list:
            for target in node.targets:
                edge = tuple([node.source, target[0]])
                if edge in relations:
                    print("Es un multigrafo.")
                    return
                
                relations.append(tuple([node.source, target[0]]))
        print("Es un grafo simple.")

    def IsACompleteGraph(self) -> None:
        listOfNodes = set(self.adjacency_list.nodesList)

        for node_name in listOfNodes: 
            actual = listOfNodes - set(node_name)
            node = self.findNodeByName(node_name)

            if set(node.targeted) != actual:
                print("No es un grafo completo")
                return
        
        print("Es un grafo completo.")


    