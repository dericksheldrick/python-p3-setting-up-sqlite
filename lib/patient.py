from __init__ import connection, cursor

class Patient:

    all = []

    def __init__(self, name):
        self.name = name 
       

    def save(self):
        sql ="""
            INSERT INTO patients(name)
            VALUES(?);
        """
        cursor.execute(sql, (self.name,))
        connection.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS patients(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            );
        """

        cursor.execute(sql)
        connection.commit()
 
    @classmethod
    def drop_table(cls):
        sql ="""
            DROP TABLE IF EXISTS patients
        """
        cursor.execute(sql)
        connection.commit()

Patient.drop_table()
Patient.create_table()
Patient("Kimani").save()
Patient("Joe").save()
#