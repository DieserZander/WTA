import datetime

from db.database import Database


class ModelManager:
    def __init__(self, table_name, columns):
        self.table_name = table_name
        self.columns = columns
        self.db = Database()

    def get_all(self):
        self.db.cursor.execute(f"SELECT * FROM {self.table_name}")
        return self.db.cursor.fetchall()

    def get_by_id(self, id):
        self.db.cursor.execute(f"SELECT * FROM {self.table_name} WHERE id={id}")
        return self.db.cursor.fetchone()

    def validate_data(self, column, data):
        self.db.cursor.execute(f"SELECT count('*') as c FROM {self.table_name} WHERE {column} = '{data}'")
        return self.db.cursor.fetchone()['c']
        # return query['count']

    def post_entry(self, data):
        if data is not None:
            entry = {
                'columns': "",
                'values': ""
            }
            _columns = ""
            _values = ""
            can_post = True
            for key in data:
                if key in self.columns:
                    if self.columns[key]['unique']:
                        if self.validate_data(column=key, data=data[key]) > 0:
                            can_post = False
                    _columns += key + ", "
                    _values += f"'{data[key]}', "
            entry['columns'] = f"({_columns[:-2]})"
            entry['values'] = f"({_values[:-2]})"
            if can_post:
                self.db.cursor.execute(f"INSERT INTO {self.table_name} {entry['columns']} VALUES {entry['values']};")
                self.db.conn.commit()
            else:
                print("Can´t post data")
