import sqlite3
import tkinter as tk 
from tkinter import messagebox

from main import Patient,Appointment
from main import Appointment
import main

conn=sqlite3.connect("hospital.db")
cursor=conn.cursor()

# DASHBOARD WINDOW#
window=tk.Tk()
dashboard=tk.Frame(window,bg="#147D78")
dashboard.pack(fill="both",expand=True)
dashboard_heading=tk.Label(
    dashboard,
    text="💞 BLOOM CARE CLINIC",
    font=("Arial",24,"bold"),
    bg="#147D78",
    fg="#F6F2EA"
).pack( pady=30,)
#DASHBOARD BUTTONS#
register_button=tk.Button(
    dashboard,
    text=" 🧕Register New Patient",
    font=("Arial",12,"bold"),
    bg="#FFF",
    fg="#000",
    width=20
)
register_button.pack(pady=10)


Search_button=tk.Button(
    dashboard,

    text="🧕Search Patients",
    font=("Arial",12,"bold"),
    bg="#FFF",
    fg="#000",
    width=25
)
Search_button.pack(pady=10)




#WINDOW AND EXTRA FRAMES#
window.title("BloomCare Clinic")
window.geometry("400x400")
window.minsize(380,300)
window.maxsize(600,700)
window.config(bg="#147d78")
registration_frame=tk.Frame(window,bg="#147D78")
search_frame=tk.Frame(window,bg="#147D78")
history_frame=tk.Frame(window,bg="#147d78")
appointment1=tk.Frame(window,bg="#147d78")



#SUBTITLE#
#ALL THE BUTTONS AND HEADERS IN THE REGISTRATION FRAME#
tk.Label(
    registration_frame,
    text="Patient Registration",
    bg="#147D78",
    fg="#E8F5F3",
    font=("segoe UI",11,"bold")
).pack()

#REGISTRATION HEADER#
tk.Label(
    registration_frame,
    
    text="Please enter the patient's details below.",
    bg="#147D78",
    fg="#000",
    font=("segoe UI",12,"bold")
).pack(pady=34)

#PATIENT REGISTRATION#
name_frame=tk.Frame(registration_frame)
name_frame.pack(anchor="w",pady=13)

name_Label=tk.Label(
    name_frame,
   
    text="Full name:",
    fg="#000",
    bg="#147D78",
    font=("segoe UI",12,"bold")
    
)
name_Label.grid(row=0,column=0)
name_entry=tk.Entry(name_frame)
name_entry.grid(row=0,column=1)


#PATIENT ID#
age_frame=tk.Frame(registration_frame)
age_frame.pack(pady=13,anchor="w",padx=13)

age_label=tk.Label(
    age_frame,
    text="Patient ID:",
    fg="#000",
    bg="#147D78",
    font=("segoe  UI",12,"bold")

)
age_label.grid(row=0,column=0)
age_entry=tk.Entry(age_frame)
age_entry.grid(row=0,column=1)

#PATIENT PHONE NUMBER#
phone_frame=tk.Frame(registration_frame)
phone_frame.pack(anchor="w",pady=13)

phone_label=tk.Label(
    phone_frame,
    text="Phone Number:",
    fg="#000",
    bg="#147D78",
    font=("segoe  UI",12,"bold")

)
phone_label.grid(row=0,column=0)
phone_entry=tk.Entry(phone_frame)
phone_entry.grid(row=0,column=1)


#REGISTRATION BUTTON#
def Register_patient():
    age=age_entry.get()
    phone=phone_entry.get()
    if not age.isdigit():
        messagebox.showerror("Invalid Age","Please enter Patient age")
        return
    if not phone.isdigit() or len(phone)!=11:
        messagebox.showerror(
             "Invalid Phone Number",
             "phone number must contain exactly 11 digits"
            )
        return
    conn=sqlite3.connect("hospital.db")
    cursor=conn.cursor()
    sql="""
    INSERT INTO patients  (name,age,phone) 
    VALUES(?, ?, ?)
    """
    print(repr(sql))

    print("name entered:",repr(name_entry.get()))
    print("age:",repr(age_entry.get()))
    print("phone:",repr(phone_entry.get()))


    cursor.execute(
        sql,
        (
            name_entry.get(),
            int(age_entry.get()),
            phone_entry.get()
        ))
     
    conn.commit()
    conn.close()
    if age.isdigit() and phone.isdigit() and len(phone)==11:
        messagebox.showinfo(
            "success",
            "patient registered successfully"
    )
    else:
        messagebox.showerror(
            "Error",
            "Enter a valid age and an 11-digit phone number"
        )
    return

