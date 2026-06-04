import requests
import html
import random
from colorama import Fore, Style


EDUCATION_CATEGORY_ID = 9
URL_JOKE = "https://v2.jokeapi.dev/joke/Any?safe-mode"
API_URL_EDUCATIONAL = f"https://opentdb.com/api.php?amount=20&category={EDUCATION_CATEGORY_ID}&type=multiple"
lst = [Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.MAGENTA]

user = int(input("What do you want to do?\n1.Jokes\n2.Trivia\n"))

if user == 1:
    response = requests.get(URL_JOKE)
    data = response.json()
    if data["type"] == "single":
        print(random.choice(lst)+data["joke"])
    else:
        print(random.choice(lst)+data["setup"])
        print(random.choice(lst)+data["delivery"])
else:
    def get_education_questions():
        response = requests.get(API_URL_EDUCATIONAL)
        if response.status_code == 200:
            data = response.json()
            if data['response_code'] == 0 and data['results']:
                return data['results']
        return None

    def run_quiz():
        questions = get_education_questions()

        if not questions:
            print(Fore.RED+"Failed to fetch educational questions")
            return
        score = 0
        print(Fore.YELLOW+"Welcome to the Education Quiz!\n")

        for i, q in enumerate(questions, 1):
            question = html.unescape(q['question'])
            correct = html.unescape(q['correct_answer'])
            incorrects = [html.unescape(a) for a in q['incorrect_answers']]

            options = incorrects + [correct]
            random.shuffle(options)

            print(random.choice(lst)+f"Question {i}: {question}")
            for idx, option in enumerate(options, 1):
                print(f" {idx}. {option}")
            
            while True:
                try:
                    choice = int(input(random.choice(lst)+"\nYour answer (1-4): "))
                    if 1 <= choice <= 4:
                        break
                except ValueError:
                    pass
                print(Fore.RED+"Invalid input! Please enter 1-4")
            print(random.choice(lst)+options[choice - 1], correct)

            if options[choice-1] == correct:
                print(Fore.GREEN+"✅ Correct!\n")
                score += 1
            else:
                print(Fore.RED+f"❌ Wrong! Correct answer: {correct}\n")
        print(random.choice(lst)+f"Final Score: {score}/{len(questions)}")
        print(random.choice(lst)+f"Percentage: {score/len(questions)*100:.1f}%")


    if __name__ == "__main__":
        run_quiz()
