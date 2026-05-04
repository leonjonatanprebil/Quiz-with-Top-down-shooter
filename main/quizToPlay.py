import tkinter as tk
import random

# ------------------------
# 5 matematičnih vprašanj (fiksna)
# ------------------------
math_questions = [
    ("Ps1 Hagrid","yes"),
    ("John asks: what's 2 + 2 ?? >:)", "4"),
    ("heisenburger"),
    ("wuts 9 + 10?","21"),
    ("johngpt?", "yes"),
]


class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Kviz")

        self.score = 0
        self.index = 0

        # 5 math + 5 random slovene
        self.questions = math_questions

        self.label = tk.Label(root, text="", font=("Arial", 14))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Odgovori", command=self.check)
        self.button.pack(pady=10)

        self.result = tk.Label(root, text="")
        self.result.pack()

        self.show_question()

    def show_question(self):
        if self.index < len(self.questions):
            q, _ = self.questions[self.index]
            self.label.config(text=f"Vprašanje {self.index+1}: {q}")
            self.entry.delete(0, tk.END)
        else:
            self.label.config(text=f"Konec! Rezultat: {self.score}/10")
            self.entry.pack_forget()
            self.button.pack_forget()

    def check(self):
        user = self.entry.get().lower().strip()
        correct = self.questions[self.index][1].lower()

        if user == correct:
            self.score += 1
            self.result.config(text="Pravilno!")
        else:
            self.result.config(text=f"Napačno! Pravilen odgovor: {correct}")

        self.index += 1
        self.root.after(1000, self.show_question)


root = tk.Tk()
app = Quiz(root)
root.mainloop()