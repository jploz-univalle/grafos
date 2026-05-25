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
grafos/
│
├── main.py
├── graph.py
├── adjacencyList.py
├── node.py
├── graphicNode.py
├── GUI.py
├── data/
│   └── grafoData.txt
└── README.md
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
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Como ejecutar el programa
Para evitar errores se debe situar desde la carpeta raiz y ejecutar
```bash
python -m src.main
```

## Autor
Juan Pablo Lozano 2521505

Universidad del Valle
Matematicas Discretas II 

## Historial

25/05/2026

- Sistema adaptado para abrir archivo especificado por el usuario (csv o txt)
- Sistema de dibujado de aristas modificado para visualización adecuada
- Reestructuración de GUI.py
- Nuevo archivo execute.py encargado de la ejecución del programa, por entrega
- Nueva clase Edge que representa las aristas
- Reestructuración de clases y documentación
