import os


def graficar(lista_peliculas):
    try:
        archivo = "render/nodos.dot"
        if os.path.exists(archivo):
            archivoDOT = open(archivo, "w")
            archivoDOT.write("digraph{\n")
            archivoDOT.write("rankdir = LR;\n")
            archivoDOT.write(
                'node [fontname = "Arial Black"; fontsize = 14; margin = "0.2,0.1";];\n')
            archivoDOT.write('edge [color = "#008cff";];\n')

            archivoDOT.write("}")
        print("     [✓] Renderizacion completa!")
        input("     Presiona una tecla para continuar...")
    except:
        input("\n     [X] Hubo un error al graficar!"
              "\n     Presiona una tecla para continuar...")
