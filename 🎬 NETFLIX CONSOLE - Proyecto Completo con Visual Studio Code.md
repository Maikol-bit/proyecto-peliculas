# 🎬 NETFLIX CONSOLE - Proyecto Completo con Visual Studio Code

**Crea tu propio Netflix en la consola de Python**

------

## 📋 **TABLA DE CONTENIDOS**

1. [Preparación del entorno](#preparación-del-entorno)
2. [Configuración del proyecto](#configuración-del-proyecto)
3. [Paso 1: Estructura inicial](#paso-1-estructura-inicial)
4. [Paso 2: Cargando datos desde JSON](#paso-2-cargando-datos-desde-json)
5. [Paso 3: Menú principal interactivo](#paso-3-menú-principal-interactivo)
6. [Paso 4: Navegación por géneros](#paso-4-navegación-por-géneros)
7. [Paso 5: Detalles de películas](#paso-5-detalles-de-películas)
8. [Paso 6: Completando todos los géneros](#paso-6-completando-todos-los-géneros)
9. [Paso 7: Función de búsqueda](#paso-7-función-de-búsqueda)
10. [Paso 8: Top 10 películas](#paso-8-top-10-películas)
11. [Paso 9: Sistema de favoritos](#paso-9-sistema-de-favoritos)
12. [Paso 10: Mejoras finales](#paso-10-mejoras-finales)
13. [Debugging y solución de problemas](#debugging-y-solución-de-problemas)
14. [Expansiones avanzadas](#expansiones-avanzadas)

------

## 🛠️ **PREPARACIÓN DEL ENTORNO**

### **¿Qué necesitas instalar?**

#### **1. Python 3.8 o superior**

1. Ve a [python.org](https://www.python.org/downloads/)

2. Descarga la versión más reciente

3. **MUY IMPORTANTE:** Durante la instalación, marca la casilla "Add Python to PATH"

4. Verifica la instalación abriendo terminal/cmd y escribiendo:

   bash

   ```bash
   python --version
   ```

#### **2. Visual Studio Code**

1. Ve a [code.visualstudio.com](https://code.visualstudio.com/)
2. Descarga e instala VS Code
3. Abre VS Code

#### **3. Extensión de Python para VS Code**

1. En VS Code, presiona `Ctrl+Shift+X` (Windows/Linux) o `Cmd+Shift+X` (Mac)
2. Busca "Python" (de Microsoft)
3. Instala la extensión oficial de Python
4. Reinicia VS Code

### **Verificación del entorno**

Abre terminal en VS Code (`Ctrl+`` ` o `View → Terminal`) y ejecuta:

bash

```bash
python --version
pip --version
```

Deberías ver las versiones instaladas.

------

## 📁 **CONFIGURACIÓN DEL PROYECTO**

### **1. Crear la carpeta del proyecto**

1. Crea una carpeta en tu escritorio llamada `netflix-console`
2. Abre VS Code
3. Ve a `File → Open Folder` (o `Archivo → Abrir carpeta`)
4. Selecciona la carpeta `netflix-console`

### **2. Estructura del proyecto**

Tu proyecto tendrá esta estructura:

```
netflix-console/
├── main.py              # Archivo principal del programa
├── peliculas.json       # Base de datos de películas (ya tienes este archivo)
├── utils.py             # Funciones auxiliares (opcional)
└── README.md            # Documentación del proyecto (opcional)
```

### **3. Configurar el archivo JSON**

1. Coloca tu archivo `peliculas.json` en la carpeta `netflix-console`
2. **IMPORTANTE:** El archivo JSON debe estar en la misma carpeta que `main.py`
3. Verifica que el archivo contenga las 40 películas organizadas por género:
   - `accion` (8 películas)
   - `comedia` (8 películas)
   - `terror` (8 películas)
   - `romance` (8 películas)
   - `ciencia_ficcion` (8 películas)

### **4. Crear archivo principal**

1. En VS Code, presiona `Ctrl+N` para crear un archivo nuevo
2. Guárdalo como `main.py` (`Ctrl+S`)
3. VS Code debería reconocer automáticamente que es un archivo Python

------

## 🚀 **PASO 1: ESTRUCTURA INICIAL**

### **1.1 Configurar el archivo main.py**

Comienza escribiendo la estructura básica:

python

```python
"""
NETFLIX CONSOLE
Proyecto de programación en Python
Autor: [Tu nombre aquí]
Fecha: [Fecha actual]

Descripción: Sistema de navegación de películas tipo Netflix
usando archivos JSON y menús interactivos.
"""

import json
import os
import sys

# Variables globales
favoritas = []  # Lista para almacenar películas favoritas
historial = []  # Lista para historial de películas vistas

def main():
    """Función principal del programa"""
    print("🎬 Iniciando Netflix Console...")
    
    # Por ahora solo mostramos un mensaje
    print("✅ Programa iniciado correctamente")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
```

### **1.2 Primera prueba**

1. Guarda el archivo (`Ctrl+S`)

2. Abre la terminal en VS Code (`Ctrl+`` `)

3. Ejecuta el programa:

   bash

   ```bash
   python main.py
   ```

4. Resultado esperado:

   ```
   🎬 Iniciando Netflix Console...
   ✅ Programa iniciado correctamente
   ```

### **1.3 Configurar debugging en VS Code**

1. Presiona `F5` o ve a `Run → Start Debugging`
2. Selecciona "Python File" si se te pregunta
3. Esto te permitirá usar debugging más adelante

------

## 📊 **PASO 2: CARGANDO DATOS DESDE JSON**

### **2.1 Entender el formato JSON**

El archivo JSON tiene esta estructura:

json

```json
{
  "accion": [
    {
      "id": 1,
      "titulo": "Nombre de la película",
      "año": 2022,
      "duración": "120 min",
      "sinopsis": "Descripción de la película...",
      "rating": 8.5,
      "director": "Nombre del director",
      "actores": "Actor1, Actor2, Actor3"
    }
  ],
  "comedia": [...],
  "terror": [...],
  "romance": [...],
  "ciencia_ficcion": [...]
}
```

### **2.2 Crear función para cargar películas**

Reemplaza tu `main.py` con:

python

```python
"""
NETFLIX CONSOLE - Carga de datos JSON
"""

import json
import os

def cargar_peliculas():
    """
    Carga las películas desde el archivo JSON
    
    Returns:
        dict: Diccionario con las películas organizadas por género
        None: Si hay algún error al cargar el archivo
    """
    try:
        # Verificar que el archivo existe
        if not os.path.exists('peliculas.json'):
            print("❌ Error: No se encontró el archivo 'peliculas.json'")
            print("💡 Asegúrate de que esté en la misma carpeta que main.py")
            return None
        
        # Abrir y leer el archivo JSON
        with open('peliculas.json', 'r', encoding='utf-8') as archivo:
            peliculas = json.load(archivo)
            
        # Verificar que se cargaron datos
        if not peliculas:
            print("❌ Error: El archivo JSON está vacío")
            return None
            
        return peliculas
        
    except json.JSONDecodeError as e:
        print(f"❌ Error: El archivo JSON tiene formato incorrecto")
        print(f"Detalle del error: {e}")
        return None
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return None

def mostrar_estadisticas_carga(peliculas):
    """
    Muestra estadísticas de las películas cargadas
    
    Args:
        peliculas (dict): Diccionario con las películas
    """
    if not peliculas:
        return
    
    print("\n📊 ESTADÍSTICAS DE CARGA:")
    print("=" * 30)
    
    total_peliculas = 0
    for genero, lista_peliculas in peliculas.items():
        cantidad = len(lista_peliculas)
        total_peliculas += cantidad
        print(f"🎭 {genero.replace('_', ' ').title()}: {cantidad} películas")
    
    print("=" * 30)
    print(f"📽️ Total de películas: {total_peliculas}")
    
    # Mostrar película con mejor rating
    mejor_pelicula = None
    mejor_rating = 0
    
    for genero in peliculas.values():
        for pelicula in genero:
            if pelicula['rating'] > mejor_rating:
                mejor_rating = pelicula['rating']
                mejor_pelicula = pelicula
    
    if mejor_pelicula:
        print(f"⭐ Mejor calificada: {mejor_pelicula['titulo']} ({mejor_rating}/10)")

def main():
    """Función principal del programa"""
    print("🎬 NETFLIX CONSOLE - Cargando datos...")
    print("=" * 50)
    
    # Cargar las películas
    print("📥 Cargando películas desde peliculas.json...")
    peliculas = cargar_peliculas()
    
    if peliculas:
        print("✅ ¡Películas cargadas exitosamente!")
        mostrar_estadisticas_carga(peliculas)
    else:
        print("❌ Error: No se pudieron cargar las películas")
        print("🔧 Revisa que el archivo peliculas.json esté en la carpeta correcta")
        return
    
    print("\n🎉 Sistema listo para usar")

if __name__ == "__main__":
    main()
```

### **2.3 Prueba de carga de datos**

1. Ejecuta el programa: `python main.py`

2. Resultado esperado:

   ```
   🎬 NETFLIX CONSOLE - Cargando datos...
   ==================================================
   📥 Cargando películas desde peliculas.json...
   ✅ ¡Películas cargadas exitosamente!
   
   📊 ESTADÍSTICAS DE CARGA:
   ==============================
   🎭 Accion: 8 películas
   🎭 Comedia: 8 películas
   🎭 Terror: 8 películas
   🎭 Romance: 8 películas
   🎭 Ciencia Ficcion: 8 películas
   ==============================
   📽️ Total de películas: 40
   ⭐ Mejor calificada: [Nombre de película] (X.X/10)
   
   🎉 Sistema listo para usar
   ```

### **2.4 Manejo de errores**

Si obtienes errores, aquí están las soluciones:

**Error "FileNotFoundError":**

- El archivo `peliculas.json` no está en la carpeta correcta
- Muévelo a la misma carpeta donde está `main.py`

**Error "JSONDecodeError":**

- El archivo JSON tiene errores de formato
- Verifica que todas las comillas estén correctas
- Usa un validador JSON online para verificar el formato

**Error "UnicodeDecodeError":**

- Problema con caracteres especiales
- El código ya incluye `encoding='utf-8'` para solucionarlo

------

## 🎮 **PASO 3: MENÚ PRINCIPAL INTERACTIVO**

### **3.1 Diseñar la interfaz del menú**

Agrega estas funciones antes de `main()`:

python

```python
def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_header():
    """Muestra el encabezado del programa"""
    print("=" * 60)
    print("🎬" + " " * 20 + "NETFLIX CONSOLE" + " " * 20 + "🎬")
    print("=" * 60)
    print("🍿 Tu plataforma de películas favorita en la consola 🍿")
    print("=" * 60)

def mostrar_menu_principal():
    """Muestra el menú principal con todas las opciones"""
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
    Obtiene y valida la opción del usuario
    
    Returns:
        str: Opción válida del usuario
    """
    while True:
        try:
            opcion = input("\n👉 Elige una opción (0-9): ").strip()
            
            if opcion in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return opcion
            else:
                print("❌ Opción no válida. Usa números del 0 al 9.")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Error: {e}")

def pausar():
    """Pausa el programa hasta que el usuario presione Enter"""
    input("\n⏸️ Presiona Enter para continuar...")
```

### **3.2 Crear el bucle principal**

Reemplaza la función `main()`:

python

```python
def main():
    """Función principal con bucle de menú interactivo"""
    
    # Cargar datos
    print("🎬 Iniciando Netflix Console...")
    peliculas = cargar_peliculas()
    
    if not peliculas:
        print("❌ No se puede continuar sin las películas")
        return
    
    print("✅ Sistema cargado correctamente")
    pausar()
    
    # Bucle principal del menú
    while True:
        limpiar_pantalla()
        mostrar_header()
        mostrar_menu_principal()
        
        opcion = obtener_opcion_usuario()
        
        # Procesar la opción elegida
        if opcion == "0":
            limpiar_pantalla()
            print("🎬 ¡Gracias por usar Netflix Console! 🎬")
            print("🍿 ¡Que disfrutes viendo películas! 🍿")
            print("👋 ¡Hasta la próxima!")
            break
            
        elif opcion == "1":
            print("\n🔥 Has elegido: PELÍCULAS DE ACCIÓN")
            print("🚧 Función en desarrollo...")
            pausar()
            
        elif opcion == "2":
            print("\n😂 Has elegido: PELÍCULAS DE COMEDIA")
            print("🚧 Función en desarrollo...")
            pausar()
            
        elif opcion == "3":
            print("\n👻 Has elegido: PELÍCULAS DE TERROR")
            print("🚧 Función en desarrollo...")
            pausar()
            
        elif opcion == "4":
            print("\n❤️ Has elegido: PELÍCULAS DE ROMANCE")
            print("🚧 Función en desarrollo...")
            pausar()
            
        elif opcion == "5":
            print("\n🚀 Has elegido: PELÍCULAS DE CIENCIA FICCIÓN")
            print("🚧 Función en desarrollo...")
            pausar()
            
        elif opcion == "6":
            print("\n🔍 Has elegido: BUSCAR PELÍCULA")
            print("🚧 Función en desarrollo...")
            pausar()
            
        elif opcion == "7":
            print("\n🏆 Has elegido: TOP 10")
            print("🚧 Función en desarrollo...")
            pausar()
            
        elif opcion == "8":
            print("\n❤️ Has elegido: MIS FAVORITAS")
            print("🚧 Función en desarrollo...")
            pausar()
            
        elif opcion == "9":
            limpiar_pantalla()
            mostrar_header()
            mostrar_estadisticas_carga(peliculas)
            pausar()
```

### **3.3 Prueba del menú interactivo**

1. Ejecuta el programa: `python main.py`
2. Deberías poder:
   - Ver el menú principal
   - Navegar entre opciones
   - Ver estadísticas (opción 9)
   - Salir del programa (opción 0)

### **3.4 Debugging con VS Code**

Para debuggear tu código:

1. Coloca un breakpoint haciendo click en el margen izquierdo (círculo rojo)
2. Presiona `F5` para iniciar debugging
3. Usa `F10` para avanzar línea por línea
4. Usa `F5` para continuar la ejecución

------

## 🎭 **PASO 4: NAVEGACIÓN POR GÉNEROS**

### **4.1 Crear función para mostrar películas por género**

Agrega estas funciones antes de `main()`:

python

```python
def mostrar_peliculas_genero(peliculas, genero, nombre_genero):
    """
    Muestra todas las películas de un género específico
    
    Args:
        peliculas (dict): Diccionario con todas las películas
        genero (str): Clave del género en el diccionario
        nombre_genero (str): Nombre del género para mostrar
    """
    limpiar_pantalla()
    
    print("🎬" + f" PELÍCULAS DE {nombre_genero.upper()} " + "🎬")
    print("=" * 60)
    
    lista_peliculas = peliculas[genero]
    
    # Mostrar encabezado de la tabla
    print(f"{'#':<3} {'TÍTULO':<35} {'AÑO':<6} {'RATING':<8}")
    print("━" * 60)
    
    # Mostrar lista numerada de películas
    for i, pelicula in enumerate(lista_peliculas, 1):
        titulo = pelicula['titulo']
        if len(titulo) > 32:
            titulo = titulo[:29] + "..."
            
        print(f"{i:<3} {titulo:<35} {pelicula['año']:<6} ⭐{pelicula['rating']:<7}")
    
    print("━" * 60)
    print(f"{len(lista_peliculas) + 1}. ⬅️ Volver al menú principal")
    
    return seleccionar_pelicula_genero(lista_peliculas)

def seleccionar_pelicula_genero(lista_peliculas):
    """
    Permite al usuario seleccionar una película de la lista
    
    Args:
        lista_peliculas (list): Lista de películas del género
        
    Returns:
        dict or None: Película seleccionada o None si vuelve al menú
    """
    while True:
        try:
            print(f"\n👉 Elige una película (1-{len(lista_peliculas)}) o {len(lista_peliculas) + 1} para volver: ", end="")
            opcion = input().strip()
            
            if opcion == str(len(lista_peliculas) + 1):
                return None  # Volver al menú principal
            
            numero = int(opcion)
            if 1 <= numero <= len(lista_peliculas):
                return lista_peliculas[numero - 1]
            else:
                print(f"❌ Número fuera de rango. Usa 1-{len(lista_peliculas)} o {len(lista_peliculas) + 1}")
                
        except ValueError:
            print("❌ Por favor ingresa un número válido")
        except KeyboardInterrupt:
            return None

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
            break  # Volver al menú principal
        
        # Aquí después agregamos la función para mostrar detalles
        print(f"\n✅ Seleccionaste: {pelicula_seleccionada['titulo']}")
        print("🚧 Función de detalles en desarrollo...")
        pausar()
```

### **4.2 Integrar géneros en el menú principal**

Modifica la función `main()` para que las opciones funcionen:

python

```python
def main():
    """Función principal con bucle de menú interactivo"""
    
    # Cargar datos
    print("🎬 Iniciando Netflix Console...")
    peliculas = cargar_peliculas()
    
    if not peliculas:
        print("❌ No se puede continuar sin las películas")
        return
    
    print("✅ Sistema cargado correctamente")
    pausar()
    
    # Bucle principal del menú
    while True:
        limpiar_pantalla()
        mostrar_header()
        mostrar_menu_principal()
        
        opcion = obtener_opcion_usuario()
        
        # Procesar la opción elegida
        if opcion == "0":
            limpiar_pantalla()
            print("🎬 ¡Gracias por usar Netflix Console! 🎬")
            print("🍿 ¡Que disfrutes viendo películas! 🍿")
            print("👋 ¡Hasta la próxima!")
            break
            
        elif opcion == "1":
            procesar_seleccion_genero(peliculas, "accion", "ACCIÓN")
            
        elif opcion == "2":
            procesar_seleccion_genero(peliculas, "comedia", "COMEDIA")
            
        elif opcion == "3":
            procesar_seleccion_genero(peliculas, "terror", "TERROR")
            
        elif opcion == "4":
            procesar_seleccion_genero(peliculas, "romance", "ROMANCE")
            
        elif opcion == "5":
            procesar_seleccion_genero(peliculas, "ciencia_ficcion", "CIENCIA FICCIÓN")
            
        elif opcion == "6":
            print("\n🔍 Has elegido: BUSCAR PELÍCULA")
            print("🚧 Función en desarrollo...")
            pausar()
            
        elif opcion == "7":
            print("\n🏆 Has elegido: TOP 10")
            print("🚧 Función en desarrollo...")
            pausar()
            
        elif opcion == "8":
            print("\n❤️ Has elegido: MIS FAVORITAS")
            print("🚧 Función en desarrollo...")
            pausar()
            
        elif opcion == "9":
            limpiar_pantalla()
            mostrar_header()
            mostrar_estadisticas_carga(peliculas)
            pausar()
```

### **4.3 Prueba de navegación por géneros**

1. Ejecuta el programa: `python main.py`
2. Deberías poder:
   - Elegir cualquier género (1-5)
   - Ver la lista de películas del género
   - Seleccionar una película específica
   - Volver al menú principal

------

## 🎬 **PASO 5: DETALLES DE PELÍCULAS**

### **5.1 Crear función para mostrar detalles completos**

Agrega estas funciones:

python

```python
def mostrar_detalle_pelicula(pelicula):
    """
    Muestra todos los detalles de una película
    
    Args:
        pelicula (dict): Diccionario con los datos de la película
    """
    limpiar_pantalla()
    
    # Encabezado de la película
    print("🎬" + "=" * 58 + "🎬")
    titulo = pelicula['titulo'].upper()
    espacios = (60 - len(titulo)) // 2
    print(" " * espacios + titulo + " " * espacios)
    print("🎬" + "=" * 58 + "🎬")
    
    # Información básica
    print(f"\n📅 Año: {pelicula['año']}")
    print(f"⏱️ Duración: {pelicula['duración']}")
    print(f"⭐ Rating: {pelicula['rating']}/10")
    print(f"🎭 Director: {pelicula['director']}")
    print(f"👥 Actores principales: {pelicula['actores']}")
    
    # Sinopsis
    print(f"\n📖 SINOPSIS:")
    print("━" * 60)
    # Dividir la sinopsis en líneas de máximo 60 caracteres
    sinopsis = pelicula['sinopsis']
    palabras = sinopsis.split()
    linea_actual = ""
    
    for palabra in palabras:
        if len(linea_actual + palabra) <= 57:  # Dejar espacio para margen
            linea_actual += palabra + " "
        else:
            print(linea_actual.strip())
            linea_actual = palabra + " "
    
    if linea_actual:
        print(linea_actual.strip())
    
    print("━" * 60)
    
    return mostrar_opciones_pelicula(pelicula)

def mostrar_opciones_pelicula(pelicula):
    """
    Muestra las opciones disponibles para una película
    
    Args:
        pelicula (dict): Diccionario con los datos de la película
        
    Returns:
        str: Acción seleccionada por el usuario
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
            opcion = input("\n👉 Elige una opción (1-5): ").strip()
            
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
                print("❌ Opción no válida. Usa números del 1 al 5.")
                
        except KeyboardInterrupt:
            return "menu_principal"

def simular_reproduccion(pelicula):
    """
    Simula la reproducción de una película
    
    Args:
        pelicula (dict): Diccionario con los datos de la película
    """
    limpiar_pantalla()
    
    print("🎬" + "=" * 58 + "🎬")
    print(f"     🍿 REPRODUCIENDO: {pelicula['titulo']} 🍿")
    print("🎬" + "=" * 58 + "🎬")
    
    print("\n🎵 *Música épica de apertura* 🎵")
    print("🎥 *Títulos iniciales aparecen* 🎥")
    print("🍿 *Te acomodas en tu asiento virtual* 🍿")
    print("✨ *La magia del cine comienza* ✨")
    
    print(f"\n📽️ Disfrutando de '{pelicula['titulo']}'...")
    print(f"⏱️ Duración: {pelicula['duración']}")
    print("🎭 *Actuaciones increíbles en pantalla*")
    print("🎼 *Banda sonora épica*")
    
    input("\n⏸️ Presiona Enter cuando 'termines' de ver la película...")
    
    # Agregar al historial
    if pelicula not in historial:
        historial.append(pelicula)
    
    print("\n🎉 ¡Película terminada!")
    print("⭐ ¡Esperamos que la hayas disfrutado!")
    print(f"📚 '{pelicula['titulo']}' agregada a tu historial")
    
    pausar()
    return "volver_detalle"

def agregar_a_favoritas(pelicula):
    """
    Agrega una película a la lista de favoritas
    
    Args:
        pelicula (dict): Diccionario con los datos de la película
    """
    if pelicula in favoritas:
        print(f"\n💔 '{pelicula['titulo']}' ya está en tus favoritas")
    else:
        favoritas.append(pelicula)
        print(f"\n❤️ ¡'{pelicula['titulo']}' agregada a favoritas!")
        print(f"📊 Ahora tienes {len(favoritas)} película(s) favorita(s)")
    
    pausar()
    return "volver_detalle"

def mostrar_estadisticas_pelicula(pelicula):
    """
    Muestra estadísticas adicionales de una película
    
    Args:
        pelicula (dict): Diccionario con los datos de la película
    """
    print
```

Reintentar

SA

Continuar

Editar

python

```python
def mostrar_estadisticas_pelicula(pelicula):
   """
   Muestra estadísticas adicionales de una película
   
   Args:
       pelicula (dict): Diccionario con los datos de la película
   """
   print(f"\n📊 ESTADÍSTICAS DE '{pelicula['titulo']}'")
   print("━" * 50)
   
   # Estadísticas básicas
   print(f"🆔 ID en base de datos: {pelicula['id']}")
   print(f"📅 Año de estreno: {pelicula['año']}")
   
   # Calcular década
   decada = (pelicula['año'] // 10) * 10
   print(f"📆 Década: {decada}s")
   
   # Categorizar por rating
   rating = pelicula['rating']
   if rating >= 9.0:
       categoria = "🏆 OBRA MAESTRA"
   elif rating >= 8.0:
       categoria = "⭐ EXCELENTE"
   elif rating >= 7.0:
       categoria = "👍 MUY BUENA"
   elif rating >= 6.0:
       categoria = "😊 BUENA"
   else:
       categoria = "😐 REGULAR"
   
   print(f"🏅 Categoría: {categoria}")
   
   # Estadísticas de duración
   duracion_min = int(pelicula['duración'].split()[0])
   if duracion_min < 90:
       tipo_duracion = "⚡ CORTA"
   elif duracion_min < 150:
       tipo_duracion = "⏱️ ESTÁNDAR"
   else:
       tipo_duracion = "🕐 LARGA"
   
   print(f"⏱️ Tipo de duración: {tipo_duracion}")
   print(f"🕓 Minutos totales: {duracion_min}")
   
   # Contar actores
   num_actores = len(pelicula['actores'].split(','))
   print(f"👥 Actores principales: {num_actores}")
   
   pausar()
   return "volver_detalle"
```

### **5.2 Integrar detalles en la navegación**

Modifica la función `procesar_seleccion_genero`:

python

```python
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
            break  # Volver al menú principal
        
        # Mostrar detalles de la película
        while True:
            accion = mostrar_detalle_pelicula(pelicula_seleccionada)
            
            if accion == "volver_lista":
                break  # Volver a la lista del género
            elif accion == "menu_principal":
                return  # Volver al menú principal
            elif accion == "volver_detalle":
                continue  # Permanecer en los detalles
```

### **5.3 Prueba de detalles de películas**

1. Ejecuta el programa: `python main.py`
2. Deberías poder:
   - Seleccionar un género
   - Elegir una película específica
   - Ver todos los detalles de la película
   - "Reproducir" la película
   - Agregar a favoritas
   - Ver estadísticas adicionales
   - Navegar de vuelta

------

## 🔍 **PASO 6: COMPLETANDO TODOS LOS GÉNEROS**

En este punto, **todos los géneros ya funcionan** porque usamos la misma función `procesar_seleccion_genero` para todos. Vamos a agregar algunas mejoras específicas:

### **6.1 Personalizar mensajes por género**

Agrega esta función:

python

```python
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
    return mensajes.get(genero, "¡Disfruta de estas increíbles películas!")
```

### **6.2 Mejorar la visualización por género**

Modifica `mostrar_peliculas_genero`:

python

```python
def mostrar_peliculas_genero(peliculas, genero, nombre_genero):
    """
    Muestra todas las películas de un género específico
    
    Args:
        peliculas (dict): Diccionario con todas las películas
        genero (str): Clave del género en el diccionario
        nombre_genero (str): Nombre del género para mostrar
    """
    limpiar_pantalla()
    
    emoji = obtener_emoji_genero(genero)
    mensaje = obtener_mensaje_genero(genero)
    
    print(f"{emoji} PELÍCULAS DE {nombre_genero.upper()} {emoji}")
    print("=" * 60)
    print(f"✨ {mensaje}")
    print("=" * 60)
    
    lista_peliculas = peliculas[genero]
    
    # Mostrar encabezado de la tabla
    print(f"{'#':<3} {'TÍTULO':<35} {'AÑO':<6} {'RATING':<8}")
    print("━" * 60)
    
    # Mostrar lista numerada de películas
    for i, pelicula in enumerate(lista_peliculas, 1):
        titulo = pelicula['titulo']
        if len(titulo) > 32:
            titulo = titulo[:29] + "..."
        
        # Destacar películas con rating alto
        if pelicula['rating'] >= 8.0:
            print(f"{i:<3} {titulo:<35} {pelicula['año']:<6} ⭐{pelicula['rating']:<7} 🏆")
        else:
            print(f"{i:<3} {titulo:<35} {pelicula['año']:<6} ⭐{pelicula['rating']:<7}")
    
    print("━" * 60)
    print(f"{len(lista_peliculas) + 1}. ⬅️ Volver al menú principal")
    print(f"\n📊 Total en este género: {len(lista_peliculas)} películas")
    
    return seleccionar_pelicula_genero(lista_peliculas)
```

------

## 🔍 **PASO 7: FUNCIÓN DE BÚSQUEDA**

### **7.1 Crear función de búsqueda básica**

Agrega estas funciones:

python

```python
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
    
    termino = input("\n🔍 Escribe el título o parte del título: ").strip()
    
    if not termino:
        print("❌ Debes escribir algo para buscar")
        pausar()
        return
    
    resultados = []
    
    # Buscar en todos los géneros
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
    
    # Mostrar resultados
    print(f"{'#':<3} {'TÍTULO':<30} {'GÉNERO':<12} {'AÑO':<6} {'RATING'}")
    print("━" * 60)
    
    for i, (pelicula, genero) in enumerate(resultados, 1):
        titulo = pelicula['titulo']
        if len(titulo) > 27:
            titulo = titulo[:24] + "..."
        
        genero_mostrar = genero.replace('_', ' ').title()
        if len(genero_mostrar) > 9:
            genero_mostrar = genero_mostrar[:9] + "."
        
        print(f"{i:<3} {titulo:<30} {genero_mostrar:<12} {pelicula['año']:<6} ⭐{pelicula['rating']}")
    
    print("━" * 60)
    print(f"{len(resultados) + 1}. ⬅️ Volver al menú principal")
    
    # Permitir seleccionar una película de los resultados
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
            
            if opcion == str(len(resultados) + 1):
                return  # Volver al menú principal
            
            numero = int(opcion)
            if 1 <= numero <= len(resultados):
                pelicula_seleccionada = resultados[numero - 1][0]
                
                # Mostrar detalles de la película seleccionada
                while True:
                    accion = mostrar_detalle_pelicula(pelicula_seleccionada)
                    
                    if accion == "volver_lista":
                        return  # Volver al menú principal
                    elif accion == "menu_principal":
                        return  # Volver al menú principal
                    elif accion == "volver_detalle":
                        continue  # Permanecer en los detalles
            else:
                print(f"❌ Número fuera de rango. Usa 1-{len(resultados)} o {len(resultados) + 1}")
                
        except ValueError:
            print("❌ Por favor ingresa un número válido")
        except KeyboardInterrupt:
            return
```

### **7.2 Búsqueda avanzada**

Agrega función de búsqueda con filtros:

python

```python
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
            opcion = input("\n👉 Elige tipo de búsqueda (1-6): ").strip()
            
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
                break
            else:
                print("❌ Opción no válida. Usa números del 1 al 6.")
                
        except KeyboardInterrupt:
            break

def buscar_por_director(peliculas):
    """Busca películas por director"""
    termino = input("\n🎭 Escribe el nombre del director: ").strip()
    if not termino:
        return
    
    resultados = []
    for genero, lista_peliculas in peliculas.items():
        for pelicula in lista_peliculas:
            if termino.lower() in pelicula['director'].lower():
                resultados.append((pelicula, genero))
    
    mostrar_resultados_busqueda(resultados, f"director: {termino}")

def buscar_por_actor(peliculas):
    """Busca películas por actor"""
    termino = input("\n👥 Escribe el nombre del actor: ").strip()
    if not termino:
        return
    
    resultados = []
    for genero, lista_peliculas in peliculas.items():
        for pelicula in lista_peliculas:
            if termino.lower() in pelicula['actores'].lower():
                resultados.append((pelicula, genero))
    
    mostrar_resultados_busqueda(resultados, f"actor: {termino}")

def buscar_por_año(peliculas):
    """Busca películas por año"""
    try:
        año = int(input("\n📅 Escribe el año: ").strip())
        
        resultados = []
        for genero, lista_peliculas in peliculas.items():
            for pelicula in lista_peliculas:
                if pelicula['año'] == año:
                    resultados.append((pelicula, genero))
        
        mostrar_resultados_busqueda(resultados, f"año: {año}")
        
    except ValueError:
        print("❌ Por favor ingresa un año válido")
        pausar()

def buscar_por_rating(peliculas):
    """Busca películas por rating mínimo"""
    try:
        rating_min = float(input("\n⭐ Escribe el rating mínimo (ej: 8.0): ").strip())
        
        resultados = []
        for genero, lista_peliculas in peliculas.items():
            for pelicula in lista_peliculas:
                if pelicula['rating'] >= rating_min:
                    resultados.append((pelicula, genero))
        
        mostrar_resultados_busqueda(resultados, f"rating ≥ {rating_min}")
        
    except ValueError:
        print("❌ Por favor ingresa un número válido")
        pausar()
```

### **7.3 Integrar búsqueda en el menú principal**

Modifica la opción 6 en la función `main()`:

python

```python
elif opcion == "6":
    busqueda_avanzada(peliculas)
```

------

## 🏆 **PASO 8: TOP 10 PELÍCULAS**

### **8.1 Crear función para Top 10**

Agrega estas funciones:

python

```python
def mostrar_top_10(peliculas):
    """
    Muestra las 10 películas mejor calificadas
    
    Args:
        peliculas (dict): Diccionario con todas las películas
    """
    limpiar_pantalla()
    
    print("🏆 TOP 10 PELÍCULAS MEJOR CALIFICADAS 🏆")
    print("=" * 60)
    
    # Reunir todas las películas en una sola lista
    todas_peliculas = []
    for genero, lista_peliculas in peliculas.items():
        for pelicula in lista_peliculas:
            todas_peliculas.append((pelicula, genero))
    
    # Ordenar por rating de mayor a menor
    todas_peliculas.sort(key=lambda x: x[0]['rating'], reverse=True)
    
    # Tomar solo las primeras 10
    top_10 = todas_peliculas[:10]
    
    print("🥇 ¡Las mejores películas según su calificación!")
    print("=" * 60)
    print(f"{'POS':<4} {'TÍTULO':<30} {'GÉNERO':<12} {'RATING':<8} {'AÑO'}")
    print("━" * 60)
    
    for i, (pelicula, genero) in enumerate(top_10, 1):
        # Emojis especiales para los primeros 3 lugares
        if i == 1:
            pos = "🥇"
        elif i == 2:
            pos = "🥈"
        elif i == 3:
            pos = "🥉"
        else:
            pos = f"{i:2d}."
        
        titulo = pelicula['titulo']
        if len(titulo) > 27:
            titulo = titulo[:24] + "..."
        
        genero_mostrar = genero.replace('_', ' ').title()
        if len(genero_mostrar) > 9:
            genero_mostrar = genero_mostrar[:9] + "."
        
        print(f"{pos:<4} {titulo:<30} {genero_mostrar:<12} ⭐{pelicula['rating']:<7} {pelicula['año']}")
    
    print("━" * 60)
    print(f"11. ⬅️ Volver al menú principal")
    
    # Permitir seleccionar una película del top 10
    seleccionar_del_top_10(top_10)

def seleccionar_del_top_10(top_10):
    """
    Permite seleccionar una película del top 10
    
    Args:
        top_10 (list): Lista de tuplas (pelicula, genero) del top 10
    """
    while True:
        try:
            print(f"\n👉 Elige una película (1-10) o 11 para volver: ", end="")
            opcion = input().strip()
            
            if opcion == "11":
                return  # Volver al menú principal
            
            numero = int(opcion)
            if 1 <= numero <= 10:
                pelicula_seleccionada = top_10[numero - 1][0]
                
                # Mostrar detalles de la película seleccionada
                while True:
                    accion = mostrar_detalle_pelicula(pelicula_seleccionada)
                    
                    if accion in ["volver_lista", "menu_principal"]:
                        return
                    elif accion == "volver_detalle":
                        continue
            else:
                print("❌ Número fuera de rango. Usa 1-10 o 11")
                
        except ValueError:
            print("❌ Por favor ingresa un número válido")
        except KeyboardInterrupt:
            return

def estadisticas_ratings(peliculas):
    """
    Muestra estadísticas adicionales sobre ratings
    
    Args:
        peliculas (dict): Diccionario con todas las películas
    """
    print("\n📊 ESTADÍSTICAS DE RATINGS")
    print("━" * 40)
    
    todas_peliculas = []
    for lista_peliculas in peliculas.values():
        todas_peliculas.extend(lista_peliculas)
    
    ratings = [p['rating'] for p in todas_peliculas]
    
    promedio = sum(ratings) / len(ratings)
    rating_max = max(ratings)
    rating_min = min(ratings)
    
    print(f"📈 Rating promedio: {promedio:.2f}/10")
    print(f"🏆 Rating más alto: {rating_max}/10")
    print(f"📉 Rating más bajo: {rating_min}/10")
    
    # Contar por categorías
    excelentes = len([r for r in ratings if r >= 8.0])
    muy_buenas = len([r for r in ratings if 7.0 <= r < 8.0])
    buenas = len([r for r in ratings if 6.0 <= r < 7.0])
    regulares = len([r for r in ratings if r < 6.0])
    
    print(f"\n🏆 Excelentes (≥8.0): {excelentes} películas")
    print(f"⭐ Muy buenas (7.0-7.9): {muy_buenas} películas")
    print(f"👍 Buenas (6.0-6.9): {buenas} películas")
    print(f"😐 Regulares (<6.0): {regulares} películas")
    
    pausar()
```

### **8.2 Integrar Top 10 en el menú**

Modifica la opción 7 en la función `main()`:

python

```python
elif opcion == "7":
    mostrar_top_10(peliculas)
    estadisticas_ratings(peliculas)
```

------

## ❤️ **PASO 9: SISTEMA DE FAVORITOS**

### **9.1 Gestión de favoritos**

Agrega estas funciones:

python

```python
def mostrar_favoritas():
    """Muestra la lista de películas favoritas"""
    limpiar_pantalla()
    
    print("❤️ MIS PELÍCULAS FAVORITAS ❤️")
    print("=" * 50)
    
    if not favoritas:
        print("💔 No tienes películas favoritas aún")
        print("\n💡 Consejos para agregar favoritas:")
        print("   • Navega por géneros")
        print("   • Selecciona una película")
        print("   • Elige 'Agregar a favoritas'")
        pausar()
        return
    
    print(f"❤️ Tienes {len(favoritas)} película(s) favorita(s)")
    print("=" * 50)
    print(f"{'#':<3} {'TÍTULO':<35} {'AÑO':<6} {'RATING'}")
    print("━" * 50)
    
    for i, pelicula in enumerate(favoritas, 1):
        titulo = pelicula['titulo']
        if len(titulo) > 32:
            titulo = titulo[:29] + "..."
        
        print(f"{i:<3} {titulo:<35} {pelicula['año']:<6} ⭐{pelicula['rating']}")
    
    print("━" * 50)
    print(f"{len(favoritas) + 1}. 🗑️ Eliminar película de favoritas")
    print(f"{len(favoritas) + 2}. 📊 Estadísticas de favoritas")
    print(f"{len(favoritas) + 3}. ⬅️ Volver al menú principal")
    
    gestionar_favoritas()

def gestionar_favoritas():
    """Gestiona las acciones en la lista de favoritas"""
    while True:
        try:
            opcion_max = len(favoritas) + 3
            print(f"\n👉 Elige una opción (1-{opcion_max}): ", end="")
            opcion = input().strip()
            
            if opcion == str(len(favoritas) + 3):
                return  # Volver al menú principal
            elif opcion == str(len(favoritas) + 2):
                mostrar_estadisticas_favoritas()
                return
            elif opcion == str(len(favoritas) + 1):
                eliminar_de_favoritas()
                return
            
            numero = int(opcion)
            if 1 <= numero <= len(favoritas):
                pelicula_seleccionada = favoritas[numero - 1]
                
                # Mostrar detalles de la película seleccionada
                while True:
                    accion = mostrar_detalle_pelicula(pelicula_seleccionada)
                    
                    if accion in ["volver_lista", "menu_principal"]:
                        return
                    elif accion == "volver_detalle":
                        continue
            else:
                print(f"❌ Número fuera de rango. Usa 1-{opcion_max}")
                
        except ValueError:
            print("❌ Por favor ingresa un número válido")
        except KeyboardInterrupt:
            return

def eliminar_de_favoritas():
    """Permite eliminar películas de favoritas"""
    if not favoritas:
        print("❌ No hay películas para eliminar")
        pausar()
        return
    
    limpiar_pantalla()
    print("🗑️ ELIMINAR DE FAVORITAS")
    print("=" * 40)
    
    print(f"{'#':<3} {'TÍTULO':<30} {'AÑO'}")
    print("━" * 40)
    
    for i, pelicula in enumerate(favoritas, 1):
        titulo = pelicula['titulo']
        if len(titulo) > 27:
            titulo = titulo[:24] + "..."
        print(f"{i:<3} {titulo:<30} {pelicula['año']}")
    
    print("━" * 40)
    print(f"{len(favoritas) + 1}. ⬅️ Cancelar")
    
    while True:
        try:
            print(f"\n👉 ¿Cuál quieres eliminar? (1-{len(favoritas) + 1}): ", end="")
            opcion = input().strip()
            
            if opcion == str(len(favoritas) + 1):
                return
            
            numero = int(opcion)
            if 1 <= numero <= len(favoritas):
                pelicula_eliminada = favoritas.pop(numero - 1)
                print(f"\n💔 '{pelicula_eliminada['titulo']}' eliminada de favoritas")
                pausar()
                return
            else:
                print(f"❌ Número fuera de rango")
                
        except ValueError:
            print("❌ Por favor ingresa un número válido")
        except KeyboardInterrupt:
            return

def mostrar_estadisticas_favoritas():
    """Muestra estadísticas de las películas favoritas"""
    if not favoritas:
        print("\n❌ No hay favoritas para mostrar estadísticas")
        pausar()
        return
    
    print("\n📊 ESTADÍSTICAS DE TUS FAVORITAS")
    print("━" * 45)
    
    # Rating promedio
    ratings = [p['rating'] for p in favoritas]
    promedio = sum(ratings) / len(ratings)
    print(f"⭐ Rating promedio: {promedio:.2f}/10")
    
    # Año más antiguo y más reciente
    años = [p['año'] for p in favoritas]
    print(f"📅 Película más antigua: {min(años)}")
    print(f"📅 Película más reciente: {max(años)}")
    
    # Géneros favoritos (requiere buscar el género de cada película)
    print(f"🎬 Total de favoritas: {len(favoritas)}")
    
    # Mejor calificada en favoritas
    mejor = max(favoritas, key=lambda x: x['rating'])
    print(f"🏆 Tu favorita mejor calificada: {mejor['titulo']} ({mejor['rating']}/10)")
    
    pausar()
```

### **9.2 Integrar favoritos en el menú**

Modifica la opción 8 en la función `main()`:

python

```python
elif opcion == "8":
    mostrar_favoritas()
```

------

## 📊 **PASO 10: MEJORAS FINALES**

### **10.1 Estadísticas completas del sistema**

Mejora la función de estadísticas:

python

```python
def mostrar_estadisticas_completas(peliculas):
    """Muestra estadísticas completas del sistema"""
    limpiar_pantalla()
    
    print("📊 ESTADÍSTICAS COMPLETAS DEL SISTEMA")
    print("=" * 60)
    
    # Estadísticas básicas
    total_peliculas = sum(len(genero) for genero in peliculas.values())
    print(f"🎬 Total de películas en el sistema: {total_peliculas}")
    print(f"❤️ Películas en favoritas: {len(favoritas)}")
    print(f"📚 Películas vistas: {len(historial)}")
    
    print("\n🎭 PELÍCULAS POR GÉNERO:")
    print("━" * 30)
    for genero, lista_peliculas in peliculas.items():
        emoji = obt
```

Reintentar

SA

Continuar

Editar

python

```python
def mostrar_estadisticas_completas(peliculas):
   """Muestra estadísticas completas del sistema"""
   limpiar_pantalla()
   
   print("📊 ESTADÍSTICAS COMPLETAS DEL SISTEMA")
   print("=" * 60)
   
   # Estadísticas básicas
   total_peliculas = sum(len(genero) for genero in peliculas.values())
   print(f"🎬 Total de películas en el sistema: {total_peliculas}")
   print(f"❤️ Películas en favoritas: {len(favoritas)}")
   print(f"📚 Películas vistas: {len(historial)}")
   
   print("\n🎭 PELÍCULAS POR GÉNERO:")
   print("━" * 30)
   for genero, lista_peliculas in peliculas.items():
       emoji = obtener_emoji_genero(genero)
       nombre = genero.replace('_', ' ').title()
       print(f"{emoji} {nombre}: {len(lista_peliculas)} películas")
   
   # Estadísticas de años
   print("\n📅 ESTADÍSTICAS POR DÉCADAS:")
   print("━" * 30)
   todas_peliculas = []
   for lista_peliculas in peliculas.values():
       todas_peliculas.extend(lista_peliculas)
   
   decadas = {}
   for pelicula in todas_peliculas:
       decada = (pelicula['año'] // 10) * 10
       decadas[decada] = decadas.get(decada, 0) + 1
   
   for decada in sorted(decadas.keys()):
       print(f"📆 {decada}s: {decadas[decada]} películas")
   
   # Estadísticas de ratings
   print("\n⭐ ESTADÍSTICAS DE CALIFICACIONES:")
   print("━" * 35)
   ratings = [p['rating'] for p in todas_peliculas]
   promedio = sum(ratings) / len(ratings)
   
   print(f"📈 Rating promedio general: {promedio:.2f}/10")
   print(f"🏆 Rating más alto: {max(ratings)}/10")
   print(f"📉 Rating más bajo: {min(ratings)}/10")
   
   # Distribución de calificaciones
   excelentes = len([r for r in ratings if r >= 8.0])
   muy_buenas = len([r for r in ratings if 7.0 <= r < 8.0])
   buenas = len([r for r in ratings if 6.0 <= r < 7.0])
   regulares = len([r for r in ratings if r < 6.0])
   
   print(f"\n🏆 Excelentes (≥8.0): {excelentes} ({excelentes/total_peliculas*100:.1f}%)")
   print(f"⭐ Muy buenas (7.0-7.9): {muy_buenas} ({muy_buenas/total_peliculas*100:.1f}%)")
   print(f"👍 Buenas (6.0-6.9): {buenas} ({buenas/total_peliculas*100:.1f}%)")
   print(f"😐 Regulares (<6.0): {regulares} ({regulares/total_peliculas*100:.1f}%)")
   
   # Directores y actores más frecuentes
   mostrar_estadisticas_personas(todas_peliculas)
   
   pausar()

def mostrar_estadisticas_personas(todas_peliculas):
   """Muestra estadísticas de directores y actores"""
   print("\n🎭 DIRECTORES Y ACTORES MÁS FRECUENTES:")
   print("━" * 40)
   
   # Contar directores
   directores = {}
   for pelicula in todas_peliculas:
       director = pelicula['director']
       directores[director] = directores.get(director, 0) + 1
   
   # Mostrar top 3 directores
   top_directores = sorted(directores.items(), key=lambda x: x[1], reverse=True)[:3]
   print("🎬 Top directores:")
   for i, (director, cantidad) in enumerate(top_directores, 1):
       print(f"   {i}. {director}: {cantidad} película(s)")
   
   # Contar actores (esto es más complejo porque hay múltiples actores por película)
   actores = {}
   for pelicula in todas_peliculas:
       lista_actores = [actor.strip() for actor in pelicula['actores'].split(',')]
       for actor in lista_actores:
           actores[actor] = actores.get(actor, 0) + 1
   
   # Mostrar top 3 actores
   top_actores = sorted(actores.items(), key=lambda x: x[1], reverse=True)[:3]
   print("\n👥 Top actores:")
   for i, (actor, cantidad) in enumerate(top_actores, 1):
       print(f"   {i}. {actor}: {cantidad} película(s)")
```

### **10.2 Mejorar la navegación general**

Agrega función para confirmación de salida:

python

```python
def confirmar_salida():
    """Confirma si el usuario realmente quiere salir"""
    print("\n❓ ¿Estás seguro de que quieres salir?")
    print("1. ✅ Sí, salir del programa")
    print("2. ❌ No, volver al menú")
    
    while True:
        try:
            opcion = input("\n👉 Elige (1 o 2): ").strip()
            if opcion == "1":
                return True
            elif opcion == "2":
                return False
            else:
                print("❌ Opción no válida. Usa 1 o 2.")
        except KeyboardInterrupt:
            return True

def mostrar_resumen_sesion():
    """Muestra un resumen de la sesión actual"""
    print("\n📋 RESUMEN DE TU SESIÓN:")
    print("━" * 30)
    print(f"❤️ Películas agregadas a favoritas: {len(favoritas)}")
    print(f"🍿 Películas 'vistas': {len(historial)}")
    
    if historial:
        print("\n🎬 Últimas películas vistas:")
        for i, pelicula in enumerate(historial[-3:], 1):  # Últimas 3
            print(f"   {i}. {pelicula['titulo']} ({pelicula['año']})")
    
    if favoritas:
        print(f"\n❤️ Tu película favorita mejor calificada:")
        mejor_favorita = max(favoritas, key=lambda x: x['rating'])
        print(f"   🏆 {mejor_favorita['titulo']} ({mejor_favorita['rating']}/10)")

def limpiar_datos_sesion():
    """Pregunta si quiere limpiar los datos de la sesión"""
    if favoritas or historial:
        print("\n🗑️ ¿Quieres limpiar los datos de esta sesión?")
        print("   (Esto eliminará favoritas e historial)")
        print("1. ✅ Sí, limpiar todo")
        print("2. ❌ No, mantener datos")
        
        try:
            opcion = input("\n👉 Elige (1 o 2): ").strip()
            if opcion == "1":
                favoritas.clear()
                historial.clear()
                print("🧹 Datos de sesión limpiados")
        except:
            pass
```

### **10.3 Función main() final completa**

Aquí está la función `main()` final con todas las mejoras:

python

```python
def main():
    """Función principal con bucle de menú interactivo"""
    
    # Cargar datos
    print("🎬 Iniciando Netflix Console...")
    print("⏳ Cargando base de datos de películas...")
    
    peliculas = cargar_peliculas()
    
    if not peliculas:
        print("❌ No se puede continuar sin las películas")
        input("Presiona Enter para salir...")
        return
    
    print("✅ Sistema cargado correctamente")
    print(f"📊 {sum(len(genero) for genero in peliculas.values())} películas disponibles")
    pausar()
    
    # Bucle principal del menú
    while True:
        try:
            limpiar_pantalla()
            mostrar_header()
            mostrar_menu_principal()
            
            opcion = obtener_opcion_usuario()
            
            # Procesar la opción elegida
            if opcion == "0":
                if confirmar_salida():
                    limpiar_pantalla()
                    mostrar_header()
                    mostrar_resumen_sesion()
                    limpiar_datos_sesion()
                    
                    print("\n🎬 ¡Gracias por usar Netflix Console! 🎬")
                    print("🍿 ¡Que disfrutes viendo películas reales! 🍿")
                    print("👋 ¡Hasta la próxima!")
                    break
                
            elif opcion == "1":
                procesar_seleccion_genero(peliculas, "accion", "ACCIÓN")
                
            elif opcion == "2":
                procesar_seleccion_genero(peliculas, "comedia", "COMEDIA")
                
            elif opcion == "3":
                procesar_seleccion_genero(peliculas, "terror", "TERROR")
                
            elif opcion == "4":
                procesar_seleccion_genero(peliculas, "romance", "ROMANCE")
                
            elif opcion == "5":
                procesar_seleccion_genero(peliculas, "ciencia_ficcion", "CIENCIA FICCIÓN")
                
            elif opcion == "6":
                busqueda_avanzada(peliculas)
                
            elif opcion == "7":
                mostrar_top_10(peliculas)
                
            elif opcion == "8":
                mostrar_favoritas()
                
            elif opcion == "9":
                mostrar_estadisticas_completas(peliculas)
                
        except KeyboardInterrupt:
            if confirmar_salida():
                break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            print("🔧 El programa continuará funcionando...")
            pausar()

if __name__ == "__main__":
    main()
```

------

## 🐛 **DEBUGGING Y SOLUCIÓN DE PROBLEMAS**

### **Errores comunes y soluciones:**

#### **1. FileNotFoundError**

```
❌ Error: No se encontró el archivo 'peliculas.json'
```

**Solución:**

- Verifica que `peliculas.json` esté en la misma carpeta que `main.py`
- En VS Code, verifica en el explorador de archivos que ambos estén al mismo nivel

#### **2. JSONDecodeError**

```
❌ Error: El archivo JSON tiene formato incorrecto
```

**Solución:**

- Usa un validador JSON online (jsonlint.com)
- Verifica comillas dobles en lugar de simples
- Verifica que no falten comas entre elementos

#### **3. UnicodeDecodeError**

```
❌ Error de codificación de caracteres
```

**Solución:**

- El código ya incluye `encoding='utf-8'`
- Si persiste, guarda el JSON con codificación UTF-8

#### **4. IndentationError**

```
❌ Error de indentación
```

**Solución:**

- Usa 4 espacios consistentemente
- En VS Code: `View → Command Palette → "Convert Indentation to Spaces"`

### **Debugging en VS Code:**

1. Colocar breakpoints:
   - Click en el margen izquierdo (aparece punto rojo)
2. Iniciar debugging:
   - Presiona `F5`
   - Selecciona "Python File"
3. Controles de debugging:
   - `F5`: Continuar
   - `F10`: Paso sobre (step over)
   - `F11`: Paso dentro (step into)
   - `Shift+F11`: Paso fuera (step out)
4. Ver variables:
   - Panel izquierdo muestra variables locales
   - Panel "Watch" para monitorear variables específicas

------

## 🚀 **EXPANSIONES AVANZADAS**

### **1. Guardado de datos persistente**

python

```python
import pickle

def guardar_datos_usuario():
    """Guarda favoritas e historial en archivo"""
    datos = {
        'favoritas': favoritas,
        'historial': historial
    }
    try:
        with open('datos_usuario.pkl', 'wb') as archivo:
            pickle.dump(datos, archivo)
        print("✅ Datos guardados correctamente")
    except Exception as e:
        print(f"❌ Error guardando datos: {e}")

def cargar_datos_usuario():
    """Carga favoritas e historial desde archivo"""
    global favoritas, historial
    try:
        with open('datos_usuario.pkl', 'rb') as archivo:
            datos = pickle.load(archivo)
            favoritas.extend(datos.get('favoritas', []))
            historial.extend(datos.get('historial', []))
        print("✅ Datos de usuario cargados")
    except FileNotFoundError:
        print("ℹ️ Primera vez ejecutando, no hay datos previos")
    except Exception as e:
        print(f"❌ Error cargando datos: {e}")
```

### **2. Sistema de recomendaciones**

python

```python
def recomendar_peliculas(peliculas):
    """Sistema básico de recomendaciones"""
    if not favoritas:
        print("❌ Agrega películas a favoritas para recibir recomendaciones")
        return
    
    # Calcular géneros favoritos
    generos_favoritos = {}
    for pelicula in favoritas:
        # Buscar género de cada película favorita
        for genero, lista in peliculas.items():
            if pelicula in lista:
                generos_favoritos[genero] = generos_favoritos.get(genero, 0) + 1
    
    # Género más frecuente en favoritas
    genero_favorito = max(generos_favoritos, key=generos_favoritos.get)
    
    # Recomendar películas del género favorito que no estén en favoritas
    recomendaciones = []
    for pelicula in peliculas[genero_favorito]:
        if pelicula not in favoritas and pelicula['rating'] >= 7.0:
            recomendaciones.append(pelicula)
    
    # Mostrar recomendaciones
    print(f"🎯 RECOMENDACIONES PARA TI")
    print(f"🎭 Basado en tu amor por {genero_favorito.replace('_', ' ').title()}")
    
    for i, pelicula in enumerate(recomendaciones[:5], 1):
        print(f"{i}. {pelicula['titulo']} ({pelicula['año']}) ⭐{pelicula['rating']}")
```

### **3. Filtros avanzados**

python

```python
def filtros_avanzados(peliculas):
    """Filtros múltiples combinados"""
    print("🔧 FILTROS AVANZADOS")
    
    # Filtro por rango de años
    año_min = int(input("Año mínimo (ej: 2000): ") or 1900)
    año_max = int(input("Año máximo (ej: 2023): ") or 2030)
    
    # Filtro por rating mínimo
    rating_min = float(input("Rating mínimo (ej: 7.0): ") or 0.0)
    
    # Aplicar filtros
    resultados = []
    for genero, lista_peliculas in peliculas.items():
        for pelicula in lista_peliculas:
            if (año_min <= pelicula['año'] <= año_max and 
                pelicula['rating'] >= rating_min):
                resultados.append((pelicula, genero))
    
    mostrar_resultados_busqueda(resultados, f"filtros: {año_min}-{año_max}, rating≥{rating_min}")
```

### **4. Estadísticas visuales (ASCII)**

python

```python
def grafico_ascii_ratings(peliculas):
    """Crea un gráfico ASCII de distribución de ratings"""
    todas_peliculas = []
    for lista in peliculas.values():
        todas_peliculas.extend(lista)
    
    # Agrupar por rating (redondeado)
    distribucion = {}
    for pelicula in todas_peliculas:
        rating_grupo = int(pelicula['rating'])
        distribucion[rating_grupo] = distribucion.get(rating_grupo, 0) + 1
    
    print("\n📊 DISTRIBUCIÓN DE RATINGS")
    print("=" * 40)
    
    max_cantidad = max(distribucion.values())
    
    for rating in range(1, 11):
        cantidad = distribucion.get(rating, 0)
        barra = "█" * int((cantidad / max_cantidad) * 20) if cantidad > 0 else ""
        print(f"{rating:2d} |{barra:<20} {cantidad}")
    
    print("=" * 40)
```

### **5. Modo aleatorio**

python

```python
import random

def modo_aleatorio(peliculas):
    """Selecciona una película aleatoria"""
    print("🎲 MODO ALEATORIO - ¡SORPRÉNDEME!")
    
    todas_peliculas = []
    for genero, lista in peliculas.items():
        for pelicula in lista:
            todas_peliculas.append((pelicula, genero))
    
    pelicula_aleatoria, genero = random.choice(todas_peliculas)
    
    print(f"🎯 Tu película sorpresa:")
    print(f"🎬 {pelicula_aleatoria['titulo']}")
    print(f"🎭 Género: {genero.replace('_', ' ').title()}")
    print(f"⭐ Rating: {pelicula_aleatoria['rating']}/10")
    
    if input("\n¿Quieres ver los detalles? (s/n): ").lower() == 's':
        mostrar_detalle_pelicula(pelicula_aleatoria)
```

------

## 📚 **RESUMEN FINAL DEL PROYECTO**

### **¿Qué has creado?**

Un sistema completo de gestión de películas con:

✅ **40 películas reales** organizadas por género ✅ **Navegación intuitiva** con menús interactivos ✅ **Búsqueda avanzada** por múltiples criterios ✅ **Sistema de favoritos** personalizado ✅ **Top 10** de mejores películas ✅ **Estadísticas completas** del sistema ✅ **Simulación de reproducción** de películas ✅ **Manejo robusto de errores** ✅ **Interfaz visual atractiva** con emojis

### **Habilidades desarrolladas:**

- 📁 Manejo de archivos JSON
- 🔧 Programación orientada a funciones
- 🎮 Interfaces de usuario en consola
- 🐛 Debugging y manejo de errores
- 📊 Manipulación de datos complejos
- 🔍 Algoritmos de búsqueda y filtrado
- 💾 Gestión de estado de aplicación

### **Posibles mejoras futuras:**

- 🌐 Integración con APIs de películas reales
- 💾 Base de datos SQLite en lugar de JSON
- 🎨 Interfaz gráfica con tkinter o PyQt
- 🔐 Sistema de usuarios múltiples
- 📱 Versión web con Flask/Django
- 🤖 IA para recomendaciones avanzadas

**¡Felicitaciones! Has creado tu propio Netflix Console completamente funcional.** 🎉

------

**Autor:** [Tu nombre]
 **Fecha:** [Fecha actual]
 **Versión:** 1.0
 **Lenguaje:** Python 3.8+
 **Dependencias:** Ninguna (solo librerías estándar)