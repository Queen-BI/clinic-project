
# patient#
class Patient:
    def __init__(self,name,patient_id,number,age):
        self.name=name
        self.patient_id=patient_id
        self.number=number
        self.age=age
        

# doctor#
class Doctor:
    def __init__(self,name,doctor_id,specialization):
        self.name=name
        self.doctor_id=doctor_id
        self.specialization=specialization

#appointment#
class appointment:
    def __init__(self,appointment_id,patient_id,doctor_id,name,date,time):
        self.appointment_id=appointment_id
        self.patient_id=patient_id
        self.doctor_id=doctor_id
        self.date=date
        self.time=time
        self.name=name
    def book_appointment(self):
        conn=sqlite3.connect("hospital.db")
        cursor=conn.cursor()

        cursor.execute("""
        INSERT INTO appointment (patient_id,doctor_id,name,date,time)
        VALUES(?,?,?,?,?)
        """,(
            self.patient_id,
            self.doctor_id,
            self.name,
            self.date,
            self.time
        ))
        conn.commit()
        print("appointment saved")
        conn.close()

    def update_appointment(self,new_date,new_time):
        conn=sqlite3.connect("hospital.db")
        cursor=conn.cursor()
            
        cursor.execute("""
        UPDATE appointment
        SET date=?,time=?
        WHERE "appointment_id"=?
        """,(new_date,new_time,self.appointment_id))

        conn.commit()
        print("updated")
        conn.close()
    
    def cancel_appointment(self):
        conn=sqlite3.connect("hospital.db")
        cursor=conn.cursor()

        cursor.execute("""
        DELETE FROM appointment
        WHERE "appointment_id"=? 
        """,(self.appointment_id,))
         
        conn.commit()
        conn.close()
        print("deletted")
      

        



import sqlite3
conn=sqlite3.connect("hospital.db")
cursor=conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Patients(
        patient_id INTEGER
        PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        phone TEXT
)
""")
conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Doctor(
        doctor_id INTEGER
        PRIMARY KEY,
        name TEXT NOT NULL,
        specialization TEXT NOT NULL
)
""")
conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Appointment(
        appointment_id INTEGER
        PRIMARY KEY,
        patient_id INTEGER,
        doctor_id INTEGER,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT
)
""")
conn.commit()
patient1=Patient("lisa",1,"090672311",16)
doctor1=Doctor("Dr.mary",1,"dentistry")
appointment1=appointment(1,1,1,"seki","2026-10-12","10.00")
print(patient1.name)
print(doctor1.name)
print(appointment1.date)



appointment2=appointment(3,2,3,"ali","2023-12-13","10.00")
appointment2.book_appointment()
appointment2.update_appointment("2023-23-12","12.00")
appointment2.cancel_appointment()





# conn=sqlite3.connect("hospital.db")
# cursor=conn.cursor()

# cursor.execute(""" 
# SELECT*FROM appointment 
# WHERE "appointment_id"=3 
# """)
# print(cursor.fetchone())
# conn.close()
cursor.execute("SELECT * FROM appointment")
print(cursor.fetchall())


