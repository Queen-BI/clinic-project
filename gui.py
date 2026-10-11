import sqlite3
import tkinter as tk 
from tkinter import messagebox
conn=sqlite3.connect("hospital.db")
cursor=conn.cursor()

# REGISTRATION WINDOW#
window=tk.Tk()

window.title("BloomCare Clinic")
window.geometry("400x400")
window.minsize(380,300)
window.maxsize(600,700)
window.config(bg="#001F3F")

#MAIN TITILE#
tk.Label(
    window,
    text="💞 BLOOM CARE CLINIC",
    bg="#001F3F",
    fg="#fff",
    font=("segoe UI",24,"bold")
).pack(pady=20)

#SUBTITLE#
tk.Label(
    window,
    text="Your Health is our priority",
    bg="#001F3F",
    fg="#fff",
    font=("segoe UI",11,"bold")
).pack()

#REGISTRATION HEADER#
tk.Label(
    window,
    
    text="PATIENT MANAGEMENT SYSTEM",
    bg="#FFF",
    fg="#000",
    font=("segoe UI",12,"bold")
).pack(pady=34)

#PATIENT REGISTRATION#
name_frame=tk.Frame(window)
name_frame.pack(anchor="w",pady=13)

name_Label=tk.Label(
    name_frame,
   
    text="Patient Name:",
    fg="#fff",
    bg="#001F3F",
    font=("segoe UI",12,"bold")
    
)
name_Label.grid(row=0,column=0)
name_entry=tk.Entry(name_frame)
name_entry.grid(row=0,column=1)

#PATIENT AGE#
age_frame=tk.Frame(window)
age_frame.pack(pady=13,anchor="w",padx=13)

age_label=tk.Label(
    age_frame,
    text="Patient Age:",
    fg="#fff",
    bg="#001F3F",
    font=("segoe  UI",12,"bold")

)
age_label.grid(row=0,column=0)
age_entry=tk.Entry(age_frame)
age_entry.grid(row=0,column=1)

#PATIENT PHONE NUMBER#
phone_frame=tk.Frame(window)
phone_frame.pack(anchor="w",pady=13)

phone_label=tk.Label(
    phone_frame,
    text="Phone Number:",
    fg="#fff",
    bg="#001F3F",
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
    window,
    width=15,
    text="Register",
    fg="white",
    bg="#001F3F",
    font=("segoe UI",12,"bold"),
    command=Register_patient
).pack()



#MESSAGE BOX AND CONDITIONS#








window.mainloop()
