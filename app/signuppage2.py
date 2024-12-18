import customtkinter as ctk
import re
from tkinter import messagebox
from services import registerUser

format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def validateSignUp(emailVal, passwordVal, confirmPasswordVal) -> bool:
    isFormValid = True

    if(emailVal == '' or passwordVal == '' or confirmPasswordVal ==''):
        messagebox.showerror(title="Error",  message="All fields are  required")
        return False

    
    if(re.fullmatch(format, emailVal)):
        email.configure(border_color="light gray")
        emailError.configure(text="")
    else:
        email.configure(border_color="red")
        emailError.configure(text="Invalid Email !")
        isFormValid = False

    # Password and Confirm Password validation
    if(len(passwordVal) < 8):
        password.configure(border_color="red")
        critError.configure(text="Password must be at least 8 characters long")
        return False
    
    if((passwordVal  and confirmPasswordVal) and passwordVal == confirmPasswordVal):
        password.configure(border_color="light gray")
        confirmPassword.configure(border_color="light gray")
        PasswordError.configure(text="")
    else:
        password.configure(border_color="red")
        confirmPassword.configure(border_color="red")
        PasswordError.configure(text="Password and Confirm Password not matching !")
        isFormValid = False

    return isFormValid

def clearSignUpForm():
    userName.delete(0, ctk.END)
    email.delete(0, ctk.END)
    address.delete(0, ctk.END)
    password.delete(0, ctk.END)
    confirmPassword.delete(0, ctk.END)

def onSignUpBtnClick():
    name = userName.get()
    emailVal = email.get()
    passwordVal = password.get()
    confirmPasswordVal = confirmPassword.get()
    addressVal = address.get()

    isFormValid = validateSignUp(emailVal, passwordVal, confirmPasswordVal)

    if(isFormValid):
        try:
            payload = {
                "userName": name,
                "email": emailVal,
                "password": passwordVal,
                "address": addressVal,
                        }
            response = registerUser(payload)

            if(response == "User already exists !"):
                messagebox.showerror(title="Error", message="User already exists !") 
            else:
                messagebox.showinfo(title="Success", message="Registration Successful")
                signupWindow.destroy()
                import loginpage

            clearSignUpForm()
            

        except Exception as e:
            if(e == "User already exists !"):
                messagebox.showerror(title="Error", message="User already exists !")    
        except:
            messagebox.showerror(title="Error", message="Registration Failed")


def goToLoginPage():
    clearSignUpForm()
    signupWindow.destroy()
    import loginpage

signupWindow = ctk.CTk()

signupWindow.title("Sign Up")
signupWindow.geometry("300x500")
signupWindow.resizable(False, False)

headingLabel = ctk.CTkLabel(signupWindow, 
                            text="Sign Up", font=ctk.CTkFont(size=30, weight="bold"))
headingLabel.pack(padx=10, pady=(40, 20))

userName = ctk.CTkEntry(signupWindow, placeholder_text="User Name", width=250)
userName.pack(pady=15)

email = ctk.CTkEntry(signupWindow, placeholder_text="Email", width=250)
email.pack(pady=(15,0))

emailError = ctk.CTkLabel(signupWindow, text="", font=ctk.CTkFont(size=12), text_color="#fc0000")
emailError.pack(pady=(2,0))

address = ctk.CTkEntry(signupWindow, placeholder_text="Address", width=250)
address.pack(pady=(0, 15))

password = ctk.CTkEntry(signupWindow, placeholder_text="Password", show=["*"], width=250)
password.pack(pady=(15,0))

critError = ctk.CTkLabel(signupWindow, text="", font=ctk.CTkFont(size=12), text_color="#fc0000")
critError.pack(pady=(2,0))


confirmPassword = ctk.CTkEntry(signupWindow, placeholder_text="Confirm Password", show=["*"], width=250)
confirmPassword.pack(pady=0)

PasswordError = ctk.CTkLabel(signupWindow, text="", font=ctk.CTkFont(size=12), text_color="#fc0000")
PasswordError.pack(pady=(2,0))

signUpBtn = ctk.CTkButton(signupWindow, text="Register", width=250, command=onSignUpBtnClick)
signUpBtn.pack(pady=(0,5))

signInLink = ctk.CTkButton(signupWindow, text="Already have an account? Sign in here", font=ctk.CTkFont(size=12, underline=True), text_color="#fff", fg_color="#2b2b2b", hover_color="#2b2b2b", command=goToLoginPage,  anchor="center")
signInLink.pack(pady=(5,0))

signupWindow.mainloop()