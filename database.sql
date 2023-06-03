        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(250) NOT NULL,
            artista_id INTEGER REFERENCES artistas(id) NOT NULL,
            img VARCHAR(250) NOT NULL,
            archivo_mp3 BYTEA,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
