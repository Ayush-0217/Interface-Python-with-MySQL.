#  Python Quiz Application

Hi, I'm **Ayush Solanki**. I originally built this project during my Class 12 CBSE assessment to get hands-on with Python and MySQL integration. It was pretty basic back then — just questions and a score save. Now with more knowledge I've reworked it quite a bit, added proper table relationships, per-answer tracking, input validation, a timer, and a leaderboard. Still a work in progress, but a good one.

A terminal-based quiz application built with **Python** and **MySQL** that fetches questions from a database, tracks user answers, saves scores, and displays a leaderboard.

---

##  Project Structure

```
CS PROJECT/
│
├── QUIZ.PY           # Main Python quiz application
├── database.sql      # MySQL database schema + questions
└── README.md         # Project documentation
```

---

##  Database Structure

The project uses a MySQL database called `quiz_db` with **3 connected tables**:

### 1. `quiz_questions`
Stores all quiz questions and their correct answers.

| Column | Type | Description |
|---|---|---|
| question_id | INT (PK) | Auto-generated unique ID |
| question_text | VARCHAR(255) | The question |
| option1–4 | VARCHAR(255) | Four answer choices |
| correct_answer | VARCHAR(1) | Correct option ('1', '2', '3', or '4') |

### 2. `user_scores`
Stores each user's quiz result.

| Column | Type | Description |
|---|---|---|
| user_id | INT (PK) | Auto-generated unique ID |
| username | VARCHAR(255) | Player's name |
| score | INT | Number of correct answers |
| total_questions | INT | Total questions attempted |
| attempted_at | DATETIME | Date and time of quiz |
| time_taken | INT | Seconds taken to finish |

### 3. `user_answers`
Stores every individual answer given by a user.

| Column | Type | Description |
|---|---|---|
| answer_id | INT (PK) | Auto-generated unique ID |
| user_id | INT (FK) | Links to `user_scores` |
| question_id | INT (FK) | Links to `quiz_questions` |
| chosen_option | VARCHAR(1) | Answer the user picked |
| is_correct | BOOLEAN | Whether the answer was correct |

###  How Tables Are Linked
```
quiz_questions ──────┐
  (question_id)      │
                     ▼
                user_answers
                     ▲
  (user_id)          │
user_scores ─────────┘
```

---

##  Libraries Used

| Library | Purpose |
|---|---|
| `mysql.connector` | Connects Python to MySQL database |
| `random` | Shuffles questions randomly each quiz |
| `datetime` | Records quiz time and calculates time taken |

---

##  Python Concepts Used

### Functions
Each task is separated into its own function:
```
connect_to_db()    →  Connect to MySQL
fetch_questions()  →  Read questions from DB
take_quiz()        →  Run the quiz loop
store_score()      →  Save score to user_scores
store_answers()    →  Save each answer to user_answers
show_leaderboard() →  Display top 5 players
```

### Other Concepts
- **Loops** — `for` loop to go through each question; `while` loop for input validation
- **Conditionals** — Check if answer is correct; ask if user wants leaderboard
- **Lists & Dictionaries** — `answers_log` list stores each answer as a dictionary
- **f-Strings** — Used for formatted output messages
- **Input Validation** — Only accepts '1', '2', '3', or '4' as valid answers

---

##  Database Interactions

| Action | Table | Method Used |
|---|---|---|
| Fetch questions | `quiz_questions` | `cursor.fetchall()` |
| Save score | `user_scores` | `cursor.execute()` + `commit()` |
| Get new user ID | `user_scores` | `cursor.lastrowid` |
| Save each answer | `user_answers` | `cursor.execute()` + `commit()` |
| Show leaderboard | `user_scores` | `cursor.fetchall()` |

---

##  Program Flow

```
START
  ↓
Ask for username
  ↓
Fetch questions from quiz_questions table
  ↓
Shuffle questions randomly
  ↓
For each question:
  → Show question + 4 options
  → Get valid answer (1–4)
  → Check correct / incorrect
  → Log answer
  ↓
Calculate score + time taken
  ↓
Save to user_scores → get user_id
  ↓
Save each answer to user_answers
  ↓
Ask if user wants leaderboard → Show Top 5
  ↓
END
```

---

##  Setup & How to Run

### Requirements
- Python 3.x
- MySQL Server
- mysql-connector-python

### Install Python Library
```bash
pip install mysql-connector-python
```

### Setup Database
1. Open MySQL and run the full `database.sql` file:
```sql
-- Select all (Ctrl+A) and run the entire file at once
```
2. This will create the database, all 3 tables, and insert the 10 questions.

### Run the Quiz
```bash
python QUIZ.PY
```

---

##  Features

- ✅ Questions fetched from MySQL database
- ✅ Questions shuffled randomly every quiz
- ✅ Input validation (only accepts 1, 2, 3, or 4)
- ✅ Tracks time taken to complete quiz
- ✅ Saves score with timestamp to database
- ✅ Records every individual answer (correct/wrong)
- ✅ Leaderboard showing Top 5 players

---

## 📝 Sample Output

```
=============================================
   Welcome to the Python Quiz Application!
=============================================
Enter your username: Alex

What is the capital of France?
1. Berlin
2. Madrid
3. Paris
4. Rome
Enter your answer (1-4): 3
✅ Correct!

...

=============================================
  Alex, your final score: 8/10
  Time taken: 45 seconds
=============================================
✅ Your score and answers have been saved!

Would you like to see the leaderboard? (y/n): y

 ── TOP 5 LEADERBOARD ──────────────────
Rank  Username             Score      Date
-------------------------------------------------------
1     Alex                 8/10       2024-01-15 11:05
2     John                 7/10       2024-01-14 09:30
```

---

##  Author

**Ayush Solanki** — Class 12 CBSE CS Project, later modified with improved schema, validation, and new features.
