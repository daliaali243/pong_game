# 🕹️ Pong Game with Falling Shapes

A fun twist on the classic Pong game — catch falling shapes, earn points, and dodge danger!  
Built entirely using Python’s Turtle module, this game blends classic paddle mechanics with fast-paced falling objects.

---

## 🎨 Features

- Uses Turtle Graphics for colorful and dynamic visuals  
- Collision Detection between paddle and falling shapes  
- Object-Oriented Design with multiple classes for clarity  
- Score System with varied point values  
- Increasing Difficulty as game speed progressively rises  

---

## 🧩 Classes Used

- `Paddle` — Handles player movement and collision detection  
- `Ball` / `Object` — Manages falling shapes and their behavior  
- `Score` — Tracks and displays the current score  
- `Turtle` & `Screen` — From the turtle module for graphics and setup  

---

## 🕹️ How to Play

- ← Left Arrow: Move paddle left  
- → Right Arrow: Move paddle right  
- Catch falling shapes to score points  
- Avoid dangerous shapes to keep the game going!  

---

## 🔺 Shapes & Scoring

| Shape | Points / Effect | Description |
|:------|:----------------|:-------------|
| 🔵 Circle | +1 point | Basic shape |
| 🟥 Square | +2 points | Higher-value shape |
| 🔺 Triangle | Reset score to 0 | Risky — avoid it! |
| 🐢 Colored Turtle | +5 points | Bonus shape |
| ⚪ White Turtle | Game Over | Ends the game |

---

## ⚙️ Game Mechanics

- Shapes fall from the top of the screen  
- Collision is detected when a shape hits the paddle  
- The game speed increases gradually to make it more challenging  
- Shapes reset position after hitting the paddle or the bottom of the screen  

---

## 🚀 Run the Game

Make sure you have Python 3.x installed.  
To play, run the following command in your terminal:

```bash
python pong_game.py
