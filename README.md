# ❌⭕ Tic Tac Toe

A clean, text-based implementation of the classic strategy game, played directly in your terminal.

## 📝 Project Overview

This Python project brings the timeless pen-and-paper game to the command line. It features a robust game loop that handles two-player turns, input validation, and automatic win/draw detection. It's designed to be simple to run and easy to extend.

## 🚀 Features

- **Interactive Gameplay**: A turn-based system for two players (Player 1 is 'X', Player 2 is 'O').
- **Smart Win Detection**: Algorithms to instantly detect wins across rows, columns, and diagonals.
- **Visual Board**: A clear, ASCII-art grid with numbered slots makes selecting moves intuitive.
- **Draw Handling**: Automatically recognizes when the board is full and declares a tie.
- **Graceful Exit**: Includes a "quit" command to leave the game cleanly at any moment.

## 💻 Installation & Usage

### Prerequisites
- Python 3.x

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/DavitEgoian/Tic-Tac-Toe.git
   cd Tic-Tac-Toe
   ```

2. **Run the game**
   ```bash
   python main.py
   ```

### How to Play
The board is displayed with numbers 1-9 representing the available slots:
```text
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
```
When prompted, simply type the number of the spot you want to claim.

**Example Session:**
> Player 1's turn: Pick your spot or type 'quit': **5**  
> Player 2's turn: Pick your spot or type 'quit': **1**  
> ...  
> **Player 1 Won!**

## 📂 Project Structure

```text
Tic-Tac-Toe/
├── main.py      # The game controller: handles the loop, inputs, and game state
└── board.py     # The view & logic: handles rendering and win condition checks
```

## ⚙️ Customization

The modular design allows for easy tinkering:

- **Symbols**: Change the `'X'` and `'O'` characters in `board.py`'s `check_turn` function to emojis or other letters.
- **Logic**: Modify `check_win` in `board.py` to experiment with different winning patterns.
- **AI Opponent**: Use `main.py` as a base to implement a computer opponent algorithm (like Minimax).

## 📄 License

This project is open source and available for personal and educational use.
