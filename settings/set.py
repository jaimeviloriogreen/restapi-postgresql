from dotenv import load_dotenv
from os import getenv

load_dotenv()

dataConnection = dict(
    dbname=getenv("DATABASE"),
    user=getenv("USER"),
    port=getenv("PORT"),
    password=getenv("PASSWORD"),
    host=getenv("HOST")
)