# Prompt Log

## AI Tool Used
Codex in VS Code

---

## Prompt 1: Create the Flask Backend

I am completing a college homework assignment where I need to build and deploy a backend and connect it to a frontend.

I already have an existing personal portfolio website that will eventually be the frontend. For now, we are ONLY building the backend.

I want to make a simple rule-based Portfolio Assistant chatbot. Do NOT use an AI API, database, authentication, or any external API. I want this to be simple and reliable.

Use Python and Flask.

Create the following files:

app.py
requirements.txt
.gitignore

The backend should have two routes:

1. GET /
This should return JSON confirming that the Portfolio Assistant backend is running.

Example:
{
  "status": "Portfolio Assistant backend is running"
}

2. POST /chat
This route should accept JSON in this format:

{
  "message": "What projects have you built?"
}

It should analyze the user's message using simple keyword-based logic and return JSON in this format:

{
  "reply": "..."
}

Create responses for these categories:

projects
skills
education
experience
interests
contact
resume
greeting

For now, use placeholder information for the actual personal details and clearly label the section in app.py where I should replace the placeholders with my real information.

If the message does not match a category, return a friendly default response explaining that the user can ask about projects, skills, education, experience, interests, contact information, or resume.

Requirements:

- Use Flask
- Use flask-cors and enable CORS so my GitHub Pages frontend can eventually communicate with this backend
- Validate that the message exists
- Handle empty messages
- Return appropriate JSON error messages
- Include a standard if __name__ == "__main__" block for local development
- Make the code straightforward and beginner-friendly
- Add comments explaining the important sections
- requirements.txt must include everything necessary for deployment to Render, including gunicorn
- .gitignore should ignore .venv, __pycache__, .env, .DS_Store, and other common Python files
- Do not add unnecessary complexity
- Do not create frontend files yet

After creating the files, explain exactly what you created and tell me the command I should use to run the backend locally.

---

## Prompt 2: Replace Placeholder Information With Real Portfolio Information

The Flask backend is working correctly and I have tested the /chat endpoint.

Now replace the placeholder Portfolio Assistant responses in app.py with real portfolio information.

Use the following information:

Education:
I am a student at Carnegie Mellon University studying Business with a minor in Artificial Intelligence through the School of Computer Science.

Projects:
1. Interactive Portfolio Website
A game-style personal portfolio where the visitor controls a character and walks around a room to interact with my projects, resume, interests, and contact information. Built with HTML, CSS, and JavaScript.

2. MarketScope
A web application that uses World Bank API data to let users explore and compare economic indicators between countries. It includes country and indicator selection and displays historical economic data.

3. Crossy Road Style Game
A browser-based game inspired by Crossy Road with character movement, obstacles, collisions, scoring, and custom character animations.

Skills:
Python, HTML, CSS, JavaScript, Flask, working with APIs, Git, GitHub, GitHub Pages, and basic backend/frontend web development.

Interests:
Entrepreneurship, business, technology, artificial intelligence, football, viola, and building software projects.

Contact:
Do not hardcode any private contact information. Tell users that my GitHub, LinkedIn, and email links are available in the Contact section of the portfolio.

Resume:
Tell users that my resume can be opened from the Resume section of the portfolio.

Experience:
Keep this response general. Tell users that information about my experience can be found in my portfolio and resume. Do not invent jobs or experiences that have not been provided.

Greeting:
Make this friendly and short. Explain that the Portfolio Assistant can answer questions about my projects, skills, education, experience, interests, resume, or contact information.

Default response:
Keep the current idea, but make it concise and friendly.

Also improve the keyword lists so that natural questions work. For example:

projects:
project, projects, built, build, made, portfolio, marketscope, game

skills:
skill, skills, know, programming, language, languages, code, coding, technology, technologies

education:
education, school, college, university, cmu, carnegie, major, minor, study, studying

experience:
experience, work, job, jobs, background

