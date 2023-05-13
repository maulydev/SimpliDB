# SimpliDB

The `SimpliDB` class provides a simplified interface for interacting with a SQLite database. It offers methods to perform various operations related to tables, columns, and rows.

### Table Methods

- `create_table`: Creates a new table in the database with specified columns.
- `drop_table`: Deletes a table from the database if it exists.
- `truncate_table`: Removes all the data from a table while keeping the table structure intact.
- `rename_table`: Renames a table.
- `fetch_table_column` : Retrieve table columns
- `table_query`: Retrieves the query for the table
- `table_info`: Returns the table information
- `__tables__`: Returns all tables in the database

### Column Methods

- `add_column`: Adds one or more columns to an existing table.
- `drop_column`: Drops one or more columns from an existing table.
- `rename_column`: Renames a column in an existing table.

### Row Methods

- `insert_multiple`: Inserts multiple rows of data into a table.
- `insert_row`: Inserts a single row of data into a table.
- `fetch_all`: Retrieves all rows from a table.
- `delete_row`: Deletes rows from a table based on a condition.
- `count_row`: Counts the number of rows in a table.

### Other Methods

- `execute_sql`: Executes a custom SQL query on the database.
- `close`: Closes the database connection.

The `SimpliDB` class simplifies common database operations, such as creating and manipulating tables, managing columns, inserting and retrieving rows, and executing custom SQL queries. It abstracts away the complexities of working directly with SQLite, providing a user-friendly interface for database interactions.

Feel free to explore and use the methods provided by `SimpliDB` to streamline your SQLite database operations.

# Getting Started

## Dependencies

To use the provided code, ensure that the following dependencies and prerequisites are met:

### Python

- Python: Make sure you have Python installed on your system. The code provided should work with Python 3.x versions.

No additional libraries or external dependencies are required for the code. The code utilizes the built-in `sqlite3` module, which is part of the Python Standard Library.

### Operating System

The code should work on any operating system that supports Python and the `sqlite3` module. This includes Windows, macOS, and Linux distributions.

Ensure that you have a compatible version of Python installed on your system.

## Installing SimpliDB

---

SimpliDB can be installed from the GitHub repository using pip. Follow the steps below to install SimpliDB:

1. Open a command prompt or gitbash terminal (NB: works mostly on _gitbash_).

2. Run the following command to install SimpliDB directly from the GitHub repository:

```shell
pip install git+https://github.com/maulydev/SimpliDB.git
```

