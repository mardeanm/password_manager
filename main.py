from tkinter import *
from tkinter import messagebox
import secrets
import pyperclip

DEFAULT_EMAIL="mardean@csu.fullerton.edu"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    password=secrets.token_urlsafe(16)

    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website=website_entry.get()
    username=email_username_entry.get()
    password=password_entry.get()
    if 0 in  {len(website),len(username),len(password)}:
        messagebox.showerror(title="Empty Field",message="One or more fields is empty\n"
                                                         "Fill it in, please.\n")
        return
    # message boxes
    is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}"
                                                  f"\nPasswrod: {password}\n"
                                                  f"Are these details ok to save?")
    if is_ok:
        with open("saved_password","a") as file:
            file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
canvas=Canvas(width=200,height=200,highlightthickness=0)
window.config(padx=20,pady=20)
logo_img=PhotoImage(file="logo.png")

canvas.create_image(110,110,image=logo_img)
canvas.grid(column=1,row=0)

#wensite label and entry
website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
website_entry=Entry(width=55)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
#email/name label and entry
email_username=Label(text="Email/Username:")
email_username.grid(column=0,row=2)
email_username_entry=Entry(width=55)
email_username_entry.grid(column=1,row=2,columnspan=2)
email_username_entry.insert(END, DEFAULT_EMAIL)
#password label and entry
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)
password_entry=Entry(width=36)
password_entry.grid(column=1,row=3)
#password gen button
gen_password_button=Button(text="Generate Password",command=pass_gen)
gen_password_button.grid(column=2,row=3)
#add entry to button gen
add_button=Button(width=47,text="Add",command=save_password)
add_button.grid(column=1,row=4,columnspan=2)
window.mainloop()