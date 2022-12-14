from pydantic import BaseSettings

class Settings(BaseSettings):
    debug: bool = False
    environment: str
    s3_url: str

    class Config:
        env_file = ".env"