registration_button=tk.Button(
    registration_frame,
    
    text="Register Patient",
    fg="#000",
    bg="#FFF9F7",
    font=("segoe UI",12,"bold"),
    command=Register_patient
).pack(anchor="nw",padx=20)





#DASHBOARD AND CONNECTING OF BUTTONS #
def show_dashboard():
    registration_frame.pack_forget()
    dashboard.pack(fill="both",expand=True)

def show_registration():
    dashboard.pack_forget()
    registration_frame.pack(fill="both",expand=True)

register_button.config(command=show_registration)




return_button=tk.Button(
    registration_frame,
    text=" ← back to dashboard",
    font=("Arial",12),
    bg="#F6F2EA",
    fg="#000",
    command=show_dashboard
).pack(anchor="ne",padx=20)

show_dashboard()

#SEARCH FRAME#
search1_frame=tk.Frame(search_frame)
search1_frame.pack(anchor="w",pady=13)

search_Label=tk.Label(
    search1_frame,
   
    text="search patient using name or ID:",
    fg="#000",
    bg="#147D78",
    font=("segoe UI",12,"bold")
    
)
search_Label.grid(row=0,column=0)
search1_entry=tk.Entry(search1_frame)
search1_entry.grid(row=0,column=1)

#connecting the search button#
def search_patient():
    search_value=name_entry.get()
    patient=Patient(None,None,None,None)
    result=patient.search_patient(search_value)
    for widget in result_frame.winfo_children():
        widget.destroy()
    if result:
        tk.Label(
            result_frame,
            text=f"Patient ID: {result[0]}",
            font=("Arial",14,"bold"),
            bg="#147d78",
            fg="#000"
        ).pack()
        tk.Label(
            result_frame,
            text=f"name: {result[1]}",
            font=("Arial",14,"bold"),
            bg="#147d78",
            fg="#000"
        ).pack()

        tk.Label(
            result_frame,
            text=f"age: {result[2]}",
            font=("Arial",14,"bold"),
            bg="#147d78",
            fg="#000"
        ).pack()

        
        tk.Label(
            result_frame,
            text=f"phone: {result[3]}",
            font=("arial",14,"bold"),
            bg="#147d78",
            fg="#000"
        ).pack()
       
        
    else:
        print("patient not found")

        
search_button=tk.Button(
    search_frame,
    text=" search",
    font=("Arial",12),
    bg="#F6F2EA",
    fg="#000",
) 
search_button.pack(anchor="n",padx=20)
search_button.config(command=search_patient)
result_frame=tk.Frame(
    search_frame

)
result_frame.pack()
#history frame#
tk.Label(
    history_frame,
    text="appointment history",
    font=("arial",18,"bold"),
    bg="#147d78",
    fg="#000"
).pack(pady=10)

#show the search frame#
def show_dashboard2():
    dashboard.pack(fill="both",expand="True")
    registration_frame.pack_forget()
    search_frame.pack_forget()
def show_search():
    dashboard.pack_forget()
    registration_frame.pack_forget()
    search_frame.pack(fill="both",expand=True)
Search_button.config(command=show_search)
def show_dashboard3():
    dashboard.pack(fill="both",expand="True")
    registration_frame.pack_forget()
    search_frame.pack_forget()
    history_frame.pack_forget()

def appointment_frame():
    dashboard.pack_forget()
    records_frame.pack_forget()
    search_frame.pack_forget()
    history_frame.pack_forget()
    appointment1.pack(fill="both",expand=True)

appointment_button=tk.Button(
    dashboard,

    text="appointments",
    font=("Arial",12,"bold"),
    bg="#FFF",
    fg="#000",
    width=25
)
appointment_button.pack(pady=10)
appointment_button.config(command=appointment_frame)

#appointment booking form#
tk.Label(
    appointment1,
    text="book appointment",
    font=("Arial",20,"bold"),
    bg="#147d78",
    fg="#000",

).pack()

tk.Label(
    appointment1,
    text="patient id",
    font=("Arial",20,"bold"),
    bg="#147d78",
    fg="#000",

).pack()
patient_id_entry=tk.Entry(appointment1)
patient_id_entry.pack(pady=5)

tk.Label(
    appointment1,
    text="doctor id",
    font=("Arial",20,"bold"),
    bg="#147d78",
    fg="#000",

).pack()
doctor_id_entry=tk.Entry(appointment1)
doctor_id_entry.pack(pady=5)

tk.Label(
    appointment1,
    text="appointment date (yyy-mm-dd)",
    font=("Arial",20,"bold"),
    bg="#147d78",
    fg="#000",

).pack()
appointment_date_entry=tk.Entry(appointment1)
appointment_date_entry.pack(pady=5)

