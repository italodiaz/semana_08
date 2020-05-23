from psycopg2 import connect, Error


class Conexion:
    def __init__(self, **parametros):
        try:
            self.db = connect(
                host=parametros['host'],
                user=parametros['user'],
                password=parametros['password'],
                database=parametros['database']
            )
            self.cursor = self.db.cursor()
        except Error as e:
            print(e)
    
    def __del__(self):
        self.db.close()

'''
    def _ejecutar_sql(
        self, sentencia_sql, parametros=None, 
        escribir_en_bd=True
    ):
        try:
            self.cursor.execute(sentencia_sql, parametros) # execute corre las sentencias sql
            if escribir_en_bd:
                self.db.commit()
        except Exception as e:
            print(str(e), f"\nOcurrio un error al ejecutar la sentencia SQL:\n\n{sentencia_sql}\n")
            if escribir_en_bd:
                self.db.rollback()

    def _leer_desde_sql(self):
        registros = []
        try:
            registros = self.cursor.fetchall()
        except Exception as e:
            print(str(e), f'\nUn error ocurrió al momento de leer desde la BD')
        return registros

    def leer_datos(self):
        # Ejecutar SELECTs
        self._ejecutar_sql(
            "SELECT * FROM " + self.tabla + " ",
            escribir_en_bd=False
        )
        return self._leer_desde_sql()  

    def obtener_registro(self, registro_id):
        self._ejecutar_sql(
            "SELECT * FROM " + self.tabla + " WHERE id=%s",
            (registro_id,),
            escribir_en_bd=False
        )
        return self._leer_desde_sql()
    
    def eliminar_registro(self, registro_id):
        self._ejecutar_sql(
            "DELETE FROM " + self.tabla + " WHERE id=%s",
            (registro_id,)
        )

    def cambiar_tabla(self, tabla):
        self.tabla = tabla
'''