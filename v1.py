#---------------------------------
# Random Resource Web ©
# Randomresourceweb.blogspot.com
#---------------------------------

import tkinter as tk
import webbrowser

root = tk.Tk()

new = 1
url = "https://www.google.com"

def openweb():
    webbrowser.open(url,new=new)

Btn = tk.Button(root, text = "This opens Google",command=openweb)
Btn.pack()

root.mainloop()