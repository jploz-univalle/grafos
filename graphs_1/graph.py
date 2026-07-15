from graphs_1.adjacencyList import AdjacencyList
from graphs_1.node import Node

class Graph:
    """Esta clase representa un grafo
    """    

    def __init__(self, adjacencyList: AdjacencyList):
        self.nodes_list = []
        self.adjacency_list = adjacencyList
        self.construct_by_adjancency_list()

    # Carga la lista de adyacencia a la entidad grafo
    def construct_by_adjancency_list (self) -> None:
        """Permite incializar una lista de objetos node: list[Node]
        """        
        for node_name in self.adjacency_list.nodesList:
            self.nodes_list.append(
                Node(
                    source=node_name,
                    targets=self.adjacency_list.nodesExit.get(node_name, list()),
                    targeted=self.adjacency_list.nodesEntry.get(node_name, list())
                    )
                )


    # Muestra informacion acerca de los nodos
    def show_nodes(self) -> None:
        """Muestra informacion sobre los nodos
        """        
        print("\tShow all")
        for node in self.nodes_list:
            print(f"{node.targeted} => {node.source} => {node.targets}")

        print("\n\tDetails")
        for node in self.nodes_list: 
            for target in node.targets:
                print(f"Source: {node.source}\tTarget:{target[0]}\tWeight:{target[1]}")

    def getNodesStr(self) ->str:
        """Retorna los nodos existentes

        Returns:
            str: Nombres de nodos separados por espacios
        """        
        return " ".join([node.source for node in self.nodes_list])

    # Cuenta el grado de salida de un nodo
    def degreeOut(self, node_name: str) -> None:
        """Muestra el grado de salida de un nodo en especifico

        Args:
            node_name (str): Nombre del nodo a mostrar el grado de salida
        """
        node = self.findNodeByName(node_name)
        if node is not None:
            print(f"El grado de salida del nodo: {node_name} es: {len(node.targeted)}")

    # Cuenta el grado de entrada de un nodo
    def degreeIn(self, node_name: str) -> None:
        """Muestra el grado de entrada de un nodo en especifico

        Args:
            node_name (str): Nombre del nodo a mostrar el grado de entrada
        """
        node = self.findNodeByName(node_name)
        if node is not None:
            print(f"El grado de entrada del nodo: {node_name} es: {len(node.targeted)}")
        
    # Encontrar un Nodo por su nombre 
    def findNodeByName(self, node_name: str) -> None | Node:
        """Retorna un objeto Node buscando por su nombre (Node.source)

        Args:
            node_name (str): Nombre del nodo a buscar

        Returns:
            Node: Objeto Node buscado.
        """        
        for node in self.nodes_list:
            if node.source == node_name:
                return node
            
        print("El nodo buscado no existe.")
        return None

    
    # Definir si es un grafo simple o multigrafo
    def IsAMultigraph(self) -> None:
        """Dice si es un multigrafo o un grafo simple
        """        
        relations = []
        for node in self.nodes_list:
            for target in node.targets:
                edge = tuple([node.source, target[0]])
                if edge in relations:
                    print("Es un multigrafo.")
                    return
                relations.append(edge)
        print("Es un grafo simple.")

    def IsACompleteGraph(self) -> None:
        """Dice si es un grafo completo o no
        """        
        listOfNodes = set(self.adjacency_list.nodesList)

        for node_name in listOfNodes: 
            remaining_nodes = listOfNodes - set([node_name])
            node = self.findNodeByName(node_name)

            if node is dict or set(node.targeted) != remaining_nodes:
                print("No es un grafo completo")
                return
        
        print("Es un grafo completo.")


    