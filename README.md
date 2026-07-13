# Grafos dirigidos con peso en python

Proyecto creado para la materia Matematicas Discretas II.

## Descripcion general

Este proyecto esta diseñado para virtualizar informacion de un grafo dada en un formato especifico y evaluar algunas caracteristicas del mismo, por ejemplo si es un multigrafo o si es completo, decidi usar la plataforma python y tkinter por que es una tecnologia que habia usado anteriormente y en la cual tengo cierto dominio, ademas que para calculos
prefiero usar Python por su versatilidad.

- Crear grafos dirigidos
- Agregar vértices y aristas
- Manejar pesos en las aristas
- Calcular grado de entrada y salida
- Detectar multigrafos
- Verificar si un grafo es completo
- Leer grafos desde archivos .txt
- Uso de GUI

## Estructura del Proyecto

```text
GRAFOS/ (raíz del proyecto)
│
├── README.md
├── requeriments.txt
├── install_deps.bat
├── src/
│   ├── __init__.py
│   └── main.py
└── graphs_1/
    ├── __init__.py
    ├── execute.py
    ├── adjacencyList.py
    ├── graph.py
    ├── node.py
    ├── graphicNode.py
    ├── graphicEdge.py
    ├── GUI.py
    └── data/
        ├── grafo*.csv
        └── int.txt
```

## Ejecucion del archivo python
### Crear entorno virtual
Desde la carpeta del proyecto ejecutar en la consola 
```bash
python -m venv venv
```
### Ejecutar el entorno virtual
Windows:

```bash
install_deps.bat
```

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
bash install_deps_linux.sh
```

```bash
source venv/bin/activate
```

### Como ejecutar el programa
Para evitar errores se debe situar desde la carpeta raiz y ejecutar
```bash
python -m src.main
```

## Autores
Juan Pablo Lozano 2521505
Jhonny Alexander Moreno Florez 2522112

Universidad del Valle
Matematicas Discretas II 

## Historial
13/07/2026
- **Sistema puede verificar si el grafo es un arbol:** Se modifico la clase graph con un metodo que permite corroborar si el grafo de entrada es un arbol.
- **Sistema de instalacion de dependencias:** Se implemento un sistema de instalacion de dependencias autonomo.
- **Se incluye archivo de configuracion para visual studio:** De forma opcional se incluye una configuracion de depuracion para Visual Studio Code.

25/05/2026

- **Sistema adaptado para abrir archivo especificado por el usuario (csv o txt):** Se modificó el lector para procesar de forma transparente ambos formatos eliminando espacios residuales.
- **Sistema de dibujado de aristas modificado para visualización adecuada:** Optimización matemática en el renderizado de las flechas y las conexiones dirigidas.
- **Corrección Geométrica en GUI:** Ajuste dinámico de las coordenadas base para evitar el colapso de los nodos en el centro de la pantalla.
- **Nuevo archivo execute.py encargado de la ejecución del programa, por entrega:** Creación del punto de entrada limpio e independiente que unifica el sistema.
- **Nueva clase Edge que representa las aristas:** Separación de responsabilidades mediante un modelo de datos propio para los arcos ponderados.
- **Reestructuración de clases y documentación:** Refactorización general de variables y funciones al inglés bajo estándares de la industria.
- **Movimiento y zoom en la representación visual:** Integración de bindings en el lienzo para navegación fluida mediante arrastre y rueda del ratón.
- **Coeficiente dinámico agregado para datos muy grandes:** Ajuste de escala automático que previene el amontonamiento visual cuando el grafo escala en densidad.
- **Soporte Completo para Lazos Propios:** Resolución de excepciones matemáticas (división por cero) al renderizar aristas que conectan un nodo consigo mismo.
