from flask import Flask;
from flask_cors import CORS
from routes.users import users_bp
from routes.artist import artist_bp
from routes.songs import songs_bp
from database import create_tables

app=Flask(__name__)
CORS(app, origins='http://localhost:5173/')
app.register_blueprint(users_bp)
app.register_blueprint(artist_bp)
app.register_blueprint(songs_bp)


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)