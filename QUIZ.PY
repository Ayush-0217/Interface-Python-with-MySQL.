import mysql.connector
import random

# Step 1: Database connection function
def connect_to_db():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='quiz_db'
    )
    return connection

# Step 2: Fetch questions from the database
def fetch_questions():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT question_text, option1, option2, option3, option4, correct_answer FROM quiz_questions")
    questions = cursor.fetchall()
    connection.close()
    random.shuffle(questions)  # Shuffle questions for randomness
    return questions

# Step 3: Display questions and get user's answers
def take_quiz(questions):
    score = 0

    for question in questions:
        print("\n" + question[0])  # Display the question text
        print("1.", question[1])
        print("2.", question[2])
        print("3.", question[3])
        print("4.", question[4])
        
        # User's answer input
        answer = input("Enter the option number (1-4): ")
        correct_option = question[5]  # Correct answer stored as '1', '2', '3', or '4'

        # Check if the answer is correct
        if answer == correct_option:
            score += 1
            print("Correct!")
        else:
            print("Incorrect! The correct answer was:", correct_option)
    
    return score

# Step 4: Store the score in MySQL
def store_score(username, score):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO user_scores (username, score) VALUES (%s, %s)", (username, score))
    connection.commit()
    connection.close()

# Main execution
if __name__ == "__main__":
    print("Welcome to the Python Quiz Application!")
    username = input("Enter your username: ")
    
    questions = fetch_questions()  # Fetch questions from the database
    score = take_quiz(questions)  # Conduct the quiz
    
    print(f"\n{username}, your final score is: {score}/{len(questions)}")
    
    # Store the score in the database
    store_score(username, score)
    print("Your score has been saved. Thank you for playing!")
