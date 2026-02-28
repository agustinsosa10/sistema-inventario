#imagen base
FROM python:3.14-slim 

#directorio dentro del contenedor
WORKDIR /code

#copia los requerimientos dentro del directorio del contenedor
COPY ./requirements.txt /code/requirements.txt

#instala dependencias dentro del contenedor
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#copia el codigo dentro del contenedor
COPY ./app /code/app

#comando que se ejecuta cuando el contenedor arranca. levanta uvicorn en el puerto 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]