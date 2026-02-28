# Ping Pong Game (Python + Pygame)

A simple and fun **Ping Pong / Table Tennis game** built with **Python** and **Pygame**.

Players control paddles to bounce the ball back and forth. First to reach the winning score wins the game!

---

## Features

- Two-player gameplay
- Smooth paddle movement
- Ball movement with collision
- Simple scoring system
- Game restart support

---

## How to Play

1. **Clone the repository**

```bash
git clone https://github.com/natchat-c/proj-python.git
```

2. **Install dependencies**

```bash
pip install pygame
```
3. **Run the game**

```bash
python shooter_game.py
```
# Controls

| Player | Keys      |
| ------ | --------- |
| Left   | W / S     |
| Right  | Up / Down |

# Game Rules

- Use your paddle to hit the ball back.
- If a player misses the ball, the other player gets a point.
- First player to reach the win condition wins the game.

# Project Structure
```
ping-pong/
├── assets/
│   ├── ball.png        # Game ball sprite
│   ├── left.png        # Left paddle sprite
│   └── right.png       # Right paddle sprite
├── main.py             # Game entry point
├── README.md           # This file
└── requirements.txt    # Python deps (optional)
```

## Requirements

- Python 3.x
- Pygame library

## Notes

- This game is designed to be simple and educational.
- Feel free to fork and add features such as:
   - Sound effects
   - Pause menu 
   - AI opponent 
   - Improved win screen

 ## License

This project is released into the public domain.
Feel free to use, modify, and share!
