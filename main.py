from tkinter import *
from tkinter import messagebox
import secrets
import pyperclip
import json

DEFAULT_EMAIL = "mardean@csu.fullerton.edu"


# searches through file for specified website and has a popup with the information
# if file doesn't exist or there's not data under the website popups occur
def search_websites():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="No File", message="File can't be found\n")
        return
    else:
        if website in data:
            email_username = data[website]["email_u_name"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email_username}\n"
                                                       f"Password: {password}\n")
        else:
            if website != "":
                messagebox.showerror(title="Data Not Found", message=f"No password for {website} saved\n")
                return


# uses secrets to generate a password which is then shown on the password entry box
def pass_gen():
    password = secrets.token_urlsafe(16)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# saves the info in the entry boxes to a json file
# if the file doesn't exist make a new one if it does update and add to it

def save_password():
    website = website_entry.get()
    username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email_u_name": username,
            "password": password
        }
    }
    # popup if one of the fields is empty
    if 0 in {len(website), len(username), len(password)}:
        messagebox.showerror(title="Empty Field", message="One or more fields is empty\n"
                                                          "Fill it in, please.\n")
        return
    # error checking if the file exists or not
    else:
        try:
            with open("data.json", "r") as file:
                # read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as new_file:
                json.dump(new_data, new_file, indent=4)
        else:
            # update old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # saving the data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# window settings
window = Tk()
window.title("Password Manager")
canvas = Canvas(width=200, height=200, highlightthickness=0)
window.config(padx=20, pady=20)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(110, 110, image=logo_img)
canvas.grid(column=1, row=0)

# wensite label and entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1)
website_entry.focus()
# email/name label and entry
email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)
email_username_entry = Entry(width=36)
email_username_entry.grid(column=1, row=2)
email_username_entry.insert(END, DEFAULT_EMAIL)
# password label and entry
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=36)
password_entry.grid(column=1, row=3)
# search button
search_button = Button(text="Search", command=search_websites, width=15)
search_button.grid(column=2, row=1, columnspan=2)
# password gen button
gen_password_button = Button(text="Generate Password", command=pass_gen)
gen_password_button.grid(column=2, row=3)
# add entry to button gen
add_button = Button(width=47, text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
