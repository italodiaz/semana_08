

class Model:
    """Generic model class."""
    conn = None
    table_name = None

    def insert(self):
        table_name = self.table_name
        conn = self.conn
        keys = ", ".join(self.__dict__.keys())
        values_placeholders = ", ".join(["%s"]*len(self.__dict__.keys()))
        values = self.__dict__.values()

        query = f"""
            INSERT INTO {table_name} ({keys}) VALUES ({values_placeholders});
        """
        conn.execute_query(query, tuple(values))

    def update(self):
        table_name = self.table_name
        conn = self.conn
        query = f"""
            UPDATE {table_name}
            SET COLUMNS = VALUES
            WHERE table.id = id_val;
        """
        conn.execute_query(query)

    def delete(self):
        table_name = self.table_name
        conn = self.conn
        query = f"""
            DELETE FROM {table_name}
            WHERE table.id = id_val;
        """
        conn.execute_query(query)

    def get_all(self):
        table_name = self.table_name
        conn = self.conn
        query = f"""
            SELECT * FROM {table_name}
        """
        conn.execute_query(query)

    def find_by(self):
        table_name = self.table_name
        conn = self.conn
        query = f"""
            SELECT * FROM {table_name}
            where column = value
        """
        conn.execute_query(query)

    def find_by_like(self):
        table_name = self.table_name
        conn = self.conn
        query = f"""
            SELECT * FROM {table_name}
            where column like '%value%'
        """
        conn.execute_query(query)
