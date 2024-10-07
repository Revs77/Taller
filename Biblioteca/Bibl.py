import os
import json
from datetime import datetime, timedelta

# Configuración del archivo de datos
RUTA_DATOS = 'libros.json'
RUTA_USUARIOS = 'usuarios.json'

def cargar_datos():
    """Carga los datos de los libros desde el archivo JSON."""
    if os.path.exists(RUTA_DATOS):
        with open(RUTA_DATOS, 'r') as archivo:
            return json.load(archivo)
    return []

def guardar_datos(libros):
    """Guarda los datos de los libros en el archivo JSON."""
    with open(RUTA_DATOS, 'w') as archivo:
        json.dump(libros, archivo, indent=2)

def cargar_usuarios():
    """Carga los datos de los usuarios desde el archivo JSON."""
    if os.path.exists(RUTA_USUARIOS):
        with open(RUTA_USUARIOS, 'r') as archivo:
            return json.load(archivo)
    return []

def guardar_usuarios(usuarios):
    """Guarda los datos de los usuarios en el archivo JSON."""
    with open(RUTA_USUARIOS, 'w') as archivo:
        json.dump(usuarios, archivo, indent=2)

def inicializar_archivos():
    """Inicializa los archivos JSON si no existen."""
    if not os.path.exists(RUTA_DATOS):
        guardar_datos([])
        print(f"Archivo {RUTA_DATOS} creado e inicializado con una lista vacía.")
    if not os.path.exists(RUTA_USUARIOS):
        guardar_usuarios([])
        print(f"Archivo {RUTA_USUARIOS} creado e inicializado con una lista vacía.")

def agregar_libro(titulo, autor, año):
    """Agrega un nuevo libro a la biblioteca."""
    libros = cargar_datos()
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "prestado": False,
        "usuario": None,
        "fecha_prestamo": None,
        "fecha_devolucion": None
    }
    libros.append(nuevo_libro)
    guardar_datos(libros)
    print(f"Libro agregado: {titulo} por {autor}")

def prestar_libro(titulo, nombre_usuario, tarjeta_identidad):
    """Marca un libro como prestado y registra el usuario y la fecha."""
    libros = cargar_datos()
    usuarios = cargar_usuarios()

    # Agregar usuario si no existe
    usuario_existente = next((u for u in usuarios if u['tarjeta_identidad'] == tarjeta_identidad), None)
    if not usuario_existente:
        nuevos_datos_usuario = {
            "nombre": nombre_usuario,
            "tarjeta_identidad": tarjeta_identidad,
            "penalizacion": None,
            "fecha_penalizacion": None
        }
        usuarios.append(nuevos_datos_usuario)
        guardar_usuarios(usuarios)

    for libro in libros:
        if libro["titulo"].lower() == titulo.lower() and not libro["prestado"]:
            libro["prestado"] = True
            libro["usuario"] = {"nombre": nombre_usuario, "tarjeta_identidad": tarjeta_identidad}
            libro["fecha_prestamo"] = datetime.now().isoformat()
            libro["fecha_devolucion"] = (datetime.now() + timedelta(days=5)).isoformat()
            guardar_datos(libros)
            print(f"Libro prestado: {libro['titulo']} a {nombre_usuario}. Debe devolverse antes de {libro['fecha_devolucion']}.")
            return
    print("Libro no disponible o no encontrado.")

def devolver_libro(titulo):
    """Marca un libro como devuelto y verifica la fecha de devolución."""
    libros = cargar_datos()
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower() and libro["prestado"]:
            libro["prestado"] = False
            libro["usuario"] = None
            fecha_devolucion = datetime.fromisoformat(libro["fecha_devolucion"])
            if datetime.now() > fecha_devolucion:
                print(f"Libro devuelto: {libro['titulo']}. Penalización aplicada: 1 semana.")
                registrar_penalizacion(libro["usuario"]["tarjeta_identidad"])
            else:
                print(f"Libro devuelto: {libro['titulo']}. Gracias por devolver a tiempo.")
            libro["fecha_prestamo"] = None
            libro["fecha_devolucion"] = None
            guardar_datos(libros)
            return
    print("No se puede devolver este libro.")

