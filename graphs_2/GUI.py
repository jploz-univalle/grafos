import tkinter as tk
import math

from graphs_2.graph import Graph
from graphs_2.graphicNode import GraphicNode
from graphs_2.node import Node
from graphs_2.graphicEdge import GraphicEdge


class Graphic:
    """Clase que representa la interfaz grafica
    """    
    def __init__(self, grafo: Graph) -> None:

        self.window_loader()

        # Variables de operacion para logica de calculo de posiciones
        self.numberOfNodes = len(grafo.adjacency_list.nodesList)
        self.surrounding = 360/self.numberOfNodes
        self.increment_center_distance_coeficient = self.numberOfNodes//32
        self.centerDistance = 200 * max(1, self.numberOfNodes / 32)
            
        self.ovalSize=20
        self.radius=self.ovalSize/2
        self.graphic_nodes_list = list()
        
        # Cargar elementos visuales
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
                
                edge = GraphicEdge(
                        graphicNode,
                        self.findNodeByName(target[0],self.graphic_nodes_list),
                        weight=target[1]
                    )

                graphicNode.edges_list.append(edge)

                edge.create_arrow(self.canvas)

    def window_loader(self) -> None:
        """Carga la configuracion inicial de la GUI
        """        
        self.ventana = tk.Tk()
        self.ventana.title("Visualizador de Grafo")
        self.ventana.geometry(f"{self.ventana.winfo_screenwidth()}x{self.ventana.winfo_screenheight()}")

        def zoom(event):
            factor = 1.1 if event.delta > 0 else 0.9

            self.canvas.scale(
                "all",
                event.x,
                event.y,
                factor,
                factor
            )
        
        def start_pan(event):
            self.canvas.scan_mark(event.x, event.y)

        def pan(event):
            self.canvas.scan_dragto(event.x, event.y, gain=1)

        self.canvas = tk.Canvas(self.ventana, width=self.ventana.winfo_screenwidth(), height=self.ventana.winfo_screenheight(), bg="white")
        self.CENTER_WIDTH = self.ventana.winfo_screenwidth()/2
        self.CENTER_HEIGHT = self.ventana.winfo_screenheight()/2
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<MouseWheel>", zoom)
        self.canvas.bind("<ButtonPress-1>", start_pan) # Escaneo
        self.canvas.bind("<B1-Motion>", pan) # Movimiento


    

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