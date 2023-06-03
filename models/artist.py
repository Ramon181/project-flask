artist = """
        CREATE TABLE IF NOT EXISTS artist (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(250) NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """