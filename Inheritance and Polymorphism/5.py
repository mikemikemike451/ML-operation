class Question:
    def __init__(self):
        self._question_text = ""
        self._answer = ""
    def setQuestionText(self, question_text):
        self._question_text = question_text
    def setAnswer(self, answer):
        self._answer = answer
    def checkAnswer(self,user_answer):
        return user_answer.replace(" ", "").lower() == self._answer.replace(" ", "").lower()  
    def getAnswer(self):
        return self._answer
    def display(self):
        print(self._question_text)

class MultipleChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self._choices = []
    def setChoices(self, choices):
        self._choices = choices
    def setAnswer(self, answer):
        answer = set(answer.split())
        self._answer = answer
    def display(self):
        super().display()
        for i, choice in enumerate(self._choices):
            print(f"{i + 1}. {choice}")
    def checkAnswer(self, user_answer):
        user_answer = set(user_answer.split())
        return user_answer == self._answer

q5 = MultipleChoiceQuestion()
q5.setQuestionText("Which of the following are programming languages?")
q5.setChoices(["Python", "Java", "HTML", "CSS"])
q5.setAnswer("1 2")
q5.display()
user_answer = input("Your answer (separate multiple answers with spaces): ")
print(q5.checkAnswer(user_answer))