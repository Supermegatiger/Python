import sqlite3

DB_NAME = "space.db"


with open("head.txt","r") as f:
    print(f.read())

unit_dict = {
    "size": "ly",
    "radius": "m",
    "mass": "kg",
    "temperature": "K"
}


con = sqlite3.connect(DB_NAME)


tables = map(lambda i: i[0], con.cursor().execute("SELECT name FROM sqlite_master WHERE type='table' AND NOT name='sqlite_sequence';").fetchall())


data = {}
columns = {}

for table in tables:
    columns[table] = con.cursor().execute(f"PRAGMA table_info({table});").fetchall()
    data[table] = con.cursor().execute(f"SELECT * FROM {table};").fetchall()


print('<div class="d-flex flex-column align-items-center justify-content-center">')
print('<a href="/" class="btn btn-secondary" style="margin-left:-1rem !important">Назад</a><br><br><div class="justify-content-center text-center">')

# print(f"<label for='table'>Таблица :</label>")
# print(f"<select required class='form-control' name='table'>\n")
# for table in tables:
#     print(f"<option value='{table}'>{table}</option>\n")
# print("</select>")

for i,v in columns.items():
    print(f"<table class='table table-dark'>")
    print(f"<h2>{i}</h2>")
    print("<tr>")
    for column in v:
        col_name = column[1]
        print(f"<th>{col_name} {'('+unit_dict[col_name]+')' if col_name in unit_dict else ''}:</th>")
    print("</tr>")
    for col in data[i]:
        print(f"<tr><td>{'</td><td>'.join(map(str, col))}</td></tr>")
    
    print("</table><br>")


print("</div></div>")

con.close()
