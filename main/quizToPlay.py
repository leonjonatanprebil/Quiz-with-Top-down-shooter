import tkinter as tk

questions = [
    ("Koliko je 124 / 2?", "62"),
    ("\n 2x + 5 = x + 8, \n Koliko je x?", "3"),
    ("Glavno mesto Slovenije?", "Ljubljana"),
    ("Kaj je: 'Was it a car or a cat I saw' obratno?", "was it a car or a cat I saw"),
]


class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Kviz")

        self.score = 0
        self.index = 0
        self.questions = questions

        self.label = tk.Label(root, text="", font=("Arial", 14))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Odgovori", command=self.check)
        self.button.pack(pady=10)

        self.result = tk.Label(root, text="")
        self.result.pack()

        self.root.bind("<Return>", self.check)

        self.show_question()

    def show_question(self):
        if self.index < len(self.questions):
            q, _ = self.questions[self.index]
            self.label.config(text=f"Vprašanje {self.index+1}: {q}")
            self.entry.delete(0, tk.END)
        else:
            percentage = (self.score / len(self.questions)) * 100

            if percentage < 50:
                self.label.config(
                    text=f"Rezultat: {self.score}/{len(self.questions)} ({int(percentage)}%)\nPremalo! Ponovi kviz."
                )
                self.reset_quiz()
            else:
                self.label.config(
                    text=f"Uspeh! Rezultat: {self.score}/{len(self.questions)} ({int(percentage)}%)"
                    #root.after(3000, root.destroy)

                )
                self.entry.pack_forget()
                self.button.pack_forget()

    def reset_quiz(self):
        self.score = 0
        self.index = 0
        self.root.after(2000, self.show_question)

    def check(self, event=None): 
        user = self.entry.get().lower().strip()
        correct = self.questions[self.index][1].lower()

        if user == correct:
            self.score += 1
            self.result.config(text="Pravilno!")
        else:
            self.result.config(text=f"Napačno! Pravilen odgovor: {correct}")

        self.index += 1
        self.root.after(1000, self.show_question)



