users = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY NOT NULL,
            userName VARCHAR(250) NOT NULL,
            email VARCHAR(250) NOT NULL,
            password VARCHAR(250) NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """
