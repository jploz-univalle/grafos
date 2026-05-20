# Entidad Nodo
class Node:
    def __init__(self, source: str, targets: list, targeted: list):
        self.source = source
        self.targets = targets
        self.targeted = targeted

    