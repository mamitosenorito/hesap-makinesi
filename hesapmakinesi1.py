import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_700=tk.Button(root)
        GButton_700["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_700["font"] = ft
        GButton_700["fg"] = "#000000"
        GButton_700["justify"] = "center"
        GButton_700["text"] = "topla"
        GButton_700.place(x=20,y=190,width=70,height=25)
        GButton_700["command"] = self.GButton_700_command

        GButton_140=tk.Button(root)
        GButton_140["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_140["font"] = ft
        GButton_140["fg"] = "#000000"
        GButton_140["justify"] = "center"
        GButton_140["text"] = "çıkart"
        GButton_140.place(x=100,y=190,width=70,height=25)
        GButton_140["command"] = self.GButton_140_command

        GButton_107=tk.Button(root)
        GButton_107["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_107["font"] = ft
        GButton_107["fg"] = "#000000"
        GButton_107["justify"] = "center"
        GButton_107["text"] = "çarp"
        GButton_107.place(x=180,y=190,width=70,height=25)
        GButton_107["command"] = self.GButton_107_command

        GButton_147=tk.Button(root)
        GButton_147["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_147["font"] = ft
        GButton_147["fg"] = "#000000"
        GButton_147["justify"] = "center"
        GButton_147["text"] = "böl"
        GButton_147.place(x=260,y=190,width=70,height=25)
        GButton_147["command"] = self.GButton_147_command

        GLabel_32=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_32["font"] = ft
        GLabel_32["fg"] = "#333333"
        GLabel_32["justify"] = "center"
        GLabel_32["text"] = "rakam 1"
        GLabel_32.place(x=70,y=80,width=70,height=25)

        GLabel_125=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_125["font"] = ft
        GLabel_125["fg"] = "#333333"
        GLabel_125["justify"] = "center"
        GLabel_125["text"] = "rakam 2"
        GLabel_125.place(x=200,y=80,width=70,height=25)

        GLabel_580=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_580["font"] = ft
        GLabel_580["fg"] = "#333333"
        GLabel_580["justify"] = "center"
        GLabel_580["text"] = "sonuc"
        GLabel_580.place(x=360,y=80,width=70,height=25)

        GLineEdit_411=tk.Entry(root)
        GLineEdit_411["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_411["font"] = ft
        GLineEdit_411["fg"] = "#333333"
        GLineEdit_411["justify"] = "center"
        GLineEdit_411["text"] = "Entry"
        GLineEdit_411.place(x=70,y=120,width=70,height=25)

        GLineEdit_44=tk.Entry(root)
        GLineEdit_44["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_44["font"] = ft
        GLineEdit_44["fg"] = "#333333"
        GLineEdit_44["justify"] = "center"
        GLineEdit_44["text"] = "Entry"
        GLineEdit_44.place(x=200,y=120,width=70,height=25)

        GLineEdit_396=tk.Entry(root)
        GLineEdit_396["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_396["font"] = ft
        GLineEdit_396["fg"] = "#333333"
        GLineEdit_396["justify"] = "center"
        GLineEdit_396["text"] = "Entry"
        GLineEdit_396.place(x=360,y=120,width=70,height=25)

    def GButton_700_command(self):
        print("toplandı")


    def GButton_140_command(self):
        print("çıkarıldı")


    def GButton_107_command(self):
        print("çarpıldı")


    def GButton_147_command(self):
        print("bölündü")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()