import tkinter as tk
import math

from graphs_1.graph import Graph
from graphs_1.graphicNode import GraphicNode
from graphs_1.node import Node
from graphs_1.graphicEdge import GraphicEdge


class Graphic:
    """Clase que representa la interfaz grafica
    """    
    def __init__(self, grafo: Graph) -> None:

        self.window_loader()

        # Variables de operacion para logica de calculo de posiciones
        self.surrounding = 360/len(grafo.adjacency_list.nodesList)
        self.centerDistance = 180
        self.ovalSize=40
        self.radius=self.ovalSize/2
        self.graphic_nodes_list = list()
        
        # Cargare elementos visuales
        self.load_nodes(grafo)
        self.load_arrows()

        # Bucle principal de la ventana, interrumpe el flujo de ejecucion de la consola
        self.ventana.mainloop()

    def load_nodes(self, grafo: Graph) -> None:
        """Permite cargar los nodos en la GUI

        Args:
            grafo (Graph): entidad grafo
        """        

        degreeCount = self.surrounding

        # Graficar y ordenar los nodos en forma circundante
        for node in grafo.nodes_list:
            node:Node
            theta = math.radians(degreeCount) # Calcular de forma proporcional al centro

            x = self.CENTER_WIDTH - self.centerDistance * math.cos(theta)
            y = self.CENTER_HEIGHT - self.centerDistance * math.sin(theta)

            id = self.create_oval(self.ovalSize, x, y)
            self.canvas.create_text(x,y, text=node.source)

            self.graphic_nodes_list.append(
                GraphicNode(
                    id = id,
                    source=node.source,
                    targets=node.targets,
                    targeted=node.targeted,
                    coox=x,
                    cooy=y,
                    ovalSize=self.ovalSize,
                    radius=self.radius
                )
            )
            degreeCount+=self.surrounding

    def load_arrows(self) -> None:
        """Permite cargar las aristas de los nodos en la GUI
        """        
        # Crear aristas
        for graphicNode in self.graphic_nodes_list:
            graphicNode:GraphicNode

            for target in graphicNode.targets:
                if graphicNode.source == target[0]:
                    self.canvas: tk.Canvas
                    self.canvas.itemconfig(graphicNode.ID, fill="red")
                    continue
                
                edge = GraphicEdge(
                        graphicNode,
                        self.findNodeByName(target[0],self.graphic_nodes_list),
                        weight=target[1]
                    )

                graphicNode.edges_list.append(
                    edge
                )

                edge.create_arrow(
                    self.canvas
                )

    def window_loader(self) -> None:
        """Carga la configuracion inicial de la GUI
        """        
        self.ventana = tk.Tk()
        self.ventana.title("Visualizador de Grafo")

        self.canvas = tk.Canvas(self.ventana, width=800, height=600, bg="white")
        self.CENTER_WIDTH = 400
        self.CENTER_HEIGHT = 300
        self.canvas.pack()

        # Centro simulado de referencia
        self.canvas.create_oval(self.CENTER_WIDTH-10, self.CENTER_HEIGHT-10, self.CENTER_WIDTH+10, self.CENTER_HEIGHT+10, fill="lightblue")
        self.canvas.create_text(self.CENTER_WIDTH, self.CENTER_HEIGHT, text="O")

    # Metodo para crear ovalos(Nodos) rapidamente
    def create_oval(self, size: int, x:int, y:int) -> int:
        """Crea un ovalo sencillo

        Args:
            size (int): tamaño del ovalo
            x (int): coordenada x
            y (int): coordenada y
        """        
        sizeFactor = size // 2
        return self.canvas.create_oval(x-sizeFactor, y-sizeFactor, x+sizeFactor, y+sizeFactor, fill="lightblue")

            
    def findNodeByName(self, name:str, graphic_nodes_list: list) -> GraphicNode | None:
        """Buscar nodo por nombre

        Args:
            name (str): Nombre del nodo a buscar
            graphic_nodes_list (list): Lista de nodos graficos list[GraphicNode]

        Returns:
            None: No se encontro el nodo
            GraphicNode: Se encontro el nodo
        """            
        for grnode in graphic_nodes_list:
            grnode:GraphicNode
            if grnode.source == name:
                return grnode
            
        return None