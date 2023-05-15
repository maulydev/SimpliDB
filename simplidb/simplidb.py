import sqlite3


"""
********** SIMPLIDB METHODS **********
=>  ✅  CONNECT OR CREATE DB
=>  ✅  CREATE TABLE (table_name, columns)
=>  ✅  DROP TABLE (table_name)         
=>  ✅  TRUNCATE TABLE (table_name)
=>  ✅  RENAME TABLE (old_table_name, new_table_name)
=>  ✅  GET TABLE COLUMNS
=>  ✅  SHOW TABLES
=>  ✅  ALTER TABLE (table_name, new_columns)
=>  ✅  GET TABLE INFO (table_name)
=>  JOIN TABLES

=>  ✅  INSERT ROW (table_name, data)
=>  ✅  INSERT MULTIPLE ROW (table_name, data)
=>  ✅  FETCH ALL ROWS (table_name)
=>  ✅  EXECUTE SQL (sql_query)
=>  ✅  DROP COLUMN (table_name, column_name)
=>  ✅  DROP ROW (table_name, id)
=>  ✅  COUNT ROWS (table_name)
=>  ✅  CLOSE DB
=>  UPDATE ROW (table_name, row_id, data)
=>  SELECT ROW (table_name, condition=None)
=>  SELECT DISTINCT ROW(table_name)

def method_name(self):
    try:
        pass
    except sqlite3.Error as e:
        print(e)

"""


class SimpliDB:
    # UPDATE ===> 12-05-2023
    def __init__(self, db_name=None):
        if db_name is not None:
            self.connect(db_name)

    """
    TABLE METHODS
    """

    @classmethod
    def __extend__(self):
        return self.db

    # NEW ===> 12-05-2023
    def connect(self, db_name: str):
        self.db_name = db_name
        try:
            self.db = sqlite3.connect(db_name)
            self.cursor = self.db.cursor()
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)

    def create_table(self, table_name: str, columns: dict, key: str = None):
        columns_str = ", ".join(
            "{} {}".format(column, data_type) for column, data_type in columns.items()
        )
        if key:
            columns_str += ", PRIMARY KEY ({})".format(key)
        try:
            query = "CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, columns_str)
            print(query)
            self.cursor.execute(query)
            self.db.commit()

        except sqlite3.Error as e:
            print("Error creating table:", e)

    def drop_table(self, table_name: str):
        try:
            query = "DROP TABLE IF EXISTS {}".format(table_name)
            self.cursor.execute(query)
            self.db.commit()
        except sqlite3.Error as e:
            print("Error dropping table:", e)

    def truncate_table(self, table_name: str):
        try:
            query = "DELETE FROM {}".format(table_name)
            self.cursor.execute(query)
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def rename_table(self, old_table_name: str, new_table_name: str):
        try:
            query = "ALTER TABLE {} RENAME TO {}".format(old_table_name, new_table_name)
            self.cursor.execute(query)
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def fetch_table_column(self, table_name: str):
        try:
            query = "PRAGMA table_info({})".format(table_name)
            return [column[1] for column in self.cursor.execute(query)]
        except sqlite3.Error as e:
            print(e)

    def table_query(self, table_name: str):
        try:
            query = "SELECT sql FROM sqlite_schema WHERE name = '{}'".format(table_name)
            return self.cursor.execute(query).fetchone()[0]
        except sqlite3.Error as e:
            print(e)

    def table_info(self, table_name: str):
        query = "PRAGMA table_info({})".format(table_name)
        return self.cursor.execute(query).fetchone()

    @property
    def __tables__(self):
        try:
            query = "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%'"
            return self.cursor.execute(query).fetchall()
        except sqlite3.Error as e:
            print(e)

    """
    COLUMN METHODS
    """

    def add_column(self, table_name: str, columns: dict):
        try:
            for column_name, column_type in columns.items():
                query = "ALTER TABLE {} ADD COLUMN {} {}".format(
                    table_name, column_name, column_type
                )
                self.cursor.execute(query)
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def drop_column(self, table_name: str, columns: list):
        try:
            for column in columns:
                query = "ALTER TABLE {} DROP COLUMN {}".format(table_name, column)
                self.cursor.execute(query)
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def rename_column(self, table_name: str, old_name: str, new_name: str):
        try:
            query = "ALTER TABLE {} RENAME COLUMN {} TO {}".format(
                table_name, old_name, new_name
            )
            self.cursor.execute(query)
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    """
    ROW METHODS
    """

    def insert_multiple(self, table_name: str, data: list):
        try:
            num_of_columns = len(data[0])
            value_template = ",".join(["?"] * num_of_columns)
            query = "INSERT INTO {} VALUES ({})".format(table_name, value_template)
            self.cursor.executemany(query, data)
            self.db.commit()
        except sqlite3.Error as e:
            print("Error inserting multiple rows:", e)

    def insert_row(self, table_name: str, data: tuple):
        try:
            num_of_columns = len(data)
            values_template = ",".join(["?"] * num_of_columns)
            query = "INSERT INTO {} VALUES ({})".format(table_name, values_template)
            self.cursor.execute(query, data)
            self.db.commit()
        except sqlite3.Error as e:
            print("Error inserting row:", e)

    def fetch_all(self, table_name: str):
        try:
            query = "SELECT * FROM {}".format(table_name)
            return self.cursor.execute(query).fetchall()
        except sqlite3.Error as e:
            print("Error fetching rows:", e)
            return []

    def delete_row(self, table_name: str, operator: str, condition: dict):
        try:
            condition = " {} ".format(operator).join(
                "{}={}".format(key, value) for key, value in condition.items()
            )
            query = "DELETE FROM {} WHERE {}".format(table_name, condition)
            self.cursor.execute(query)
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def count_row(self, table_name: str):
        try:
            query = "SELECT COUNT(*) FROM {}".format(table_name)
            return (
                "count",
                self.cursor.execute(query).fetchone()[0],
            )
        except sqlite3.Error as e:
            print(e)

    #
    def fetch_distinct(self, table_name: str, column_name: str):
        try:
            query = "SELECT DISTINCT({}) FROM {}".format(column_name, table_name)
            print(query)
            return self.cursor.execute(query).fetchall()
        except sqlite3.Error as e:
            print(e)

    def fetch(
        self,
        table_name: str,
        columns: tuple = ("*",),
        where: str = None,
        order_by: tuple = None,
        limit: int = None,
    ):
        try:
            columns_str = ", ".join(columns)
            query = "SELECT {} FROM {}".format(columns_str, table_name)

            if where:
                query += " WHERE {}".format(where)

            if order_by:
                order_by_str = ", ".join(order_by)
                query += " ORDER BY {}".format(order_by_str)

            if limit:
                query += " LIMIT {}".format(limit)

            return self.cursor.execute(query).fetchall()
        except sqlite3.Error as e:
            print(e)

    """
    OTHER METHODS
    """

    # UPDATE 13-05-2023

    def execute_sql(self, sql_query: str, params: tuple = ()):
        """
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        params = ("john_doe", "password123")
        result = execute_sql(query, params)
        """
        try:
            self.cursor.execute(sql_query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print("Error executing SQL query:", e)
            return None

    def close(self):
        try:
            self.cursor.close()
        except sqlite3.Error as e:
            print(e)
