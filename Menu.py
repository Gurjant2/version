import customtkinter as ctk
from tkinter import ttk
from PIL import Image

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

class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        
        ctk.CTkFrame.__init__(self, master)
        logo = ctk.CTkImage(light_image=Image.open("images/light_logo.png"),
                    dark_image = Image.open("images/dark_logo.png"),
                    size = (275,77))
        logo_label = ctk.CTkLabel(self, text = "", image=logo)
        logo_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        Home = ctk.CTkImage(light_image=Image.open("images/home.png"),
                            dark_image = Image.open("images/home.png"),
                            size = (40,40))
        homeButton = ctk.CTkButton(self, 
                                   image=Home, 
                                   height=40, 
                                   width=70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command=lambda: master.switch_frame(HomePage))
        
        homeButton.place(relx=0.1, rely=0.95, anchor=ctk.CENTER)

        chart = ctk.CTkImage(light_image=Image.open("images/chart.png"),
                            dark_image = Image.open("images/chart.png"),
                            size = (40,40))
        chartButton = ctk.CTkButton(self, 
                                    image=chart, 
                                    height=40, 
                                    width=70, 
                                    text= "",
                                    fg_color="transparent", 
                                    bg_color="white", 
                                    hover=True,
                                    command=lambda: master.switch_frame(Chart))
        chartButton.place(relx=0.3, rely=0.95, anchor=ctk.CENTER)

        ai = ctk.CTkImage(light_image=Image.open("images/AI.png"),
                        dark_image = Image.open("images/AI.png"),
                        size = (40,40))
        aiButton = ctk.CTkButton(self, 
                                 image=ai, 
                                 height=40, 
                                 width=70, 
                                 text= "",
                                 fg_color="transparent",
                                 bg_color="white", 
                                 hover=True,
                                 command=lambda: master.switch_frame(AI))
        aiButton.place(relx=0.7, rely=0.95, anchor=ctk.CENTER)

        user = ctk.CTkImage(light_image=Image.open("images/user.png"),
                            dark_image = Image.open("images/user.png"),
                            size = (40,40))
        userButton = ctk.CTkButton(self, 
                                   image=user, 
                                   height=40, 
                                   width = 70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command= lambda: master.switch_frame(UserPage))
        userButton.place(relx=0.9, rely=0.95, anchor=ctk.CENTER)

        icon = ctk.CTkImage(light_image=Image.open("images/icon.png"),
                            dark_image = Image.open("images/icon.png"),
                            size = (40,40))
        iconButton = ctk.CTkButton(self, 
                                   image=icon, 
                                   height=40  , 
                                   width=70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command = lambda: master.switch_frame(IconPage))
        iconButton.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

class Chart(ctk.CTkFrame):
    def __init__(self, master):
        
        ctk.CTkFrame.__init__(self, master)

        Home = ctk.CTkImage(light_image=Image.open("images/home.png"),
                            dark_image = Image.open("images/home.png"),
                            size = (40,40))
        homeButton = ctk.CTkButton(self, 
                                   image=Home, 
                                   height=40, 
                                   width=70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command=lambda: master.switch_frame(HomePage))
        
        homeButton.place(relx=0.1, rely=0.95, anchor=ctk.CENTER)

        chart = ctk.CTkImage(light_image=Image.open("images/chart.png"),
                            dark_image = Image.open("images/chart.png"),
                            size = (40,40))
        chartButton = ctk.CTkButton(self, 
                                    image=chart, 
                                    height=40, 
                                    width=70, 
                                    text= "",
                                    fg_color="transparent", 
                                    bg_color="white", 
                                    hover=True,
                                    command=lambda: master.switch_frame(Chart))
        chartButton.place(relx=0.3, rely=0.95, anchor=ctk.CENTER)

        ai = ctk.CTkImage(light_image=Image.open("images/AI.png"),
                        dark_image = Image.open("images/AI.png"),
                        size = (40,40))
        aiButton = ctk.CTkButton(self, 
                                 image=ai, 
                                 height=40, 
                                 width=70, 
                                 text= "",
                                 fg_color="transparent",
                                 bg_color="white", 
                                 hover=True,
                                 command=lambda: master.switch_frame(AI))
        aiButton.place(relx=0.7, rely=0.95, anchor=ctk.CENTER)

        user = ctk.CTkImage(light_image=Image.open("images/user.png"),
                            dark_image = Image.open("images/user.png"),
                            size = (40,40))
        userButton = ctk.CTkButton(self, 
                                   image=user, 
                                   height=40, 
                                   width = 70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command= lambda: master.switch_frame(UserPage))
        userButton.place(relx=0.9, rely=0.95, anchor=ctk.CENTER)

        icon = ctk.CTkImage(light_image=Image.open("images/icon.png"),
                            dark_image = Image.open("images/icon.png"),
                            size = (40,40))
        iconButton = ctk.CTkButton(self, 
                                   image=icon, 
                                   height=40  , 
                                   width=70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command = lambda: master.switch_frame(IconPage))
        iconButton.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)



