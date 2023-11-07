import sqlite3
import cgi

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

galaxy_types = con.cursor().execute("SELECT * FROM GalaxyType;").fetchall()
galaxies = con.cursor().execute("SELECT galaxy_id, name FROM Galaxy;").fetchall()
systems = con.cursor().execute("SELECT system_id, name FROM StarSystem;").fetchall()
habitable = [(0, "жизни нет"), (1, "возможна жизнь")]

d = {'type_id': galaxy_types, 'galaxy_id': galaxies, 'system_id': systems, 'habitable': habitable}
d_names = {'type_id': 'galaxy_type', 'galaxy_id': 'galaxy', 'system_id': 'system', 'habitable': 'habitable'}

print('<div class="d-flex flex-column align-items-center justify-content-center">')
print('<a href="/" class="btn btn-secondary" style="margin-left:-1rem !important">Назад</a><br><br><div class="row justify-content-center text-center">')


tables = con.cursor().execute("SELECT name FROM sqlite_master WHERE type='table' AND NOT name='sqlite_sequence';").fetchall()
for table in tables:
    print(f"<form class='col col-4' action='/cgi-bin/post.py?{table[0]}' method='post' autocomplete='off'>")
    print(f"<h3>{table[0]}</h3>")
    columns = con.cursor().execute(f"PRAGMA table_info({table[0]});").fetchall()
    for column in columns[1:]:
        col_name = column[1]
        if not col_name in d:
            print(f"<label for='{col_name}'>{col_name} {'('+unit_dict[col_name]+')' if col_name in unit_dict else ''}:</label>")
            print(f"<input required class='form-control type='text' id='{col_name}' name='{col_name}'>")
        else:
            print(f"<label for='{col_name}'>{d_names[col_name]} :</label>")
            print(f"<select required class='form-control' name='{col_name}'>\n")
            for id, name in d[col_name]:
                print(f"<option value='{id}'>{name}</option>\n")
            print("</select>")
    print("<br><input class='m-2' type='submit' value='Submit'>")
    print("</form><br>")

print("</div></div>")
con.close()



print("</body></html>")