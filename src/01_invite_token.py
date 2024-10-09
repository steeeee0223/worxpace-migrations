from pydantic_settings import BaseSettings, SettingsConfigDict

from config import get_connection


class ENV(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    mongo_uri: str


def main():
    conn = get_connection()
    session = conn.start_session()
    db = session.client.get_database()

    collection = db.get_collection("Workspace")
    for doc in collection.find():
        res = collection.update_one(
            filter={"_id": doc["_id"]}, update={"$set": {"inviteToken": doc["_id"]}}
        )
        print(f"Modified: {res.raw_result}")

    conn.close()


if __name__ == "__main__":
    main()
