import re


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

class FillInQuestion(Question):
    def __init__(self):
        super().__init__()
    # override the method 
    def setQuestionText(self, question_text):
        pattern = r"_"
        positions = [match.start() for match in re.finditer(pattern, question_text)]
        self._question_text = question_text[0:positions[0]] + "_____" + question_text[positions[1]+1:]
        self._answer = question_text[positions[0]+1:positions[1]]

    def setAnswer(self, answer):
        raise NotImplementedError("Use setQuestionText to set the answer for FillInQuestion.")


q2 = FillInQuestion()
q2.setQuestionText("The capital of France is _Paris_.")
q2.display()
print(q2.checkAnswer(input("Your answer: ")))
