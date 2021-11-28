class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:
    peliculas = [] # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, peliculas=[]):
        Catalogo.peliculas = peliculas

    def agregar(self, p): # p será un objeto Pelicula
        Catalogo.peliculas.append(p)

    def mostrar(self):
        for p in Catalogo.peliculas:
            print(p) # Print toma por defecto str(p)


# Objetos dentro de objetos
# Nos permite no repetir, uso los self de pelicula dentro de catalogo,
# no los repito en catalogo

p = Pelicula("El Padrino", 175, 1972)
c= Catalogo([p])
c.mostrar()
c.agregar(Pelicula("El Padrino parte 2", 202, 1974))
c.mostrar()