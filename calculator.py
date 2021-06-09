import tkinter as tk
from functools import partial


class Calculator:
    
    # Desc: a function to initialize the class
    # Arg: the string variable
    # Return : initialized string variable
    def __init__(self, string):
        self.string = ''

    # Desc: a function to show numbers in the calculator 
    # Arg: the numbr or operation that user has clicked
    # Return : show the umber or operation that user has clicked in the calculator
    def show_number(self,e):
        label = tk.Label(self.shownum, text= '                                       ')
        label.place(x=160, y=17)
        label = tk.Label(self.shownum, text= e)
        label.place(x=160, y=17)


    # Desc: a function to add the numbr or operation that user has clicked to a string
    # Arg: the numbr or operation that user has clicked
    # Return : shows the result string in the calculator 
    def add(self,e):
        self.string += e
        self.show_number(self.string)

    # Desc: a function to calculate the string when user wants to see the result
    # Arg: None (string is taken from class by self)
    # Return : shows the calculated string in the calculator 
    def calculate(self):
        self.string = str(eval(self.string))
        self.show_number(self.string)
    
    # Desc: a function to clear one number from the end of string
    # Arg: None (string is taken from class by self)
    # Return : shows the result string in the calculator
    def clearone(self):
        self.string = self.string[:len(self.string)-1]
        if(len(self.string) > 1 and (self.string[len(self.string)-1] == '+' or self.string[len(self.string)-1] == '/' or string[len(string)-1] == '%' 
           or self.string[len(self.string)-1] == '-' or self.string[len(self.string)-1] == '*')):
            self.string = self.string[:len(self.string)-1]

        self.show_number(self.string)
    
    # Desc: a function to clear the whole string
    # Arg: None (string is taken from class by self)
    # Return : an empty label in calculator
    def clear(self):
        self.show_number('                                       ')
        self.string = ''
    
    # Desc: a function to create GUI
    # Arg: None 
    # Return : creates a GUI
    def create_gui(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=600, width=550, bg='#ffcc5c')
        self.canvas.pack()
        self.frame = tk.Frame(self.root, bg='#651e3e')
        self.frame.place(relwidth=0.85, relheight=0.7, relx=0.05, rely=0.2)

        self.shownum = tk.Frame(self.root, bg='#651e3e')
        self.shownum.place(relwidth=0.85, relheight=0.1, relx=0.05, rely=0.05)

        a = 240
        b = 100
        for i in range(10)[::-1]:
            if(i < 9 and i%3 == 0):
                b += 70
                a = 240
            if(i==0):
                a=140
            s = 'but'+str(i)
            s = tk.Button(self.frame, text=i, padx=25, pady=15, fg='black', bg='#fff4e6', command=partial(self.add, str(i)))
            s.place(x=a, y=b)
            a -= 100
        plus = tk.Button(self.frame, text='+', padx=25, pady=15, fg='black', bg='#fff4e6', command=partial(self.add, '+'))
        plus.place(x=40, y=310)
        mines = tk.Button(self.frame, text='-', padx=25, pady=15, fg='black', bg='#fff4e6', command=partial(self.add, '-'))
        mines.place(x=340, y=240)
        multi = tk.Button(self.frame, text='x', padx=25, pady=15, fg='black', bg='#fff4e6', command=partial(self.add, '*'))
        multi.place(x=340, y=170)
        div = tk.Button(self.frame, text='/', padx=25, pady=15, fg='black', bg='#fff4e6', command=partial(self.add, '/'))
        div.place(x=340, y=100)
        dot = tk.Button(self.frame, text='.', padx=25, pady=15, fg='black', bg='#fff4e6', command=partial(self.add, '.'))
        dot.place(x=240, y=310)
        Modu = tk.Button(self.frame, text='%', padx=25, pady=15, fg='black', bg='#fff4e6', command=partial(self.add, '%'))
        Modu.place(x=140, y=30)
        clr = tk.Button(self.frame, text='C', padx=25, pady=15, fg='black', bg='#fff4e6', command=self.clear)
        clr.place(x=40, y=30)
        cone = tk.Button(self.frame, text='<=', padx=68, pady=15, fg='black', bg='#fff4e6', command=self.clearone)
        cone.place(x=240, y=30)
        run = tk.Button(self.frame, text='=', padx=25, pady=15, fg='black', bg='#88d8b0', command=self.calculate)
        run.place(x=340, y=310)

        self.root.mainloop()

    # Desc: main function
    # Arg: None
    # Return : returns GUI and whole functionalities of it
    def main(self):
        self.create_gui()

if __name__ == '__main__': 
    calculator = Calculator('')
    calculator.main()



