import requests
import html
import random
import time

def game_settings():

     
    questions_amount = int(input("How many questions would you like to have? (maximum 50) "))

    if questions_amount > 50:
         print("Only 50 questions at a time!")
    else:
            url = f"https://opentdb.com/api.php?amount={questions_amount}"



    cat_url = "https://opentdb.com/api_category.php"

    time.sleep(0.2)

    print("Now let's select a category.")
    time.sleep(0.2)
    print()
    print("These are the categories and the corresponding numbers. Pick one!")
    print()

    response = requests.get(cat_url)
    data = response.json()

    categories = data["trivia_categories"]


    for category in categories:

        print(f"Number: {category['id']} - Category: {category['name']}")
        time.sleep(0.2)

    print()
    selected_category = int(input("For any category, just press 0! "))

    if 9 <= selected_category <=32:
        url += f"&category={selected_category}"


    difficulty = input("Difficulty (easy, medium, hard, any (press enter for any))) ").lower()

    if difficulty in ["easy", "medium", "hard"]:
        url += f"&difficulty={difficulty}"


    type = input("Type (multiple, boolean, any (press enter for any))" ).lower()

    
    if type in ["multiple", "boolean"]:
         url += f"&type={type}"

    return url


def main():

    score = 0
    url = game_settings()
    print(url)
    
    
    response = requests.get(url)
    data = response.json()

    if data["response_code"]==1:
         print("Not enough questions for this query. Try fewer questions or another category.")
         return

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
    
    print(f"Your total score was {score} points out of {len(question_data)}")



if __name__ == "__main__":
    main()