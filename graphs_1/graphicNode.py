from graphs_1.node import Node

class GraphicNode(Node):
    def __init__(self,source, targets, targeted, coox, cooy):
        super().__init__(source, targets, targeted)
        self.coox = coox
        self.cooy = cooy

    def getCoo(self)->tuple:
        return (self.coox, self.cooy)
    
    def getSize(self)->int:
        return self.size