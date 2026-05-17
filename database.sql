DROP DATABASE IF EXISTS quiz_db;
CREATE DATABASE quiz_db;
USE quiz_db;
-- TABLE 1: Questions (must be first, others reference it)
CREATE TABLE quiz_questions (
    question_id    INT PRIMARY KEY AUTO_INCREMENT,
    question_text  VARCHAR(255) NOT NULL,
    option1        VARCHAR(255) NOT NULL,
    option2        VARCHAR(255) NOT NULL,
    option3        VARCHAR(255) NOT NULL,
    option4        VARCHAR(255) NOT NULL,
    correct_answer VARCHAR(1)   NOT NULL
);

-- TABLE 2: User Scores
CREATE TABLE user_scores (
    user_id         INT PRIMARY KEY AUTO_INCREMENT,
    username        VARCHAR(255) NOT NULL,
    score           INT NOT NULL,
    total_questions INT DEFAULT 10,
    attempted_at    DATETIME DEFAULT NOW(),
    time_taken      INT
);

-- TABLE 3: User Answers (references both tables above)
CREATE TABLE user_answers (
    answer_id      INT PRIMARY KEY AUTO_INCREMENT,
    user_id        INT,
    question_id    INT,
    chosen_option  VARCHAR(1),
    is_correct     BOOLEAN,
    FOREIGN KEY (user_id)     REFERENCES user_scores(user_id),
    FOREIGN KEY (question_id) REFERENCES quiz_questions(question_id)
);


INSERT INTO quiz_questions (question_text, option1, option2, option3, option4, correct_answer)
VALUES
('What is the capital of France?', 'Berlin', 'Madrid', 'Paris', 'Rome', '3'),
('What is 2 + 2?', '3', '4', '5', '6', '2'),
('Who wrote "To Kill a Mockingbird"?', 'Harper Lee', 'Mark Twain', 'George Orwell', 'Ernest Hemingway', '1'),
('Which planet is known as the Red Planet?', 'Earth', 'Mars', 'Venus', 'Jupiter', '2'),
('Who developed the theory of relativity?', 'Isaac Newton', 'Nikola Tesla', 'Albert Einstein', 'Galileo Galilei', '3'),
('What is the largest ocean on Earth?', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean', '4'),
('What is the square root of 16?', '2', '4', '8', '16', '2'),
('Who painted the Mona Lisa?', 'Vincent van Gogh', 'Leonardo da Vinci', 'Pablo Picasso', 'Claude Monet', '2'),
('Which country is known as the Land of the Rising Sun?', 'China', 'Japan', 'South Korea', 'India', '2'),
('What is the smallest prime number?', '1', '2', '3', '5', '2');

-- Check all 3 tables exist
SHOW TABLES;

-- Check questions loaded correctly
SELECT * FROM quiz_questions;

-- Check scores table is empty (ready for Python to fill)
SELECT * FROM user_scores;

-- Check answers table is empty (ready for Python to fill)
SELECT * FROM user_answers;

-- See who played and their scores
SELECT * FROM user_scores;

-- See every answer each user gave
SELECT 
    us.username,
    qq.question_text,
    ua.chosen_option,
    ua.is_correct
FROM user_answers ua
JOIN user_scores us    ON ua.user_id    = us.user_id
JOIN quiz_questions qq ON ua.question_id = qq.question_id;