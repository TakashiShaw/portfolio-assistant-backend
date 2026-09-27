import os
import re

from flask import Flask, jsonify, request
from flask_cors import CORS


# Create the Flask app.
app = Flask(__name__)

# Enable CORS so a future frontend, such as GitHub Pages, can call this API.
CORS(app)


# ------------------------------------------------------------
# PORTFOLIO INFORMATION
# Update these responses when your portfolio details change.
# ------------------------------------------------------------
PORTFOLIO_RESPONSES = {
    "projects": (
        "Projects: I have built an Interactive Portfolio Website, a game-style "
        "personal portfolio where visitors control a character and walk around a "
        "room to interact with my projects, resume, interests, and contact "
        "information. It was built with HTML, CSS, and JavaScript. I also built "
        "MarketScope, a web application that uses World Bank API data to let users "
        "explore and compare economic indicators between countries. It includes "
        "country and indicator selection and displays historical economic data. "
        "Another project is a Crossy Road style browser game with character "
        "movement, obstacles, collisions, scoring, and custom character animations."
    ),
    "skills": (
        "Skills: Python, HTML, CSS, JavaScript, Flask, working with APIs, Git, "
        "GitHub, GitHub Pages, and basic backend/frontend web development."
    ),
    "education": (
        "Education: I am a student at Carnegie Mellon University studying Business "
        "with a minor in Artificial Intelligence through the School of Computer "
        "Science."
    ),
    "experience": (
        "Experience: Information about my experience can be found in my portfolio "
        "and resume."
    ),
    "interests": (
        "Interests: Entrepreneurship, business, technology, artificial intelligence, "
        "football, viola, and building software projects."
    ),
    "contact": (
        "Contact: My GitHub, LinkedIn, and email links are available in the Contact "
        "section of the portfolio."
    ),
    "resume": (
        "Resume: My resume can be opened from the Resume section of the portfolio."
    ),
    "greeting": (
        "Hi! I can answer questions about my projects, skills, education, "
        "experience, interests, resume, or contact information."
    ),
}


# Keywords used to match a user's message to a response category.
KEYWORDS = {
    "projects": [
        "project",
        "projects",
        "built",
        "build",
        "made",
        "portfolio",
        "marketscope",
        "game",
    ],
    "skills": [
        "skill",
        "skills",
        "know",
        "programming",
        "language",
        "languages",
        "code",
        "coding",
        "technology",
        "technologies",
    ],
    "education": [
        "education",
        "school",
        "college",
        "university",
        "cmu",
        "carnegie",
        "major",
        "minor",
        "study",
        "studying",
    ],
    "experience": ["experience", "work", "job", "jobs", "background"],
    "interests": ["interest", "interests", "hobby", "hobbies", "like", "enjoy"],
    "contact": ["contact", "email", "github", "linkedin", "reach", "connect"],
    "resume": ["resume", "cv"],
    "greeting": ["hello", "hi", "hey"],
}


DEFAULT_REPLY = (
    "I am not sure about that yet. Try asking about projects, skills, education, "
    "experience, interests, contact information, or resume."
)


def message_matches_keywords(message, keywords):
    """Check whether a message contains any complete keyword from a list."""
    for keyword in keywords:
        pattern = r"\b" + re.escape(keyword) + r"\b"
        if re.search(pattern, message):
            return True
    return False


@app.get("/")
def home():
    """Return a simple health check message."""
    return jsonify({"status": "Portfolio Assistant backend is running"})


@app.post("/chat")
def chat():
    """Accept a user message and return a keyword-based chatbot reply."""
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be valid JSON."}), 400

    if "message" not in data:
        return jsonify({"error": "Message is required."}), 400

    message = data["message"]

    if not isinstance(message, str):
        return jsonify({"error": "Message must be a string."}), 400

    cleaned_message = message.strip().lower()

    if not cleaned_message:
        return jsonify({"error": "Message cannot be empty."}), 400

    for category, keywords in KEYWORDS.items():
        if message_matches_keywords(cleaned_message, keywords):
            return jsonify({"reply": PORTFOLIO_RESPONSES[category]})

    return jsonify({"reply": DEFAULT_REPLY})


if __name__ == "__main__":
    # Render provides a PORT environment variable during deployment.
    # The default of 5001 is used for local development.
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
