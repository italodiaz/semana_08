import os
from psycopg2 import connect, Error
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Conexion:
    def __init__(self):
        try:
            self.db = connect(
                host=os.getenv('DB_HOST'),
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                port=os.getenv('DB_PORT')
            )
            self.cursor = self.db.cursor()
        except Error as e:
            print(e)

    def execute_query(
        self, sentencia_sql, parametros=None, escribir_en_bd=True
    ):
        try:
            self.cursor.execute(sentencia_sql, parametros)
            if escribir_en_bd:
                self.db.commit()
            return self.cursor
        except Exception as e:
            print(str(e))
            print(f'Ocurrio un error en la sentencia\n{sentencia_sql}')
            if escribir_en_bd:
                self.db.rollback()
        return None
