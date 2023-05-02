import tkinter
from tkinter import *
from view.tabuleiro import Board
class ViewTelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Fly Flag")
        self.canvas = Canvas(root,width=3000,height=2600)
        self.canvas.pack()
        self.__nome = str
        self.canvas.config(bg="black")
        self.view_beginning()


    def view_beginning(self):
        play_online = Button(self.canvas ,text="Play online",command=self.get_popup)
        play_online.pack(padx=30,pady=30,anchor=CENTER)


        quit = Button(self.canvas, text="exit")
        quit.pack(padx= 30,pady=30,anchor=CENTER)


    def get_popup(self):
        popup = tkinter.Toplevel(self.root)
        label = tkinter.Label(popup, text="Digite seu nome")
        label.pack()
        input_entry = tkinter.Entry(popup)
        input_entry.pack()
        salvar = tkinter.Button(popup, text="salvar", command=self.abrir_tabuleiro)
        self.__nome = input_entry.get()
        salvar.pack()
        popup.wait_window(popup)
        self.abrir_tabuleiro()

    def abrir_tabuleiro(self):
        self.limpar_tela()
        Board(self.root)
        self.root.mainLoop()

    def limpar_tela(self):
        # destruir todos os widgets da janela
        for widget in self.root.winfo_children():
            widget.destroy()

