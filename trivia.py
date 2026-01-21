import requests
import html
import random


#url = "https://opentdb.com/api.php?amount=10"


def get_questions():


    return

def run_quiz():

        return




def game_settings():
     
    questions_amount = int(input("How many questions would you like to have? (maximum 50) "))

    if questions_amount > 50:
         print("Only 50 questions at a time!")
         return

    difficulty = input("Difficulty (easy, medium, hard, any (press enter for many))) ").lower()

    type = input("Type (multiple, boolean, any (press enter for any))" ).lower()

    url = f"https://opentdb.com/api.php?amount={questions_amount}"

    if difficulty in ["easy", "medium", "hard"]:

        url += f"&difficulty={difficulty}"
    
    if type in ["multiple", "boolean"]:
         url += f"&type={type}"

    return url


def main():

    score = 0
    url = game_settings()
    
    response = requests.get(url)
    data = response.json()

    question_data = data["results"]
    print()

    for i, q in enumerate(question_data, start=1):
         
        question = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])
        incorrect = [html.unescape(ans) for ans in q["incorrect_answers"]]

        options = [correct] + incorrect
        random.shuffle(options)



        print(question)
        print(options)

        user_answer = input("Enter your answer: ")
        print()

        if user_answer == correct:
            print("Correct answer!")
            score += 1  
            print(f"You have {score} points!")

        else:
             print(f"Incorrect answer! The correct answer was {correct}")
             print()



if __name__ == "__main__":
    main()