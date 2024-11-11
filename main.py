import random
import math
def generate_math_question(min_number: int, max_number: int) -> str:
    num1 = random.randint(min_number, max_number)
    num2 = random.randint(min_number, max_number)
    operator = random.choice("+-*/")
    return f"{num1} {operator} {num2}"



def check_answer(question: str, user_answer: str) -> bool:
    answer = eval(question)
    try:
        user_answer = float(user_answer)
        return  math.isclose(answer, user_answer, abs_tol=0.05)
    except ValueError:
        print("результат математического действия может быть только числом")
        return False



def math_quiz(number_of_questions):
    score = 0
    print(f"Добро пожаловать в математический тест.\nРешите {number_of_questions} разных примеров и узнайте свой результат!")
    for i in range(number_of_questions):
        problem: str = generate_math_question(1, 10)
        answer = input(f"{problem} = ")
        if check_answer(problem, answer):
            score += 1
    print("Тест завершен.")
    print(f"Вы правильно решили {score} из {number_of_questions} вопросов.")
    if number_of_questions / score > 0.8:
        print("Ваша оценка 5")
    elif number_of_questions / score > 0.6:
        print("Ваша оценка 4")
    else:
        print("Ваша оценка 3")
math_quiz(12)