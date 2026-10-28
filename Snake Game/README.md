🐍 Snake Game — Python & Pygame

A classic Snake Game built with Python and Pygame. Control the snake, eat the red food, grow longer, and try to achieve the highest score without hitting the walls or your own body.

🎮 Features
Snake movement using arrow keys or WASD
Randomly generated food
Score tracking
Snake grows when it eats food
Wall collision detection
Self-collision detection
Game-over and victory screens
Restart functionality
Dark grid background
Sound effect tutorial included in code comments for future use
🛠️ Technologies Used
Python
Pygame
Random module
📁 Project Structure
text
pygame lesson/
├── snake_game.py
└── README.md

📋 Requirements
Python installed on your computer
Visual Studio Code (VS Code)
Pygame or pygame-ce installed
⚙️ Installation

Open the VS Code terminal and install Pygame:

bash
python -m pip install pygame-ce


Verify the installation:

bash
python -c "import pygame; print(pygame.version.ver)"

▶️ How to Run
Open the project folder in VS Code.
Open the terminal.
Run the following command:
bash
python snake_game.py

The game window will open. Start playing!
🕹️ Controls
Key	Action
⬆️ Up Arrow / W	Move up
⬇️ Down Arrow / S	Move down
⬅️ Left Arrow / A	Move left
➡️ Right Arrow / D	Move right
R	Restart after game over
ESC	Quit the game
🏆 How to Play
Control the snake using the arrow keys or WASD.
Eat the red food to increase your score.
The snake grows longer each time it eats food.
Avoid hitting the walls.
Avoid running into your own body.
Try to achieve the highest possible score!
📚 Python and Pygame Concepts Learned
Initializing Pygame with pygame.init()
Creating a game window with pygame.display.set_mode()
Handling keyboard and window events
Using lists and tuples to represent the snake's body
Drawing shapes using pygame.draw
Generating random food positions
Detecting collisions
Managing frame rate with pygame.time.Clock()
Displaying text and scores
Organizing code into functions
Using a game loop to update and draw the game
🔊 Future Improvements
Add sound effects when food is collected.
Add background music.
Create a start menu and pause button.
Increase the snake's speed as the score increases.
Save the highest score.
Add different themes and colors.
👩‍💻 Author
KHADIJA__ANSARI

Created as a Python and Pygame learning project.

Enjoy playing Snake! 🐍🎮