def registrar_penalizacion(tarjeta_identidad, dias=7):
    """Registra una penalización para un usuario específico."""
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["tarjeta_identidad"] == tarjeta_identidad:
            usuario["penalizacion"] = dias  # Días de penalización
            usuario["fecha_penalizacion"] = (datetime.now() + timedelta(days=dias)).isoformat()
            guardar_usuarios(usuarios)
            print(f"Penalización de {dias} días registrada para {usuario['nombre']}. Debe esperar hasta {usuario['fecha_penalizacion']}.")
            return
    print("Usuario no encontrado.")

def establecer_penalizacion(tarjeta_identidad, dias):
    """Establece una penalización manualmente para un usuario específico."""
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["tarjeta_identidad"] == tarjeta_identidad:
            usuario["penalizacion"] = dias
            usuario["fecha_penalizacion"] = (datetime.now() + timedelta(days=dias)).isoformat()
            guardar_usuarios(usuarios)
            print(f"Penalización de {dias} días establecida manualmente para {usuario['nombre']}.")
            return
    print("Usuario no encontrado.")

def listar_libros():
    """Muestra todos los libros en la biblioteca."""
    libros = cargar_datos()
    if not libros:
        print("La biblioteca está vacía.")
    else:
        print("Libros en la biblioteca:")
        for libro in libros:
            estado = "Prestado" if libro["prestado"] else "Disponible"
            usuario_info = f" | Prestado a: {libro['usuario']['nombre']}" if libro["prestado"] else ""
            print(f"- {libro['titulo']} por {libro['autor']} ({libro['año']}) | Estado: {estado}{usuario_info}")

def listar_usuarios():
    """Muestra todos los usuarios registrados en la biblioteca."""
    usuarios = cargar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for usuario in usuarios:
            penalizacion_info = f" | Penalización hasta: {usuario['fecha_penalizacion']}" if usuario["penalizacion"] else " | No penalizado"
            print(f"- {usuario['nombre']} | Tarjeta de identidad: {usuario['tarjeta_identidad']}{penalizacion_info}")

def buscar_por_autor(autor):
    """Busca y muestra los libros de un autor específico."""
    libros = cargar_datos()
    libros_autor = [libro for libro in libros if libro["autor"].lower() == autor.lower()]
    if libros_autor:
        print(f"Libros de {autor}:")
        for libro in libros_autor:
            estado = "Prestado" if libro["prestado"] else "Disponible"
            print(f"- {libro['titulo']} ({libro['año']}) | Estado: {estado}")
    else:
        print(f"No se encontraron libros de {autor}.")

def menu():
    print("--- Menú de la Biblioteca ---")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar por autor")
    print("6. Listar usuarios")
    print("7. Establecer penalización manual")
    print("8. Salir")
    return input("Seleccione una opción: ")

def main():
    inicializar_archivos()

    while True:
        opcion = menu()
        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            año = input("Ingrese el año de publicación: ")
            agregar_libro(titulo, autor, año)
        elif opcion == '2':
            listar_libros()
        elif opcion == '3':
            titulo = input("Ingrese el título del libro a prestar: ")
            nombre_usuario = input("Ingrese su nombre: ")
            tarjeta_identidad = input("Ingrese su tarjeta de identidad: ")
            prestar_libro(titulo, nombre_usuario, tarjeta_identidad)
        elif opcion == '4':
            titulo = input("Ingrese el título del libro a devolver: ")
            devolver_libro(titulo)
        elif opcion == '5':
            autor = input("Ingrese el nombre del autor: ")
            buscar_por_autor(autor)
        elif opcion == '6':
            listar_usuarios()
        elif opcion == '7':
            tarjeta_identidad = input("Ingrese la tarjeta de identidad del usuario: ")
            dias = int(input("Ingrese la cantidad de días de penalización: "))
            establecer_penalizacion(tarjeta_identidad, dias)
        elif opcion == '8':
            print("¡Gracias por usar la biblioteca!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
