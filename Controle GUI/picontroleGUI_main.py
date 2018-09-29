import tkinter
import picontroleGUI

def main():
    root = tkinter.Tk()
    app = picontroleGUI.Application(master=root)
    app.master.title("PIControle")
    app.master.minsize(745,420)
    icone = tkinter.PhotoImage(file = 'Imagens/icone.png')
    root.tk.call("wm","iconphoto",root._w,icone)
    root.geometry("700x420+0+0")
    app.master.resizable(False,False)
    app.mainloop()

if __name__ == '__main__':
    main()
