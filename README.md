# Quiz Game
This is a simple Quiz Game built in Python using the Tkinter library for the graphical user interface (GUI). The game presents a series of true or false questions fetched from an API and allows the player to answer them. The player's score is calculated based on the number of correct answers.

# Project Structure
The project consists of the following files:

question_model.py: This file defines the Question class, which represents a question and its answer.

data.py: This file contains the question_data list, which stores the data retrieved from the API.

quiz_brain.py: This file contains the QuizBrain class, which handles the game logic, tracks the player's score, and provides methods for getting the next question and checking the answer.

ui.py: This file contains the QuizUI class, which creates the graphical user interface for the game using Tkinter. It displays the question, buttons for true and false answers, and updates the score.

# How to Play
Ensure you have Python installed on your system.
Run the ui.py file using a Python interpreter.
The game window will appear with the first question and two buttons for true and false answers.
Click the appropriate button to answer the question.
The game will display the next question and update the score accordingly.
Continue answering the questions until all questions have been answered.
The final score will be displayed at the end of the game.
Dependencies
The project relies on the following libraries:

requests: Used to make HTTP requests to the API for retrieving the quiz questions.
tkinter: Used for creating the GUI and handling user interactions.
Ensure that you have these libraries installed before running the game.

# API Usage
The game fetches the quiz questions from the Open Trivia Database API. The API is queried with the desired number of questions and the type of questions (in this case, boolean).

# Acknowledgements
This Quiz Game project was developed as part of a learning experience. It demonstrates the use of classes, API integration, GUI programming, and event handling in Python.

Feel free to modify and enhance the game as per your requirements.
