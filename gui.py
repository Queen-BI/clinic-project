import sqlite3
import tkinter as tk 
from tkinter import messagebox
conn=sqlite3.connect("hospital.db")
cursor=conn.cursor()

# REGISTRATION WINDOW#
window=tk.Tk()
dashboard=tk.Frame(window,bg="#B69B6B")
dashboard.pack(fill="both",expand=True)
dashboard_heading=tk.Label(
    dashboard,
    text="💞 BLOOM CARE CLINIC",
    font=("Arial",24,"bold"),
    bg="#B69B6B",
    fg="#343626"
).pack(pady=30)

register_button=tk.Button(
    dashboard,
    text=" 🧕Register New Patient",
    font=("Arial",12,"bold"),
    bg="#FFF",
    fg="#000",
    width=25
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


appointment_button=tk.Button(
    dashboard,
    text=" 📆Appointment History",
    font=("Arial",12,"bold"),
    bg="#FFF",
    fg="#000",
    width=25
)
appointment_button.pack(pady=10)

window.title("BloomCare Clinic")
window.geometry("400x400")
window.minsize(380,300)
window.maxsize(600,700)
window.config(bg="#B69B6B")
registration_frame=tk.Frame(window,bg="#B69B6B")



#SUBTITLE#
tk.Label(
    registration_frame,
    text="Patient Registration",
    bg="#B69B6B",
    fg="#3f412b",
    font=("segoe UI",11,"bold")
).pack()

#REGISTRATION HEADER#
tk.Label(
    registration_frame,
    
    text="Please enter the patient's details below.",
    bg="#B69B6B",
    fg="#3f412b",
    font=("segoe UI",12,"bold")
).pack(pady=34)

#PATIENT REGISTRATION#
name_frame=tk.Frame(registration_frame)
name_frame.pack(anchor="w",pady=13)

name_Label=tk.Label(
    name_frame,
   
    text="Full name:",
    fg="#3f412b",
    bg="#B69B6B",
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
    text="ID:",
    fg="#3f412b",
    bg="#B69B6B",
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
    fg="#3f412b",
    bg="#B69B6B",
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
        messagebox.showerror("Invalid Age","Please enter a valid age")
        return
    if not phone.isdigit() or len(phone)!=11:
        messagebox.showerror(
             "Invalid Phone Number",
             "phone number must contain exactly 11 digits"
            )
        return
    conn=sqlite3.connect("hospital.db")
    cursor=conn.cursor()
    sql="INSERT INTO Patients VALUES (NULL,?, ?, ?)"

    cursor.execute(
        sql,
        (
            name_entry.get(),
            int(age_entry.get()),
            phone_entry.get()
        )
    )
     
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
    fg="#3F412B",
    bg="#B69B6B",
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
    bg="#B69B6B",
    fg="#3f412b",
    command=show_dashboard
).pack(anchor="ne",padx=20)
show_dashboard()









window.mainloop()
