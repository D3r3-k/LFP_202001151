import glob
from movie import *


lista_peliculas = []

# LECTURA DE ARCHIVO


def cargarArchivo(ruta, arreglo):
    archivo = open(ruta, 'r')
    lineas = archivo.readlines()
    total = 0
    for linea in lineas:
        titulo, actores, anio, genero = linea.split(';')
        tmp_titulo = titulo.strip()
        tmp_actores = actores.split(',')
        tmp_anio = anio.strip()
        tmp_genero = genero.strip()
        pelicula = Pelicula(tmp_titulo, tmp_actores, tmp_anio, tmp_genero)
        repetido = False
        for peli in arreglo:
            if peli.titulo == tmp_titulo:
                peli.actores = tmp_actores
                peli.anio = tmp_anio
                peli.genero = tmp_genero
                repetido = True
                continue
        if not repetido:
            arreglo.append(pelicula)
        total += 1
    print(len(arreglo))
    return total

# MENU PRINCIPAL


def menu_principal():
    limpiar()
    try:
        print("\n==========[ Menu Principal ]=========="
              "\n  1. Cargar Archivo de entrada"
              "\n  2. Gestionar Películas"
              "\n  3. Filtrado"
              "\n  4. Gráfica"
              "\n  5. Salir"
              "\n======================================")
        opcion = int(input("Selecciona una opcion...\n|>>| "))
        return opcion
    except ValueError:
        return None


def limpiar():
    print("\033c", end="")

# OPCION 1


def menu_cargarArchivo():
    limpiar()
    try:
        print("\n==============[ Cargar Archivos ]=============="
              "\n  1. Escribir la ruta del directorio"
              "\n  2. Seleccionar Archivos guardados"
              "\n  3. Retroceder"
              "\n|===============================================|"
              "\n|  Nota: Puedes guardar el archivo .lfp en      |"
              "\n|  la carpeta ./archivos/ para luego cargarlo...|"
              "\n|===============================================|\n")
        opcion = int(input("Selecciona una opcion...\n|>>| "))
        return opcion
    except ValueError:
        return None


def cargaPorRuta():
    limpiar()
    try:
        print("\n==============[ Cargar Archivos ]=============="
              "\nEscriba E para regresar al menu anterior."
              "\n==============================================\n")
        ruta = input("Escriba la ruta del archivo a leer: \n|>>| ")
        if ruta.lower() == 'e':
            return 1
        open(ruta, 'r')
        total = cargarArchivo(ruta, lista_peliculas)
        print("\n     Peliculas cargadas: ", total)
        input("\n     [✓] El archivo se ha cargado correctamente!"
              "\n     Presiona una tecla para continuar...")
        return 3
    except Exception:
        print("     [X] No se puede acceder a ese archivo!")
        input("     Presiona una tecla para continuar...\n ")
        return 1


def cargaPorListado():
    limpiar()
    ruta = "./archivos/*.lfp"
    archivos = glob.glob(ruta)
    index = 1
    print("============[ Lista de Archivos ]===========")
    for i in archivos:
        print("|>>|", str(index) + ". " +
              i.replace(ruta.replace("/*.lfp", ""), "").replace("\\", ""))
        index += 1
    print("============================================"
          "\nEscriba E para regresar al menu anterior.")
    try:
        opcion_archivo = input("\nSeleccione una opcion: \n|>>| ")
        if opcion_archivo.lower() == 'e':
            return 1
        opcion_archivo = int(opcion_archivo)
        if opcion_archivo <= 0 or opcion_archivo > len(archivos):
            print("\n     [X] La opcion no existe!")
            input("     Presiona una tecla para regresar...\n ")
            return 2
        else:
            opcion_archivo = opcion_archivo - 1
            total = cargarArchivo(archivos[opcion_archivo], lista_peliculas)
            print("\n     Peliculas cargadas: ", total)
            input("\n     [✓] El archivo se ha cargado correctamente!"
                  "\n     Presiona una tecla para continuar...")
            return 3
    except ValueError:
        limpiar()
        input("\n     [X] Opcion invalida!"
              "\n     Presiona una tecla para continuar...")
        return 1


