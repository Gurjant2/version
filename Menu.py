import customtkinter as ctk
from tkinter import ttk
from PIL import Image
from datetime import date

class SampleApp(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        self._frame = None
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        self.geometry("300x500")
        
        new_frame = frame_class(self)

        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill=ctk.BOTH, expand=True)


class BasePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_navigation_buttons(master)

    def create_navigation_buttons(self, master):
        button_data = [
            ("version/images/home.png", HomePage),
            ("version/images/chart.png", Chart),
            ("version/images/icon.png", IconPage),
            ("version/images/AI.png", AI),
            ("version/images/user.png", UserPage)   
        ]

        for index, (image_path, frame_class) in enumerate(button_data):
            image = ctk.CTkImage(light_image=Image.open(image_path),
                                 dark_image=Image.open(image_path),
                                 size=(40, 40))
            button = ctk.CTkButton(self, 
                                   image=image, 
                                   height=40, 
                                   width=70, 
                                   text="", 
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True, 
                                   command=lambda page=frame_class: master.switch_frame(page))
            button.place(relx=0.1 + index * 0.2, rely=0.95, anchor=ctk.CENTER)

class HomePage(BasePage):
    def __init__(self, master):
        super().__init__(master)
        logo = ctk.CTkImage(light_image=Image.open("version/images/light_logo.png"),
                            dark_image=Image.open("version/images/dark_logo.png"),
                            size=(275, 77))
        logo_label = ctk.CTkLabel(self, text="", image=logo)
        logo_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

class Chart(BasePage):
    def __init__(self, master):
        super().__init__(master)
        # Additional initialization for Chart can go here

class AI(BasePage):
    def __init__(self, master):
        super().__init__(master)
        # Additional initialization for AI can go here

class IconPage(BasePage):
    def __init__(self, master):
        super().__init__(master)

class UserPage(BasePage):
    def __init__(self, master):
        super().__init__(master)
        # Additional initialization for UserPage can go here

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()