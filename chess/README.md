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

Then open **http://localhost:5000** in your browser.

#### LAN sharing (let others on your network play)

```bash
HOST=0.0.0.0 python app.py
```

Find your local IP with `ipconfig getifaddr en0` (Mac) or `ipconfig` (Windows), then share `http://192.168.x.x:5000`.
> **Note:** Never set `HOST=0.0.0.0` together with `DEBUG=true` — the app will refuse to start to prevent exposing the debug console on the network.

## Security

The Flask server applies the following hardening out of the box:

| Header / Control | Value |
|-----------------|-------|
| Content-Security-Policy | Restricts scripts to `'self'`, no inline JS, fonts from Google only |
| X-Frame-Options | `DENY` — prevents clickjacking |
| X-Content-Type-Options | `nosniff` — prevents MIME-type sniffing |
| Referrer-Policy | `no-referrer` |
| Permissions-Policy | Disables camera, microphone, geolocation |
| Default host binding | `127.0.0.1` (localhost only) — set `HOST=0.0.0.0` to expose on LAN |
| Debug guard | Server refuses to start with `DEBUG=true` on a public interface |

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
