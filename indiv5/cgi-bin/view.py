import sqlite3
print("Content-type: text/html")
print()
print("<h1>Hello world!</h1>")


DB_NAME = "space.db"


def planetInSystem(cur: sqlite3.Cursor):
    s = "SELECT p.name, s.name FROM Planet p, StarSystem s WHERE p.system_id = s.system_id;"
    for i in cur.execute(s):
        print(f"Планета {i[0]} в системе {i[1]}<br>")

def systemInGalaxy(cur: sqlite3.Cursor):
    s = "SELECT s.name, g.name FROM StarSystem s, Galaxy g WHERE s.galaxy_id = g.galaxy_id;"
    for i in cur.execute(s):
        print(f"Система {i[0]} находится в галактике {i[1]}<br>")

def planetsInfo(cur: sqlite3.Cursor):
    s = "SELECT * FROM Planet p"
    for i in cur.execute(s):
        print(f"Планета {i[1]} имеет возраст {i[2]}, радиус {i[3]}, массу {i[4]}, {['жизни нет', 'жизнь есть'][i[5]]}<br>")



con = sqlite3.connect(DB_NAME)
print("<h2>Планеты в системах</h2>")
planetInSystem(con.cursor())
print("<h2>Системы в галактиках</h2>")
systemInGalaxy(con.cursor())
print("<h2>Свойства планет</h2>")
planetsInfo(con.cursor())
con.close()
