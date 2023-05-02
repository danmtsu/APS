import tkinter as tk
from view.tabuleiro import Board

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="white")
    app = Board(root)
    #app.bind('<Button-1> ',app.handle_click)
    root.mainloop()