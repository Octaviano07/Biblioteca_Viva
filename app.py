from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# =========================
# CONFIG
# =========================
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_PASS = os.getenv("ADMIN_PASS")


# =========================
# FUNÇÕES AUXILIARES
# =========================
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# =========================
# HOME
# =========================
@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts ORDER BY id DESC")
    posts = cursor.fetchall()

    conn.close()

    return render_template("index.html", posts=posts)


# =========================
# SOBRE
# =========================
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


# =========================
# POST INDIVIDUAL
# =========================
@app.route("/post/<int:id>")
def post(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts WHERE id=?", (id,))
    post = cursor.fetchone()

    conn.close()

    return render_template("post.html", post=post)


# =========================
# LOGIN
# =========================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == ADMIN_USER and password == ADMIN_PASS:
            session["admin"] = True
            return redirect(url_for("admin"))

        return "Login inválido"

    return render_template("login.html")


# =========================
# ADMIN
# =========================
@app.route("/admin")
def admin():

    if not session.get("admin"):
        return redirect(url_for("login"))

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts ORDER BY id DESC")
    posts = cursor.fetchall()

    conn.close()

    return render_template("admin.html", posts=posts)


# =========================
# CREATE POST
# =========================
@app.route("/create", methods=["GET", "POST"])
def create_post():

    if not session.get("admin"):
        return redirect(url_for("login"))

    if request.method == "POST":

        titulo = request.form["titulo"]
        categoria = request.form["categoria"]
        resumo = request.form["resumo"]
        conteudo = request.form["conteudo"]

        file = request.files.get("imagem")

        filename = "default.jpg"

        if file and file.filename != "" and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            # 🔐 evita sobrescrever ficheiros
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

            count = 1
            while os.path.exists(filepath):
                name, ext = os.path.splitext(filename)
                filename = f"{name}_{count}{ext}"
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                count += 1

            file.save(filepath)

        # guardar no banco
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO posts (titulo, categoria, resumo, conteudo, imagem)
            VALUES (?, ?, ?, ?, ?)
        """, (titulo, categoria, resumo, conteudo, filename))

        conn.commit()
        conn.close()

        return redirect(url_for("admin"))

    return render_template("create_post.html")


# =========================
# EDIT
# =========================
import os

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_post(id):

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # buscar post atual
    c.execute("SELECT * FROM posts WHERE id=?", (id,))
    post = c.fetchone()

    old_image = post[5]  # coluna imagem

    if request.method == "POST":

        titulo = request.form["titulo"]
        categoria = request.form["categoria"]
        resumo = request.form["resumo"]
        conteudo = request.form["conteudo"]

        file = request.files.get("imagem")

        if file and file.filename != "":

            # 1. apagar imagem antiga
            if old_image:
                old_path = os.path.join(app.config["UPLOAD_FOLDER"], old_image)

                if os.path.exists(old_path):
                    os.remove(old_path)

            # 2. guardar nova imagem
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            # 3. atualizar tudo
            c.execute("""
                UPDATE posts
                SET titulo=?, categoria=?, resumo=?, conteudo=?, imagem=?
                WHERE id=?
            """, (titulo, categoria, resumo, conteudo, filename, id))

        else:
            # sem mexer na imagem
            c.execute("""
                UPDATE posts
                SET titulo=?, categoria=?, resumo=?, conteudo=?
                WHERE id=?
            """, (titulo, categoria, resumo, conteudo, id))

        conn.commit()
        conn.close()

        return redirect("/admin")

    conn.close()
    return render_template("edit_post.html", post=post)

# =========================
# DELETE
# =========================
@app.route("/delete/<int:id>")
def delete_post(id):

    if not session.get("admin"):
        return redirect(url_for("login"))

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM posts WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("admin"))


# =========================
# LOGOUT
# =========================
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("login"))


# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)