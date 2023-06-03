songs = """
        CREATE TABLE IF NOT EXISTS songs (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(250) NOT NULL,
            artist_id INTEGER REFERENCES artist(id) NOT NULL,
            img VARCHAR(250) NOT NULL,
            archivo_mp3 VARCHAR(250) NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """