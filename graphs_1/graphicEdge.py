from math import hypot
from tkinter import LAST, Canvas
from graphs_1.graphicNode import GraphicNode

class GraphicEdge:
    """Clase que representa una arista con direccion
    """    
    def __init__(self, node1, node2, weight=1) -> None:
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
        self.ID = int()

    # Metodo para crear aristas entre los nodos
    def create_arrow(self, canvas: Canvas) -> None:
        """Permite crear una arista Edge entre dos nodos Node

        Args:
            canvas (Canvas): Objeto Canvas donde se dibujan los objetos
        """        
            
        self.node1:GraphicNode
        self.node2:GraphicNode

        x1, y1 = self.node1.getCoo()
        r1 = self.node1.radius
        x2, y2 = self.node2.getCoo()
        r2 = self.node2.radius

        # Acomodar visualmente las flechas usando una estrategia de reduccion de coordenada en base a su posicion final e inicial

        difx = x2 - x1 
        dify = y2 - y1

        d = hypot(difx, dify)

        ux = difx / d
        uy = dify / d

        startx = x1 + ux * r1
        starty = y1 + uy * r1

        endx = x2 - ux * r2
        endy = y2 - uy * r2

        self.ID = canvas.create_line(startx,
                            starty,
                            endx,
                            endy,
                            arrow=LAST)