import mysql.connector
import random
from datetime import datetime

# ─────────────────────────────────────────
# Step 1: Database Connection
# ─────────────────────────────────────────
def connect_to_db():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='quiz_db'
    )
    return connection


# ─────────────────────────────────────────
# Step 2: Fetch Questions from DB
# ─────────────────────────────────────────
def fetch_questions():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT question_id, question_text, option1, option2, option3, option4, correct_answer
        FROM quiz_questions
    """)
    questions = cursor.fetchall()
    connection.close()
    random.shuffle(questions)   # Shuffle for randomness
    return questions


# ─────────────────────────────────────────
# Step 3: Conduct the Quiz
# Returns: (score, list of answer dicts)
# ─────────────────────────────────────────
def take_quiz(questions):
    score = 0
    answers_log = []    # Will be saved to user_answers table

    for question in questions:
        question_id     = question[0]
        question_text   = question[1]
        options         = question[2:6]   # option1 to option4
        correct_answer  = question[6]     # '1', '2', '3', or '4'

        print("\n" + question_text)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        # Get valid input from user
        while True:
            answer = input("Enter your answer (1-4): ").strip()
            if answer in ('1', '2', '3', '4'):
                break
            print("  ⚠  Please enter a number between 1 and 4.")

        is_correct = (answer == correct_answer)

        if is_correct:
            score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Incorrect! The correct answer was: {correct_answer}")

        # Log each answer for user_answers table
        answers_log.append({
            'question_id'   : question_id,
            'chosen_option' : answer,
            'is_correct'    : is_correct
        })

    return score, answers_log


# ─────────────────────────────────────────
# Step 4: Store Score → user_scores table
# Returns: new user_id (needed for user_answers)
# ─────────────────────────────────────────
def store_score(username, score, total_questions, time_taken):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO user_scores (username, score, total_questions, attempted_at, time_taken)
        VALUES (%s, %s, %s, %s, %s)
    """, (username, score, total_questions, datetime.now(), time_taken))
    connection.commit()
    user_id = cursor.lastrowid   # Get the auto-generated user_id
    connection.close()
    return user_id


# ─────────────────────────────────────────
# Step 5: Store Per-Answer → user_answers table
# ─────────────────────────────────────────
def store_answers(user_id, answers_log):
    connection = connect_to_db()
    cursor = connection.cursor()
    for ans in answers_log:
        cursor.execute("""
            INSERT INTO user_answers (user_id, question_id, chosen_option, is_correct)
            VALUES (%s, %s, %s, %s)
        """, (user_id, ans['question_id'], ans['chosen_option'], ans['is_correct']))
    connection.commit()
    connection.close()


# ─────────────────────────────────────────
# Step 6: Show Leaderboard (Bonus Feature)
# ─────────────────────────────────────────
def show_leaderboard():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT username, score, total_questions, attempted_at
        FROM user_scores
        ORDER BY score DESC, attempted_at ASC
        LIMIT 5
    """)
    rows = cursor.fetchall()
    connection.close()

    print("\n🏆 ── TOP 5 LEADERBOARD ──────────────────")
    print(f"{'Rank':<5} {'Username':<20} {'Score':<10} {'Date'}")
    print("-" * 55)
    for rank, row in enumerate(rows, start=1):
        date_str = row[3].strftime("%Y-%m-%d %H:%M") if row[3] else "N/A"
        print(f"{rank:<5} {row[0]:<20} {row[1]}/{row[2]:<6}  {date_str}")
    print("─" * 55)


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 45)
    print("   Welcome to the Python Quiz Application!")
    print("=" * 45)

    username = input("Enter your username: ").strip()

    questions = fetch_questions()           # Fetch from quiz_questions

    start_time = datetime.now()
    score, answers_log = take_quiz(questions)   # Conduct quiz
    end_time = datetime.now()

    time_taken = int((end_time - start_time).total_seconds())  # Seconds

    total = len(questions)
    print(f"\n{'='*45}")
    print(f"  {username}, your final score: {score}/{total}")
    print(f"  Time taken: {time_taken} seconds")
    print(f"{'='*45}")

    # Save to user_scores → get user_id → save to user_answers
    user_id = store_score(username, score, total, time_taken)
    store_answers(user_id, answers_log)

    print("✅ Your score and answers have been saved!")

    # Optional: show leaderboard
    show_lb = input("\nWould you like to see the leaderboard? (y/n): ").strip().lower()
    if show_lb == 'y':
        show_leaderboard()

    print("\nThank you for playing! 🎉")