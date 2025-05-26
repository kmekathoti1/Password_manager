
from tkinter import messagebox
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepassword():
#Password Generator Project
    from random import choice,randint,shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]
    password_list=password_numbers+password_symbols+password_letters
    shuffle(password_list)

    password = ""
    password ="".join(password_list)
    password_input.delete(0,"end")

    password_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password_to_file():
    website_data=website_input.get()
    email_data=email_input.get()
    password_data=password_input.get()
    new_data={
        website_data:{
            "email":email_data,
            "password":password_data,
        }
    }
    if len(website_data)==0 or len(email_data)==0 or len(password_data)==0:
        messagebox.askretrycancel(title="OOps!" , message="Do not leave a field empty")
    else:
        try:
            with open("data.json", "r") as data:
                read_data = json.load(data)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:

            read_data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(read_data,data_file,indent=4)
        finally:
            website_input.delete(0, "end")
            password_input.delete(0, "end")

#_________________________SEARCH EMAIL PASSWORD_______________________

def search_email_pwd():
    website = website_input.get().title()
    try:
        with open("data.json", "r") as data:
            full_data = json.load(data)
    except FileNotFoundError:
        messagebox.askokcancel(title="Error",message="No data file found")
    else:
            if website in full_data:
                email = full_data[website]["email"]
                password = full_data[website]["password"]

                messagebox.askokcancel(title=f"{website} Details", message=f"Email:{email} \n Password: {password}")
            else:
                messagebox.askokcancel(title="Error",message=f"No details for {website} exists")















# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *



window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

#labels
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)


#entries
website_input=Entry(width=21)
website_input.focus()
website_input.grid(row=1,column=1)
email_input=Entry(width=50)
email_input.insert(0,"kiranmayi.mekathoti@gmail.com")
email_input.grid(row=2,column=1,columnspan=2)
password_input=Entry(width=21)
password_input.grid(row=3,column=1)

gen_password_button=Button(text="Generate Password",width=15,command=generatepassword)
gen_password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=40,command=save_password_to_file)
add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(text="Search",width=15,command=search_email_pwd)
search_button.grid(row=1,column=2)

window.mainloop()