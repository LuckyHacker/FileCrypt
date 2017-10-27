from tkinter import *
from tkinter import filedialog
import algorithms

class MainWindow:

    def __init__(self):
        self.secretkey = ""
        self.src_filepath = ""
        self.dst_filepath = ""
        self.init_ui()

    def init_ui(self):
        self.root = Tk()
        self.root.title("ACB crypting machine")
        self.root.geometry("600x400+350+70")
        #self.button = Button(self.root, text = 'Press me', command = self.Call)
        #self.button.pack()

        #DROPDOWN MENU
        dropdownHeader = Label(self.root)
        dropdownHeader.config(text="Please choose a cipher:")
        dropdownHeader.pack()

        #JUST A TEXT BOX REMINDER
        #text = Text(self.root, height=1, width=23)
        #text.pack()
        #text.insert(END, "Please choose a cipher:")
        #text.config(state=DISABLED)

        Options = ["AES", "Crypt", "Blowfish"]
        variable = StringVar(self.root)
        variable.set(Options[0])
        w = OptionMenu(*(self.root, variable) + tuple(Options))
        w.pack(ipadx=10, pady=10)

        #CHECKBOXES
        checkboxHeader = Label(self.root)
        checkboxHeader.config(text="Do you want to decrypt, encrypt or both?")
        checkboxHeader.pack()
        enc = IntVar(self.root)
        radioEnc = Radiobutton(self.root, text="Encrypt", variable=enc)
        radioEnc.pack()
        dec = IntVar(self.root)
        radioDec = Radiobutton(self.root, text="Decrypt", variable=dec)
        radioDec.deselect()
        radioDec.pack()

        #BROWSE BUTTON
        browseHeader = Label(self.root)
        browseHeader.config(text="Choose file to encrypt/decrypt:")
        browseHeader.pack(pady=10)
        self.browsebutton = Button(self.root, text="Browse", command=self.Browsefunc)
        self.browsebutton.pack(ipadx=10)

        self.root.mainloop()

    def Browsefunc(self):
        pathHeader = Label(self.root)
        pathHeader.config(text="Chosen file:")
        pathHeader.pack()
        #FILE PATH
        filename = filedialog.askopenfilename()
        self.pathlabel = Label(self.root)
        self.pathlabel.config(text=filename)
        self.pathlabel.pack()

        #START BUTTON
        self.startbutton = Button(self.root, text="Start!")
        self.startbutton.pack(ipadx=15, pady=10)

    def Call(self):
        lab = Label(self.root, text = 'You pressed\nthe button')
        lab.pack()
        self.button['bg'] = 'blue'
        self.button['fg'] = 'white'

if __name__ == "__main__":
    MainWindow()
