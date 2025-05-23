from __init__ import connection, cursor

class Doctor:

    all = []

    def __init__(self, name, speciality_id):
        self.name = name 
        self.speciality_id = speciality_id

    def save(self):
        sql ="""
            INSERT INTO doctors(name, speciality_id)
            VALUES(?, ?);
        """
        cursor.execute(sql, (self.name, self.speciality_id))
        connection.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS doctors(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                speciality_id INTEGER,
                FOREIGN KEY (speciality_id) REFERENCES 	specialities(id)
                
            );
        """

        cursor.execute(sql)
        connection.commit()
 
    @classmethod
    def drop_table(cls):
        sql ="""
            DROP TABLE IF EXISTS doctors
        """
        cursor.execute(sql)
        connection.commit()
Doctor.drop_table()
Doctor.create_table()
Doctor("Charity", 1).save()
Doctor("Kevin", 2).save()
