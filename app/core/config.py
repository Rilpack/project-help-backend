from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 20


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = "postgresql://postgres:2341@localhost:5432/ProjectHelp"
    auth_jwt: AuthJWT = AuthJWT()


settings = Setting()
