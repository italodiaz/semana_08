from models.editorial import Editorial
from connection.conn import Conexion

conn = Conexion()


class Editorial_contr:

    @classmethod
    def insertar_editorial(cls, **kwargs):
        editorial = Editorial(**kwargs)
        query = "INSERT INTO editorial(nombre) values (%s)"
        values = (editorial.nombre,)
        conn.execute_query(query, values)
