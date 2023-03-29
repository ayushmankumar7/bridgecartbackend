from pydantic import BaseSettings


class Config(BaseSettings):
    API_V1_STR: str = "/api/v1"
    USER_TABLE_STR: str = 'users'


config = Config()
