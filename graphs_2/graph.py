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

    def dijkstra(self, start: str, end: str | None = None):
        """Algoritmo de Dijkstra para grafo dirigido ponderado.

        Usa `self.adjacency_list.nodesExit` como lista de adyacencia:
        - keys: nodo source (string)
        - values: lista de tuplas (target, weight)

        Args:
            start: nodo origen (string)
            end: nodo destino (string) opcional.

        Returns:
            Si end es None: dict con distancias mínimas.
            Si end no es None: (dist, path) donde path es lista de nodos.
        """
        nodes = list(self.adjacency_list.nodesList)
        nodes_set = set(nodes)
        if start not in nodes_set:
            return float("inf"), []

        if end is not None and end not in nodes_set:
            return float("inf"), []


        import heapq

        # distancia mínima conocida
        dist: dict[str, float] = {node: float("inf") for node in nodes}
        dist[start] = 0.0

        # para reconstruir ruta
        prev: dict[str, str | None] = {node: None for node in nodes}

        pq: list[tuple[float, str]] = [(0.0, start)]

        while pq:
            cur_dist, u = heapq.heappop(pq)
            if cur_dist != dist[u]:
                continue

            if end is not None and u == end:
                break

            for v, w in self.adjacency_list.nodesExit.get(u, []) :
                # weight viene como string; permitir ints/float
                try:
                    weight = float(w)
                except (TypeError, ValueError):
                    weight = float(str(w).strip())

                if dist[u] + weight < dist.get(v, float("inf")):
                    dist[v] = dist[u] + weight
                    prev[v] = u
                    heapq.heappush(pq, (dist[v], v))

        if end is None:
            return dist

        if end not in dist:
            return float("inf"), []

        if dist[end] == float("inf"):
            return float("inf"), []

        # reconstruir ruta
        path = []
        cur: str | None = end
        while cur is not None:
            path.append(cur)
            if cur == start:
                break
            cur = prev[cur]

        path.reverse()
        if not path or path[0] != start:
            return float("inf"), []

        return dist[end], path

    def isTree(self):

        """Verifica si el grafo recibido es un árbol (no dirigido).

        Condiciones para árbol en grafo no dirigido:
        - No tiene ciclos
        - Es conexo
        - Tiene exactamente n-1 aristas (equivalente si es conexo y acíclico)

        Nota: usa `adjacency_list.edge_reg` como conjunto de aristas (u,v) normalizadas.
        """

        nodes = list(self.adjacency_list.nodesList)

        n = len(nodes)
        if n == 0:
            return False

        # Construir grafo no dirigido para conectividad y detección de ciclos (DFS)
        adj_undirected: dict[str, set[str]] = {node: set() for node in nodes}
        edges = set()
        for u, v in self.adjacency_list.edge_reg:
            u = str(u)
            v = str(v)
            if u == v:
                return False  # lazo propio => ciclo
            edges.add((u, v))
            adj_undirected.setdefault(u, set()).add(v)
            adj_undirected.setdefault(v, set()).add(u)

        # Conectividad (BFS/DFS)
        start = nodes[0]
        visited: set[str] = set()
        stack = [start]
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            for nxt in adj_undirected.get(cur, set()):
                if nxt not in visited:
                    stack.append(nxt)

        isConex = len(visited) == n
        if not isConex:
            return False

        # Si es conexo, para que sea árbol debe tener exactamente n-1 aristas
        m = len(edges)
        return m == n - 1
    
    def has_eulerian_circuit(self) -> bool:
        if not self.is_weakly_connected():
            return False
        

    def is_weakly_connected(self) -> bool:
        nodes = list(self.adjacency_list.nodesList)
        if not nodes:
            return True
        
        active_nodes = set()
        adj_undirected: dict[str, set[str]] = {}

        for u, v in self.adjacency_list.edge_red:
            u, v = str(u), str(v)
            active_nodes.add(u)
            active_nodes.add(v)
            adj_undirected.setdefault(u, set()).add(v)
            adj_undirected.setdefault(v, set()).add(u)

        if not active_nodes:
            return True
        
        start = list(active_nodes)[0]
        visited = set()
        stack = [start]

        while stack:
            cur = stack.pop()
            if cur not in visited:
                visited.add(cur)
                for nxt in adj_undirected.get(cur, set()):
                    if nxt not in visited:
                        stack.append(nxt)

        return len(visited) == len(active_nodes)
    
    def has_eulerian_circuit(self) -> bool:
        """
        Retorna True si el grafo dirigido tiene un circuito de Euler.
        """
        if not self.is_weakly_connected():
            return False

        for node in self.nodes_list:
            in_degree = len(node.targeted)
            out_degree = len(node.targets)

            if in_degree != out_degree:
                return False

        return True
      
     def has_eulerian_path(self) -> bool:
        """
        Retorna True si el grafo dirigido tiene un camino de Euler.
        """
        if not self.is_weakly_connected():
            return False

        if self.has_eulerian_circuit():
            return True

        start_nodes = 0
        end_nodes = 0
        balanced_nodes = 0
        total_nodes = len(self.nodes_list)

        for node in self.nodes_list:
            in_degree = len(node.targeted)
            out_degree = len(node.targets)

            if out_degree - in_degree == 1:
                start_nodes += 1
            elif in_degree - out_degree == 1:
                end_nodes += 1
            elif in_degree == out_degree:
                balanced_nodes += 1
            else:
                return False

        return start_nodes == 1 and end_nodes == 1 and (balanced_nodes == total_nodes - 2)