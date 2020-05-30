from models.editorial import Editorial
from connection.conn import Conexion

conn = Conexion()


class Editorial_controller:

    @classmethod
    def add(cls, **kwargs):
        editorial = Editorial(**kwargs)
        editorial.insert()
        return editorial

    @classmethod
    def update(cls, **kwargs):
        editorial = Editorial(**kwargs)
        editorial.insert()
        return editorial
