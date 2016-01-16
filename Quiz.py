import random
import csv

class Question:
    def __init__(self, qID, question, answer, correct = 0, asked = 0, battingAvg = 1):
        self.qID = qID # Question's ID
        self.question = question
        self.answer = answer
        self.asked = asked
        self.correct = correct
        self.battingAvg = battingAvg # Assume people are Pro

    def ask(self):
        right = False
        if self.asked != 0:
            print("Your Average for this question is {:.2%}\nCorrect {} : Asked {}".format
                    (self.battingAvg, self.correct, self.asked))
        self.asked += 1
        print(self.question)
        raw_input("[Hit Enter to Reveal Answer] > ")
        print(self.answer)
        if raw_input("Enter a word starting with y if you got it right. > ").lower()[0] == 'y':
            self.correct += 1
            right = True
        else:
            print("Better luck next time")
        self.updateAverage()
        return right

    def updateAverage(self):
        self.battingAvg = self.correct / float(self.asked)

    def reset(self):
        self.asked = 0
        self.correct = 0
        self.battingAvg = 1

class Quiz:
    def __init__(self, questionList):
        self.asked = 0
        self.questionList = questionList

    def start(self, SORTBYAVERAGE = False):
        """
        Starts the quiz. If SORTBYAVERAGE is True, questions will be asked
        from lowest batting average to highest batting average.
        Else, all questions will be asked in random order.
        """
        self.asked += 1
        questionsAsked = 0
        questionsCorrect = 0
        if SORTBYAVERAGE:
            random.shuffle(self.questionList)
        else:
            self.questionList.sort(key = lambda x: x.battingAvg)
        i = 0
        while i < self.questionList:
            questionsAsked += 1
            questionsCorrect += 1 if self.questionList[i].ask() else 0
            print("Your score so far is {:.2%}".format(questionsCorrect/questionsAsked))
            opt = "-1"
            while opt[0].lower() not in ['c', 'q', 'a']:
                opt = raw_input("[c]ontinue? [q]uit? [a]sk again?\nPlease enter the appropriate letter > ")
            if opt[0].lower() == 'c':
                i += 1
            elif opt[0].lower() == 'q':
                break
            elif opt[0].lower() == 'a':
                pass
        print("Your final average {:.2%}\nCorrect {} : Answered {}".format
                (questionsCorrect/questionsAsked, questionsCorrect, questionsAsked))

        def export(self, filename):
            self.questionList.sort(key = lambda x : x.qID)
            with open(filename, 'w+') as csvfile:
                w = csv.writer(csvfile, delimiter='~', quotechar='"')
                w.writerow(["ID","Question","Answer","Correct #", "Asked #", "Average Correctness"])
                for i in self.questionList:
                    w.writerow([str(i.qId), i.question, i.answer, str(i.correct), str(i.asked), str(i.battingAvg)])

def makeQuestion(row):
    return Question(int(row[0]), row[1], row[2], int(row[3]), int(row[4]), float(row[5]))

def makeQuiz(filename):
    with open(filename, "rU") as csvfile:
        r = csv.reader(csvfile, delimiter="~", quotechar='"')
        return Quiz(list(map(makeQuestion, [i for i in r][1:])))

def main():
    quiz = None
    print("Hi, and welcome to the Big O Game!")
    while True:
        opt = "-1"
        while opt[0].lower() not in ['s', 'h', 'l', 'p', 'q']:
            opt = raw_input("[s]ave, [l]oad, [p]lay, [q]uit, [h]elp > ")
            if not quiz and opt[0].lower() in ['s', 'p']:
                print("Please do [l]oad, since you don't have a quiz to use")
                opt = "-1"
        if opt[0].lower() == 'q':
            print("Bye!")
            quit()
        elif opt[0].lower() == 'h':
            print("This a game which uses Flash Card mechanics to quiz your Big O knowledge")
            print("[l]oad: to load a csvfile with questions. After that, you unlock the [s]ave and [p]lay features")
            print("[s]ave: saves stats and questions of current quiz")
            print("[p]lay: plays the current quiz, which updates the score as you play")
            print("[q]uit: Quits the program")
            print("[h]elp: Prints this menu")
        elif opt[0].lower() == 's':
            filename = raw_input("Filename? > ")
            quiz.export(filename)
            print("Done!")
        elif opt[0].lower() == 'p':
            p_opt = "-1"
            while p_opt[0].lower() not in ["w", "r"]:
                p_opt = raw_input("""Do you want to play in worst to best order? Or in random order?
[w]orst?
[r]andom? > """)
            if p_opt[0].lower() == "w":
                quiz.start(False)
            elif p_opt[0].lower() == "r":
                quiz.start()
        elif opt[0].lower() == "l":
            filename = raw_input("Filename? > ")
            quiz = makeQuiz(filename)


if __name__ == "__main__": main()
