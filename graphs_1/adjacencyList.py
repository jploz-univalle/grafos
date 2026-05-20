from pathlib import Path

class AdjacencyList:
    def __init__(self):

        BASE_DIR = Path(__file__).resolve().parent
        path = BASE_DIR / "data" / "grafoData.txt"

        self.nodesList = set() # Set de los nodos existentes

        self.nodesEntry = dict() # Estructura de nodos en forma inversa
        self.nodesExit = dict() # Estructura de nodos en salida

        # Crear la estructura de datos que permite identificar hacia donde apuntan los nodos y con que peso
        with open(path, "r") as file:
            for line in file:
                line = line.replace("\n", "")
                newLine = line.split(",")

                self.nodesExit[newLine[0]] = self.nodesExit.get(newLine[0], []) + [tuple(newLine[1:])]
                
                self.nodesList.add(newLine[0])
                self.nodesList.add(newLine[1])

        # Crear la estructura de datos que permite identificar que nodos son apuntados por otros nodos
        for source, targets in self.nodesExit.items():
            for target in targets:
                target: tuple
                self.nodesEntry[target[0]] = self.nodesEntry.get(target[0], []) + [(source)]


        self.nodesList = list(self.nodesList)
        # for k, v in self.nodesEntry.items():
        #     print(f"{k} : {v}")


