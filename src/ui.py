from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#FFFFE8"
TRUE_A_COLOR = "#CDE990"
FALSE_A_COLOR = "#F15A59"
CANVAS_COLOR = "#F1C376"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.score_label = Label(text="score: 0",
                                 fg=CANVAS_COLOR,
                                 bg=THEME_COLOR,
                                 font=("David", 20, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=300, bg=CANVAS_COLOR, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="",
                                                     fill="#2D4356",
                                                     font=("sans-serif", 20, "bold"),
                                                     width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=CANVAS_COLOR)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"you answered all questions.\n\n"
                                                            f" FINAL SCORE: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg=TRUE_A_COLOR)
        else:
            self.canvas.config(bg=FALSE_A_COLOR)
        self.window.after(500, self.get_next_question)

    def false_pressed(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(bg=TRUE_A_COLOR)
        else:
            self.canvas.config(bg=FALSE_A_COLOR)
        self.window.after(500, self.get_next_question)
