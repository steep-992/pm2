from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

def get_db():
    return pymysql.connect(
        host="192.168.0.2",
        user="steep992",
        password="aB94$2##aHi$&u92&354$B#^#8",
        database="flask_app",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Нет данных"}), 400

    username = data.get("username")
    email = data.get("email")

    if not username or not email:
        return jsonify({"error": "Некорректные данные"}), 400

    db = get_db()
    cursor = db.cursor()

    # 1. Проверка существования пользователя
    cursor.execute(
        "SELECT id FROM users WHERE username = %s OR email = %s",
        (username, email)
    )
    existing_user = cursor.fetchone()

    if existing_user:
        return jsonify({"error": "Пользователь уже существует"}), 409

    # 2. Создание пользователя
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (%s, %s)",
        (username, email)
    )
    user_id = cursor.lastrowid

    # 3. Логирование
    cursor.execute(
        "INSERT INTO logs (user_id, action) VALUES (%s, %s)",
        (user_id, "create_user")
    )

    db.commit()

    return jsonify({"status": "ok", "user_id": user_id}), 201

if __name__ == "__main__":
    app.run(debug=True)