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


def main():
    ##############################
    # uncomment to init database #
    ##############################
    # con = init()
    # con.close()
    server_address = ("localhost", 8000)
    http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
    http_server.serve_forever()


if __name__ == "__main__":
    main()


"""
Создать БД в соответствии с предметной областью,
- БД должна содержать не менее трех связанных таблиц,
- заполнить таблицы БД информацией с помощью SQL-запросов,
- написать не менее трех статистических запросов (SELECT),
- создать CGI-сервер
- создать форму(формы) для заполнения полей таблиц,
- осуществить вывод содержимого таблиц,
- экспорт/импорт таблицы в xml, используя заданную библиотеку.

Тема: "Космос"

"""