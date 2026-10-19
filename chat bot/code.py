
# 🤖 Friendly Chatbot Project
# Hashtags: #Python #Chatbot #BeginnerProject #Coding

import time
import random

# Function to display messages with a small delay
def bot_say(message):
    print("🤖 Bot:", message)
    time.sleep(1)


# Welcome message
bot_say("Hello! Welcome to my chatbot.")
name = input("😊 What is your name? ").strip()

if not name:
    name = "Friend"

bot_say(f"Nice to meet you, {name}!")

# Ask about the user's mood
feeling = input("How are you feeling today? ").strip().lower()

if any(word in feeling for word in ["good", "great", "happy", "fine", "awesome"]):
    bot_say("I'm glad to hear that! Keep smiling! 😄")
elif any(word in feeling for word in ["bad", "sad", "upset", "tired", "angry"]):
    bot_say("I'm sorry to hear that. I hope your day gets better! 💙")
else:
    bot_say("Thanks for sharing that with me!")

# Ask about favorite color
color = input("What is your favorite color? ").strip()

if color:
    bot_say(f"{color.title()} is a lovely color!")
else:
    bot_say("That's okay! You can tell me your favorite color anytime.")

# Random jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "Why was the computer cold? It left its Windows open! 😂",
    "Why do Python programmers wear glasses? Because they can't C! 🤓"
]

answer = input("Would you like to hear a joke? (yes/no): ").strip().lower()

if answer in ["yes", "y", "sure"]:
    bot_say(random.choice(jokes))
else:
    bot_say("No problem! Maybe next time.")

# Fun fact
facts = [
    "Python was named after Monty Python, a comedy group.",
    "The first computer bug was an actual moth found in a computer.",
    "Python is widely used in web development, automation, and data science."
]

bot_say("Here is a fun fact: " + random.choice(facts))

# Goodbye
bot_say(f"It was nice talking to you, {name}!")
bot_say("Goodbye! Have a wonderful day! 👋")