class AI(ctk.CTkFrame):
    def __init__(self, master):
        
        ctk.CTkFrame.__init__(self, master)

        Home = ctk.CTkImage(light_image=Image.open("images/home.png"),
                            dark_image = Image.open("images/home.png"),
                            size = (40,40))
        homeButton = ctk.CTkButton(self, 
                                   image=Home, 
                                   height=40, 
                                   width=70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command=lambda: master.switch_frame(HomePage))
        
        homeButton.place(relx=0.1, rely=0.95, anchor=ctk.CENTER)

        chart = ctk.CTkImage(light_image=Image.open("images/chart.png"),
                            dark_image = Image.open("images/chart.png"),
                            size = (40,40))
        chartButton = ctk.CTkButton(self, 
                                    image=chart, 
                                    height=40, 
                                    width=70, 
                                    text= "",
                                    fg_color="transparent", 
                                    bg_color="white", 
                                    hover=True,
                                    command=lambda: master.switch_frame(Chart))
        chartButton.place(relx=0.3, rely=0.95, anchor=ctk.CENTER)

        ai = ctk.CTkImage(light_image=Image.open("images/AI.png"),
                        dark_image = Image.open("images/AI.png"),
                        size = (40,40))
        aiButton = ctk.CTkButton(self, 
                                 image=ai, 
                                 height=40, 
                                 width=70, 
                                 text= "",
                                 fg_color="transparent",
                                 bg_color="white", 
                                 hover=True,
                                 command=lambda: master.switch_frame(AI))
        aiButton.place(relx=0.7, rely=0.95, anchor=ctk.CENTER)

        user = ctk.CTkImage(light_image=Image.open("images/user.png"),
                            dark_image = Image.open("images/user.png"),
                            size = (40,40))
        userButton = ctk.CTkButton(self, 
                                   image=user, 
                                   height=40, 
                                   width = 70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command= lambda: master.switch_frame(UserPage))
        userButton.place(relx=0.9, rely=0.95, anchor=ctk.CENTER)

        icon = ctk.CTkImage(light_image=Image.open("images/icon.png"),
                            dark_image = Image.open("images/icon.png"),
                            size = (40,40))
        iconButton = ctk.CTkButton(self, 
                                   image=icon, 
                                   height=40  , 
                                   width=70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command = lambda: master.switch_frame(IconPage))
        iconButton.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

