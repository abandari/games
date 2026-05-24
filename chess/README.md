# Royal Chess

A fully-featured browser chess game with an elegant dark-gold UI, high-quality SVG pieces, and a Python/Flask server.

## Features

- **Player vs Computer** — choose White or Black; the board flips automatically
- **Three difficulty levels** — Beginner (random), Medium (minimax depth 2), Hard (minimax depth 4 + alpha-beta pruning)
- **High-quality SVG pieces** — vector graphics with radial gradients and drop shadows
- **Legal move hints** — click any piece to see all valid moves highlighted
- **Retract Move** — undo your last move *and* the computer's response in one click
- **Subtle notifications** — toast alerts for captures, checks, castling, promotions (toggle off in the panel)
- **Full chess rules** — castling, en passant, pawn promotion, check/checkmate/stalemate detection
- **Move history** — algebraic notation sidebar

## How to Run

There are two ways to play — choose whichever suits you.

---

### Option 1 — Open directly in your browser (easiest, no install needed)

The game is a single self-contained HTML file with no external dependencies.

1. Download or clone this repository
2. Double-click `index.html` in Finder (Mac) or File Explorer (Windows)
3. The game opens instantly in your default browser

Or from the Terminal:

```bash
open index.html          # Mac
start index.html         # Windows
xdg-open index.html      # Linux
```

---

### Option 2 — Run with the Python / Flask server

Use this if you want to host the game so others on your network can play.

**Prerequisites:** Python 3.8 or later

```bash
# 1. Clone the repo
git clone https://github.com/abandari/games.git
cd games/chess

# 2. Install Flask
pip install -r requirements.txt

# 3. Start the server
python app.py
```

Then open **http://localhost:5000** in your browser.

To let others on the same Wi-Fi network play, share your local IP address (e.g. `http://192.168.1.x:5000`). Find it with `ipconfig getifaddr en0` on Mac or `ipconfig` on Windows.

## Project Structure

```
chess/
├── app.py           # Flask server
├── index.html       # Self-contained chess game (HTML + CSS + JS)
├── requirements.txt
├── static/          # Placeholder for future static assets
└── README.md
```

## Tech Stack

- **Frontend**: Vanilla HTML/CSS/JavaScript — zero dependencies, runs standalone
- **Backend**: Python / Flask — lightweight server, easily deployable
- **AI**: Minimax with alpha-beta pruning and piece-square table evaluation
