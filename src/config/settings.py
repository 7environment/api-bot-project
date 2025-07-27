from os import getenv
from dotenv import load_dotenv

class settings:
    def __init__(self):
        load_dotenv()
        self.BOT_TOKEN = getenv("BOT_TOKEN")
        self.DB_HOST = getenv("DB_HOST")
        self.DB_PORT = getenv("DB_PORT")
        self.DB_USER = getenv("DB_USER")
        self.DB_PASS = getenv("DB_PASS")
        self.DB_NAME = getenv("DB_NAME")
        #self.DATABASE_URL_asyncpg = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        self.DATABASE_URL_asyncpg = "postgresql+asyncpg://sw_test_user:ZACZq7yfm7frt9GTg6hHjUttjSkk5UKG@dpg-d22rl1e3jp1c7397ogt0-a.oregon-postgres.render.com/sw_test"