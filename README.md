# Tic Tac Toe

A text-based version of the Tic Tac Toe game.

## 🚀 Features

- Two-player, turn-based gameplay in the terminal.  
- Win detection for rows, columns, and diagonals.  
- Clear board drawing with numbered spots for easy selection.  
- “Quit” command to exit the game at any time.  
- Tie detection when all spots are filled without a winner.

## ⚙️ Usage

Clone the repository and run the main script, you’ll see the board displayed like this:

```
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
```

On your turn, type the number of the spot you want to claim, or enter `quit` to exit.

**Example session:**

```
Player 1's turn: Pick your spot or type 'quit' to quit the game: 5
Player 2's turn: Pick your spot or type 'quit' to quit the game: 1
Player 1's turn: Pick your spot or type 'quit' to quit the game: 9
...
-------------
| X | 2 | 3 |
-------------
| 4 | O | 6 |
-------------
| 7 | 8 | X |
-------------
Player 1 Won!
```

## 📦 Project Structure

```
.
├── main.py      # Game loop and user interaction
└── board.py     # Board rendering and win/turn logic
```

- **main.py**: Handles input, turn tracking, quitting, and end‑of‑game logic.  
- **board.py**:  
  - `draw_board(spots)` – Renders the current board.  
  - `check_turn(turn)` – Returns `'X'` or `'O'` based on turn count.  
  - `check_win(spots)` – Checks whether a player has won.

## ✏️ Customization

- Change the board size or win conditions by editing the checks in `board.py`.  
- Swap symbols (`'X'`, `'O'`) by modifying `check_turn`.  
- Add AI or network play by extending the main loop in `main.py`.
