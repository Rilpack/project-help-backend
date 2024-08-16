from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db_url: str = "postgresql://postgres:2341@localhost:5432/ProjectHelp"
    db_url_echo: bool = True


settings = Setting()
