import tkinter as tk
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("380x500")
        self.root.configure(bg="#b0b0b0")
        self.root.resizable(False, False)

        # Display Entry
        self.entry = tk.Entry(
            root, 
            font=("Arial", 20), 
            relief=tk.SUNKEN, 
            bd=3, 
            justify="right"
        )
        self.entry.pack(pady=15, padx=20, fill="x")

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#b0b0b0")
        btn_frame.pack(padx=10, pady=5, fill="both", expand=True)

        # Button Layout Grid
        buttons = [
            ('√', 0, 0), ('x²', 0, 1), ('%', 0, 2), ('±', 0, 3), ('⌫', 0, 4),
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('log', 1, 3), ('π', 1, 4),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('÷', 2, 3), ('(', 2, 4),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('×', 3, 3), (')', 3, 4),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('^', 4, 4),
            ('0', 5, 0), ('.', 5, 1), ('+', 5, 2)
        ]

        btn_bg = "#8c8c8c"
        btn_fg = "black"
        font_style = ("Arial", 12, "bold")

        for (text, row, col) in buttons:
            action = lambda x=text: self.on_button_click(x)
            tk.Button(
                btn_frame, text=text, width=4, height=2,
                font=font_style, bg=btn_bg, fg=btn_fg, relief=tk.RAISED,
                command=action
            ).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        # Bottom Buttons (CLEAR & =)
        tk.Button(
            btn_frame, text="CLEAR", font=font_style, bg=btn_bg, fg=btn_fg,
            relief=tk.RAISED, command=self.clear
        ).grid(row=6, column=0, columnspan=3, sticky="nsew", padx=2, pady=2)

        tk.Button(
            btn_frame, text="=", font=font_style, bg=btn_bg, fg=btn_fg,
            relief=tk.RAISED, command=self.calculate
        ).grid(row=5, column=3, rowspan=2, columnspan=2, sticky="nsew", padx=2, pady=2)

        # Configure Grid Rows and Columns
        for i in range(5):
            btn_frame.columnconfigure(i, weight=1)
        for i in range(7):
            btn_frame.rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == '⌫':
            self.entry.delete(len(self.entry.get()) - 1, tk.END)
        elif char == '±':
            current = self.entry.get()
            if current and current[0] == '-':
                self.entry.delete(0, 1)
            else:
                self.entry.insert(0, '-')
        elif char == 'x²':
            self.entry.insert(tk.END, '**2')
        elif char == '^':
            self.entry.insert(tk.END, '**')
        elif char == '√':
            self.entry.insert(tk.END, 'math.sqrt(')
        elif char == 'sin':
            self.entry.insert(tk.END, 'math.sin(math.radians(')
        elif char == 'cos':
            self.entry.insert(tk.END, 'math.cos(math.radians(')
        elif char == 'tan':
            self.entry.insert(tk.END, 'math.tan(math.radians(')
        elif char == 'log':
            self.entry.insert(tk.END, 'math.log10(')
        elif char == 'π':
            self.entry.insert(tk.END, str(math.pi))
        elif char == '÷':
            self.entry.insert(tk.END, '/')
        elif char == '×':
            self.entry.insert(tk.END, '*')
        elif char == '%':
            self.entry.insert(tk.END, '/100')
        else:
            self.entry.insert(tk.END, char)

    def clear(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression, {"math": math})
            self.clear()
            self.entry.insert(tk.END, str(result))
        except Exception:
            self.clear()
            self.entry.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()