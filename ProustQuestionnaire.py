#This is The Proust Questionnaire written in Python 

class ProustQuestionnaire:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.questionnaire()


    def questionnaire(self):
        
        all = questions = [
        "it is not the first question. Just say your name"
        "What is your idea of perfect happiness?",
        "What is your greatest fear?",
        "What is the trait you most deplore in yourself?",
        "What is the trait you most deplore in others?",
        "Which living person do you most admire?",
        "What is your greatest extravagance?",
        "What do you consider the most overrated virtue?",
        "What do you most dislike about your appearance?",
        "Which living person do you most despise?",
        "Which words or phrases do you most overuse?",
        "When and where were you happiest?",
        "Which talent would you most like to have?",
        "If you could change one thing about yourself, what would it be?",
        "What do you consider your greatest achievement?",
        "If you were to die and come back as a person or a thing, what would it be?",
        "Where would you most like to live?",
        "What is your most treasured possession?",
        "Which historical figure do you most identify with?",
        "Who are your heroes in real life?",
        "What is your greatest regret?"]
        number = 1
        for q in all:
            answer = str(input(f"{q}\n"))
            self.answers.append(answer)

   

proust = ProustQuestionnaire()





