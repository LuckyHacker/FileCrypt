from tkinter import *
from tkinter import filedialog
import algorithms
import tkinter.messagebox
import os

class MainWindow:

    def __init__(self):
        self.src_filepath = ""
        self.dst_filepath = ""
        self.secretkey = ""
        self.cipher_options = ["AES", "Crypt", "Blowfish"]
        self.method_options = ["Encrypt", "Decrypt"]
        self.init_ui()

    def init_ui(self):
        self.root = Tk()
        self.root.title("FileCrypt")
        self.root.geometry("300x480")

        # Choose cipher
        dropdownHeader1 = Label(self.root)
        dropdownHeader1.config(text="Choose cipher:", font=("Calibri", 9, "bold"))
        dropdownHeader1.pack()
        self.cipher = StringVar(self.root)
        self.cipher.set(self.cipher_options[0])
        w1 = OptionMenu(*(self.root, self.cipher) + tuple(self.cipher_options))
        w1.pack(ipadx=10, pady=10)

        # Choose method
        dropdownHeader2 = Label(self.root)
        dropdownHeader2.config(text="Choose method:", font=("Calibri", 9, "bold"))
        dropdownHeader2.pack()
        self.method = StringVar(self.root)
        self.method.set(self.method_options[0])
        w2 = OptionMenu(*(self.root, self.method) + tuple(self.method_options))
        w2.pack(ipadx=10, pady=10)

        # Open file
        browseHeader = Label(self.root)
        browseHeader.config(text="Choose file to encrypt/decrypt:", font=("Calibri", 9, "bold"))
        browseHeader.pack(pady=10)
        self.browsebutton = Button(self.root, text="Browse", command = lambda: self.BrowseOpen(self.src_pathlabel))
        self.browsebutton.pack(ipadx=10)
        self.src_pathlabel = Label(self.root)
        self.src_pathlabel.pack()

        # Save file
        browseHeader2 = Label(self.root)
        browseHeader2.config(text="Choose location to save:", font=("Calibri", 9, "bold"))
        browseHeader2.pack(pady=10)
        self.browsebutton2 = Button(self.root, text="Browse", command = lambda: self.BrowseSave(self.dst_pathlabel))
        self.browsebutton2.pack(ipadx=10)
        self.dst_pathlabel = Label(self.root)
        self.dst_pathlabel.pack()

        # Insert password
        passwd_label = Label(self.root)
        passwd_label.config(text="Enter secret key:", font=("Calibri", 9, "bold"))
        passwd_label.pack(pady=10)
        self.password_entry = Entry(self.root, show="*", width=15)
        self.password_entry.pack()

        self.delete_src = IntVar()
        if os.name == "posix":
            c = Checkbutton(self.root, text="Delete source file after operation?", variable=self.delete_src)
            c.pack()

        # Start
        self.startbutton = Button(self.root, text="Start!", command = self.start)
        self.startbutton.pack(ipadx=15, pady=10)

        # Status label
        self.status_label = Label(self.root)
        self.status_label.config(text="Status: idle")
        self.status_label.pack(pady=10)

        self.root.mainloop()

    def BrowseOpen(self, label):
        self.src_filepath = filedialog.askopenfilename()
        label.config(text=self.src_filepath)

    def BrowseSave(self, label):
        self.dst_filepath = filedialog.asksaveasfilename()
        label.config(text=self.dst_filepath)

    def status(self, s):
        self.status_label.config(text=s)


    def start(self):
        self.secretkey = self.password_entry.get()
        if len(self.secretkey) == 0:
            tkinter.messagebox.showinfo("Error", "Please enter a secret key.")
            return
        self.status("Status: processing")
        try:
            if self.cipher.get() == "AES":
                if self.method.get() == "Encrypt":
                    algorithms.AESCipher(self.secretkey, self.src_filepath, self.dst_filepath).encrypt()
                else:
                    algorithms.AESCipher(self.secretkey, self.src_filepath, self.dst_filepath).decrypt()

            elif self.cipher.get() == "Crypt":
                if self.method.get() == "Encrypt":
                    algorithms.CryptCipher(self.secretkey, self.src_filepath, self.dst_filepath).encrypt()
                else:
                    algorithms.CryptCipher(self.secretkey, self.src_filepath, self.dst_filepath).decrypt()

            elif self.cipher.get() == "Blowfish":
                if self.method.get() == "Encrypt":
                    algorithms.BlowfishCipher(self.secretkey, self.src_filepath, self.dst_filepath).encrypt()
                else:
                    algorithms.BlowfishCipher(self.secretkey, self.src_filepath, self.dst_filepath).decrypt()
        except FileNotFoundError:
            tkinter.messagebox.showinfo("Error", "Please choose a file to encrypt/decrypt and the saving location.")
            self.status("Status: idle")
            return

        if self.delete_src.get() == 1:
            os.system("shred --remove {}".format(self.src_filepath))

        self.status("Status: done")

if __name__ == "__main__":
    MainWindow()
