#Calculator as in class
from tkinter import *


class Calculator:


    def __init__(self) -> None:
        #shape of calculator
        self.root = Tk()
        self.root.title("Calculator")
        
        # entry value
        self.e = Entry(self.root, width=35, borderwidth=5)
        self.e.grid(row=0, column=0, columnspan=3, padx=10, pady=10,)

        #button values
        self.one = Button(self.root, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        self.one.grid(row=3, column=0)

        self.two = Button(self.root, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        self.two.grid(row=3, column=1)

        self.three = Button(self.root, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        self.three.grid(row=3, column=2)

        self.four = Button(self.root, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        self.four.grid(row=2, column=0)

        self.five = Button(self.root, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        self.five.grid(row=2, column=1)

        self.six = Button(self.root, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        self.six.grid(row=2, column=2)

        self.seven = Button(self.root, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        self.seven.grid(row=1, column=0)

        self.eigth = Button(self.root, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        self.eigth.grid(row=1, column=1)

        self.nine = Button(self.root, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        self.nine.grid(row=1, column=2)

        self.zero = Button(self.root, text="0", padx=40, pady=20, command=lambda: self.button_click(0))
        self.zero.grid(row=4, column=0)

        self.clear = Button(self.root, text="C", padx=82, pady=20, command=lambda: self.button_clear())
        self.clear.grid(row=4, column=1, columnspan=2)

        self.add_button = Button(self.root, text="+", padx=40, pady=20, command=lambda: self.button_add())
        self.add_button.grid(row=5, column=0) 

        

        self.button_equal = Button(self.root, text="=", padx=82, pady=20, command=lambda: self.button_equal_to())
        self.button_equal.grid(row=5, column=1, columnspan=2)



        #provide values

        self.root.mainloop()

    def button_click(self, number):
        current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, str(current) + str(number))

    def button_clear(self):
        self.e.delete(0, END)

    def button_add(self):
        first_num = self.e.get()
        global f_num
        f_num = int(first_num)
        self.e.delete(0, END)

    def button_equal_to(self):
        second_num = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, f_num + int(second_num))


    
if __name__ == "__main__":
    Calculator()
    
        