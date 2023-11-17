import sqlite3
from xml.dom.minidom import parse
from tkinter import filedialog
import tkinter as tk

DB_NAME = "space.db"


with open("head.txt","r") as f:
    print(f.read())


def import_from_xml(cursor, doc):
    for node in doc.documentElement.childNodes:
        if node.nodeType != node.ELEMENT_NODE:
            table_name = node.tagName
            entries = node.childNodes()

            for entry in entries[0].getElementsByTagName('entry'):
                values = [field.firstChild.nodeValue for field in entry.childNodes]

                placeholders = ', '.join(['?' for _ in range(len(values))])
                query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                cursor.execute(query, values)

root = tk.Tk()
root.withdraw()
xml_file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])

if xml_file_path:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    doc = parse(xml_file_path)

    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table' and name != 'sqlite_sequence';")
    # table_names = set(node.tagName for node in doc.documentElement.childNodes if node.nodeType == node.ELEMENT_NODE)
    # print(table_names)
    import_from_xml(cursor, doc)

    conn.commit()
    conn.close()

# print("<script>location.href='/'</script>")