interests:
interest, interests, hobby, hobbies, like, enjoy

contact:
contact, email, github, linkedin, reach, connect

resume:
resume, cv

greeting:
hello, hi, hey

Do not change the Flask routes or working request/response structure. Do not add an AI API, database, authentication, or any additional dependencies.

Keep the code beginner-friendly and easy to understand.

---

## Prompt 3: Add the Chatbot to the Existing Portfolio

I have an existing personal portfolio website that is already working and deployed on GitHub Pages.

This portfolio is an interactive game-style website, so I do NOT want you to redesign the site or change any existing game logic, movement, collisions, interactions, project sections, resume behavior, or other existing functionality.

I need to add one small new feature for a homework assignment: a Portfolio Assistant chatbot.

My backend is already deployed and working at:

https://portfolio-assistant-backend-sqp8.onrender.com

It accepts POST requests at:

https://portfolio-assistant-backend-sqp8.onrender.com/chat

The request format is:

{
  "message": "What projects have you built?"
}

The response format is:

{
  "reply": "response text here"
}

First inspect my existing HTML, CSS, and JavaScript files so you understand how the portfolio is structured.

Then add a small chatbot interface to the existing portfolio.

Requirements:

1. Add a small fixed button in the bottom-right corner labeled:
"Ask About Me"

2. Clicking the button should open a compact chat panel.

3. The chat panel should include:
- Title: Portfolio Assistant
- A short welcome message
- Conversation area
- Text input
- Send button
- Close button

4. When the user sends a message, use fetch() to POST to:
https://portfolio-assistant-backend-sqp8.onrender.com/chat

5. Send JSON in this exact format:
{
  "message": userMessage
}

6. Display the "reply" returned by the backend inside the chat.

7. Allow pressing Enter to send a message.

8. Prevent empty messages from being submitted.

9. While waiting for the backend response, show:
"Thinking..."

10. If the backend cannot be reached, display:
"Sorry, the Portfolio Assistant is unavailable right now. Please try again."

11. Style the chatbot so it fits the visual style of my existing portfolio rather than looking like a completely separate website.

12. Keep it compact so it does not obstruct the main game.

13. Do not install any frameworks or libraries.

14. Use only the HTML, CSS, and JavaScript structure already in my project.

15. Most importantly, do not modify or break any existing portfolio functionality. Only add what is necessary for the chatbot.

16. If possible, keep the chatbot code isolated and clearly labeled in the existing files so it is easy to understand what was added.

After making the changes, explain exactly which files you edited and what you added to each one.

Do not deploy anything yet. I want to test the chatbot locally first.

---

## Prompt 4: Improve the Rule-Based Chatbot Logic

Improve the rule-based chatbot logic in app.py so the Portfolio Assistant feels smarter and handles more realistic questions.

Do not change the Flask routes, request/response format, frontend, or dependencies.

Keep it simple and rule-based.

Add more specific handling for these topics:

- MarketScope
- interactive portfolio website
- Crossy Road style game
- Python
- JavaScript
- Flask
- APIs
- Git and GitHub
- Carnegie Mellon / CMU
- major
- minor
- resume
- contact
- interests
- "what can I ask?"
- "who are you?"

Important:
Specific questions should be checked before broad categories.

For example:
- "Tell me about MarketScope" should return a MarketScope-specific answer
- "Do you know Python?" should return a Python-specific answer
- "What is your major?" should return the Business major answer
- "What is your minor?" should return the AI minor answer
- "How does MarketScope work?" should not accidentally match a general experience category

Also add more natural variations of common questions, such as:
- what have you built
- what projects have you made
- what languages do you know
- do you know Python
- do you know JavaScript
- where do you go to school
- what do you study
- how can I contact you
- where is your resume
- what are your hobbies
- what can I ask
- who are you

Keep all current working functionality.
Do not add AI, databases, authentication, external APIs, or new libraries.

After making the changes, explain what logic you added.