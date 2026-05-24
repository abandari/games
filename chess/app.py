"""
Royal Chess - Flask Web Application
Serves the chess game as a web application with optional API endpoints.
"""

import os
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder="static", template_folder=".")


@app.route("/")
def index():
    """Serve the main chess game."""
    return send_from_directory(".", "index.html")


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "game": "Royal Chess"})


@app.route("/static/<path:filename>")
def static_files(filename):
    """Serve static assets."""
    return send_from_directory("static", filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "false").lower() == "true"
    print(f"Royal Chess running at http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=debug)
