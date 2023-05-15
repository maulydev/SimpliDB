from simplidb import SimpliDB

db = SimpliDB()
db.connect("database.db")

db.create_table("user", {"username": "TEXT", "password": "TEXT"})

# db.insert_row("user", ["johndoe", "256454"])
# db.insert_multiple("user", [("desmond", "123456"), ("elorm", "7897879")])

# x = db.fetch_all("user")
# print(x)

# print(db.select_distinct("user", "username"))

# result = db.fetch(
#     table_name="user",
#     order_by=("username", "password DESC"),
#     limit=3,
# )

# print(result)


# simplidb = SimpliDB("expose.db")
# simplidb.connect("expose.db")
# simplidb.insert_row("movie", ("Monty Python and the Holy Grail", 1975, 8.2))
# data = [
#     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
# simplidb.__extend__.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
# simplidb.__extend__.commit()

# res = simplidb.__extend__.execute("SELECT * FROM movie")
# for x in res:
#     print(x)

# res = simplidb.fetch(table_name="movie", columns=("min(score)",), where="score > 7")
# print(res)
