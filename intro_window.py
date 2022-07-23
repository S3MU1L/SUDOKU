import tkinter
from sudoku_window import SudokuWindow
from generate_sudoku import Generate

class IntroWindow:
    def __init__(self):
        self.root = tkinter.Tk()
        self.my_font = ("Helvetica", 20)
        self.my_bg = "#bff5e9"
        self.root.title("INTRO")
        self.root.configure(bg = self.my_bg)
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.label = tkinter.Label(self.root, text = "SELECT DIFFICULTY :", font = self.my_font, bg = self.my_bg)
        self.label.pack(padx = 5, pady = 5)
        self.easy_button = tkinter.Button(self.root, text = "Easy", width = 10, font = self.my_font, fg = "Green", command = self.generate)
        self.easy_button.pack(padx = 10, pady = 10)
        self.medium_button = tkinter.Button(self.root, text = "Medium", width = 10, font = self.my_font, fg = "Orange", command = self.generate)
        self.medium_button.pack(padx = 10, pady = 10)
        self.hard_button = tkinter.Button(self.root, text = "Hard", width = 10, font = self.my_font, fg = "Red", command = self.generate)
        self.hard_button.pack(padx = 10, pady = 10)
        self.root.mainloop()

    def generate(self):
        self.root.destroy()
        g = Generate()
        SudokuWindow(g.sudoku, g.solved, self)