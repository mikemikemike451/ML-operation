# provided code
class Question:
    def __init__(self):
        self._question_text = ""
        self._answer = ""
    def setQuestionText(self, question_text):
        self._question_text = question_text
    def setAnswer(self, answer):
        self._answer = answer
    def checkAnswer(self,user_answer):
        return user_answer == self._answer  
    # new method: get the answer to avoid direct access to the private variable
    def getAnswer(self):
        return self._answer
    def display(self):
        print(self._question_text)


#new class NumericalQuestion that inherits from Question
class NumericalQuestion(Question):
    def __init__(self):
        super().__init__()
        self._tolerance = 0.01  
    # override the method to allow for numerical answers with a tolerance
    def checkAnswer(self, user_answer):
        try:
            user_answer = float(user_answer)
            correct_answer = float(self._answer)
            return abs(user_answer - correct_answer) <= self._tolerance
        except ValueError:
            return False  


q1 = NumericalQuestion()
q1.setQuestionText("What is 5.3 + 3?")
q1.setAnswer("8.3")
q1.display()
print(q1.checkAnswer(input("Your answer: ")))