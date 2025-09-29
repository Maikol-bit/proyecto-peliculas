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

"""
NETFLIX CONSOLE - Carga de datos JSON
"""

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
      
def procesar_seleccion_genero(peliculas, genero, nombre_genero):
      """
      Procesa la navegación completa de un género
      
      Args:
            peliculas (dict): Diccionario con todas las películas
            genero (str): Clave del género
            nombre_genero (str): Nombre del género para mostrar
      """
      while True:
            pelicula_seleccionada = mostrar_peliculas_genero(peliculas, genero, nombre_genero)
            if pelicula_seleccionada is None:
                  break
            
            while True:
                  accion = mostrar_detalle_pelicula(pelicula_seleccionada)
                  
                  if accion == "volver_lista":
                        break
                  elif accion == "menu_principal":
                        return 
                  elif accion == "volver_detalle":
                        continue
            
            print(f"\n Seleccionaste: {pelicula_seleccionada['titulo']}")
            print("Funcion de detalles en desarrollo")
            pausar()
            
def mostrar_peliculas_genero(peliculas, genero, nombre_genero):
      """
      Muestra todas las peliculas de un genero especifico
      
      Args:
            peliculas (dict): Diccionario con todas las peliculas
            gereno (str): Clave del género para mostrar
      """
      limpiar_pantalla()

      emoji = obtener_emoji_genero(genero)
      mensaje = obtener_mensaje_genero(genero)
      
      print(f"{emoji} Peliculas de {nombre_genero.upper()} {emoji}")
      print("=" * 60)
      print(f"{mensaje}")
      print("=" * 60)
      
      lista_peliculas = peliculas[genero]
      
      print(f"{'#':<3} {'TITULO': <35} {'AÑO': <6} {'RATING':<8}")
      print("-" * 60)
      
      for i, pelicula in enumerate(lista_peliculas, 1): 
            titulo = pelicula['titulo']
            if len(titulo) >32:
                  titulo = titulo[:29] + "..."
            
            print(f"{i:<3} {titulo:<35} {pelicula['año']:<6} {pelicula['rating']:<7}")
      
      print("-" * 60)
      print(f"{len(lista_peliculas) + 1}. Volver al menu principal")
      
      return seleccionar_pelicula_genero(lista_peliculas)
      
def seleccionar_pelicula_genero(lista_peliculas):
      """
      permite al usuario seleccionar una pelicula de la lista
      
      Args:
      lista_peliculas (lits): Lista de peliculas del genero
      
      Returns:
      dict or None: Pelicula seleccionada o None si vuelve al menu
      """
      while True:
            try:
                  print(f"\n Elije una pelicula (1-{len(lista_peliculas)}) o {len(lista_peliculas) + 1} para volver: ", end="")
                  opcion = input().strip()
                  
                  if opcion == str(len(lista_peliculas) + 1):
                        return None
                  
                  numero = int(opcion)
                  if 1 <=numero <= len(lista_peliculas):
                        return lista_peliculas[numero - 1]
                  else:
                        print(f" Numero fuera de rango. Usa 1-{len(lista_peliculas)} o {len(lista_peliculas) + 1}")
                        
            except ValueError:
                  print(" Por favor ingrese un numero valido")
            except KeyboardInterrupt:
                  return None
            
def procesar_seleccion_genero(peliculas, genero, nombre_genero):
      """
      Procesa la navegacion completa de un genero
      
      Args:
            peliculas (dict): Diccionario con todas las peliculas
            genero (str): Clave del genero
            nombre_genero (str): Nombre del genero para mostrar
      """
      while True:
            pelicula_seleccionada = mostrar_peliculas_genero(peliculas, genero, nombre_genero)

            if pelicula_seleccionada is None:
                  break
            print(f"\n Seleccionaste: {pelicula_seleccionada['titulo']}")
            print(" Funcion de detalles en desarrollo...")
            pausar()
