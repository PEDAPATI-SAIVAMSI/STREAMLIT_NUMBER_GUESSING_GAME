import streamlit as st

import random

# Set up the page title and sidebar title
st.title("Enhanced Number Guessing Game")
st.sidebar.title("Game Settings")

# User sets the range for the guessing game
min_value = st.sidebar.number_input("Minimum Value", value=1)
max_value = st.sidebar.number_input("Maximum Value", value=100)
max_attempts = st.sidebar.number_input("Maximum Attempts", value=10)

# Initialize the game state
if 'number' not in st.session_state:
    st.session_state.number = random.randint(min_value, max_value)
    st.session_state.attempts_left = max_attempts

# Function to reset the game
def reset_game():
    st.session_state.number = random.randint(min_value, max_value)
    st.session_state.attempts_left = max_attempts

# Function to check the guess
def check_guess(guess):
    st.session_state.attempts_left -= 1
    if guess < st.session_state.number:
        return "Too low!"
    elif guess > st.session_state.number:
        return "Too high!"
    else:
        return "Correct!"

# Display the number of attempts left
st.write(f"Attempts left: {st.session_state.attempts_left}")

# Get user input for the guess
guess = st.number_input("Enter your guess:", min_value=min_value, max_value=max_value, step=1)

# Button to submit the guess
if st.button("Submit Guess"):
    feedback = check_guess(guess)
    st.write(feedback)
    
    if feedback == "Correct!":
        st.balloons()
        st.write("Congratulations! You guessed the correct number.")
        st.button("Play Again", on_click=reset_game)
    elif st.session_state.attempts_left <= 0:
        st.write(f"Game Over! The correct number was {st.session_state.number}.")
        st.button("Try Again", on_click=reset_game)
