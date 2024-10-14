import customtkinter as ctk
import tkinter as tk
from PIL import Image


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

class WelcomePage(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Welcome Page")
        self.geometry("300x500")
        self.resizable(False, False)

        # Load the image
        self.image = ctk.CTkImage(light_image=Image.open("images/logo.png"), 
                                  dark_image = Image.open("images/logo.png"),
                                  size = (200,200))
        
        # Create a label to display the image
        self.image_label = ctk.CTkLabel(self,
                                        text = "",
                                        image=self.image)
        self.image_label.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

        # Create a continue button
        self.continue_button = ctk.CTkButton(self, 
                                             text="Continue",
                                             height=50,
                                             width = 200,
                                             corner_radius=20, 
                                             command=self.open_next_page)
        self.continue_button.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

    def open_next_page(self):
        self.destroy()
        self.next_page = NextPage()
        self.next_page.mainloop()

class NextPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Next Page")
        self.geometry("300x500")
        self.resizable(False, False)

        self.image = ctk.CTkImage(light_image=Image.open("images/progress dark.png"), 
                                  dark_image = Image.open("images/progress dark.png"),
                                  size = (250,130))
        
        self.image_label  = ctk.CTkLabel(self,
                                        text = "",
                                        image=self.image)
        self.image_label.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
        
        self.signup_button = ctk.CTkButton(self, text="Sign Up", command=self.sign_up, height=50, width = 200, corner_radius=20)
        self.signup_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

        self.login_button = ctk.CTkButton(self, text="Log In", command=self.log_in, height=50, width = 200, corner_radius=20)
        self.login_button.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

    def sign_up(self):
        self.destroy()
        import signuppage
    def log_in(self):
        self.destroy()
        import loginpage





if __name__ == "__main__":
    welcome_page = WelcomePage()
    welcome_page.mainloop()