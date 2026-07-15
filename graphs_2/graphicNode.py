from graphs_1.node import Node

class GraphicNode(Node):
    """Clase que representa un Nodo Grafico

    Args:
        Node (Node): Clase Node simple
    """    
    def __init__(self, id, source, targets, targeted, coox, cooy, ovalSize, radius):
        super().__init__(source, targets, targeted)
        self.ID = id
        self.coox = coox
        self.cooy = cooy
        self.ovalSize = ovalSize
        self.radius = radius
        self.edges_list = list()
        

    def getCoo(self)->tuple:
        """Retorna las coordenadas X y Y en el canvas

        Returns:
            tuple: coordenadas X y Y empaquetadas en una tupla (x, y)
        """        
        return (self.coox, self.cooy)
    
    def getSize(self)->int:
        """Retorna el tamaño del nodo

        Returns:
            int: Tamaño del nodo
        """        
        return self.size