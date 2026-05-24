"""
Royal Chess - Flask Web Application
Serves the chess game as a web application with optional API endpoints.
"""

import os
from flask import Flask, send_from_directory, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, static_folder="static", template_folder=".")


@app.after_request
def set_security_headers(response):
    """Apply defensive HTTP headers to every response."""
    response.headers["Content-Security-Policy"] = (
        "default-src 'none'; "
        "script-src 'self'; "
        "style-src 'self' 'unsafe-inline'; "
        "font-src 'self'; "
        "img-src 'none'; "
        "connect-src 'none'; "
        "base-uri 'none'; "
        "form-action 'none';"
    )
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Permissions-Policy"] = (
        "geolocation=(), camera=(), microphone=()"
    )
    return response


@app.route("/")
def index():
    """Serve the main chess game."""
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "game": "Royal Chess"})


@app.route("/static/<path:filename>")
def static_files(filename):
    """Serve static assets from the static/ subdirectory."""
    return send_from_directory(STATIC_DIR, filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "false").lower() == "true"
    # Default to localhost only; set HOST=0.0.0.0 explicitly for LAN sharing.
    host = os.environ.get("HOST", "127.0.0.1")

    if debug and host != "127.0.0.1":
        raise RuntimeError(
            "Refusing to start: DEBUG mode must not run on a public interface. "
            "Set HOST=127.0.0.1 or disable DEBUG."
        )

    print(f"Royal Chess running at http://{host}:{port}")
    app.run(host=host, port=port, debug=debug)
