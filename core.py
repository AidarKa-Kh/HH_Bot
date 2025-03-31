from pydantic_settings import BaseSettings, SettingsConfigDict
from logs.log_conf import setup_logging


class Settings(BaseSettings):
    LOGIN: str
    PASSWORD: str

    BASE_URL: str

    FILE_PATH: str

    model_config = SettingsConfigDict(env_file=".env")

setup_logging()
settings = Settings()
