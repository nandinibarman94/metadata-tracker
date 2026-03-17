from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Config(BaseSettings):
    DB_FILE: str = Field(
        default="sqlite/MetadataTracker.db",
        description="Path to SQLite database file"
    )
 
    @property
    def DB_PATH(self) -> str:
        return f"sqlite:///{self.DB_FILE}"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

configSetting = Config()