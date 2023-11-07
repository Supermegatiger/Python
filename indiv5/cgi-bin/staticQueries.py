import sqlite3

DB_NAME = "space.db"


with open("head.txt","r") as f:
    print(f.read())


def planetInSystem(cur: sqlite3.Cursor):
    s = "SELECT p.name, s.name FROM Planet p, StarSystem s WHERE p.system_id = s.system_id;"
    res = ""
    for i in cur.execute(s):
        res += f"<li>Планета {i[0]} в системе {i[1]}</li>"
    return res

def systemInGalaxy(cur: sqlite3.Cursor):
    s = "SELECT s.name, g.name FROM StarSystem s, Galaxy g WHERE s.galaxy_id = g.galaxy_id;"
    res = ""
    for i in cur.execute(s):
        res += f"<li>Система {i[0]} находится в галактике {i[1]}</li>"
    return res

def planetsInfo(cur: sqlite3.Cursor):
    s = "SELECT * FROM Planet p"
    res = ""
    for i in cur.execute(s):
        res += f"<li>Планета {i[1]} имеет возраст {i[2]:.2e} лет, радиус {i[3]:.2e} м, массу {i[4]:.2e} кг, {['жизни нет', 'возможна жизнь'][i[5]]}</li>"
    return res


con = sqlite3.connect(DB_NAME)
print('<div class="d-flex flex-column align-items-center justify-content-center"><div>')
print('<a href="/" class="btn btn-secondary" style="margin-left:-1rem !important">Назад</a><br><br>')
print("<h2>Планеты в системах</h2>")
print(f"<ul>{planetInSystem(con.cursor())}</ul>")
print("<h2>Системы в галактиках</h2>")
print(f"<ul>{systemInGalaxy(con.cursor())}</ul>")
print("<h2>Свойства планет</h2>")
print(f"<ul>{planetsInfo(con.cursor())}</ul>")
print("</div></div>")
con.close()
