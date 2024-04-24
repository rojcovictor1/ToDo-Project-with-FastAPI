from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def ASYNC_DATABASE_URL(self):
        return (f"postgresql+asyncpg://"
                f"{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:"
                f"{self.DB_PORT}/{self.DB_NAME}")

    class Config:
        env_file = ".env"


settings = Settings()