tk.Label(
    appointment1,
    text="appointment time (hh:mm)",
    font=("Arial",20,"bold"),
    bg="#147d78",
    fg="#000",

).pack()
appointment_time_entry=tk.Entry(appointment1)
appointment_time_entry.pack(pady=5)
#return to dashboard#

def show_dashboard4():
    dashboard.pack(fill="both",expand="True")
    registration_frame.pack_forget()
    search_frame.pack_forget()
    history_frame.pack_forget()
    appointment1.pack_forget()
return_button2=tk.Button(
appointment1,
text=" ← back to dashboard",
font=("Arial",12),
bg="#F6F2EA",
fg="#000",
command=show_dashboard4
).pack(anchor="ne",padx=20)

#save#
def save_appointment():
    patient_id=patient_id_entry.get().strip()
    doctor_id=doctor_id_entry.get().strip()
    date=appointment_date_entry.get().strip()
    time=appointment_time_entry.get().strip()

    if not all([patient_id,doctor_id,date,time]):
        messagebox.showerror(
            "missing details",
            "please fill in all feilds"
        )
        return
    try:
        patient_id=int(patient_id)
        doctor_id=int(doctor_id)
        # print("doctor id entered:",doctor_id)

        conn=sqlite3.connect("hospital.db")
        cursor=conn.cursor()

        cursor.execute(
            "SELECT name FROM patients WHERE patient_id=?",
            (patient_id,)
        )
        patient=cursor.fetchone()

        cursor.execute(
            "SELECT name FROM Doctor WHERE doctor_id=?",(doctor_id,)
        )

        doctor=cursor.fetchone()

        if patient is None:
            messagebox.showerror(
                "Error","doctor_id not found"
            )
            conn.close()
            return
        conn.close()

        appointment=Appointment(
            None,
            patient_id,
            doctor_id,
            patient[0],
            date,
            time
        )
        print("about to book")
        appointment.book_appointment()
        print("booking")
        messagebox.showinfo(
            "success","appointment booked successfully"
            )
        patient_id_entry.delete(0,tk.END)
        doctor_id_entry.delete(0,tk.END)
        appointment_date_entry.delete(0,tk.END)
        appointment_time_entry.delete(0,tk.END)
    except ValueError:
        messagebox.showerror(
            "invalid input",
            "patient id and doctor id must be numbers."
            )
    except sqlite3.Error as error:
        import traceback
        traceback.print_exc()
        messagebox.showerror(
            "database error",
            str(error)
        )

#book_ appointment button#
tk.Button(
    appointment1,
    text="book appointment",
    command=save_appointment,
    bg="#147d78",
    fg="#000"
).pack(pady=15)







#appointment frame and button#
def show_appointment_history():
    dashboard.pack_forget()
    history_frame.pack(fill="both",expand=True)
appointment=Appointment(None,None,None,None,None,None)
result=appointment.get_appointment_details()

print("total appointments:",len(result))
if result:
    print("appointments found")
else:
    print("appointments not found")
records_frame=tk.Frame(history_frame,bg="#147d78")
records_frame.pack(fill="both",expand=True)

canvas=tk.Canvas(records_frame,bg="#147d78")
canvas.pack(side="left",fill="both",expand=True)

scrollbar=tk.Scrollbar(records_frame,orient="vertical",command=canvas.yview)
scrollbar.pack(side="right",fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

records_inner_frame=tk.Frame(canvas,bg="#147d78")
canvas.create_window((0,0),
window=records_inner_frame,anchor="nw")

records_inner_frame.bind(
    "<Configure>",
    lambda event:canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)


for row in result:
    tk.Label(
        records_inner_frame,
        text=str(row),
        bg="#147d78",
        fg="#000"
    ).pack(pady=5)



appointment_button=tk.Button(
    dashboard,
    text=" 📆Appointment History",
    font=("Arial",12,"bold"),
    bg="#FFF",
    fg="#000",
    command=show_appointment_history,
    width=25
)
appointment_button.pack(pady=10)

return3_button=tk.Button(
    history_frame,
    text=" ← back to dashboard",
    font=("Arial",12),
    bg="#F6F2EA",
    fg="#000",
    command=show_dashboard3
).pack(anchor="nw",padx=20)



show_dashboard2()

return2_button=tk.Button(
    search_frame,
    text=" ← back to dashboard",
    font=("Arial",12),
    bg="#F6F2EA",
    fg="#000",
    command=show_dashboard2
).pack(anchor="nw",padx=20)




















window.mainloop()
