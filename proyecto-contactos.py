import os
#CONSTANTES
CARPETA = 'contactos/' #Carpeta de contactos
EXTENSION = '.txt'# Extension de archivos

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #Revisa si la carpeta existe o no
    crear_directorio()

    #Muestra el menu de opciones
    mostrar_menu()

    #Preguntar al usuario la acción que desea realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n' )
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            borrar_contacto()
            preguntar = False
        else:
            print('Opción no valida, intente de nuevo')

def borrar_contacto():
    nombre = input('Escriba el  Nombre del contacto que desea eliminar: \r\n' )
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado Correctamente')
    except IOError:
        print('Ese contacto no existe')
    #Reiniciar la app
    app()
def buscar_contacto():
    nombre = input('Escriba el  Nombre del contacto que desea buscar: \r\n' )
    
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
    #Reiniciar app
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA +  archivo) as contacto:
            for linea in contacto:
                #Imprime los contactos
                print(linea.rstrip())
            #Imprime un separador entre contactos
            print('\r\n')
    app()

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del Contacto que desea editar: \r\n')
    #Revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)
    
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            #Resto de los campos
            nombre_contacto = input('Agrega el nuevo nombre contacto: \n')
            telefono_contacto = input('Agrega el Nuevo Teléfono: \n')
            categoria_contacto = input('Agrega la Nueva Categoria: \n')

            #Instanciar la clase contacto
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            #Escribir en el archivo
            archivo.write('Nombre: '+ contacto.nombre + '\n')
            archivo.write('Teléfono: '+ contacto.telefono + '\n')
            archivo.write('Categoría: '+ contacto.categoria + '\n')

            #cierro el archivo
            archivo.close()
            #Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            #Mostrar un mensaje de éxito
            print('\r\n Contacto Editado Correctamente \r\n')

    else:
        print('Ese contacto no existe')
    #Reiniciar la aplicaión
    app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del contacto: \n')

    #Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:
    

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            #Resto de los campos
            telefono_contacto = input('Agrega el Teléfono: \n')
            categoria_contacto = input('Categoría Contacto: \n')

            #Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre: '+ contacto.nombre + '\n')
            archivo.write('Teléfono: '+ contacto.telefono + '\n')
            archivo.write('Categoría: '+ contacto.categoria + '\n')

            #Mostrar un mensaje de exito
            print('\r\n Contacto creado Correctamente \r\n')

    else:
        print('Ese contacto ya existe')
    #Reiniciar la app
    app()   

def mostrar_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('1. Agregar Nuevo Contacto')
    print('2. Editar Contacto')
    print('3. Ver Contactos')
    print('4. Buscar contacto')
    print('5. Eliminar contacto')

def crear_directorio():
    if not os.path.exists('contactos/'):
        #Crear la carpeta
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre +EXTENSION)
app()