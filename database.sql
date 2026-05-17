CREATE DATABASE quiz_db;


USE quiz_db;


CREATE TABLE quiz_questions (
    question_id INT PRIMARY KEY AUTO_INCREMENT,
    question_text VARCHAR(255) NOT NULL,
    option1 VARCHAR(255) NOT NULL,
    option2 VARCHAR(255) NOT NULL,
    option3 VARCHAR(255) NOT NULL,
    option4 VARCHAR(255) NOT NULL,
    correct_answer VARCHAR(1) NOT NULL  -- Stores the correct option as '1', '2', '3', or '4'
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


CREATE TABLE user_scores (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    score INT NOT NULL
);
   




