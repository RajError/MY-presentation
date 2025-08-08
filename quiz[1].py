# quiz.py
from questions import QUESTIONS
from utils import clear_screen, get_choice, pause
from storage import load_scores, save_score

def show_intro():
    clear_screen()
    print("=== Simple Quiz App ===\n")
    print("You will be asked multiple-choice questions.")
    print("Answer by typing the letter (A, B, C, ...).")
    print()

def take_quiz():
    score = 0
    total = len(QUESTIONS)
    for i, item in enumerate(QUESTIONS, start=1):
        print(f"Q{i}. {item['q']}")
        for choice in item["choices"]:
            print("   " + choice)
        valid = [c[0] for c in item["choices"]]  # letters like 'A','B',...
        answer = get_choice("Your answer: ", valid)
        if answer == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. Correct answer: {item['answer']}\n")
    return score, total

def show_scores():
    scores = load_scores()
    if not scores:
        print("No saved scores yet.")
        return
    print("\n--- High Scores ---")
    for i, s in enumerate(scores[:5], start=1):
        print(f"{i}. {s['name']} - {s['score']}")

def main():
    show_intro()
    pause("Ready? Press Enter to start the quiz...")
    clear_screen()
    score, total = take_quiz()
    print(f"Quiz finished. Your score: {score}/{total}\n")
    name = input("Enter your name to save score (or leave empty to skip): ").strip()
    if name:
        save_score(name, score)
        print("Saved!")
    show_scores()
    print()
    pause("Done. Press Enter to exit.")

if __name__ == "__main__":
    main()
