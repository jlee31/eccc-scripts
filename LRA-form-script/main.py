import fitz
import customtkinter as ctk
from tkinter import filedialog, messagebox
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

incoming_pdf = resource_path("input/Incoming.pdf")
returning_pdf = resource_path("input/Returning.pdf")

def create_form(values):
    try:
        print(values)
        # Open the correct PDF based on the first value in the list
        if values[0]:
            doc = fitz.open(incoming_pdf)
        else:
            doc = fitz.open(returning_pdf)

        for page in doc:
            for field in page.widgets():
                if field.field_name == "Subscriber Last Name":
                    field.field_value = values[1]
                elif field.field_name == "Subscriber First Name":
                    field.field_value = values[2]
                elif field.field_name == "Subscriber Email":
                    field.field_value = values[3]
                elif field.field_name == "Telephone Number":
                    field.field_value = values[4]
                elif field.field_name == "Driver's Licence" and "Driver's Licence" in values[5]:
                    field.field_value = True
                elif field.field_name == "Credit Card" and "Credit Card" in values[5]:
                    field.field_value = True
                elif field.field_name == "Government of Canada ID" and "GovID" in values[5]:
                    field.field_value = True
                elif field.field_name == "Other (please identify)" and "Other" in values[5]:
                    field.field_value = True
                elif field.field_name == "Other Explanation":
                    other_dict = next((item for item in values[5] if isinstance(item, dict) and "Other" in item), None)
                    if other_dict:
                        field.field_value = other_dict["Other"]

                field.update()

        save_path = filedialog.asksaveasfilename(initialfile=f'{values[1]}{values[2]}LRAform.pdf', defaultextension=".pdf")
        if save_path:
            doc.save(save_path)
        doc.close()
        messagebox.showinfo("Success", "Document successfully created!")

    except Exception as e:
        print(f"Some error occurred: {e}")

# Main App
app = ctk.CTk()
app.title("LRA Quick Form Filler")
app.geometry("1000x600")

container = ctk.CTkFrame(app)
container.pack(expand=True)

container.grid_columnconfigure(0, weight=1)
container.grid_columnconfigure(1, weight=1)

check_var_incoming = ctk.IntVar(value=0)
checkbox_incoming = ctk.CTkCheckBox(container, text="Incoming", variable=check_var_incoming, onvalue=1, offvalue=0)
checkbox_incoming.grid(row=0, column=0, padx=20, pady=8, sticky="ew")

check_var_returning = ctk.IntVar(value=0)
checkbox_returning = ctk.CTkCheckBox(container, text="Returning", variable=check_var_returning, onvalue=1, offvalue=0)
checkbox_returning.grid(row=0, column=1, padx=20, pady=8, sticky="ew")

# Entries
first_name = ctk.CTkEntry(container, placeholder_text="Enter First Name here")
first_name.grid(row=1, column=0, columnspan=2, padx=20, pady=8, sticky="ew")

last_name = ctk.CTkEntry(container, placeholder_text="Enter Last Name here")
last_name.grid(row=2, column=0, columnspan=2, padx=20, pady=8, sticky="ew")

email = ctk.CTkEntry(container, placeholder_text="Enter Email here")
email.grid(row=3, column=0, columnspan=2, padx=20, pady=8, sticky="ew")

number = ctk.CTkEntry(container, placeholder_text="Enter Phone Number here")
number.grid(row=4, column=0, columnspan=2, padx=20, pady=8, sticky="ew")

# ID Checkboxes
driverlicence_var = ctk.IntVar(value=0)
driverlicence = ctk.CTkCheckBox(container, text="Driver's Licence", variable=driverlicence_var, onvalue=1, offvalue=0)
driverlicence.grid(row=5, column=0, padx=20, pady=8, sticky="ew")

creditcard_var = ctk.IntVar(value=0)
creditcard = ctk.CTkCheckBox(container, text="Credit Card", variable=creditcard_var, onvalue=1, offvalue=0)
creditcard.grid(row=5, column=1, padx=20, pady=8, sticky="ew")

passport_var = ctk.IntVar(value=0)
passport = ctk.CTkCheckBox(container, text="Passport", variable=passport_var, onvalue=1, offvalue=0)
passport.grid(row=6, column=0, padx=20, pady=8, sticky="ew")

gcid_var = ctk.IntVar(value=0)
gcid_checkbox = ctk.CTkCheckBox(container, text="Government of Canada ID", variable=gcid_var, onvalue=1, offvalue=0)
gcid_checkbox.grid(row=6, column=1, padx=20, pady=8, sticky="ew")

# Other ID entry
other = ctk.CTkEntry(container, placeholder_text="Enter other ID (If more than one, separate by comma)")
other.grid(row=7, column=0, columnspan=2, padx=20, pady=8, sticky="ew")

def clear_fields():
    check_var_incoming.set(0)
    check_var_returning.set(0)
    first_name.delete(0, 'end')
    last_name.delete(0, 'end')
    email.delete(0, 'end')
    number.delete(0, 'end')
    other.delete(0, 'end')
    driverlicence_var.set(0)
    creditcard_var.set(0)
    passport_var.set(0)
    gcid_var.set(0)

clear = ctk.CTkButton(container, text="Clear Fields", command=clear_fields)
clear.grid(row=8, column=0, columnspan=2, padx=20, pady=8, sticky="ew")

def get_info():
    ret = []
    incoming = check_var_incoming.get() == 1
    ret.append(incoming)
    
    # Get values from entry fields
    first_name_value = first_name.get()
    ret.append(first_name_value)
    
    last_name_value = last_name.get()
    ret.append(last_name_value)
    
    email_value = email.get()
    ret.append(email_value)
    
    number_value = number.get()
    ret.append(number_value)
    
    # Assuming provided license is a list of options the user selects
    provided_license = []
    if driverlicence_var.get() == 1:
        provided_license.append("Driver's Licence")
    if creditcard_var.get() == 1:
        provided_license.append("Credit Card")
    if passport_var.get() == 1:
        provided_license.append("Passport")
    if gcid_var.get() == 1:
        provided_license.append("GovID")
    if other.get():
        provided_license.append("Other")
        provided_license.append({"Other": other.get()})
    ret.append(provided_license)
    return ret
    
# Save Button
save = ctk.CTkButton(container, text = "Save", command=lambda: create_form(values=get_info()))
save.grid(row=9, column=0, columnspan=2, padx=20, pady=8, sticky="ew")

app.mainloop()