Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from github import Github

class Tarea:
    def __init__(self, titulo, descripcion, fecha, costo, completada=False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha
        self.costo = costo
        self.completada = completada

class SistemaGestionTareas:
    def __init__(self, repo_nombre1, repo_nombre2, token):
        self.repo_nombre1 = repo_nombre1
        self.repo_nombre2 = repo_nombre2
        self.token = token
        self.repo1 = None
        self.repo2 = None
        self.tareas = []

    def autenticar_github(self):
        g = Github(self.token)
        self.repo1 = g.get_repo(self.repo_nombre1)
        self.repo2 = g.get_repo(self.repo_nombre2)

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def ver_tareas(self, completadas=False):
        for tarea in self.tareas:
            if tarea.completada == completadas:
                print(f"Título: {tarea.titulo}")
                print(f"Descripción: {tarea.descripcion}")
                print(f"Fecha: {tarea.fecha}")
                print(f"Costo: {tarea.costo}")
                print("Estado: Completada" if tarea.completada else "Estado: Pendiente")
                print("")

    def marcar_como_completada(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.completada = True

    def editar_tarea(self, titulo, nueva_descripcion, nueva_fecha, nuevo_costo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.descripcion = nueva_descripcion
                tarea.fecha = nueva_fecha
                tarea.costo = nuevo_costo

    def borrar_tarea(self, titulo):
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo != titulo]

    def cargar_tareas(self):
        contenido1 = self.repo1.get_contents("tareas1.json")
        data1 = json.loads(contenido1.decoded_content.decode())
        contenido2 = self.repo2.get_contents("tareas2.json")
        data2 = json.loads(contenido2.decoded_content.decode())
        self.tareas = [Tarea(t['titulo'], t['descripcion'], t['fecha'], t['costo'], t['completada']) for t in data1]
        self.tareas.extend([Tarea(t['titulo'], t['descripcion'], t['fecha'], t['costo'], t['completada']) for t in data2])

    def guardar_tareas(self):
        contenido = json.dumps([t.__dict__ for t in self.tareas])
        self.repo1.update_file("tareas1.json", "Guardando tareas", contenido, self.repo1.get_contents("tareas1.json").sha)
        self.repo2.update_file("tareas2.json", "Guardando tareas", contenido, self.repo2.get_contents("tareas2.json").sha)


# Ejemplo de uso:
# Reemplaza 'NOMBRE_USUARIO/NOMBRE_REPOSITORIO' por tu nombre de usuario y nombre del repositorio en GitHub
repo_nombre1 = "J0NA18/Proyecto-final-progra"
repo_nombre2 = "J0NA18/Proyecto-final-progra"
# Coloca aquí tu token de acceso personal de GitHub
token = "TU_TOKEN_DE_ACCESO_PERSONAL"

sistema = SistemaGestionTareas(repo_nombre1, repo_nombre2, token)
sistema.autenticar_github()
sistema.cargar_tareas()

while True:
    print("1. Agregar tarea")
    print("2. Ver tareas pendientes")
    print("3. Ver tareas completadas")
...     print("4. Marcar tarea como completada")
...     print("5. Editar tarea")
...     print("6. Borrar tarea")
...     print("7. Guardar y salir")
... 
...     opcion = input("Selecciona una opción: ")
... 
...     if opcion == '1':
...         titulo = input("Introduce el título de la tarea: ")
...         descripcion = input("Introduce la descripción de la tarea: ")
...         fecha = input("Introduce la fecha de la tarea: ")
...         costo = input("Introduce el costo de la tarea: ")
...         nueva_tarea = Tarea(titulo, descripcion, fecha, costo)
...         sistema.agregar_tarea(nueva_tarea)
...     elif opcion == '2':
...         print("Tareas pendientes:")
...         sistema.ver_tareas(completadas=False)
...     elif opcion == '3':
...         print("Tareas completadas:")
...         sistema.ver_tareas(completadas=True)
...     elif opcion == '4':
...         titulo = input("Introduce el título de la tarea a marcar como completada: ")
...         sistema.marcar_como_completada(titulo)
...     elif opcion == '5':
...         titulo = input("Introduce el título de la tarea a editar: ")
...         nueva_descripcion = input("Introduce la nueva descripción de la tarea: ")
...         nueva_fecha = input("Introduce la nueva fecha de la tarea: ")
...         nuevo_costo = input("Introduce el nuevo costo de la tarea: ")
...         sistema.editar_tarea(titulo, nueva_descripcion, nueva_fecha, nuevo_costo)
...     elif opcion == '6':
...         titulo = input("Introduce el título de la tarea a borrar: ")
...         sistema.borrar_tarea(titulo)
...     elif opcion == '7':
...         sistema.guardar_tareas()
...         break
...     else:
