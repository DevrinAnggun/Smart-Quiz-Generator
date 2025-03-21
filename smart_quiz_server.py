import os
import json
import random
from flask import Flask, request, jsonify, send_file # type: ignore

app = Flask(__name__)
QUESTION_FILE = "questions.json"

# Cek apakah file database pertanyaan sudah ada, jika tidak buat default
if not os.path.exists(QUESTION_FILE):
    with open(QUESTION_FILE, "w") as f:
        json.dump([{"topic": "Sejarah", "question": "Siapa yang mendeklarasikan Proklamasi Indonesia?", "answer": "Soekarno-Hatta"}], f)

# Load pertanyaan dari file JSON
def load_questions():
    with open(QUESTION_FILE, "r") as f:
        return json.load(f)

def save_questions(questions):
    with open(QUESTION_FILE, "w") as f:
        json.dump(questions, f, indent=4)

@app.route("/get_question", methods=["GET"])
def get_question():
    questions = load_questions()
    question = random.choice(questions)
    return jsonify({"question": question["question"]})

@app.route("/upload_questions", methods=["POST"])
def upload_questions():
    if "file" not in request.files:
        return jsonify({"message": "No file provided"}), 400
    file = request.files["file"]
    file.save(QUESTION_FILE)
    return jsonify({"message": "File uploaded successfully"})

@app.route("/download_questions", methods=["GET"])
def download_questions():
    return send_file(QUESTION_FILE, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
