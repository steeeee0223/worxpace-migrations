import pymongo
from pydantic_settings import BaseSettings, SettingsConfigDict


class ENV(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    mongo_uri: str


def get_connection():
    env = ENV()
    conn = pymongo.MongoClient(env.mongo_uri)
    return conn
