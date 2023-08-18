import tkinter
from tkinter import font
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(
            text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 20, "bold")
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Here is question.", font=FONT, fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = tkinter.PhotoImage(file="images/true.png")
        false_img = tkinter.PhotoImage(file="images/false.png")
        self.true_button = tkinter.Button(
            image=true_img, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)
        self.false_button = tkinter.Button(
            image=false_img, highlightthickness=0, command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        self.reset_button = tkinter.Button(text="reset", font=("Arial", 20, "bold"))
        self.reset_button.grid(row=0, column=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(
                self.question_text, text="You reached the end of this quiz!"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
