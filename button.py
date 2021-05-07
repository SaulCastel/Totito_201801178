from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class pushBt():
    def __init__(self,parent,x,y,main) -> None:
        self.main = main
        self.button = ttk.Button(parent,padding="30",command=self.push)
        self.button.grid(column=x,row=y,sticky=(N,W,E,S))
        self.pushed = False
        self.label = None

    # Presina el boton para cambiar su Label
    def push(self):
        if not self.pushed:
            self.pushed = True
            label = self.main.play()
            self.label = label
            self.button["text"] = label
            state = self.verify()
            if state == "X" or state == "O":
                messagebox.showinfo("Victoria",f"Las [{state}] han ganado")
                self.main.fillBoard()
            elif state == "draw":
                messagebox.showinfo("Empate",f"Nadie ha ganado...")
                self.main.fillBoard()

    # Verifica si ya se cumple la condicion de victoria
    def verify(self):
        # Validar filas
        for row in self.main.rows:
            rCount = 0
            check = row[0].label
            for bt in row:
                if bt.label == check:
                    rCount += 1
            if rCount == 3:
                return check
        # Validar columnas
        for i in range(3):
            cCount = 0
            check = self.main.rows[0][i].label
            for row in self.main.rows:
                if row[i].label == check:
                    cCount += 1
            if cCount == 3:
                return check
        # Validar diagonal izquierda
        check = self.main.rows[0][0].label
        dCount = 0
        for i in range(3):
            if self.main.rows[i][i].label == check:
                dCount += 1
        if dCount == 3:
            return check
        # Validar diagonal derecha
        check = self.main.rows[0][2].label
        dCount = 0
        for i in range(3):
            if self.main.rows[i][2-i].label == check:
                dCount += 1
        if dCount == 3:
            return check
        drawCount = 0
        for row in self.main.rows:
            for bt in row:
                if bt.label == None:
                    drawCount += 1
        if drawCount == 0:
            return "draw"
