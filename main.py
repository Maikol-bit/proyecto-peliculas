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
            print("=" * 30)

            total_peliculas = 0
            for genero, Lista_de_peliculas in peliculas.items():
                  cantidad = len(Lista_de_peliculas)
                  total_peliculas += cantidad
                  print(f"{genero.replace('-','').title()}: {cantidad} peliculas")

            print("=" * 30)
            print(f"Total de peliculas: {total_peliculas}")

            mejor_pelicula = None
            mejor_rating = 0

            for genero in peliculas.values():
                  for pelicula in genero:
                        if pelicula['rating'] > mejor_rating:
                              mejor_rating = pelicula ['rating']
                              mejor_pelicula = pelicula

            if mejor_pelicula:
                  print(f"Mejor calificada: {mejor_pelicula['titulo']} ({mejor_rating}/10)")

def main():
            """Funcion principal del programa"""
            print("Netflix Console - Cargando Datos...")
            print("=" * 50)

            print("Cargando peliculas desde peliculas.json...")
            peliculas = cargar_peliculas()

            if peliculas:
                  print("Peliculas cargadas exitosmente")
                  mostrar_estadisticas_carga(peliculas)

            else:
                  print("Error: no se pudieron cargar las peliculas")
                  print("Revisa que el archivo de peliculas.json este en la carpeta correcta")
                  return
            
            print("\n Sistema listo para usar")

if __name__ == "__main__":
            main()

def limpiar_pantalla():
      """Limpia la pantalla de la consola"""
      os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_header():
      """Muestra el encabezado del programa"""
      print("=" * 60)
      print("🎬" + " " * 20 + "NETFLIX CONSOLE" + " " * 20 + "🎬")
      print("=" * 60)
      print("Tu platforma de peliculas favoritas en la consola")
      print("=" * 60)

def mostrar_menu_principal():
      """Muestrame el menu principal con todas las opciones"""
      print("\n🎯 ¿QUÉ QUIERES HACER HOY?")
      print("━" * 35)
      print("1. 🔥 Películas de Acción")
      print("2. 😂 Películas de Comedia")
      print("3. 👻 Películas de Terror")
      print("4. ❤️ Películas de Romance")
      print("5. 🚀 Películas de Ciencia Ficción")
      print("6. 🔍 Buscar película específica")
      print("7. 🏆 Top 10 mejor calificadas")
      print("8. ❤️ Ver mis películas favoritas")
      print("9. 📊 Estadísticas del sistema")
      print("0. ❌ Salir del programa")
      print("━" * 35)

def obtener_opcion_usuario():
      """
      obtiene y valida la opcion del usuario

      Returns:
            str: Opcion valida del usuario
      """
      while True:
            try:
                     opcion = input("\n Elije una opcion (0-9): ").strip()

                     if opcion in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            return opcion
                     else:
                            print("Opcion no valida. Usa numeros del 0 al 9.")

            except KeyboardInterrupt:
                     print("\n\n Hasta luego")
                     sys.exit(0)
            except Exception as e:
                     print(f"Error: {e}")

def pausar():
       """Pausa el programa hasta que el usuario presione Enter"""
       input("\n Presiona Enter para continuar...")

def main():
      """Funcion principal del menu interactivo"""

      print(" Iniciando Netflix Console...")
      peliculas = cargar_peliculas()

      if not peliculas:
              print("No se puede continuar sin las peliculas")
              return
       
      print("Sistema cargado correctamente")
      pausar()

      while True:
            limpiar_pantalla()
            mostrar_header()
            mostrar_menu_principal()

            opcion = obtener_opcion_usuario

            if opcion == "0":
                     limpiar_pantalla()
                     print("Gracias por usar Netflix Console")
                     print("Que disfruts viendo peliculas")
                     print("Hasta la proxima")

            elif opcion == "1":
                     print("\n Has elegido: Peliculas de accion")
                     print("Funcion en desarrollo...")
                     pausar()

            elif opcion == "2":
                     print("\n Has elejido: Peliculas de comedia")
                     print("Funcion en desarrollo...")
                     pausar()

            elif opcion == "3":
                     print("\n Has elejido: Peliculas de terror")
                     print("Funcion en desarrollo...")
                     pausar()

            elif opcion == "4":
                     print("\n Has elejido: Peliculas de romance")
                     print("Funcion en desarrollo...")
                     pausar()

            elif opcion == "5":
                     print("\n Has elejido: Peliculas de ciencia ficcion")
                     print("Funcion en desarrollo...")
                     pausar()

            elif opcion == "6":
                     print("\n Has elejido: Buscar pelicula")
                     print("Funcion en desarrollo...")
                     pausar()

            elif opcion == "7":
                     print("\n Has elijido: Top 10")
                     print("Funcion en desarrollo...")
                     pausar()

            elif opcion == "8":
                     print("\n Has elegido: Mis favoritas")
                     print("Funcion en desarrollo")
                     pausar()

            elif opcion == "9":
                     limpiar_pantalla()
                     mostrar_header()
                     mostrar_estadisticas_carga()
                     pausar()