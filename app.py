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
    role_id = data.get("role_id")

    if not username or not email or not role_id:
        return jsonify({
            "error": "username, email и role_id обязательны"
        }), 400

    db = get_db()
    cursor = db.cursor()

    # Проверка уникальности
    cursor.execute(
        "SELECT id FROM users WHERE username = %s OR email = %s",
        (username, email)
    )
    if cursor.fetchone():
        return jsonify({"error": "Пользователь уже существует"}), 409

    # Создание пользователя
    cursor.execute(
        "INSERT INTO users (username, email, role_id) VALUES (%s, %s, %s)",
        (username, email, role_id)
    )
    user_id = cursor.lastrowid

    # Логирование
    cursor.execute(
        "INSERT INTO logs (user_id, action) VALUES (%s, %s)",
        (user_id, "create_user")
    )

    db.commit()
    return jsonify({"status": "ok", "user_id": user_id}), 201


@app.route("/users", methods=["GET"])
def list_users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT u.id, u.username, u.email, r.name as role
        FROM users u
        LEFT JOIN roles r ON u.role_id = r.id
        """
    )
    users = cursor.fetchall()
    return jsonify(users), 200


if __name__ == "__main__":
    app.run(debug=True)
