import sqlite3

conn=sqlite3.connect("hospital.db")
cursor=conn.cursor()







cursor.execute("""
    SELECT 
        appointment."appointment_id",
        appointment."patient_id",
        COALESCE(patients.name,appointment.name),
        doctor.name,
        appointment.date,
        appointment.time
    FROM appointment
    LEFT JOIN patients
        ON appointment."patient_id"=patients.patient_id
    LEFT JOIN doctor
        ON appointment."doctor_id"=doctor.doctor_id
""")
results=cursor.fetchall()
for row in results:
    print(row)
print("total appointments displayed:", len(results))



conn.close()