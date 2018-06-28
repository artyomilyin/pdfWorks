
from tkinter.filedialog import askopenfilenames

from tkinter import *
root = Tk()

root.iconbitmap(r'C:\Users\aailyin\Documents\dev\converter\assets\favicon.ico')

root.withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilenames() # show an "Open" dialog box and return the path to the selected file
print(filename)