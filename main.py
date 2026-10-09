
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
    def __init__(self,appointment_id,patient_id,doctor_id,date,time):
        self.appointment_id=appointment_id
        self.patient_id=patient_id
        self.doctor_id=doctor_id
        self.date=date
        self.time=time

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
appointment1=appointment(1,1,1,"2026-10-12","10.00")
print(patient1.name)
print(doctor1.name)
print(appointment1.date)



