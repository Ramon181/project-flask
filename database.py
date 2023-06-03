from psycopg2 import connect
from models.users import users
from models.songs import songs
from models.artist import artist

host = "localhost"
port = 5432
dbname = "music"
user = "postgres"
password = "12345"

def get_Connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

def create_tables():
    conn = get_Connection()
    cur = conn.cursor()
    cur.execute(users)
    cur.execute(songs)
    cur.execute(artist)
    conn.commit()
    cur.close()
    conn.close()