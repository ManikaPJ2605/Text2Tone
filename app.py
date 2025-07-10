from flask import Flask, request, render_template, send_file, redirect, session, url_for
from elevenlabs import generate, voices, set_api_key
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

# Load .env and API Key
load_dotenv()
set_api_key(os.getenv("ELEVENLABS_API_KEY"))

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config["UPLOAD_FOLDER"] = "static"
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

def get_audio_history():
    return [f for f in os.listdir("static") if f.endswith(".mp3")]

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "Manika" and password == "Manika@2004":
            session["user"] = username
            return redirect(url_for("home"))
        return "Invalid credentials", 401
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect(url_for("login"))

    all_voices = voices()
    audio_url = None

    if request.method == "POST":
        text = request.form.get("text")
        selected_voice = request.form.get("voice")
        if text and selected_voice:
            audio = generate(text=text, voice=selected_voice)
            filename = secure_filename(os.urandom(16).hex() + ".mp3")
            path = os.path.join("static", filename)
            with open(path, "wb") as f:
                f.write(audio)
            audio_url = path

    return render_template("index.html", voices=all_voices, audio_url=audio_url, show_history_buttons=True)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["textfile"]
    voice = request.form["voice"]
    content = file.read().decode("utf-8")
    audio = generate(text=content, voice=voice)
    filename = secure_filename(os.urandom(16).hex() + ".mp3")
    path = os.path.join("static", filename)
    with open(path, "wb") as f:
        f.write(audio)
    return redirect("/")

@app.route("/clear_history")
def clear_history():
    for f in os.listdir("static"):
        if f.endswith(".mp3"):
            os.remove(os.path.join("static", f))
    return redirect("/history")

@app.route("/history")
def history():
    if "user" not in session:
        return redirect(url_for("login"))
    files = get_audio_history()
    return render_template("history.html", history=files)

if __name__ == "__main__":
    app.run(debug=True)