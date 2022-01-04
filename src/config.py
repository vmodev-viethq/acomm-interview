import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG: bool = os.getenv("DEBUG", False)
    PORT:int = os.getenv("PORT", 9999)
    HOST:str = os.getenv("HOST", '127.0.0.1')
