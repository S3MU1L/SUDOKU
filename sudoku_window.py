import tkinter
from tkinter import messagebox
from pop_window import PopWindow

class SudokuWindow:
    def __init__(self, grid, solved, main_class):
        self.grid = grid
        self.solved = solved
        self.main_class = main_class
        self.window = tkinter.Tk()
        self.truth_grid = [[True if x != 0 else False for x in row] for row in self.grid]
        self.highlight_color = "#a2cbfa"
        self.font = ("Comic Sans", 20)
        self.button_color = "#4fdb74"
        self.window.resizable(False, False)
        self.window.title("SUDOKU")
        self.canvas_width = 810
        self.canvas_height = 810
        self.font = ("Comic Sans", 20)
        self.tile_size = self.canvas_width//9
        self.canvas = tkinter.Canvas(self.window, width = self.canvas_width+2, height = self.canvas_height+2, bg = "white")
        self.canvas.grid(row = 0, column = 0, sticky = "nswe", padx = 5, pady = 5, columnspan =  3)
        self.solve_btn = tkinter.Button(self.window , text = "Solve", font = self.font,  bg = self.button_color, command = self.solve)
        self.solve_btn.grid(row = 1, column = 0, sticky = "nsew", padx = 100, pady = 20)
        self.check_btn = tkinter.Button(self.window, text = "Check", font = self.font, bg = self.button_color, command = self.check)
        self.check_btn.grid(row = 1, column = 1, sticky = "nsew", padx = 50, pady = 20)
        self.new_btn = tkinter.Button(self.window, text = "New Sudoku", font = self.font, bg = self.button_color, command = self.new)
        self.new_btn.grid(row = 1, column = 2, sticky = "nsew", padx = 50, pady = 20)
        self.time_label = tkinter.Button(self.window, text = "00:00:00",  font = self.font, fg = "black")
        self.time_label.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "nsew")
        self.canvas.bind('<Button-1>', self.click)
        self.running = True
        self.fill_grid()
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.tick()
        self.window.mainloop()
    
    def draw_grid(self):
        
        for y in range(2, self.canvas_height + 3, self.tile_size):
            if y % (3*self.tile_size) == 2:
                self.canvas.create_line(0, y, self.canvas_width + 2, y, fill = "black", width = 3)
            else:
                self.canvas.create_line(0, y, self.canvas_width + 2, y, fill = "black")
        
        for x in range(2, self.canvas_width + 3, self.tile_size):
            if x % (3*self.tile_size) == 2:
                self.canvas.create_line(x, 0, x, self.canvas_height + 2, fill = "black", width = 3)
            else:
                self.canvas.create_line(x, 0, x, self.canvas_height + 2, fill = "black")
                
                
    def fill_grid(self):
        self.draw_grid()
        for y in range(9):
            for x in range(9):
                if self.truth_grid[y][x]:
                    self.draw_text(y, x, "green")
                else:
                    self.draw_text(y, x, "black")
                
    def update(self):
        self.canvas.delete("all")
        self.draw_grid()
        self.fill_grid()

    def draw_text(self, y, x, color):
        y_pos = y * (self.tile_size + 1)
        x_pos = x * (self.tile_size + 1)
        txt = ""
        if self.grid[y][x] == 0:
            txt = ""
        else:
            txt = str(self.grid[y][x])
        self.canvas.create_text(x_pos + self.tile_size//2, y_pos + self.tile_size//2, text = txt, font = self.font, fill = color)
    
    
    def highlight(self, y0, x0):
        
        for x in range(9):
            self.canvas.create_rectangle(x * self.tile_size + 2, y0 * self.tile_size + 2, (x + 1)* self.tile_size + 2, (y0 + 1) * self.tile_size + 2, fill = self.highlight_color)
            self.draw_text(y0, x, "black")
        for y in range(9):
            self.canvas.create_rectangle(x0 * self.tile_size + 2, y * self.tile_size + 2, (x0 + 1) * self.tile_size + 2, (y + 1) * self.tile_size + 2, fill = self.highlight_color)
            self.draw_text(y, x0, "black")
        PopWindow(self, y0, x0)
        
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes = 1 
        if self.minutes >= 60:
            self.hours += 1
            self.minutes = 0
        
        hours_preffix =  "" if self.hours > 9 else "0"
        minutes_preffix = "" if self.minutes > 9 else "0"
        seconds_preffix = "" if self.seconds > 9 else "0"
        self.time_label.config(text = hours_preffix + str(self.hours) +  ":" + minutes_preffix + str(self.minutes) + ":" + seconds_preffix + str(self.seconds))
        if self.running:
            update_time = self.time_label.after(1000, self.tick)
                    
    def solve(self):
       self.grid = self.solved
       self.update()
    
    def check(self):
        wrong = 0
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] != self.solved[y][x]:
                    self.draw_text(y, x, "red")
                    wrong += 1
                else:
                    self.draw_text(y, x, "green")
        if wrong == 0:
            messagebox.showinfo(title = "Winning message", message = "          You have won !\n Click New Sudoku to play again.")           
    
    def click(self, event):
        y = event.y
        x = event.x
        y0 = y // 92
        x0 = x // 92
        if not self.truth_grid[y0][x0]:
            self.highlight(y0, x0)
        
    def new(self):
        self.window.destroy()
        self.main_class.__init__()
        self.running = False
        