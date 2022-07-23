import tkinter

class PopWindow:
    def __init__(self, main_window, y, x):
        self.main_window = main_window
        self.y = y
        self.x = x
        self.root = tkinter.Tk()
        self.root.title("Values")
        val = 1
        for y in range(3):
            for x in range(3):
                button = tkinter.Button(self.root, text = f"{val}", font = ("Arial", 15))
                button.configure(command = lambda btn = button: self.select(btn))   
                button.grid(row = y, column = x, padx = 5, pady = 5, sticky = "nsew")
                val += 1
        self.root.mainloop()    
    
    def select(self, btn):
        text = btn.cget("text")
        print(text)
        self.main_window.grid[self.y][self.x] = int(text)
        self.main_window.update()
        self.root.destroy()  
    
        