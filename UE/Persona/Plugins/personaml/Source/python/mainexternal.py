import subprocess
import sys
import importlib
import shutil
import os

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from api import *
win=Tk()
win.geometry("00x0")
win.title("Persona")
path = ""
goodname= "ML_Head.png"
pathout = Path('D:/Persona/Maya/Input')

def open_files():
   global path 
   path = filedialog.askopenfilename(title="Select a file")
   button.config(state=DISABLED)
   win.destroy()
button=ttk.Button(win, text="Select",command=open_files)
button.pack(pady=30)
open_files()
win.mainloop()
path = Path(path)
dirname = os.path.dirname(path)
newname = os.path.join(pathout, goodname)
shutil.copyfile(path, newname)

newname = Path(newname)
process_file(newname, pathout)
subprocess.call([r'D:\Persona\Maya\HBaker_v003.bat'])


 
