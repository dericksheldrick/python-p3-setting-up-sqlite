from __init__ import connection, cursor

class Appointment:
    all = []

    def __init__(self, name,patient_id , doctor_id, date):
        self.name = name
        self.patient_id = patient_id 
        self.doctor_id =  doctor_id
        self.date =  date
        self.all.append(self)
    
    def save(self):
        sql ="""
            INSERT INTO appointments(name,patient_id, doctor_id, date)
            VALUES(?, ? ,?, ?);
        """
        cursor.execute(sql, (self.name,self.patient_id,self.doctor_id, self.date))
        connection.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS appointments(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                patient_id INTEGER,
                doctor_id INTEGER,
                date DATETIME, 
                FOREIGN KEY (patient_id) REFERENCES patients(id),
                FOREIGN KEY (doctor_id) REFERENCES doctors(id)
            );
        """

        cursor.execute(sql)
        connection.commit()
 
    @classmethod
    def drop_table(cls):
        sql ="""
            DROP TABLE IF EXISTS appointments
        """
        cursor.execute(sql)
        connection.commit()

Appointment.drop_table()
Appointment.create_table()

Appointment("Thursday", 2, 1, "2025/06/12").save()
