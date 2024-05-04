import db.database as db

# class Executor:
class Executor:
    """
    A class that executes a query to the database. It contains a constructor to initialize
    the data attributes (filling), a method execute that works with data and calls a method with a request,
    getter method getRowData.
    """
    csv_text = []
    table_names = []
    row_data = []

    def __init__(self, reader):
        for row in reader:
            self.csv_text.append(row)
        for name in self.csv_text[0]:
            self.table_names.append(name)

    def execute(self):
        db.create_tables(self.table_names)
        self.row_data = self.csv_text[1:-1]
        for fields in self.row_data:
            db.add_new_columns(self.table_names, fields)

    def getRowData(self):
        """ Getter. """
        return self.row_data