<!-- [SimpliDB](https://github.com/maulydev/SimpliDB.git "Visit SimpliDB Repository") -->

3. Wait for the installation process to complete. Pip will download the SimpliDB package from the GitHub repository and install it along with any necessary dependencies.

4. Once the installation is finished, you can start using SimpliDB in your Python projects by importing the `SimpliDB` class:

```python
from simplidb import SimpliDB
```

## Create an instance of SimpliDB

```python
db = SimpliDB("my_database.db")
```

Here's how you can use the `create_table` method of the SimpliDB library:

```python
# Define the table name and columns
table_name = 'users'
columns = {
    'id': 'INTEGER',
    'name': 'TEXT',
    'age': 'INTEGER',
    'email': 'TEXT'
}

# Create the table
db.create_table(table_name, columns)
```

## Dropping a Table

To drop a table from the database, use the `drop_table` method:

```python
db.drop_table(table_name)
```

`table_name` (str): The name of the table to be dropped.

## Truncating a Table

To remove all data from a table while keeping its structure intact, use the `truncate_table` method:

```python
db.truncate_table(table_name)
```

`table_name` (str): The name of the table to be truncated.

## Renaming a Table

To change the name of a table, use the rename_table method:

```python
db.rename_table(old_table_name, new_table_name)
```

`old_table_name` (str): The current name of the table.
`new_table_name` (str): The new name for the table.

## Fetching Table Columns

To retrieve the column names of a table, use the `fetch_table_column` method:

`columns = db.fetch_table_column(table_name)`

`table_name` (str): The name of the table.

## Retrieving Table Query

To get the query of a table, use the `table_query` method:

```python
structure = db.table_query(table_name)
```

## Retrieving Table Info

To get the structure of a table, use the `table_info` method:

```python
structure = db.table_info(table_name)
```

`table_name` (str): The name of the table.

## Getting a List of Tables

To obtain a list of tables in the database, use the tables property:

```python
table_list = db.__tables__
```

The `tables` property returns a list of table names.

## Adding Columns to a Table

The add_column method allows you to add one or more columns to an existing table.

```python
db.add_column(table_name, columns)
```

`table_name` (str): The name of the table.
`columns` (dict): A dictionary specifying the columns to be added, where the keys are the column names and the values are the column types.
The `add_column` method executes the SQL statement ALTER TABLE table_name ADD COLUMN column_name column_type for each column in the provided dictionary. It adds the specified columns to the table and commits the changes to the database. Any errors encountered during the column addition process are handled gracefully.

## Dropping Columns from a Table

To drop one or more columns from an existing table, use the `drop_column` method.

```python
db.drop_column(table_name, columns)
```

`table_name` (str): The name of the table.
`columns` (list): A list of column names to be dropped.
The `drop_column` method executes the SQL statement ALTER TABLE table_name DROP COLUMN column_name for each column in the provided list. It removes the specified columns from the table and commits the changes to the database. Any errors encountered during the column dropping process are handled gracefully.

## Renaming a Column

To rename a column in an existing table, use the `rename_column` method.

```python
db.rename_column(table_name, old_name, new_name)
```

`table_name` (str): The name of the table.
`old_name` (str): The current name of the column.
`new_name` (str): The new name for the column.
The `rename_column` method executes the SQL statement ALTER TABLE table_name RENAME COLUMN old_name TO new_name. It renames the specified column in the table and commits the changes to the database. Any errors encountered during the column renaming process are handled gracefully.

## Inserting Rows

The `insert_multiple` method allows you to insert multiple rows of data into a table.

```python
db.insert_multiple(table_name, data)
```

`table_name` (str): The name of the table.
`data` (list): A list of lists, where each inner list represents a row of data to be inserted.
The `insert_multiple` method uses the `executemany` function to efficiently execute the SQL statement INSERT INTO table_name VALUES (?, ?, ...), where the number of placeholders (?) matches the number of columns in the table. It inserts multiple rows of data into the table and commits the changes to the database. Any errors encountered during the insertion process are handled gracefully.

To insert a single row of data into a table, you can use the `insert_row` method.

```python
db.insert_row(table_name, data)
```

`table_name` (str): The name of the table.
`data` (list): A list containing the values for each column in the row.
The `insert_row` method executes the SQL statement INSERT INTO table_name VALUES (?, ?, ...), where the number of placeholders (?) matches the number of values in the provided list. It inserts a single row of data into the table and commits the changes to the database. Any errors encountered during the insertion process are handled gracefully.

## Fetching Rows

To retrieve all rows from a table, you can use the `fetch_all` method.

```python
rows = db.fetch_all(table_name)
```

`table_name` (str): The name of the table.
The `fetch_all` method executes the SQL statement SELECT \* FROM table_name to fetch all rows from the table. It returns the result as a list of tuples, where each tuple represents a row of data. If any errors occur during the fetch process, an empty list is returned.

## Deleting Rows

To delete rows from a table based on a condition, use the `delete_row` method.

```python
operator = 'AND'  # Operator for multiple conditions (e.g., 'AND', 'OR')
condition = {'column1': value1, 'column2': value2, ...}  # Conditions for deletion

db.delete_row(table_name, operator, condition)
```

`table_name` (str): The name of the table.
`operator` (str): The logical operator to combine multiple conditions (e.g., 'AND', 'OR').
`condition` (dict): A dictionary specifying the column-value pairs to be matched for deletion.
The `delete_row` method constructs a SQL statement using the provided operator and conditions and executes it to delete the matching rows from the table. It commits the changes to the database. Any errors encountered during the deletion process are handled gracefully.

## Counting Rows

To count the number of rows in a table, use the `count_row` method.

```python
count = db.count_row(table_name)
```

`table_name` (str): The name of the table.
The `count_row` method executes the SQL statement `SELECT COUNT(\*) FROM table_name` to retrieve the count of rows in the table. It returns the result as a tuple containing the label "count" and the count value. If any errors occur during the count process, an empty tuple is returned.

## Executing Custom SQL Queries

The `execute_sql` method allows you to execute custom SQL queries on the database.

```python
result = db.execute_sql(sql_query)
```

`sql_query` (str): The SQL query to be executed.
The `execute_sql` method takes an SQL query as input and executes it using the cursor's `execute` method. It returns the result of the query execution. If any errors occur during the execution, an error message is printed, and None is returned.

## Closing the Database Connection

To close the database connection and release any associated resources, use the `close` method.

```python
db.close()
```

The `close` method closes the cursor used for executing queries. If any errors occur during the closing process, they are printed.

## Authors

- [Mauly dotDev](https://github.com/maulydev)

## Version History

- 1.0 (2023-05-09): Initial release

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for more details.

## Acknowledgement

We would like to acknowledge the contributions and inspiration from the open-source community. We are grateful for the valuable resources and tools provided by developers worldwide.
