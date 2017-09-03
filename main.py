from tkinter import *
import algorithms

class MainWindow:

    def __init__(self):
        self.secretkey = ""
        self.src_filepath = ""
        self.dst_filepath = ""
        self.init_ui()

    def init_ui(self):
        self.root = Tk()
        self.root.geometry('400x600+350+70')
        self.button = Button(self.root, text = 'Press me', command = self.Call)
        self.button.pack()
        self.root.mainloop()

    def Call(self):
        lab = Label(self.root, text = 'You pressed\nthe button')
        lab.pack()
        self.button['bg'] = 'blue'
        self.button['fg'] = 'white'

if __name__ == "__main__":
    MainWindow()
