import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def descargar_imagenes(url, carpeta_destino):
    # Crear la carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Obtener el contenido de la página
    respuesta = requests.get(url)
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    # Encontrar todos los elementos img en la página
    etiquetas_img = soup.find_all('img')

    # Descargar las imágenes con extensión .jpg
    for img_tag in etiquetas_img:
        src = img_tag.get('src')
        if src and src.lower().endswith(('.jpg', '.jpeg')):
            # Crear la URL completa de la imagen
            img_url = urljoin(url, src)

            # Obtener el nombre de archivo de la URL
            nombre_archivo = os.path.join(carpeta_destino, os.path.basename(urlparse(img_url).path))

            # Descargar la imagen
            with open(nombre_archivo, 'wb') as archivo:
                respuesta_img = requests.get(img_url)
                archivo.write(respuesta_img.content)
                print(f'Imagen descargada: {nombre_archivo}')

if __name__ == '__main__':
    # URL de la página web
    url_pagina = 'https://earthobservatory.nasa.gov/world-of-change/AralSea'

    # Carpeta de destino para las imágenes
    carpeta_destino = 'aral_sea_img'

    # Llamar a la función para descargar imágenes
    descargar_imagenes(url_pagina, carpeta_destino)
