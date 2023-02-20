class Pelicula:
    def __init__(self, titulo, actores, anio, genero):
        self.titulo = titulo
        self.actores = actores
        self.anio = anio
        self.genero = genero

    def actores(self):
        return self.actores

    def titulo(self):
        return self.titulo

    def anio(self):
        return self.anio

    def genero(self):
        return self.genero

    def allinfo(self):
        print("\n|  Titulo: ", self.titulo,
              "\n|  Actores:", self.actores,
              "\n|  Año:    ", self.anio,
              "\n|  Genero: ", self.genero,)

    def movieinfo(self, index):
        print("|====================[ ", index, " ]====================|"
              "\n|"
              "\n|>> ", self.titulo,
              "\n|")
