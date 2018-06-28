
from tkinter.filedialog import askopenfilenames

from tkinter import *
#root = Tk()

#root.iconbitmap(r'C:\Users\aailyin\Documents\dev\converter\assets\favicon.ico')
#Button(root, text = '1').place(x = 10, y = 10, width = 30)
#root.mainloop() # we don't want a full GUI, so keep the root window from appearing
#filename = askopenfilenames() # show an "Open" dialog box and return the path to the selected file
#print(filename)


#root.


from tkinter import *

class GUI(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid()

        self.fnameLabel = Label(master, text="First Name")
        self.fnameLabel.grid()

        self.fnameEntry = StringVar()
        self.fnameEntry = Entry(textvariable=self.fnameEntry)
        self.fnameEntry.grid()

        self.lnameLabel = Label(master, text="Last Name")
        self.lnameLabel.grid()

        self.lnameEntry = StringVar()
        self.lnameEntry = Entry(textvariable=self.lnameEntry)
        self.lnameEntry.grid()

        def buttonClick():
            print("You pressed Submit!")
            print(self.fnameEntry.get() + " " + self.lnameEntry.get() +",you clicked the button!")

        self.submitButton = Button(master, text="Submit", command=buttonClick)
        self.submitButton.grid()

if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()