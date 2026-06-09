# 🎮 Neon Tic-Tac-Toe AI

A futuristic Neon-themed Tic-Tac-Toe game built with Python and Pygame, featuring an **unbeatable AI opponent powered by the Minimax algorithm**.

The game randomly assigns symbols, provides glowing neon visuals, and challenges players against an AI that never loses.

---

## ✨ Features

* Neon-themed game interface
* Unbeatable AI using Minimax
* Random player symbol assignment (X or O)
* Intelligent move evaluation
* Smooth Pygame graphics
* Win and draw detection
* Object-oriented architecture

---

## 📂 Project Structure

```text
Neon-TicTacToe-AI/
├── main.py
├── agent.py
└── assets/
```

### Files

* **main.py** → Game loop, rendering, event handling
* **agent.py** → AI logic using Minimax Algorithm

---

## 🧠 AI Implementation

The AI uses the **Minimax Algorithm** to evaluate every possible future game state.

### AI Strategy

* Maximizes its own winning chances
* Minimizes the opponent's chances
* Blocks winning moves
* Takes winning moves instantly
* Guarantees:

  * Win when possible
  * Draw otherwise
  * Never loses

---

## 🎨 Game Features

### Neon X

* Cyan glow effect
* Multi-layer rendering
* Dynamic visual style

### Neon O

* Red neon circle
* Glow layers using alpha transparency

### Grid

* Cyberpunk-inspired design
* Dark neon background

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/GANESH-NADKARNI/neon-tictactoe-ai.git
cd neon-tictactoe-ai
```

### Install Dependencies

```bash
pip install pygame
```

### Run

```bash
python main.py
```

---

## 🎮 How to Play

1. Launch the game.
2. You are randomly assigned X or O.
3. Click on an empty cell to place your move.
4. The AI responds automatically.
5. Try to beat the AI.

Spoiler:

```text
The AI is unbeatable 😄
```

---

## 🛠️ Technologies Used

* Python 3
* Pygame
* Minimax Algorithm
* Object-Oriented Programming

---

## 📚 Concepts Demonstrated

* Artificial Intelligence
* Game Theory
* Minimax Search
* Recursive Algorithms
* Event Handling
* GUI Development
* Object-Oriented Design
* State Space Search

---

## 🔮 Future Improvements

* Alpha-Beta Pruning
* Difficulty Levels
* Score Tracking
* Sound Effects
* Animated Win Lines
* Online Multiplayer
* Reinforcement Learning Agent
* Mobile Version

---

## 📊 Algorithm Complexity

### Minimax

* Time Complexity: O(9!)
* Space Complexity: O(9)

Since Tic-Tac-Toe has a small state space, Minimax can evaluate all possibilities efficiently.

---

## 👨‍💻 Author

Ganesh Nadkarni

A neon-themed AI-powered Tic-Tac-Toe game demonstrating game development and adversarial search algorithms.
