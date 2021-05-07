from tkinter import *
from tkinter import ttk
from button import *

class main():
    def __init__(self,root) -> None:
        # Ventana principal
        self.mainFrame = ttk.Frame(root)
        self.mainFrame.grid(column=0,row=0, sticky=(N,W,E,S))
        root.columnconfigure(0,weight=1)
        root.rowconfigure(0,weight=1)
        # Lista de filas
        self.fillBoard()

    # Cambia de X a O y visceversa
    def play(self) -> str:
        if self.turn == "X":
            self.turn = "O"
            return "X"
        else:
            self.turn = "X"
            return "O"

    def fillBoard(self):
        self.turn = "X"
        self.rows = []
        for y in range(1,4):
            # lista de columnas
            row = []
            for x in range(1,4):
                row.append(pushBt(self.mainFrame,x,y,self))
            self.rows.append(row)

# Hacer el mainloop para la apliacion
root = Tk()
root.title("Totito apurado...")
main(root)
root.mainloop()