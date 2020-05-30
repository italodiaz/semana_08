from models.model import Model


class Editorial(Model):

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"\nEditorial : {self.nombre}\n"
