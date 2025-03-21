import requests # type: ignore

SERVER_URL = "http://127.0.0.1:5000"

# Mengunggah file pertanyaan ke server
def upload_file(filename):
    with open(filename, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{SERVER_URL}/upload_questions", files=files)
        print(response.json())

# Mengunduh file pertanyaan dari server
def download_file(filename):
    response = requests.get(f"{SERVER_URL}/download_questions")
    with open(filename, "wb") as f:
        f.write(response.content)
    print("File downloaded successfully")

# Contoh penggunaan
upload_file("questions.json")  # Unggah database pertanyaan ke server
download_file("downloaded_questions.json")  # Unduh dari server