def mostrar_detalle_pelicula(pelicula):
      """
      Muestra todos los detalles de una pelicula
      
      Args:
            pelicula (dict): Diccionario con los datos de la pelicula
      """
      limpiar_pantalla()

      print("🎬" + "=" * 58 + "🎬")
      titulo = pelicula['titulo'].upper()
      espacios = (60 - len(titulo)) //2
      print(" " * espacios + titulo + " " * espacios)

      print(f"\n Año: {pelicula['año']}")
      print(f"Duracion: {pelicula['duracion']}")
      print(f"Rating: {pelicula['rating']}/10")
      print(f"Director: {pelicula['director']}")
      print(f"Actores principales: {pelicula['actores']}")

      print(f"\n SINOPSIS:")
      print("-" * 60)
      sinopsis = pelicula['sinopsis']
      palabras = sinopsis.split()
      linea_actual = ""

      for palabra in palabras:
            if len(linea_actual + palabra) <= 57:
                  linea_actual += palabra + " "
            else:
                  print(linea_actual.strip())
                  linea_actual = palabra + " "
      if linea_actual:
            print(linea_actual.strip())

      print ("-" * 60)
      return mostrar_opciones_pelicula(pelicula)

def mostrar_opciones_pelicula(pelicula):
      """
      Muestra las opciones disponibles para una pelicula

      Args:
            pelicula (dict): Diccionario con los datos de la pelicula

      Returns:
            str: Accion seleccionada por el usuario
      """
      print("\n🎯 ¿QUÉ QUIERES HACER?")
      print("━" * 30)
      print("1. 🍿 'Ver' esta película")
      print("2. ❤️ Agregar a favoritas")
      print("3. 📊 Ver más estadísticas")
      print("4. ⬅️ Volver a la lista")
      print("5. 🏠 Volver al menú principal")
      print("━" * 30)

      while True:
            try:
                  opcion = input("\n Elije una opcion (1-5):").strip()

                  if opcion == "1":
                        return simular_reproduccion(pelicula)
                  elif opcion == "2":
                        return agregar_a_favoritas(pelicula)
                  elif opcion == "3":
                        return mostrar_estadisticas_pelicula(pelicula)
                  elif opcion == "4":
                        return "volver_lista"
                  elif opcion == "5":
                        return "menu_principal"
                  else:
                        print("Opcion no valida. Usa numeros del 1 al 5")

            except KeyboardInterrupt:
                  return "menu_principal"
            
def simular_reproduccion(pelicula):
      """
      Simula la reporduccion de una pelicula
      
      Args:
            pelicula (dict): Diccionario con los datos de la pelicula
      """
      limpiar_pantalla()
      print("🎬" + "=" * 58 + "🎬")
      print(f" Reporduciendo: {pelicula['titulo']}")
      print("🎬" + "=" * 58 + "🎬")

      print("\n *Musica epica de apertura* ")
      print(" *Titulos iniciales aparecen* ")
      print(" *Te acomodas en tu asiento virtual* ")
      print(" *La magia del cine comienza* ")
      
      print(f"\n Disfrutando de '{pelicula['titulo']}'...")
      print(f" Duracion: {pelicula['duracion']}")
      print(" *Actuaciones increibles en pantalla*")
      print(" *Banda sonora epica*")
      
      input("\n Presione enter cuando 'termines' de ver la pelicula...")
      if pelicula not in historial:
            historial.append(pelicula)

      print("\n ¡Pelicula terminada!")
      print(" ¡Esperamos la haya disfrutado!")
      print(f" '{pelicula['titulo']}'agregada a tu historial")
      
      pausar()
      return "volver_detalle"

def agregar_a_favoritas(pelicula):
      """
      Agrega una pelicula a la lista de favoritas
      
      Args:
            pelicula (dict): Diccionario con los datos de la pelicula
      """
      if pelicula in favoritas:
            print(f"\n '{pelicula['titulo']}' ya esta en tus favoritas")
      else:
            favoritas.append(pelicula)
            print(f"\n ¡'{pelicula['titulo']}' agregrada a favoritas!")
            print(f"Ahora tienes {len(favoritas)} pelicula(s) favorita(s)")
      pausar()
      return "volver_detalle"

