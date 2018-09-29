import os
import _thread
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import serial
import conversor

class Application(Frame):

    def combobox_handler(self,event):
        self.porta = self.porta_cb.get()
        self.baud = (int)(self.baud_cb.get())

    def Campos_Vazios(self):
        if(self.direita_entry.get() == "" or self.esquerda_entry.get() == "" or self.cima_entry.get() == "" or self.baixo_entry.get() == "" or self.acao1_entry.get() == "" or self.acao2_entry.get() == "" or self.acao3_entry.get() == "" or self.acao4_entry.get() == "" or self.start_entry.get() == "" or self.back_entry.get() == "" or self.gatilhoe_entry.get() == "" or self.gatilhod_entry.get() == "" or self.bumpere_entry.get() == "" or self.bumperd_entry.get() == ""):
            return True
        return False

    def Abrir_Serial(self):
        if(not self.Campos_Vazios()):
            try:
                self.ser = serial.Serial(self.porta, self.baud, timeout=None)
                self.serial_aberta = True
                self.Atribuir_Atalhos()
                self.abrir.lower(self.frame)
                self.fechar.lift(self.frame)
                self.info_label["text"] = str("Lendo a porta " + self.porta + " a " + str(self.baud) + " bps.")
                try:
                    _thread.start_new_thread(self.Ler_Porta,())
                except:
                    pass
            except:
                if(not self.ser.is_open):
                    self.info_label["text"] = str("Não foi possível abrir a porta " + self.porta + ".")
        else:
            self.info_label["text"] = str("INFORME TODOS OS ATALHOS, POR FAVOR!")

    def Fechar_Serial(self):
        self.ser.close()
        self.serial_aberta = False
        self.fechar.lower(self.frame)
        self.abrir.lift(self.frame)
        self.info_label["text"] = ""

    def Atribuir_Atalhos(self):
        self.direita = self.direita_entry.get()
        self.esquerda = self.esquerda_entry.get()
        self.cima = self.cima_entry.get()
        self.baixo = self.baixo_entry.get()
        self.acao1 = self.acao1_entry.get()
        self.acao2 = self.acao2_entry.get()
        self.acao3 = self.acao3_entry.get()
        self.acao4 = self.acao4_entry.get()
        self.start = self.start_entry.get()
        self.back = self.back_entry.get()
        self.gatilhod = self.gatilhod_entry.get()
        self.gatilhoe = self.gatilhoe_entry.get()
        self.bumperd = self.bumperd_entry.get()
        self.bumpere = self.bumpere_entry.get()

    def Ler_Porta(self):
        try:
            while(self.serial_aberta == True):
                bytesToRead = self.ser.inWaiting()
                c = self.ser.read(bytesToRead)
                
                if(c == b'a'):
                    conversor.pressKey(conversor.teclas[self.esquerda][0],conversor.teclas[self.esquerda][1])
                if(c == b'A'):
                    conversor.releaseKey(conversor.teclas[self.esquerda][0],conversor.teclas[self.esquerda][1])
                if(c == b'd'):
                    conversor.pressKey(conversor.teclas[self.direita][0],conversor.teclas[self.direita][1])
                if(c == b'D'):
                    conversor.releaseKey(conversor.teclas[self.direita][0],conversor.teclas[self.direita][1])
                if(c == b'w'):
                    conversor.pressKey(conversor.teclas[self.cima][0],conversor.teclas[self.cima][1])
                if(c == b'W'):
                    conversor.releaseKey(conversor.teclas[self.cima][0],conversor.teclas[self.cima][1])
                if(c == b's'):
                    conversor.pressKey(conversor.teclas[self.baixo][0],conversor.teclas[self.baixo][1])
                if(c == b'S'):
                    conversor.releaseKey(conversor.teclas[self.baixo][0],conversor.teclas[self.baixo][1])
                if(c == b'u'):
                    conversor.pressKey(conversor.teclas[self.acao1][0],conversor.teclas[self.acao1][1])
                if(c == b'U'):
                    conversor.releaseKey(conversor.teclas[self.acao1][0],conversor.teclas[self.acao1][1])
                if(c == b'k'):
                    conversor.pressKey(conversor.teclas[self.acao2][0],conversor.teclas[self.acao2][1])
                if(c == b'K'):
                    conversor.releaseKey(conversor.teclas[self.acao2][0],conversor.teclas[self.acao2][1])
                if(c == b'j'):
                    conversor.pressKey(conversor.teclas[self.acao3][0],conversor.teclas[self.acao3][1])
                if(c == b'J'):
                    conversor.releaseKey(conversor.teclas[self.acao3][0],conversor.teclas[self.acao3][1])
                if(c == b'h'):
                    conversor.pressKey(conversor.teclas[self.acao4][0],conversor.teclas[self.acao4][1])
                if(c == b'H'):
                    conversor.releaseKey(conversor.teclas[self.acao4][0],conversor.teclas[self.acao4][1])
                if(c == b'v'):
                    conversor.pressKey(conversor.teclas[self.gatilhod][0],conversor.teclas[self.gatilhod][1])
                if(c == b'V'):
                    conversor.releaseKey(conversor.teclas[self.gatilhod][0],conversor.teclas[self.gatilhod][1])
                if(c == b'z'):
                    conversor.pressKey(conversor.teclas[self.gatilhoe][0],conversor.teclas[self.gatilhoe][1])
                if(c == b'Z'):
                    conversor.releaseKey(conversor.teclas[self.gatilhoe][0],conversor.teclas[self.gatilhoe][1])
                if(c == b'c'):
                    conversor.pressKey(conversor.teclas[self.bumperd][0],conversor.teclas[self.bumperd][1])
                if(c == b'C'):
                    conversor.releaseKey(conversor.teclas[self.bumperd][0],conversor.teclas[self.bumperd][1])
                if(c == b'x'):
                    conversor.pressKey(conversor.teclas[self.bumpere][0],conversor.teclas[self.bumpere][1])
                if(c == b'X'):
                    conversor.releaseKey(conversor.teclas[self.bumpere][0],conversor.teclas[self.bumpere][1])
                if(c == b'p'):
                    conversor.pressKey(conversor.teclas[self.start][0],conversor.teclas[self.start][1])
                    conversor.releaseKey(conversor.teclas[self.start][0],conversor.teclas[self.start][1])
                if(c == b'b'):
                    conversor.pressKey(conversor.teclas[self.back][0],conversor.teclas[self.back][1])
                    conversor.releaseKey(conversor.teclas[self.back][0],conversor.teclas[self.back][1])
        except:
            pass

    def createWidgets(self):
        self.ser = serial.Serial()
        bg = "#006666"
        self.MainFrame = tkinter.Frame(self)
        self.MainFrame.pack(side = "top", fill = "both", expand = "true")
        self.MainFrame.configure(background = "#2a2a2a")
        self.frame = tkinter.Canvas(self,width = 700,height = 380)
        self.frame["relief"] = RIDGE
        self.frame["borderwidth"] = 10
        self.frame["background"] = bg
        self.file = tkinter.PhotoImage(file = "Imagens/controle.png")
        self.frame.create_image(10,10,image = self.file,anchor = NW)
        self.frame.grid(in_ = self.MainFrame,padx = 10,pady = 10)
        frame_id = self.frame.create_window(0,0,anchor = NW)

        self.porta = "COM3"
        self.baud = 9600
        self.serial_aberto = False

        self.portaLabel = ttk.Label(self.frame,text = "PORTA COM: ")
        self.frame.itemconfigure(frame_id,window = self.portaLabel)
        self.portaLabel.place(in_ = self.frame,x = 30, y = 320)
        self.portaLabel.configure(background = bg, foreground = "#ffffff")

        self.porta_cb = ttk.Combobox(self.frame)
        self.porta_cb["values"] = ["COM3","COM5","COM6","COM12"]
        self.porta_cb.current(0)
        self.porta_cb["width"] = 15
        self.frame.itemconfigure(frame_id,window = self.porta_cb)
        self.porta_cb.place(in_ = self.frame,x = 17, y = 350)
        self.porta_cb.bind('<<ComboboxSelected>>',self.combobox_handler)

        self.baudLabel = ttk.Label(self.frame,text = "BAUD RATE: ")
        self.frame.itemconfigure(frame_id,window = self.baudLabel)
        self.baudLabel.place(in_ = self.frame,x = 235, y = 320)
        self.baudLabel.configure(background = bg, foreground = "#ffffff")

        self.baud_cb = ttk.Combobox(self.frame)
        self.baud_cb["values"] = ["1200","9600","19200","38400", "57600", "115200"]
        self.baud_cb.current(1)
        self.baud_cb["width"] = 15
        self.frame.itemconfigure(frame_id,window = self.baud_cb)
        self.baud_cb.place(in_ = self.frame,x = 217, y = 350)
        self.baud_cb.bind('<<ComboboxSelected>>',self.combobox_handler)

        self.abrir = tkinter.Button(self)
        self.frame.itemconfigure(frame_id, window=self.abrir)
        self.abrir["text"] = "ABRIR"
        self.abrir.place(in_ = self.MainFrame, x = 400, y = 356)
        self.abrir["cursor"] = "hand1"
        self.abrir["command"] = lambda: self.Abrir_Serial()

        self.fechar = tkinter.Button(self)
        self.frame.itemconfigure(frame_id, window=self.fechar)
        self.fechar["text"] = "FECHAR"
        self.fechar.place(in_ = self.MainFrame, x = 400, y = 356)
        self.fechar["cursor"] = "hand1"
        self.fechar["command"] = lambda: self.Fechar_Serial()
        self.fechar.lower(self.frame)

        self.info_label = ttk.Label(self,text = "")
        self.frame.itemconfigure(frame_id,window = self.info_label)
        self.info_label.place(in_ = self.MainFrame,x = 460, y = 357)
        self.info_label.configure(background = bg, foreground = "#ffffff")

        self.direita = "right"
        self.esquerda = "left"
        self.cima = "up"
        self.baixo = "down"
        self.acao1 = "q"
        self.acao2 = "j"
        self.acao3 = "space"
        self.acao4 = "l"
        self.start = "enter"
        self.back = "esc"
        self.gatilhod = "v"
        self.gatilhoe = "z"
        self.bumperd = "c"
        self.bumpere = "x"

        self.direita_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.direita_entry)
        self.direita_entry["width"] = 5
        self.direita_entry["justify"] = "center"
        self.direita_entry.insert(0,"right")
        self.direita_entry.place(in_ = self.frame,x = 60, y = 190)

        self.esquerda_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.esquerda_entry)
        self.esquerda_entry["width"] = 5
        self.esquerda_entry["justify"] = "center"
        self.esquerda_entry.insert(0,"left")
        self.esquerda_entry.place(in_ = self.frame,x = 60, y = 165)

        self.cima_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.cima_entry)
        self.cima_entry["width"] = 5
        self.cima_entry["justify"] = "center"
        self.cima_entry.insert(0,"up")
        self.cima_entry.place(in_ = self.frame,x = 60, y = 125)

        self.baixo_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.baixo_entry)
        self.baixo_entry["width"] = 5
        self.baixo_entry["justify"] = "center"
        self.baixo_entry.insert(0,"down")
        self.baixo_entry.place(in_ = self.frame,x = 60, y = 215)

        self.acao1_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.acao1_entry)
        self.acao1_entry["width"] = 5
        self.acao1_entry["justify"] = "center"
        self.acao1_entry.insert(0,"q")
        self.acao1_entry.place(in_ = self.frame,x = 600, y = 125)

        self.acao2_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.acao2_entry)
        self.acao2_entry["width"] = 5
        self.acao2_entry["justify"] = "center"
        self.acao2_entry.insert(0,"j")
        self.acao2_entry.place(in_ = self.frame,x = 600, y = 160)

        self.acao3_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.acao3_entry)
        self.acao3_entry["width"] = 5
        self.acao3_entry["justify"] = "center"
        self.acao3_entry.insert(0,"space")
        self.acao3_entry.place(in_ = self.frame,x = 600, y = 210)

        self.acao4_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.acao4_entry)
        self.acao4_entry["width"] = 5
        self.acao4_entry["justify"] = "center"
        self.acao4_entry.insert(0,"l")
        self.acao4_entry.place(in_ = self.frame,x = 600, y = 185)

        self.start_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.start_entry)
        self.start_entry["width"] = 5
        self.start_entry["justify"] = "center"
        self.start_entry.insert(0,"enter")
        self.start_entry.place(in_ = self.frame,x = 385, y = 30)

        self.back_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.back_entry)
        self.back_entry["width"] = 5
        self.back_entry["justify"] = "center"
        self.back_entry.insert(0,"esc")
        self.back_entry.place(in_ = self.frame,x = 285, y = 30)

        self.gatilhoe_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.gatilhoe_entry)
        self.gatilhoe_entry["width"] = 5
        self.gatilhoe_entry["justify"] = "center"
        self.gatilhoe_entry.insert(0,"z")
        self.gatilhoe_entry.place(in_ = self.frame,x = 60, y = 30)

        self.bumpere_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.bumpere_entry)
        self.bumpere_entry["width"] = 5
        self.bumpere_entry["justify"] = "center"
        self.bumpere_entry.insert(0,"x")
        self.bumpere_entry.place(in_ = self.frame,x = 60, y = 60)

        self.gatilhod_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.gatilhod_entry)
        self.gatilhod_entry["width"] = 5
        self.gatilhod_entry["justify"] = "center"
        self.gatilhod_entry.insert(0,"v")
        self.gatilhod_entry.place(in_ = self.frame,x = 600, y = 30)

        self.bumperd_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.bumperd_entry)
        self.bumperd_entry["width"] = 5
        self.bumperd_entry["justify"] = "center"
        self.bumperd_entry.insert(0,"c")
        self.bumperd_entry.place(in_ = self.frame,x = 600, y = 60)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.createWidgets()
