import psycopg2
conn = psycopg2.connect(database = "eczane", user = "postgres", password = "Yigit1323?", host = "127.0.0.1", port = "5432")
cur = conn.cursor()