def mostrar_estadisticas_pelicula(pelicula):
      """
      Muestra estadisticas adicionales de una pelicula
      
      Args:
            pelicula (dict): Diccionario con los datos de la pelicula
      """
      print(f"\n ESTADISICAS DE '{pelicula['titulo']}'")
      print("-" * 50)
      
      print(f" ID en base de datos: {pelicula['id']}")
      print(f" año de estreno: {pelicula['año']}")
      
      decada = (pelicula['año'] //10) * 10
      print(f" Decada: {decada}s")
      
      rating = pelicula['rating']
      if rating >= 9.0:
            categoria = "OBRA MAESTRA"
      elif rating >=8.0:
            categoria = "EXCELENTE"
      elif rating >=7.0:
            categoria = "MUY BUENA"
      elif rating >=6.0:
            categoria = "BUENA"
      else:
            categoria = "REGULAR"
            
      print(f"Categoria: {categoria}")
      
      duracion_min = int(pelicula['duracion'].split()[0])
      if duracion_min < 90:
            tipo_duracion = "Corta"
      if duracion_min < 150:
            tipo_duracion = "Estandar"
      else:
            tipo_duracion = "Largaaa..."
            
      print(f" Tipo de duracion: {tipo_duracion}")
      print (f" Minutos totales: {duracion_min}")
      
      num_actores = len(pelicula['actores'].split(','))
      print(f"Actores principales: {num_actores}")
      
      pausar()
      return "volver_detalle"

def obtener_emoji_genero(genero):
      """
      Obtiene el emoji correspondiente a cada género

      Args:
      genero (str): Nombre del género
      
      Returns:
      str: Emoji del género
      """

      emojis = {
            "accion": "🔥",
            "comedia": "😂",
            "terror": "👻",
            "romance": "❤️",
            "ciencia_ficcion": "🚀"
      }
      return emojis.get(genero, "🎬")

def obtener_mensaje_genero(genero):
      """
      Obtiene un mensaje personalizado para cada género
      
      Args:
            genero (str): Nombre del género
            
      Returns:
            str: Mensaje personalizado
      """
      mensajes = {
            "accion": "¡Prepárate para la adrenalina y la aventura!",
            "comedia": "¡Listos para reír hasta que te duela la barriga!",
            "terror": "¡Prepárate para sustos y emociones fuertes!",
            "romance": "¡Historias de amor que te llegarán al corazón!",
            "ciencia_ficcion": "¡Viaja al futuro y explora nuevos mundos!"
      }
      return mensajes.get(genero, "Disfrute de estas peliculas")

def buscar_peliculas(peliculas):
      """
      Permite buscar películas por título
      
      Args:
            peliculas (dict): Diccionario con todas las películas
      """
      limpiar_pantalla()

      print("🔍 BÚSQUEDA DE PELÍCULAS")
      print("=" * 40)
      print("💡 Consejo: Puedes buscar por título completo o parcial")
      print("💡 Ejemplo: 'batman', 'star', 'love', etc.")
      print("=" * 40)

      termino = input("\n Escribe el titulo o parte de este:").strip()

      if not termino:
            print("Debes esribir algo para buscar")
            pausar()
            return
      
      resultados = []

      for nombre_genero, lista_peliculas in peliculas.items():
            for pelicula in lista_peliculas:
                  if termino.lower() in pelicula['titulo'].lower():
                        resultados.append((pelicula, nombre_genero))

      mostrar_resultados_busqueda(resultados, termino)

def mostrar_resultados_busqueda(resultados, termino):
      """
      Muestra los resultados de una búsqueda
      
      Args:
            resultados (list): Lista de tuplas (pelicula, genero)
            termino (str): Término buscado
      """
      limpiar_pantalla()

      if not resultados:
            print("🔍 RESULTADOS DE BÚSQUEDA")
            print("=" * 40)
            print(f"❌ No se encontraron películas con '{termino}'")
            print("\n💡 Sugerencias:")
            print("   • Verifica la ortografía")
            print("   • Intenta con menos palabras")
            print("   • Usa solo parte del título")
            pausar()
            return
      
      print("🔍 RESULTADOS DE BÚSQUEDA")
      print("=" * 60)
      print(f"🎯 Término buscado: '{termino}'")
      print(f"📊 Se encontraron {len(resultados)} película(s)")
      print("=" * 60)

      print(f"{'#':<3} {'Titulo':<30} {'Genero':<12} {'Año':<6} {'Rating'}")
      print("-" * 60)

      for i, (pelicula, genero) in enumerate(resultados, 1):
            titulo = pelicula['titulo']
            if len(titulo) > 27:
                  titulo = titulo[:24] + "..."

            genero_mostrar = genero.replace('_',' '). title()
            if len(genero_mostrar) > 9:
                  genero_mostrar = genero_mostrar[:9] + "."

            print(f"{i:<3} {titulo:<30} {genero_mostrar:<12} {pelicula['año']:<6} ⭐{pelicula['rating']}")

      print("-" * 60)
      print(f"{len(resultados) + 1}. Volver al menu principal")

      seleccionar_de_busqueda(resultados)

def seleccionar_de_busqueda(resultados):
      """
      Permite seleccionar una película de los resultados de búsqueda
      
      Args:
            resultados (list): Lista de tuplas (pelicula, genero)
      """
      while True:
            try:
                  print(f"\n👉 Elige una película (1-{len(resultados)}) o {len(resultados) + 1} para volver: ", end="")
                  opcion = input().strip()

                  if opcion ==str(len(resultados) + 1):
                        return
                  
                  numero = int(opcion)
                  if 1 <= numero <= len(resultados):
                        pelicula_seleccionada = resultados[numero - 1][10]

                        while True:
                              accion = mostrar_detalle_pelicula(pelicula_seleccionada)

                              if accion == "volver_lista":
                                    return
                              elif accion == "menu_principal":
                                    return
                              elif accion == "volver_detalle":
                                    continue
                  else:
                        print(f"❌ Número fuera de rango. Usa 1-{len(resultados)} o {len(resultados) + 1}")
                        
            except ValueError:
                  print("Por favor ingresa un numero valido")
            except KeyboardInterrupt:
                  return
            
def busqueda_avanzada(peliculas):
      """
      Búsqueda avanzada con múltiples filtros
      
      Args:
            peliculas (dict): Diccionario con todas las películas
      """
      limpiar_pantalla()

      print("🔍 BÚSQUEDA AVANZADA")
      print("=" * 40)
      print("1. 🎬 Buscar por título")
      print("2. 🎭 Buscar por director")
      print("3. 👥 Buscar por actor")
      print("4. 📅 Buscar por año")
      print("5. ⭐ Buscar por rating mínimo")
      print("6. ⬅️ Volver al menú")
      print("=" * 40)

      while True:
            try:
                  opcion = input("\n Elige tipo de busqueda (1-6): ").strip()

                  if opcion == "1":
                        buscar_peliculas(peliculas)
                        break
                  elif opcion == "2":
                        buscar_por_director(peliculas)
                        break
                  elif opcion == "3":
                        buscar_por_actor(peliculas)
                        break
                  elif opcion == "4":
                        buscar_por_año(peliculas)
                        break
                  elif opcion == "5":
                        buscar_por_rating(peliculas)
                        break
                  elif opcion == "6":
                        busqueda_avanzada(peliculas)
                        break
                  else:
                        print("Opcion no valida. Usa numeros del 1 al 6")

            except KeyboardInterrupt:
                  break

def buscar_por_director(peliculas):
      """Busca peliculas por director"""
      termino = input ("\n Escribe el nombre del director: ").strip()
      if not termino:
            return
      
      resultados = []
      for genero, lista_peliculas in peliculas.items():
            for pelicula in lista_peliculas:
                  if termino.lower() in pelicula['director'].lower():
                        resultados.append((pelicula, genero))

      mostrar_resultados_busqueda(resultados, f"director: {termino}")

def buscar_por_actor(peliculas):
      """Busca peliculas por actor"""
      termino = input("\n Escribe el nombre del actor: ").strip()
      if not termino:
            return
      
      resultados = []
      for genero, lista_peliculas in peliculas.items():
            for pelicula in lista_peliculas:
                  if termino.lower() in pelicula['actores'].lower():
                        resultados.append((pelicula, genero))

      mostrar_resultados_busqueda(resultados, f"actor : {termino}")

def buscar_por_año(peliculas):
      """Busca peliculas por año"""
      try:
            año = int(input("\nEscribe el año: ").strip())

            resultados = []
            for genero, lista_peliculas in peliculas.items():
                  for pelicula in lista_peliculas:
                        if pelicula['año'] == año:
                              resultados.append((pelicula, genero))
      
            mostrar_resultados_busqueda(resultados, f"año: {año}")

      except ValueError:
            print("Por favor ingresa un año valido")
            pausar()

def buscar_por_rating(peliculas):
      """Buscar peliculas por rating minimo"""
      try:
            rating_min = float(input("\nEscribe el rating minimo (ej: 8.0):").strip())

            resultados = []
            for genero, lista_peliculas in peliculas.items():
                  for pelicula in lista_peliculas:
                        if pelicula['rating'] >= rating_min:
                              resultados.append((pelicula, genero))

            mostrar_resultados_busqueda(resultados, f"rating ≥ {rating_min}")

      except ValueError:
            print("Por favor ingresa un numero valido")
            pausar()

def mostrar_top_10(peliculas):
      """
      Muestra las 10 peliculas mejor calificadas
      
      Args:
            peliculas (dict): Diccionario con todas las peliculas
      """
      limpiar_pantalla()

      print("Top 10 Peliculas mejor calificadas")
      print("=" * 60)

      todas_peliculas = []
      for genero, lista_peliculas in peliculas.items():
            for pelicula in lista_peliculas:
                  todas_peliculas.append((pelicula, genero))

      todas_peliculas.sort(key=lambda x: x [0]['rating'], reverse=True)

      top_10 = todas_peliculas[:10]

      print("Las mejores peliculas segun su calificacion")
      print("=" * 60)
      print(f"{'POS' :<4} {'Titulo' :<30} {'Genero' :<12} {'Rating':<8} {'año'}")
      print("-" * 60)

      for i, (pelicula, genero) in enumerate(top_10, 1):
            if i == 1:
                  pos = "🥇"
            elif i == 2:
                  pos = "🥈"
            elif i == 3:
                  pos = "🥉"
            else:
                  pos = f"{i:2d}."

            titulo = pelicula['Titulo']
            if len(titulo) > 27:
                  titulo = titulo[:24] + "..."

            genero_mostrar = genero.replace('_', ' ').title()
            if len(genero_mostrar) > 9:
                  genero_mostrar = genero_mostrar[:9] + "."

            print(f"{pos:<4} {titulo:<30} {genero_mostrar:<12} ⭐{pelicula['rating']:<7} {pelicula['año']}")
      
      print("━" * 60)
      print(f"11. ⬅️ Volver al menú principal")

      seleccionar_del_top_10(top_10)

def seleccionar_del_top_10(top_10):
      """
      Permite seleccionar una película del top 10
      
      Args:
            top_10 (list): Lista de tuplas (pelicula, genero) del top 10
      """
      
      while True:
            
def main():
      
      """Función pirncipal del programa"""
      print("Iniciando netflix console...")

      print("Programa iniciado correctamente")
      
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
      
      """Funcion principal del menu interactivo"""

      print("Iniciando Netflix Console...")
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

            opcion = obtener_opcion_usuario()

            if opcion == "0":
                  limpiar_pantalla()
                  print("Gracias por usar Netflix Console")
                  print("Que disfrutes viendo peliculas")
                  print("Hasta la proxima")
                  break

            elif opcion == "1":
                  procesar_seleccion_genero(peliculas, "accion", "ACCION")
                  pausar()
                  
            elif opcion == "2":
                  procesar_seleccion_genero(peliculas, "comedia", "COMEDIA")
                  pausar()

            elif opcion == "3":
                  procesar_seleccion_genero(peliculas, "terror", "TERROR")
                  pausar()

            elif opcion == "4":
                  procesar_seleccion_genero(peliculas, "romance", "ROMANCE")
                  pausar()
                  
            elif opcion == "5":
                  procesar_seleccion_genero(peliculas, "ciencia_ficcion", "CIENCIA_FICCION")
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
                  mostrar_estadisticas_carga(peliculas)
                  pausar()
                  
      
      

if __name__ == "__main__":
      main()