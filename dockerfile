#obtener imagen base
FROM --platform=linux/amd64 python:3.10.4-slim-bullseye

#Configura variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Configurar directorio de trabajo
WORKDIR /GitHub

COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Copiar proyecto
COPY . .