# OPCION 2
def menu_gestionarPeliculas():
    limpiar()
    try:
        print("\n===========[ Gestionar Peliculas ]===========",
              "\n  1. Mostrar Películas",
              "\n  2. Mostrar Actores",
              "\n  3. Retroceder",
              "\n=============================================\n")
        opcion = int(input("Selecciona una opcion...\n|>>| "))
        return opcion
    except ValueError:
        return None


def mostrar_peliculas():
    if len(lista_peliculas) == 0:
        print("     [X] No hay peliculas cargadas.")
        input("     Presiona una tecla para continuar...\n")
    else:
        limpiar()
        for pelicula in lista_peliculas:
            print("|==================================================|")
            pelicula.allinfo()
        print("\n|==================================================|")
        print("\nPeliculas cargadas: ", len(lista_peliculas))
        input("Presiona una tecla para continuar...\n")


def mostrar_actores():
    if len(lista_peliculas) == 0:
        print("     [X] No hay peliculas cargadas.")
        input("     Presiona una tecla para continuar...\n")
    else:
        limpiar()
        index = 1
        for i in lista_peliculas:
            i.movieinfo(index)
            index += 1
        try:
            print("\nEscriba E para regresar al menu anterior.")
            opcion = input("\nSeleccione una opcion: \n|>>| ")
            if opcion.lower() == 'e':
                return 1
            opcion = int(opcion)
            if opcion > 0 and opcion <= len(lista_peliculas):
                opcion -= 1
                for pelicula in lista_peliculas:
                    if pelicula == lista_peliculas[opcion]:
                        limpiar()
                        arrActores = lista_peliculas[opcion].actores
                        print("|=============[", pelicula.titulo, "]=============|"
                              "\n|>> Actores:")
                        for actor in arrActores:
                            print("|    ✓ ", actor)
                        input("\n\nPresiona una tecla para continuar...\n")
                        break
            else:
                input("\n     [X] No existe esa opcion!"
                      "\n     Presiona una tecla para continuar...")
        except ValueError:
            limpiar()
            input("\n     [X] Opcion invalida!"
                  "\n     Presiona una tecla para continuar...")

# OPCION 3


def menu_filtrado():
    limpiar()
    try:
        print("\n===============[ Filtrar por: ]==============",
              "\n  1. Actor",
              "\n  2. Año",
              "\n  3. Género",
              "\n  4. Retroceder",
              "\n=============================================\n")
        opcion = int(input("Selecciona una opcion...\n|>>| "))
        return opcion
    except:
        return None


def filtro_actores():
    limpiar()
    try:
        lista_actores = []
        for pelicula in lista_peliculas:
            for actor in pelicula.actores:
                if actor not in lista_actores:
                    lista_actores.append(actor)
        print("==============[ Lista de Actores ]==============")
        index = 1
        for actor in lista_actores:
            if len(str(index)) == 1:
                print("|✓|  ", index, ".  ", actor)
            if len(str(index)) == 2:
                print("|✓| ", index, ".  ", actor)
            index += 1
        print("\nEscriba E para regresar al menu anterior.")
        opcion = input("\nSeleccione una opcion: \n|>>| ")
        if opcion.lower() == 'e':
            return 1
        opcion = int(opcion) - 1
        if opcion >= 0 and opcion <= len(lista_actores):
            limpiar()
            peliculas_filtradas = []
            for pelicula in lista_peliculas:
                for actor in pelicula.actores:
                    if lista_actores[opcion] == actor:
                        peliculas_filtradas.append(pelicula.titulo)
            if len(peliculas_filtradas) > 0:
                print("==============[ Peliculas donde participa: ",
                      lista_actores[opcion], "]==============")
                for titulo in peliculas_filtradas:
                    print('|✓| ', titulo)
            else:
                print("     [X] No se encontro ningun actor llamado ",
                      lista_actores[opcion])
            input("\n\nPresiona una tecla para continuar...\n")

        else:
            input("\n     [X] No existe esa opcion!"
                  "\n     Presiona una tecla para continuar...")
    except ValueError:
        limpiar()
        input("\n     [X] Opcion invalida!"
              "\n     Presiona una tecla para continuar...")


