from pathlib import Path
try:
    import pandas as pd
except ImportError:
    print("ImportError: falta la dependencia 'pandas' instalar usando: 'pip install pandas'")


class AdjacencyList:
    """Esta clase representa una lista de adjacencia de grafos
    """    
    def __init__(self, file_name="") -> None:
        BASE_DIR = Path(__file__).resolve().parent
        # pares (source, target) como strings.
        # No se permiten duplicados y se normaliza el orden para evitar pares opuestos.
        # Ej: si existe ("6","5") no se agrega ("5","6").
        self.edge_reg: set[tuple[str, str]] = set()
        self.nodesList = set() # Set de los nodos existentes (node_name: str, ...)

        self.nodesEntry = dict() # Estructura de nodos en forma inversa {key= node_name: str; value= [(source), ...]}
        self.nodesExit = dict() # Estructura de nodos en salida {key= node_name: str; value= [(node_name: str, weight: str), ...]}

        """if file_name == "":
            path_txt = BASE_DIR / "data" / "grafoData.txt"
            path_csv = BASE_DIR / "data" / "grafo16.csv"

            self.read_from_csv(path_csv)

        else:"""

        if file_name.endswith(".txt"):
            self.read_from_txt(path=BASE_DIR/"data"/file_name)
        elif file_name.endswith(".csv"):
            self.read_from_csv(path=BASE_DIR/"data"/file_name)
        else:
            print("Archivo no valido.")
        

        self.nodesList = list(self.nodesList) # Normalizar de set() a list()

    def _add_edge_reg(self, source: str, target: str) -> None:
        a, b = str(source), str(target)
        if a <= b:
            self.edge_reg.add((a, b))
        else:
            self.edge_reg.add((b, a))

    def read_from_csv(self, path: str) -> None:
        """Leer datos de nodos desde un archivo .csv

        Args:
            path (str): ruta del archivo
        """        

        df = pd.read_csv(path)

        # Crear la estructura de datos que permite identificar hacia donde apuntan los nodos y con que peso
        for _, fila in df.iterrows():
            source = str(fila["source"])
            target = str(fila["target"])
            weight = str(fila["weight"])

            #print(source, weight, target, sep="\t")

            self.nodesExit[source] = self.nodesExit.get(source, []) + [tuple([target, weight])]
            # edge_reg: pares (source, target) usando solo nombres en string
            self._add_edge_reg(source, target)

            self.nodesList.add(source)
            self.nodesList.add(target)


        # Crear la estructura de datos que permite identificar que nodos son apuntados por otros nodos
        for source, targets in self.nodesExit.items():
            for target in targets:
                self.nodesEntry[target[0]] = self.nodesEntry.get(target[0], []) + [(source)]

        

    def read_from_txt(self, path: str) -> None:
        """leer datos de nodos desde un archivo .txt

        Args:
            path (str): ruta del archivo
        """        
        # Crear la estructura de datos que permite identificar hacia donde apuntan los nodos y con que peso
        with open(path, "r") as file:
            for line in file:
                line = line.replace("\n", "")
                graph_data = line.split(",")

                source = graph_data[0]
                target = graph_data[1]

                self.nodesExit[source] = self.nodesExit.get(source, []) + [tuple(graph_data[1:])]
                # edge_reg: pares (source, target) usando solo nombres en string
                self._add_edge_reg(source, target)


                self.nodesList.add(source)
                self.nodesList.add(target)


        # Crear la estructura de datos que permite identificar que nodos son apuntados por otros nodos
        for source, targets in self.nodesExit.items():
            for target in targets:
                self.nodesEntry[target[0]] = self.nodesEntry.get(target[0], []) + [(source)]




