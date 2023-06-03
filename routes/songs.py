from flask import Blueprint, request, jsonify
from psycopg2 import extras
from database import get_Connection

songs_bp = Blueprint("songs", __name__)


@songs_bp.get("/songs")
def get_songs():
    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("SELECT * FROM songs")
    songs = cur.fetchall()
    conn.close()
    return jsonify(songs)


@songs_bp.post("/songs")
def add_song():
    # newSong = request.get_json()
    # name = newSong["name"]
    # artist_id = newSong["artist_id"]
    # img = newSong["img"]
    file = request.files['formData']
    print(file)

    # conn = get_Connection()
    # cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    # cur.execute(
    #     "INSERT INTO songs (name, artist_id, img, archivo_mp3) VALUES ('%s', '%s', '%s', '%s') RETURNING *",
    #     (name, artist_id, img, archivo_mp3),
    # )
    # song = cur.fetchone()
    # conn.commit()
    # conn.close()
    # cur.close()
    return jsonify("song")


@songs_bp.get("/songs/<int:song_id>")
def get_song(song_id):
    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("SELECT * FROM songs WHERE id = %s", (song_id,))
    song = cur.fetchone()
    conn.close()
    if song is None:
        return jsonify({"message": "Song not found"}), 404
    return jsonify(song)


@songs_bp.put("/songs/<int:song_id>")
def update_song(song_id):
    updatSong = request.get_json()
    name = updatSong["name"]
    artist_id = updatSong["artist_id"]
    img = updatSong["img"]
    archivo_mp3 = updatSong["archivo_mp3"]

    conn = get_Connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(
        "UPDATE songs SET name = %s, artist_id = %s, img = %s, archivo_mp3 = %s WHERE id = %s",
        (name, artist_id, img, archivo_mp3, song_id),
    )
    song = cur.fetchone()
    conn.commit()
    conn.close()
    cur.close()
    if song is None:
        return jsonify({"message": "Song not found"}), 404
    return jsonify({"message": "Song updated"}), 200
