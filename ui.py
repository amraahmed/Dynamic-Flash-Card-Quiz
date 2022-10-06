from tkinter import *
THEME_COLOR = "#375362"

class Interface:
    def __init__(self): 
        self.window = Tk()
        self.window.title("Quizlet")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,text="Some question text",fill=THEME_COLOR,font='arial 20 italic')
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        truimg = PhotoImage(file='images/true.png')
        self.trubtn = Button(image=truimg,highlightthickness=0)
        self.trubtn.grid(row=2,column=0)
        flsimg = PhotoImage(file='images/false.png')
        self.flsbtn = Button(image=flsimg,highlightthickness=0)
        self.flsbtn.grid(row=2,column=1)
        self.window.mainloop()