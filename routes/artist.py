from flask import Blueprint, request, jsonify
from psycopg2 import extras
from database import get_Connection

artist_bp = Blueprint('artist', __name__)

@artist_bp.get("/artist")
def get_artist():
    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("SELECT * FROM artist")
    artists = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(artists)

@artist_bp.post("/artist")
def add_artist():
    newArtist = request.get_json()
    name = newArtist["name"]
    print(name)
    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("INSERT INTO artist (name) VALUES ('%s') RETURNING *" % name)
    artist = cur.fetchone()
    print(artist)
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(artist)

@artist_bp.put("/artist/<id>")
def update_artist(id):
    newArtist = request.get_json()
    name = newArtist["name"]
    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("UPDATE artist SET name = %s WHERE id = %s RETURNING *", (name,id))
    artist = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if artist is None:
        return jsonify({"message": "Artist not found"}), 404
    return jsonify(artist)

@artist_bp.delete("/artist/<id>")
def delete_artist(id):
    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("DELETE FROM artist WHERE id = %s", (id,))
    artist = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if artist is None:
        return jsonify({"message": "Artist not found RETURNING *"}), 404
    return jsonify({"message": "Artist deleted"})

@artist_bp.get("/artist/<id>")
def get_artist_by_id(id):
    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("SELECT * FROM artist WHERE id = %s", (id,))
    artist = cur.fetchone()
    cur.close()
    conn.close()
    if artist is None:
        return jsonify({"message": "Artist not found"}), 404
    return jsonify(artist)
