# Trabajo Práctico Integrador - AySO

## Tema: Virtualización con Docker

Este proyecto demuestra cómo utilizar Docker para contenerizar y ejecutar un script de Python. Se trata de una calculadora de IMC (Índice de Masa Corporal) diseñada para correr de forma aislada y reproducible dentro de un contenedor Docker.

## Alumnos

- Ignacio Figueroa - ignaciofigueroadev@gmail.com - DNI 45.406.120 - Comisión 7
- Bruno Croppi - croppibruno@gmail.com - DNI 41.906.566 - Comisión 7

## Anexo

- [Enlace a video explicativo (Youtube)]()
- [Enlace al repositorio (GitHub)](https://github.com/figueroaignacio/tp-integrador-ayso-virtualizacion)

## Archivos Incluidos

- `script.py`: Script principal del programa.
- `Dockerfile`: Define el entorno de ejecución en Docker.
- `README.md`: Informe general del proyecto.
- `informe-tp-virtualizacion.pdf`: Informe completo sobre el proyecto.

## Requisitos

- Docker instalado

## Ejecutar Programa

1. Clonar el Repositorio.

```bash
git clone https://github.com/figueroaignacio/tp-integrador-ayso-virtualizacion.git
cd tp-integrador-ayso-virtualizacion
```

2. Asegurarse de tener Docker en ejecución
   Abrí Docker Desktop o asegurate de que el servicio de Docker esté corriendo en tu sistema.

3. Construir la imagen Docker

```bash
docker build -t tp-integrador-ayso-virtualizacion .
```

4. Ejecutar el contenedor

```bash
docker run -it --rm tp-integrador-ayso-virtualizacion
```

Esto iniciará el contenedor y ejecutará el script Python dentro del mismo.
