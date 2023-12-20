import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT", 5432)
DB_NAME = os.getenv("DB_NAME", "template1")