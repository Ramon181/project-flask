from flask import Blueprint, request, jsonify
from psycopg2 import extras
from database import get_Connection
from cryptography.fernet import Fernet

users_bp = Blueprint("users", __name__)

key = Fernet.generate_key()


@users_bp.get("/users")
def get_users():
    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    conn.close()
    return jsonify(users)


@users_bp.post("/users")
def post_users():
    newUser = request.get_json()
    userName = newUser["userName"]
    email = newUser["email"]
    password = Fernet(key).encrypt(bytes(newUser["password"], "utf-8"))

    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(
        "INSERT INTO users (userName, email, password) VALUES (%s, %s, %s) RETURNING *",
        (userName, email, password),
    )
    newUser = cur.fetchone()
    print(newUser)
    conn.commit()
    cur.close()
    conn.commit()

    return jsonify(newUser)


@users_bp.put("/users/<id>")
def put_users(id):
    newUser = request.get_json()
    userName = newUser["userName"]
    email = newUser["email"]
    password = Fernet(key).encrypt(bytes(newUser["password"], "utf-8"))
    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(
        "UPDATE users SET userName = %s, email = %s, password = %s WHERE id = %s RETURNING *",
        (userName, email, password, id),
    )
    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.commit()

    if user is None:
        return jsonify({"message": "User not found"}), 404
    return user


@users_bp.delete("/users/<id>")
def delete_users(id):
    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("DELETE FROM users WHERE id = %s RETURNING *", (id,))
    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if user is None:
        return jsonify({"message": "user not found"}), 404
    return jsonify({"message": "user delete"})


@users_bp.get("/users/<id>")
def patch_users(id):
    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cur.fetchone()

    if user is None:
        return jsonify({"message": "user not found"}), 404
    return jsonify(user)
