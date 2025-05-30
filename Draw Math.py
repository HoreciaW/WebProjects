#GAME DEVELOPMENT
#Name:Horecia Williams
# Date: May 29,2023
# Teacher: Mr.Manyanga
# Course Code: ICS3U0

'''#This program will ask a user to solve different math problems include the addition, subtraction and
multiplication operators.Additionally,users are encouraged to not use a calculator but use the blackboard feature
instead to workout problems on their own.'''

# NOTE: To generate a new problem click on the level of difficulty desired to generate new problems

import tkinter as tk
import random
from tkinter import messagebox
from tkinter import *
from random import randint
# Initialize the Tkinter window
root = Tk()
root.title(" Draw Math")

# Create a canvas widget
canvas = Canvas(root, bg="black", width=1000, height=400)
canvas.pack()

# Variable to store the starting coordinates of the line
start_x = None
start_y = None

# Function to handle mouse button press event
def start_drawing(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

# Function to handle mouse motion event
def draw(event):
    global start_x, start_y
    canvas.create_line(start_x, start_y, event.x, event.y, fill="white")
    start_x = event.x
    start_y = event.y
def erase(event):
    canvas.delete("all")
# Bind mouse button press and motion events to the canvas
canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
# Bind the 'e' key to erase the canvas
root.bind("e", erase)

# Generate a math problem based on the selected difficulty level
def generate_problem(difficulty):
    if difficulty == 'Easy':
        operand1 = randint(1, 10)
        operand2 = randint(1, 10)
        operator = ['+', '-'][randint(0, 1)]
        problem = f"{operand1} {operator} {operand2}"
        answer = eval(problem)
        return problem, answer
    elif difficulty == 'Medium':
        operand1 = randint(1, 100)
        operand2 = randint(1, 100)
        operator = ['+', '-', '*'][randint(0, 2)]
        problem = f"{operand1} {operator} {operand2}"
        answer = eval(problem)
        return problem, answer
    elif difficulty == 'Hard':
        operand1 = randint(1, 200)
        operand2 = randint(1, 200)
        operator = ['+', '-', '*'][randint(0, 3)]
        problem = f"{operand1} {operator} {operand2}"
        answer = eval(problem)
        return problem, answer
    

def check_answer():
    user_answer = user_entry.get()
    user_entry.delete(0, tk.END)
    if user_answer == str(current_answer):
        messagebox.showinfo("Correct!", "Your answer is correct!")
        update_score()
        
    else:
        messagebox.showerror("Incorrect!", "Your answer is incorrect!")
        update_error()
      
# Update the problem and difficulty based on user input
def update_problem(difficulty):
    global current_answer
    problem, current_answer = generate_problem(difficulty)
    problem_label.config(text=problem)
    
# Difficulty selection
difficulty_label = tk.Label(root, text="Select Difficulty:",font=("Arial",16))
difficulty_label.pack()
difficulty_var = tk.StringVar()
difficulty_dropdown = tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard", command=update_problem)
difficulty_dropdown.pack()

# Problem display
problem_label = tk.Label(root, text="")
problem_label.pack()

def update_score():
    global score
    score +=50
    score_label.config(text="Score: " + str(score))

def update_error():
    global score
    score -=10
    score_label.config(text="Score: " + str(score))

def update_timer():
    global time_left
    time_left -= 1
    timer_label.config(text="Time left: " + str(time_left) + "s")
    if time_left == 0:
        messagebox.showinfo("Time's up!", "Game Over!\nYour final score is: " + str(score))
        root.destroy()
    else:
        root.after(1000, update_timer)


score = 0
time_left = 120

#Create the problem label
problem_label = tk.Label(root, text="", font=("Arial", 14))
problem_label.pack(pady=10)

# Create the user entry widget
user_entry = tk.Entry(root, font=("Arial", 12))
user_entry.pack()

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=10)

# Create the score label
score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack()

# Create the timer label
timer_label = tk.Label(root, text="Time left: 30s", font=("Arial", 16))
timer_label.pack()


# Set initial problem
update_problem("Easy")

# Start the timer
update_timer()

#run the app
root.mainloop()

