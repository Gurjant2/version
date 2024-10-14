import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Go to Page One",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Go to Page Two",
                  command=lambda: master.switch_frame(PageTwo)).pack()
        tk.Button(self, text="Go to Page Three",
                  command=lambda: master.switch_frame(PageThree)).pack()
        tk.Button(self, text="Go to Page Four",
                  command=lambda: master.switch_frame(PageFour)).pack()

class PageOne(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Go to Start Page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="Go to Page Two",
                  command=lambda: master.switch_frame(PageTwo)).pack()
        tk.Button(self, text="Go to Page Three",
                  command=lambda: master.switch_frame(PageThree)).pack()
        tk.Button(self, text="Go to Page Four",
                  command=lambda: master.switch_frame(PageFour)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Go to Start Page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="Go to Page One",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Go to Page Three",
                  command=lambda: master.switch_frame(PageThree)).pack()
        tk.Button(self, text="Go to Page Four",
                  command=lambda: master.switch_frame(PageFour)).pack()

class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page three").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Go to Start Page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="Go to Page One",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Go to Page Two",
                  command=lambda: master.switch_frame(PageTwo)).pack()
        tk.Button(self, text="Go to Page Four",
                  command=lambda: master.switch_frame(PageFour)).pack()

class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page four").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Go to Start Page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="Go to Page One",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Go to Page Two",
                  command=lambda: master.switch_frame(PageTwo)).pack()
        tk.Button(self, text="Go to Page Three",
                  command=lambda: master.switch_frame(PageThree)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()