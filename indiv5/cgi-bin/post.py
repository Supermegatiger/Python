import cgi
import os
import sqlite3



DB_NAME = "space.db"

con = sqlite3.connect(DB_NAME)


tables = map(lambda i: i[0], con.cursor().execute("SELECT name FROM sqlite_master WHERE type='table' AND NOT name='sqlite_sequence';").fetchall())

form = cgi.FieldStorage()

with open("head.txt","r") as f:
    print(f.read())

table = os.getenv("QUERY_STRING")

if table in tables:
    columns = con.cursor().execute(f"PRAGMA table_info({table});").fetchall()
    cols = list(map(lambda i: i[1], columns[1:]))
    values = map(form.getvalue, cols)
    con.cursor().execute(f"""INSERT INTO {table} ({','.join(cols)}) VALUES ("{'","'.join(values)}");""")
    con.commit()
con.close()
print("<script>location.href='forms.py'</script>")
    # con.cursor().execute(f"INSERT {table} VALUES ({','.join(cols)});")(list(map(form.getvalue, cols)))
    # print(form)