class IconPage(ctk.CTkFrame):
    def __init__(self, master):
        
        ctk.CTkFrame.__init__(self, master)

        Home = ctk.CTkImage(light_image=Image.open("images/home.png"),
                            dark_image = Image.open("images/home.png"),
                            size = (40,40))
        homeButton = ctk.CTkButton(self, 
                                   image=Home, 
                                   height=40, 
                                   width=70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command=lambda: master.switch_frame(HomePage))
        
        homeButton.place(relx=0.1, rely=0.95, anchor=ctk.CENTER)

        chart = ctk.CTkImage(light_image=Image.open("images/chart.png"),
                            dark_image = Image.open("images/chart.png"),
                            size = (40,40))
        chartButton = ctk.CTkButton(self, 
                                    image=chart, 
                                    height=40, 
                                    width=70, 
                                    text= "",
                                    fg_color="transparent", 
                                    bg_color="white", 
                                    hover=True,
                                    command=lambda: master.switch_frame(Chart))
        chartButton.place(relx=0.3, rely=0.95, anchor=ctk.CENTER)

        ai = ctk.CTkImage(light_image=Image.open("images/AI.png"),
                        dark_image = Image.open("images/AI.png"),
                        size = (40,40))
        aiButton = ctk.CTkButton(self, 
                                 image=ai, 
                                 height=40, 
                                 width=70, 
                                 text= "",
                                 fg_color="transparent",
                                 bg_color="white", 
                                 hover=True,
                                 command=lambda: master.switch_frame(AI))
        aiButton.place(relx=0.7, rely=0.95, anchor=ctk.CENTER)

        user = ctk.CTkImage(light_image=Image.open("images/user.png"),
                            dark_image = Image.open("images/user.png"),
                            size = (40,40))
        userButton = ctk.CTkButton(self, 
                                   image=user, 
                                   height=40, 
                                   width = 70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command= lambda: master.switch_frame(UserPage))
        userButton.place(relx=0.9, rely=0.95, anchor=ctk.CENTER)

        icon = ctk.CTkImage(light_image=Image.open("images/icon.png"),
                            dark_image = Image.open("images/icon.png"),
                            size = (40,40))
        iconButton = ctk.CTkButton(self, 
                                   image=icon, 
                                   height=40  , 
                                   width=70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command = lambda: master.switch_frame(IconPage))
        iconButton.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)
        
        
class UserPage(ctk.CTkFrame):
    def __init__(self, master):
        
        ctk.CTkFrame.__init__(self, master)

        Home = ctk.CTkImage(light_image=Image.open("images/home.png"),
                            dark_image = Image.open("images/home.png"),
                            size = (40,40))
        homeButton = ctk.CTkButton(self, 
                                   image=Home, 
                                   height=40, 
                                   width=70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command=lambda: master.switch_frame(HomePage))
        
        homeButton.place(relx=0.1, rely=0.95, anchor=ctk.CENTER)

        chart = ctk.CTkImage(light_image=Image.open("images/chart.png"),
                            dark_image = Image.open("images/chart.png"),
                            size = (40,40))
        chartButton = ctk.CTkButton(self, 
                                    image=chart, 
                                    height=40, 
                                    width=70, 
                                    text= "",
                                    fg_color="transparent", 
                                    bg_color="white", 
                                    hover=True,
                                    command=lambda: master.switch_frame(Chart))
        chartButton.place(relx=0.3, rely=0.95, anchor=ctk.CENTER)

        ai = ctk.CTkImage(light_image=Image.open("images/AI.png"),
                        dark_image = Image.open("images/AI.png"),
                        size = (40,40))
        aiButton = ctk.CTkButton(self, 
                                 image=ai, 
                                 height=40, 
                                 width=70, 
                                 text= "",
                                 fg_color="transparent",
                                 bg_color="white", 
                                 hover=True,
                                 command=lambda: master.switch_frame(AI))
        aiButton.place(relx=0.7, rely=0.95, anchor=ctk.CENTER)

        user = ctk.CTkImage(light_image=Image.open("images/user.png"),
                            dark_image = Image.open("images/user.png"),
                            size = (40,40))
        userButton = ctk.CTkButton(self, 
                                   image=user, 
                                   height=40, 
                                   width = 70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command= lambda: master.switch_frame(UserPage))
        userButton.place(relx=0.9, rely=0.95, anchor=ctk.CENTER)

        icon = ctk.CTkImage(light_image=Image.open("images/icon.png"),
                            dark_image = Image.open("images/icon.png"),
                            size = (40,40))
        iconButton = ctk.CTkButton(self, 
                                   image=icon, 
                                   height=40  , 
                                   width=70, 
                                   text= "",
                                   fg_color="transparent", 
                                   bg_color="white", 
                                   hover=True,
                                   command = lambda: master.switch_frame(IconPage))
        iconButton.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()