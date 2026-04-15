AI Book App 📚🤖

This is a simple AI-powered book app that I built using Django REST Framework.
It allows users to store books, ask questions, get summaries, and even get recommendations using an LLM.

---

🚀 Features

- Add books with title, author, description, and rating
- View all stored books
- Ask questions using RAG (Retrieval-Augmented Generation)
- Get AI-based summaries
- Get book recommendations
- Simple UI using HTML, CSS, and JavaScript

---

🧠 How it works

The app stores book data in a database.
When a user asks a question, it:

1. Fetches relevant book descriptions
2. Builds a context from the data
3. Sends it to an LLM (Mistral model running locally)
4. Returns the generated answer

---

🛠️ Tech Stack

- Backend: Django REST Framework
- Frontend: HTML, CSS, JavaScript
- AI Model: Mistral 7B (via local API)
- Database: SQLite

---

📂 Project Structure

- "views.py" → API logic
- "models.py" → Book model
- "serializers.py" → Data serialization
- "urls.py" → API routes
- "index.html" → Frontend UI

---

⚙️ Setup Instructions

1. Clone the repository
2. Install dependencies
   pip install -r requirements.txt
3. Run migrations
   python manage.py migrate
4. Start the server
   python manage.py runserver

Make sure your local LLM server is running at:

http://127.0.0.1:1234

---

🔗 API Endpoints

- "/api/books/" → Get all books
- "/api/books/add/" → Add a book
- "/api/rag/" → Ask questions
- "/api/ai-summary/" → Get summary
- "/api/recommend/" → Get recommendations

---

💡 Future Improvements

- Better UI (React or Tailwind)
- Deploy on cloud
- Add authentication
- Improve search relevance

---

🙌 Final Thoughts

This project helped me understand how RAG works and how to integrate LLMs with real applications.
Still improving it step by step 🚀
