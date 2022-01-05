import sqlite3 as sq


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.cursor = self._cursor()

    def _cursor(self):
        with sq.connect(self.database_name) as con:
            con.row_factory = sq.Row
            cur = con.cursor()
        return cur

    def __len__(self):
        self.cursor.execute(f"SELECT count(*) FROM {self.table_name}")
        return self.cursor.fetchone()[0]

    def __getitem__(self, item):
        self.cursor.execute("SELECT * FROM {}"
                            " WHERE name = '{}'".format(self.table_name, item))
        return tuple(self.cursor.fetchone())

    def __contains__(self, item):
        self.cursor.execute("SELECT * FROM {}"
                            " WHERE name = '{}'".format(self.table_name, item))
        return self.cursor

    def __iter__(self):
        self.cursor.execute('SELECT * FROM {}'.format(self.table_name))
        return self.cursor


presidents = TableData('example.sqlite', 'presidents')

print(len(presidents))
print(presidents['Yeltsin'])
print("Yeltsin" in presidents)
for president in presidents:
    print(president['name'])


books = TableData('example.sqlite', 'books')

print(len(books))
print(books['1984'])
print("Farenheit 451" in books)
for book in books:
    print(book['name'])
