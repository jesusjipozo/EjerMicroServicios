# Usa una imagen oficial de Python con Alpine (una versión ligera de Linux)
FROM python:3.9-alpine

# Establecer el directorio de trabajo en el contenedor
WORKDIR /servicio1

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip3 install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente del microservicio dentro del contenedor
COPY . .

# Exponer el puerto en el que el microservicio va a correr (cambia según tu configuración)
#EXPOSE 5001

# Comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]


