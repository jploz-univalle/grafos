@echo off
setlocal

REM Instala dependencias necesarias para el proyecto.
REM Ejecutar DESPUES de activar el entorno virtual (venv).

echo Instalando dependencias...

REM Actualizar pip (opcional, pero recomendado)
python -m pip install --upgrade pip

REM Instalar desde requerimientos.txt
if exist requeriments.txt (
    python -m pip install -r requeriments.txt
) else (
    echo No se encontro el archivo requeriments.txt
)


echo.
echo Instalacion completada.
endlocal
pause

