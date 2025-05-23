from __init__ import connection, cursor

class Speciality:
    all = []

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)
    
    def save(self):
        sql ="""
            INSERT INTO specialities(name)
            VALUES(?);
        """
        cursor.execute(sql, (self.name,))
        connection.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS specialities(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            );
        """

        cursor.execute(sql)
        connection.commit()
 
    @classmethod
    def drop_table(cls):
        sql ="""
            DROP TABLE IF EXISTS specialities
        """
        cursor.execute(sql)
        connection.commit()

# Speciality.drop_table()
Speciality.create_table()
# Speciality("Oncologist").save()
Speciality("Dentist").save()