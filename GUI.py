import tkinter as tk
from graph import Graph
import math
from graphicNode import GraphicNode

class Graphic: 
    def __init__(self, grafo: Graph):
        ventana = tk.Tk()
        ventana.title("Visualizador de Grafo")

        canvas = tk.Canvas(ventana, width=800, height=600, bg="white")
        self.CENTER_WIDTH = 400
        self.CENTER_HEIGHT = 300
        canvas.pack()

        # Centro simulado de referencia
        canvas.create_oval(self.CENTER_WIDTH-10, self.CENTER_HEIGHT-10, self.CENTER_WIDTH+10, self.CENTER_HEIGHT+10, fill="lightblue")
        canvas.create_text(self.CENTER_WIDTH, self.CENTER_HEIGHT, text="O")

        # Variables de operacion para logica de calculo de posiciones
        circundantes = 360/len(grafo.adjacency_list.nodesList)
        degreeCount = circundantes
        centerDistance = 160
        graphic_nodes_list = list()
        
        # Metodo para crear ovalos(Nodos) rapidamente
        def create_oval(size: int, x, y) -> None:
            sizeFactor = size // 2
            canvas.create_oval(x-sizeFactor, y-sizeFactor, x+sizeFactor, y+sizeFactor, fill="lightblue")

        # Metodo para crear aristas entre los nodos
        def create_arrow(x1, y1, x2, y2):
            # Acomodar visualmente las flechas usando una estrategia de reduccion de coordenada en base a su posicion final e inicial

            difx = x2 - x1 
            dify = y2 - y1

            if difx > 0:
                x1+=10
                x2-=10
            else: 
                x1-=10
                x2+=10
            
            if dify > 0:
                y1+=10
                y2-=10
            else:
                y1-=10
                y2+=10

            canvas.create_line(x1,
                               y1,
                               x2,
                               y2,
                               arrow=tk.LAST)

        def findNodeByName(name:str):
            for grnode in graphic_nodes_list:
                if grnode.source == name:
                    return grnode

        # Graficar y ordenar los nodos en forma circundante
        for node in grafo.nodes_list:
            theta = math.radians(degreeCount) # Calcular de forma proporcional al centro

            x = self.CENTER_WIDTH - centerDistance * math.cos(theta)
            y = self.CENTER_HEIGHT - centerDistance * math.sin(theta)

            create_oval(40, x, y)
            canvas.create_text(x,y, text=node.source)

            graphic_nodes_list.append(
                GraphicNode(
                    source=node.source,
                    targets=node.targets,
                    targeted=node.targeted,
                    coox=x,
                    cooy=y
                )
            )
            degreeCount+=circundantes

        for grnode in graphic_nodes_list:
            grnode: GraphicNode
            print(grnode.source, grnode.coox, grnode.cooy)


        # Crear aristas
        for graphicNode in graphic_nodes_list:
            for target in graphicNode.targets:
                create_arrow(
                    *graphicNode.getCoo(), 
                    *findNodeByName(target[0]).getCoo()
                )

        ventana.mainloop()
