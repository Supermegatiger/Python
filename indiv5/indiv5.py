import sqlite3
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler
import os

DB_NAME = "space.db"



def init():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    with open("init.sql","r") as f:
        cur.executescript(f.read())
    return con

def planetInSystem(cur: sqlite3.Cursor):
    s = "SELECT p.name, s.name FROM Planet p, StarSystem s WHERE p.system_id = s.system_id;"
    for i in cur.execute(s):
        print(f"Планета {i[0]} в системе {i[1]}")

def systemInGalaxy(cur: sqlite3.Cursor):
    s = "SELECT s.name, g.name FROM StarSystem s, Galaxy g WHERE s.galaxy_id = g.galaxy_id;"
    for i in cur.execute(s):
        print(f"Система {i[0]} находится в галактике {i[1]}")

def planetsInfo(cur: sqlite3.Cursor):
    s = "SELECT * FROM Planet p"
    for i in cur.execute(s):
        print(f"Планета {i[1]} имеет возраст {i[2]}, радиус {i[3]}, массу {i[4]}, {['жизни нет', 'жизнь есть'][i[5]]}")

def main():
    # if doesn't exist
    # con = init()
    # con = sqlite3.connect(DB_NAME)
    # planetInSystem(con.cursor())
    # systemInGalaxy(con.cursor())
    # planetsInfo(con.cursor())
    # con.close()
    server_address = ("localhost", 8000)
    http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
    http_server.serve_forever()


if __name__ == "__main__":
    main()


"""
Создать БД в соответствии с предметной областью,
БД должна содержать не менее трех связанных таблиц,
заполнить таблицы БД информацией с помощью SQL-запросов,
написать не менее трех статистических запросов (SELECT),
создать CGI-сервер
создать форму(формы) для заполнения полей таблиц,
осуществить вывод содержимого таблиц,
экспорт/импорт таблицы в xml, используя заданную библиотеку.

Тема: "Космос"

"""