def filtro_anios():
    limpiar()
    try:
        lista_anios = []
        for pelicula in lista_peliculas:
            if pelicula.anio not in lista_anios:
                lista_anios.append(pelicula.anio)
        print("==============[ Lista de Años ]==============")
        index = 1
        for anio in lista_anios:
            if len(str(index)) == 1:
                print("|✓|  ", index, ".  ", anio)
            if len(str(index)) == 2:
                print("|✓| ", index, ".  ", anio)
            index += 1
        print("\nEscriba E para regresar al menu anterior.")
        opcion = input("\nSeleccione una opcion: \n|>>| ")
        if opcion.lower() == 'e':
            return 1
        opcion = int(opcion) - 1
        if opcion >= 0 and opcion < len(lista_anios):
            limpiar()
            peliculas_filtradas = []
            for pelicula in lista_peliculas:
                if lista_anios[opcion] == pelicula.anio:
                    peliculas_filtradas.append(pelicula.titulo)
            if len(peliculas_filtradas) > 0:
                print("==============[ Peliculas del año: ",
                      lista_anios[opcion], "]==============")
                for titulo in peliculas_filtradas:
                    print('|✓| ', titulo)
            else:
                print("     [X] No se encontro ninguna pelicula del año: ",
                      lista_anios[opcion])
            input("\n\nPresiona una tecla para continuar...\n")

        else:
            input("\n     [X] No existe esa opcion!"
                  "\n     Presiona una tecla para continuar...")
    except ValueError:
        limpiar()
        input("\n     [X] Opcion invalida!"
              "\n     Presiona una tecla para continuar...")


def filtro_generos():
    limpiar()
    try:
        lista_generos = []
        for pelicula in lista_peliculas:
            if pelicula.genero not in lista_generos:
                lista_generos.append(pelicula.genero)
        print("==============[ Lista de Generos ]==============")
        index = 1
        for genero in lista_generos:
            if len(str(index)) == 1:
                print("|✓|  ", index, ".  ", genero)
            if len(str(index)) == 2:
                print("|✓| ", index, ".  ", genero)
            index += 1
        print("\nEscriba E para regresar al menu anterior.")
        opcion = input("\nSeleccione una opcion: \n|>>| ")
        if opcion.lower() == 'e':
            return 1
        opcion = int(opcion) - 1
        if opcion >= 0 and opcion < len(lista_generos):
            limpiar()
            peliculas_filtradas = []
            for pelicula in lista_peliculas:
                if lista_generos[opcion] == pelicula.genero:
                    peliculas_filtradas.append(pelicula.titulo)
            if len(peliculas_filtradas) > 0:
                print("==============[ Peliculas de: ",
                      lista_generos[opcion], "]==============")
                for titulo in peliculas_filtradas:
                    print('|✓| ', titulo)
            else:
                print("     [X] No se encontro ninguna pelicula del año: ",
                      lista_generos[opcion])
            input("\n\nPresiona una tecla para continuar...\n")

        else:
            input("\n     [X] No existe esa opcion!"
                  "\n     Presiona una tecla para continuar...")
    except ValueError:
        limpiar()
        input("\n     [X] Opcion invalida!"
              "\n     Presiona una tecla para continuar...")

# OPCION 5


def salir():
    print("\n\n|=====================[ ADIOS ]=====================|"
          "\n|         Gracias por utilizar esta app             |"
          "\n|                 Regresa pronto                    |"
          "\n|===================================================|")
