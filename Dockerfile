# Usa una imagen base de Python
FROM python:3.11-slim

# Copia tu script al contenedor
COPY script.py /app/script.py

# Define el directorio de trabajo
WORKDIR /app

# Comando por defecto al ejecutar el contenedor
CMD ["python", "script.py"]
