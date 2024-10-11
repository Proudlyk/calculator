import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")

        self.current_input = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 18),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == 'C':
            self.current_input = ""
            self.result_var.set(self.current_input)
        elif button == '=':
            try:
                self.current_input = str(eval(self.current_input))
                self.result_var.set(self.current_input)
            except Exception as e:
                self.result_var.set("Ошибка")
                self.current_input = ""
        else:
            self.current_input += button
            self.result_var.set(self.current_input)

if name == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
    