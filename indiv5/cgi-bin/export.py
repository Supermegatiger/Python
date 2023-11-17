import sqlite3
from xml.dom.minidom import Document
from tkinter import filedialog
import tkinter as tk

DB_NAME = "space.db"


with open("head.txt","r") as f:
    print(f.read())

def fetch_table_data(cursor, table_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    return [column[1] for column in columns]

def export_to_xml(cursor, doc, table_name):
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()

    table_element = doc.createElement(table_name)
    doc.documentElement.appendChild(table_element)
    
    columns = fetch_table_data(cursor, table_name)

    for row in rows:
        entry = doc.createElement('entry')
        table_element.appendChild(entry)

        for i, value in enumerate(row):
            field = doc.createElement(columns[i])
            field.appendChild(doc.createTextNode(str(value)))
            entry.appendChild(field)

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

doc = Document()
doc.appendChild(doc.createElement('data'))

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' and name != 'sqlite_sequence';")
table_names = cursor.fetchall()

for table_name in table_names:
    export_to_xml(cursor, doc, table_name[0])

root = tk.Tk()
root.withdraw()

file_path = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])

if file_path:
    with open(file_path, 'w') as file:
        file.write(doc.toprettyxml())

conn.close()

print("<script>location.href='/'</script>")
