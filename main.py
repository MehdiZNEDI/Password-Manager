from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


YELLOW = "#f7f5dd"
#----------------Create the window-----------------#

window=Tk()
window .title("Password Manager")
window.config(padx=50, pady=50)

#-------Add the image and create the canvas--------#
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
#----Create labels----------------------------------
website_label = Label(text="Website :")
website_label.grid(row=1,column=0)
email_label = Label(text="email/Username :")
email_label.grid(row=2,column=0)
password_label = Label(text="Password :")
password_label.grid(row=3,column=0)

#create entries ------------------------------
website_entry = Entry(width=36)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus_set()

email_entry = Entry(width=36)
email_entry.insert(END, string="zneidi.mahdi1992@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)

password_entry = Entry(width=21)
print(password_entry.get())
password_entry.grid(row=3,column=1)

#Create buttons -------------------------------

def add_function():
  web_data=website_entry.get()
  email_data=email_entry.get()
  pass_data=password_entry.get()
 
  if len(web_data)==0 or len(pass_data)==0 :
    messagebox.showinfo(title="ooops!!!",message="something is missing!")
  else :
    is_ok=messagebox.askokcancel(title=web_data,message=f"these are the details entered : \n Email : {email_data}\nPassword : {pass_data}\n is it ok to save")
    if is_ok:
      f = open("password catalogue.txt", "a")
      f.write(f"{web_data}  |  {email_data}  |  {pass_data}\n")
      website_entry.delete(0,END)
      password_entry.delete(0,END)

generate_button =Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36, command=add_function)
add_button.grid(row=4,column=1,columnspan=2)














window.mainloop()