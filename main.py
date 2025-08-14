"""
NETFLIX CONSOLE
Proyecto de programación en Python
Autor: [Maikol Delgado]
Fecha: [14 de agosto]

Descripción: Sistema de navegación de películas tipo Netflix
usando archivos JSON y menús interactivos.
"""
import json
import os
import sys

favoritas = []
historial = []

def main():
    """Función pirncipal del programa"""
    print("Iniciando netflix console...")

    print("Programa iniciado correctamente")

if __name__ == "__main__":
        main()


"""
NETFLIX CONSOLE - Carga de datos JSON
"""

import json
import os

def cargar_peliculas():
      """
      Cargar las Peliculas desde el archivo JSON

      Returns:
      dict: Diccionario con las peliculas organizadas por género
      None: Si hay algun error al cargar el archivo
      """
      try:
            if not os.path.exists('peliculas.json'):
                  print("Error: No se encontro el archivo 'peliculas.json'")
                  print("Asegurate que este en la misma carpeta que main.py")
                  return None
            
            with open('peliculas.json', 'r', encoding='utf-8') as archivo:
                  peliculas = json.load(archivo)
                  
                  if not peliculas:
                        print("Error: El archivo JSON esta vacio")
                        return None
                  
                  return peliculas
            
      except json.JSONDecodeError as e:
            print(f"Error: El archivo JSON tiene formato incorrecto")
            print(f"Detalle del Error: {e}")
            return None
      except Exception as e:
            print(f"Error inesperado: {e}")
            return None
      
      def mostrar_estadisticas_carga(peliculas):
            """
            Muestra estadisticas de las peliculas cargadas

            Args:
            peliculas (dict): Diccionario con las peliculas
            """

            if not peliculas:
                  return
            
            print("Estadisticas de carga")