#!/usr/bin/env bash
set -euo pipefail

# Instala dependencias necesarias para el proyecto.
# Debe ejecutarse DESPUES de activar tu entorno virtual (venv).

echo "Instalando dependencias..."

# Actualizar pip (opcional)
python -m pip install --upgrade pip

# Instalar desde requerimientos.txt
if [ -f "requeriments.txt" ]; then
  python -m pip install -r requeriments.txt
else
  echo "No se encontro el archivo requeriments.txt"
fi

echo "Instalacion completada."

