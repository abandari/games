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

## Running Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open [http://localhost:5000](http://localhost:5000).

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
