from tkinter import *

BACKGROUND_COLOR = "#009999"
FONT = ("courier", 20, "bold")
PADDING = 10


class QuizInterface:

    def __init__(self):
        self.interface = Tk()
        self.interface.title("A3AJAGBE QUIZZY APP")
        self.interface.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=BACKGROUND_COLOR, font=FONT)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.q_text = self.canvas.create_text(150, 125, text="Question goes here", font=("Arial", 20, "italic"), fill="#008080")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.true = Button(text="True", fg="green")
        self.true.config(padx=PADDING, pady=PADDING, font=FONT, highlightthickness=0)
        self.true.grid(row=2, column=0)

        self.false = Button(text="False", fg="red")
        self.false.config(padx=PADDING, pady=PADDING, font=FONT, highlightthickness=0)
        self.false.grid(row=2, column=1)

        self.interface.mainloop()
