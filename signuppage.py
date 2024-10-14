import customtkinter as ctk
import re
from tkinter import messagebox
from services import registerUser

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

class SignUp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Sign Up")
        self.geometry("300x500")
        self.resizable(False, False)
        
        self.username = ctk.CTkEntry(self, 
                                     placeholder_text="User Name", 
                                     width=250
                                     )
        self.username.place(rely=0.2, relx=0.5, anchor=ctk.CENTER)
        
        self.email = ctk.CTkEntry(self,
                                  placeholder_text="Email Address",
                                  width=250
                                  )
        self.email.place(rely=0.3, relx=0.5, anchor=ctk.CENTER)
        
        self.emailError = ctk.CTkLabel(self, 
                                       text="", 
                                       text_color="#fc0000")
        self.emailError.pack(pady=(2, 0))
        
        self.address = ctk.CTkEntry(self,
                                    placeholder_text="Address",
                                    width=250
                                    )
        self.address.place(rely=0.4, relx=0.5, anchor=ctk.CENTER)
        
        self.password = ctk.CTkEntry(self, 
                                     placeholder_text="Password",
                                     show=["*"],
                                     width=250
                                     )
        self.password.place(rely=0.5, relx=0.5, anchor=ctk.CENTER)
        
        self.criterror = ctk.CTkLabel(self,
                                      text="",
                                      text_color="#fc0000"
                                      )
        self.criterror.pack(pady=(2, 0))
        
        self.confirmPassword = ctk.CTkEntry(self,
                                            placeholder_text="Confirm Password", 
                                            show=["*"], 
                                            width=250)
        self.confirmPassword.place(rely=0.6, relx=0.5, anchor=ctk.CENTER)
        
        self.passwordError = ctk.CTkLabel(self,
                                          text="",
                                          text_color="#fc0000"
                                          )
        
        self.signUpBtn = ctk.CTkButton(self, 
                                       text="Register", 
                                       width=250, 
                                       command=self.SignUpBtnClick)
        self.signUpBtn.place(rely=0.7, relx=0.5 , anchor=ctk.CENTER)
        
    def SignUpBtnClick(self):
        self.name = self.username.get()
        self.emailVal = self.email.get()
        self.addressVal = self.address.get()
        self.passwordVal = self.password.get()
        self.confirmPasswordVal = self.confirmPassword.get()
        
        self.Valid = self.validateSignUp(self.emailVal, self.passwordVal, self.confirmPasswordVal)
        
        if(self.Valid):
            try:
                payload = {
                    "userName": self.name,
                    "email": self.emailVal,
                    "password": self.passwordVal,
                    "address": self.addressVal,
                }
                response = registerUser(payload)
                
                if(response == "User already exists!"): 
                    messagebox.showerror(title="Error", message="User already exists!")
                else:
                    messagebox.showinfo(title="Success", message="Registration Successful")
                    self.destroy()
                    import loginpage
                    
                self.clearSignUp()
            except Exception as e:
                if(e=="User already exists!"):
                    messagebox.showerror(title="Error", message="User already exists!")    
            except:
                messagebox.showerror(title="Error", message="Registration Failed")
                    
                
                
    def clearSignUp(self):
        self.username.delete(0, 'end')
        self.email.delete(0, 'end')
        self.address.delete(0, 'end')
        self.password.delete(0, 'end')
        self.confirmPassword.delete(0, 'end')
        self.emailError.configure(text="")
        self.criterror.configure(text="")
        self.passwordError.configure(text="")
                    
        
    def validateSignUp(self, emailVal, passwordVal, confirmPasswordVal) -> bool:
        self.emailVal = emailVal
        self.passwordVal = passwordVal
        self.confirmPasswordVal = confirmPasswordVal
        self.isFormValid = True
        self.regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        #messagebox.showerror(title="error", message= (f"Email: {self.emailVal}, Password: {self.passwordVal}, Confirm Password: {self.confirmPasswordVal}"))
        
        if(self.emailVal == '' or self.passwordVal == '' or self.confirmPasswordVal ==''):
            messagebox.showerror(title="Error",  message="All fields are required")
            return False
    
        if(re.fullmatch(self.regex,self.emailVal)):
            self.email.configure(border_color="light gray")
            self.emailError.configure(text="")
        else:
            self.email.configure(border_color="red")
            self.emailError.configure(text="Invalid Email!")
            self.isFormValid = False
    
        if(len(self.passwordVal) < 8):
            self.password.configure(border_color="red")
            self.criterror.configure(text="Password must be at least 8 characters long")
            self.isFormValid = False
    
        if((self.passwordVal  and self.confirmPasswordVal) and self.passwordVal == self.confirmPasswordVal):
            self.password.configure(border_color="light gray")
            self.confirmPassword.configure(border_color="light gray")
            self.passwordError.configure(text="")
        else:
            self.password.configure(border_color="red")
            self.confirmPassword.configure(border_color="red")
            self.passwordError.configure(text="Password and Confirm Password not matching!")
            self.isFormValid = False
    
        return self.isFormValid
        
        

welcome_page = SignUp()
welcome_page.mainloop()