import sqlite3


"""
********** SIMPLIDB METHODS **********
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
=>  UPDATE ROW (table_name, row_id, data)
=>  SELECT ROW (table_name, condition=None)

=>  CLOSE DB
"""


class SimpliDB:
    def __init__(self, db_name):
        self.db_name = db_name
        try:
            self.db = sqlite3.connect(db_name)
            self.cursor = self.db.cursor()
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)

    #############################################   TABLE METHODS   ###########################################

    def create_table(self, table_name: str, columns: dict):
        columns_str = ", ".join(
            "{} {}".format(column, data_type) for column, data_type in columns.items()
        )
        try:
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, columns_str)
            )
            self.db.commit()
        except sqlite3.Error as e:
            print("Error creating table:", e)

    def drop_table(self, table_name: str):
        try:
            self.cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
            self.db.commit()
        except sqlite3.Error as e:
            print("Error dropping table:", e)

    def truncate_table(self, table_name: str):
        try:
            self.cursor.execute("DELETE FROM {}".format(table_name))
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def rename_table(self, old_table_name: str, new_table_name: str):
        try:
            self.cursor.execute(
                "ALTER TABLE {} RENAME TO {}".format(old_table_name, new_table_name)
            )
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def fetch_table_column(self, table_name: str):
        try:
            return [
                column[1]
                for column in self.cursor.execute(
                    "PRAGMA table_info({})".format(table_name)
                )
            ]
        except sqlite3.Error as e:
            print(e)

    def table_structure(self, table_name: str):
        try:
            return self.cursor.execute(
                "SELECT sql FROM sqlite_schema WHERE name = '{}'".format(table_name)
            ).fetchone()[0]
        except sqlite3.Error as e:
            print(e)

    @property
    def tables(self):
        try:
            return self.cursor.execute(
                "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%'"
            ).fetchall()
        except sqlite3.Error as e:
            print(e)

    #############################################   TABLE METHODS   ###########################################
    #
    #
    #############################################   COLUMN METHODS  ###########################################

    def add_column(self, table_name: str, columns: dict):
        try:
            for column_name, column_type in columns.items():
                self.cursor.execute(
                    "ALTER TABLE {} ADD COLUMN {} {}".format(
                        table_name, column_name, column_type
                    )
                )
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def drop_column(self, table_name: str, columns: list):
        try:
            for column in columns:
                self.cursor.execute(
                    "ALTER TABLE {} DROP COLUMN {}".format(table_name, column)
                )

            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def rename_column(self, table_name: str, old_name: str, new_name: str):
        try:
            self.cursor.execute(
                "ALTER TABLE {} RENAME COLUMN {} TO {}".format(
                    table_name, old_name, new_name
                )
            )
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    #############################################   COLUMN METHODS  ###########################################
    #
    #
    #############################################   ROW METHODS  ###########################################

    def insert_multiple(self, table_name: str, data: list):
        try:
            num_of_columns = len(data[0])
            value_template = ",".join(["?"] * num_of_columns)
            self.cursor.executemany(
                "INSERT INTO {} VALUES ({})".format(table_name, value_template), data
            )
            self.db.commit()
        except sqlite3.Error as e:
            print("Error inserting multiple rows:", e)

    def insert_row(self, table_name: str, data: list):
        try:
            num_of_columns = len(data)
            values_template = ",".join(["?"] * num_of_columns)
            self.cursor.execute(
                "INSERT INTO {} VALUES ({})".format(table_name, values_template), data
            )
            self.db.commit()
        except sqlite3.Error as e:
            print("Error inserting row:", e)

    def fetch_all(self, table_name: str):
        try:
            return self.cursor.execute("SELECT * FROM {}".format(table_name)).fetchall()
        except sqlite3.Error as e:
            print("Error fetching rows:", e)
            return []

    def delete_row(self, table_name: str, operator: str, condition: dict):
        try:
            condition = " {} ".format(operator).join(
                "{}={}".format(key, value) for key, value in condition.items()
            )
            self.cursor.execute("DELETE FROM {} WHERE {}".format(table_name, condition))
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def count_row(self, table_name: str):
        try:
            return (
                "count",
                self.cursor.execute(
                    "SELECT COUNT(*) FROM {}".format(table_name)
                ).fetchone()[0],
            )
        except sqlite3.Error as e:
            print(e)

    #############################################   ROW METHODS  ###########################################

    def execute_sql(self, sql_query: str):
        try:
            return self.cursor.execute(sql_query)
        except sqlite3.Error as e:
            print("Error executing SQL query:", e)
            return None

    def close(self):
        try:
            self.cursor.close()
        except sqlite3.Error as e:
            print(e)
