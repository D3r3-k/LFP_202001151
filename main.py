from functions import *
from graph import *

limpiar()
print("|===================================================|",
      "\n|                    BIENVENIDOS                    |",
      "\n|===================================================|",
      "\n|    Lenguajes Formales y de Programación           |",
      "\n|                Seccion: B-                        |",
      "\n|    202001151 - Derek Francisco Orellana Ibáñez    |",
      "\n|===================================================|",
      "\n\n")
input("Presiona una tecla para continuar...\n ")

# MENU PRINCIPAL
opcion = 0
while opcion != 5:
    opcion = menu_principal()
    if opcion == 1:
        op_submenu = 0
        while op_submenu != 3:
            op_submenu = menu_cargarArchivo()
            if op_submenu == 1:
                op_submenu = cargaPorRuta()
            elif op_submenu == 2:
                op_submenu = cargaPorListado()
            elif op_submenu == 3:
                pass
            elif type(op_submenu) is type(None):
                limpiar()
                input("\n     [X] Opcion invalida!"
                      "\n     Presiona una tecla para continuar...")
            else:
                input("\n     [X] No existe esa opcion!"
                      "\n     Presiona una tecla para continuar...")
    elif opcion == 2:
        op_submenu = 0
        while op_submenu != 3:
            op_submenu = menu_gestionarPeliculas()
            if op_submenu == 1:
                mostrar_peliculas()
            elif op_submenu == 2:
                mostrar_actores()
            elif op_submenu == 3:
                pass
            elif type(op_submenu) is type(None):
                limpiar()
                input("\n     [X] Opcion invalida!"
                      "\n     Presiona una tecla para continuar...")
            else:
                input("\n     [X] No existe esa opcion!"
                      "\n     Presiona una tecla para continuar...")
    elif opcion == 3:
        op_submenu = 0
        while op_submenu != 4:
            op_submenu = menu_filtrado()
            if op_submenu == 1:
                filtro_actores()
            elif op_submenu == 2:
                filtro_anios()
            elif op_submenu == 3:
                filtro_genero()
            elif op_submenu == 4:
                pass
            elif type(op_submenu) is type(None):
                limpiar()
                input("\n     [X] Opcion invalida!"
                      "\n     Presiona una tecla para continuar...")
            else:
                input("\n     [X] No existe esa opcion!"
                      "\n     Presiona una tecla para continuar...")
    elif opcion == 4:
        graficar(lista_peliculas)
    elif opcion == 5:
        salir()
    elif type(opcion) is type(None):
        limpiar()
        input("\n     [X] Opcion invalida!"
              "\n     Presiona una tecla para continuar...")
    else:
        input("\n     [X] No existe esa opcion!"
              "\n     Presiona una tecla para continuar...")
