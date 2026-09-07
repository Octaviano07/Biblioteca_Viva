📚 Biblioteca Viva

Biblioteca Viva is a web platform for literary expression built with Python and Flask, combining web development, database management, and creative writing.

The project started as a small blog built with HTML, CSS, and JavaScript and evolved into a Flask-based application with administrator authentication, post management, and image uploads.

«This project represents one of my first experiences building a more complete Flask application.»

---

✨ Features

- 📖 Literary post browsing
- 🔐 Administrator login
- ✍️ Create posts
- 📝 Edit posts
- 🗑️ Delete posts
- 🖼️ Image uploads
- 🗄️ SQLite database
- 📅 Automatic post timestamps
- 🔒 Environment-based configuration
- 📱 Web interface for reading and managing content

---

🛠️ Technologies

Backend

- Python
- Flask
- SQLite
- python-dotenv
- Werkzeug

Frontend

- HTML5
- CSS3
- JavaScript

Other

- Git
- GitHub
- Gunicorn

---

```
🗂️ Project Structure

Biblioteca_Viva/
│
├── static/
│   ├── uploads/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── post.html
│   ├── login.html
│   ├── admin.html
│   ├── add.html
│   └── edit.html
│
├── .env.example
├── .gitignore
├── README.md
├── app.py
├── init_db.py
└── requirements.txt
```

«The structure above represents the main organization of the project. Individual files may vary between versions.»

---

🧠 How It Works

The application uses Flask to handle routes and process HTTP requests.

Posts are stored in a SQLite database containing information such as:

- title;
- category;
- summary;
- content;
- image;
- publication date.

The administrator can access a protected area to create, edit, and delete posts.

Uploaded images are stored in the "static/uploads/" directory.

---

🔐 Environment Variables

The administrator credentials and session secret key are configured through environment variables.

Create a ".env" file based on ".env.example":

ADMIN_USER=your_username
ADMIN_PASS=your_password
SECRET_KEY=your_secret_key

Never commit your ".env" file to GitHub.

For real-world deployments, use a strong password and a randomly generated "SECRET_KEY".

---

🚀 Getting Started

1. Clone the repository

git clone https://github.com/Octaviano07/Biblioteca_Viva.git
cd Biblioteca_Viva

2. Create a virtual environment

python -m venv venv

Activate the virtual environment.

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Configure the environment

Create a ".env" file containing:

ADMIN_USER=your_username
ADMIN_PASS=your_password
SECRET_KEY=your_secret_key

5. Run the application

python app.py

Then open:

http://127.0.0.1:5000

---

🌿 Project Evolution

Biblioteca Viva has two main stages of development.

"blog_V1"

The first version was primarily a frontend project.

Posts were stored as JavaScript data, allowing the application to simulate a small dynamic blog.

"main"

The project later evolved into a Flask-based backend application.

New functionality was introduced, including:

- SQLite database integration;
- administrator authentication;
- CRUD operations for posts;
- image uploads;
- post editing and deletion;
- environment variables;
- server-side request processing.

This evolution marked my transition from primarily frontend projects to applications involving backend development and persistent data storage.

---

🔎 What I Learned

This project helped me develop a better understanding of:

- building applications with Flask;
- defining routes;
- working with templates;
- integrating SQLite;
- implementing CRUD operations;
- basic authentication;
- session management;
- file uploads;
- environment variables;
- web application structure;
- communication between the frontend, backend, and database.

It was also one of the projects that taught me the importance of separating responsibilities within an application — an approach that I started applying more systematically in later projects.

---

🔒 Security Considerations

Biblioteca Viva was developed primarily as a learning project.

Some aspects still need improvement before the application could be considered production-ready, including:

- password hashing;
- CSRF protection;
- stricter file validation;
- upload size limits;
- more appropriate HTTP methods for destructive operations;
- better separation of application responsibilities;
- more comprehensive error handling;
- automated testing.

These areas represent part of the project's natural evolution and provide opportunities for future improvements.

---

🚧 Future Improvements

- [ ] Separate routes into modules/Blueprints
- [ ] Create a dedicated database layer
- [ ] Introduce ORM models
- [ ] Implement password hashing
- [ ] Add CSRF protection
- [ ] Add automated tests
- [ ] Improve image validation
- [ ] Add post pagination
- [ ] Implement search functionality
- [ ] Improve the admin dashboard
- [ ] Introduce database migrations

---

📌 Status

🟢 Functional and evolving

Biblioteca Viva represents an important stage in my learning journey with Python, Flask, databases, and web development.

---

👨‍💻 Author

Octaviano

Student of Biology and Chemistry with interests in:

- 🧬 Bioinformatics
- 🤖 Artificial Intelligence
- 🐍 Python
- 🌐 Web Development
- 📊 Data and Machine Learning

---

«Biblioteca Viva — where code and writing meet. 📚💻»