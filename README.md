# AI Chatbot MVP

## 1. Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js (optional, for advanced frontend tooling)
- OpenAI API key (for live AI responses)

### Installation

#### Backend (Flask)
1. **Create and activate a virtual environment:**
   ```bash
   python -m venv backend/venv
   backend/venv/Scripts/activate  # On Windows
   # Or: source backend/venv/bin/activate  # On Mac/Linux
   ```
2. **Install dependencies:**
   ```bash
   backend/venv/Scripts/pip install flask flask-cors openai
   ```
3. **Configure your OpenAI API key:**
   - Open `backend/app.py` and set your API key in the `OPENAI_API_KEY` variable.
   - **(Recommended for production):** Use an environment variable or `.env` file and load it securely.

4. **Run the backend server:**
   ```bash
   backend/venv/Scripts/python backend/app.py
   ```
   The server will run at [http://127.0.0.1:5000](http://127.0.0.1:5000)

#### Frontend (HTML/JS)
1. **Serve the frontend using Python's HTTP server:**
   ```bash
   cd frontend
   python -m http.server 8000
   ```
2. **Open your browser and go to:**
   [http://localhost:8000](http://localhost:8000)

---

## 2. Technical Choices

- **Flask over FastAPI:**
  - Chosen for its simplicity, quick setup, and wide adoption for MVPs and prototypes.
  - Flask is lightweight, easy to understand, and has a large ecosystem (e.g., Flask-CORS for CORS support).
  - FastAPI is excellent for async and type-checked APIs, but Flask is more approachable for rapid prototyping and small teams.
- **Vanilla HTML/CSS/JS Frontend:**
  - No build step or framework required, so it's easy to run and modify.
  - Modern JS and CSS features are used for a clean, responsive UI.
- **OpenAI API:**
  - Provides state-of-the-art conversational AI with minimal setup.
- **LocalStorage for Chat History:**
  - Simple persistence for user experience without a database.

---

## 3. Notes on Limitations and Future Improvements

### Limitations
- **No authentication:** Anyone can use the chatbot if deployed as-is.
- **No persistent server-side chat history:** Chat history is only stored in the browser (localStorage).
- **No admin panel or analytics.**
- **No rate limiting or abuse protection.**
- **OpenAI API key is stored in code for MVP (should be secured in production).**
- **No file upload or advanced media support.**

### Future Improvements
- Add user authentication (OAuth, email/password, etc.).
- Store chat history in a database (e.g., SQLite, PostgreSQL, MongoDB).
- Add an admin dashboard for analytics and moderation.
- Support for multiple users and sessions.
- Add more advanced error handling and logging.
- Integrate with other AI providers or fallback models.
- Add support for file uploads, images, or voice.
- Deploy to cloud (Heroku, Azure, AWS, etc.) with secure environment variable management.
- Add unit and integration tests.
- Improve accessibility and internationalization.

---

**For questions or contributions, please open an issue or pull request on GitHub.** 
