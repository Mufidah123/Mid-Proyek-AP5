# koneksi MySQL
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv(""),
    port=int(os.getenv("DB_PORT"))
)
cursor = db.cursor()

# Mengecek koneksi database ke Python
#if db.is_connected():
#   print("berhasil.")

# Buat database
# cursor.execute("CREATE DATABASE game_adventure")
# print("Database berhasil dibuat")

# Buat tabel dalam database
# 1. Tabel user
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL UNIQUE,
#         password_hash TEXT NOT NULL
#     )
# ''')

# # 2. Tabel karakter dalam game
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS characters (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER NOT NULL UNIQUE,
#         role TEXT NOT NULL,
#         hp INTEGER NOT NULL,
#         max_hp INTEGER NOT NULL,
#         energi INTEGER NOT NULL,
#         max_energi INTEGER NOT NULL,
#         deff INTEGER NOT NULL,
#         damage INTEGER NOT NULL,
#         gold INTEGER DEFAULT 10,
#         exp INTEGER DEFAULT 0,
#         score INTEGER DEFAULT 0,
#         title TEXT DEFAULT 'Newbie',
#         current_floor INTEGER DEFAULT 1,
#         FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
#     )
# ''')

# # 3. Tabel item untuk karakter
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS inventory (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         character_id INTEGER NOT NULL,
#         item_name TEXT NOT NULL,
#         quantity INTEGER NOT NULL,
#         FOREIGN KEY (character_id) REFERENCES characters (id) ON DELETE CASCADE
#     )
# ''')