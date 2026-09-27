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
    "marketscope": (
        "MarketScope is an interactive global market intelligence dashboard I "
        "built with Python, Streamlit, pandas, Altair, and the World Bank API. "
        "It lets users choose countries and economic indicators, view historical "
        "trends, and compare markets side by side."
    ),
    "interactive_portfolio": (
        "The interactive portfolio website is the site you are using now. I built "
        "it as a game-style room where visitors move a character around and "
        "interact with objects to open sections like Projects, Resume, About Me, "
        "Interests, and Contact. It uses HTML, CSS, and JavaScript."
    ),
    "crossy_road": (
        "The Crossy Road style game is a browser game project with character "
        "movement, obstacles, collision detection, scoring, and custom character "
        "animations. It helped me practice JavaScript game logic and interactive "
        "frontend development."
    ),
    "python": (
        "Yes. Python is one of my main programming languages. I have used it for "
        "backend development, Flask apps, API work, automation, and data-focused "
        "projects like MarketScope."
    ),
    "javascript": (
        "Yes. I use JavaScript for interactive frontend projects, including this "
        "game-style portfolio and browser-based game mechanics such as movement, "
        "collisions, UI interactions, and animations."
    ),
    "flask": (
        "Yes. I use Flask for lightweight Python backends and API routes, including "
        "the Portfolio Assistant backend that receives chat messages and returns "
        "JSON responses."
    ),
    "apis": (
        "I have experience working with APIs and webhooks, including the World Bank "
        "API for MarketScope, OpenAI APIs, Gemini APIs, Zapier, and Twilio webhooks."
    ),
    "git_github": (
        "I use Git and GitHub for version control, organizing projects, sharing code, "
        "and deploying static sites with GitHub Pages."
    ),
    "major": (
        "My major is Business Administration at Carnegie Mellon University."
    ),
    "minor": (
        "My minor is Artificial Intelligence Studies through Carnegie Mellon's "
        "School of Computer Science."
    ),
    "cmu": (
        "I go to Carnegie Mellon University. I am studying Business Administration "
        "with a minor in Artificial Intelligence Studies."
    ),
    "what_can_i_ask": (
        "You can ask me about my projects, MarketScope, the interactive portfolio "
        "website, the Crossy Road style game, Python, JavaScript, Flask, APIs, Git "
        "and GitHub, Carnegie Mellon, my major, my minor, my resume, contact "
        "information, or interests."
    ),
    "who_are_you": (
        "I am Takashi's Portfolio Assistant, a simple rule-based chatbot that helps "
        "visitors learn about his projects, skills, education, resume, contact "
        "information, and interests."
    ),
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
# Specific categories come before broad categories so detailed questions win.
KEYWORDS = {
    "marketscope": [
        "marketscope",
        "market scope",
        "world bank",
        "economic indicator",
        "economic indicators",
        "market dashboard",
        "global market",
        "global markets",
        "how does marketscope work",
        "tell me about marketscope",
    ],
    "interactive_portfolio": [
        "interactive portfolio",
        "portfolio website",
        "portfolio site",
        "game style portfolio",
        "game style website",
        "game portfolio",
        "this website",
        "this site",
        "this portfolio",
        "website you built",
    ],
    "crossy_road": [
        "crossy road",
        "crossy road style",
        "browser game",
        "obstacle game",
        "collision game",
        "scoring game",
        "character movement",
    ],
    "python": [
        "python",
        "do you know python",
        "know python",
        "use python",
        "python experience",
    ],
    "javascript": [
        "javascript",
        "java script",
        "js",
        "do you know javascript",
        "know javascript",
        "use javascript",
        "javascript experience",
        "frontend",
        "front end",
    ],
    "flask": [
        "flask",
        "do you know flask",
        "know flask",
        "use flask",
        "flask backend",
    ],
    "apis": [
        "api",
        "apis",
        "webhook",
        "webhooks",
        "openai api",
        "gemini api",
        "twilio webhook",
        "zapier",
    ],
    "git_github": [
        "git",
        "github",
        "github pages",
        "version control",
        "repository",
        "repositories",
        "repo",
        "repos",
    ],
    "major": [
        "major",
        "business major",
        "what is your major",
        "what are you majoring in",
    ],
    "minor": [
        "minor",
        "ai minor",
        "artificial intelligence minor",
        "what is your minor",
        "what are you minoring in",
    ],
    "cmu": [
        "cmu",
        "carnegie",
        "carnegie mellon",
        "where do you go to school",
        "where do you study",
        "what do you study",
        "school",
        "college",
        "university",
        "student",
    ],
    "resume": [
        "resume",
        "cv",
        "where is your resume",
        "view resume",
        "open resume",
        "download resume",
    ],
    "contact": [
        "contact",
        "email",
        "linkedin",
        "reach",
        "connect",
        "get in touch",
        "how can i contact",
        "how do i contact",
    ],
    "interests": [
        "interest",
        "interests",
        "hobby",
        "hobbies",
        "what are your hobbies",
        "outside of work",
        "football",
        "viola",
        "strength training",
        "gaming",
        "writing",
        "like",
        "enjoy",
    ],
    "what_can_i_ask": [
        "what can i ask",
        "what should i ask",
        "what can you answer",
        "what do you know",
        "help",
        "topics",
        "question",
        "questions",
    ],
    "who_are_you": [
        "who are you",
        "what are you",
        "portfolio assistant",
        "chatbot",
        "bot",
    ],
    "projects": [
        "project",
        "projects",
        "built",
        "build",
        "made",
        "portfolio",
        "game",
        "what have you built",
        "what projects have you made",
        "what did you build",
        "what have you made",
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
        "what languages do you know",
        "what can you code",
    ],
    "education": [
        "education",
        "study",
        "studying",
    ],
    "experience": ["experience", "work", "job", "jobs", "background"],
    "greeting": ["hello", "hi", "hey"],
}


DEFAULT_REPLY = (
    "I am not sure about that yet. Try asking about projects, skills, education, "
    "experience, interests, contact information, or resume."
)


def normalize_message(message):
    """Normalize a message so punctuation-heavy questions still match."""
    return re.sub(r"[^a-z0-9+#]+", " ", message.lower()).strip()


def message_matches_keywords(message, keywords):
    """Check whether a message contains any complete keyword from a list."""
    for keyword in keywords:
        normalized_keyword = normalize_message(keyword)
        pattern = r"\b" + re.escape(normalized_keyword) + r"\b"
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

    cleaned_message = normalize_message(message)

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
