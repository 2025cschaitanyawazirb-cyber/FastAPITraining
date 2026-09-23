from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
    MONGODB_URI: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str = "it_servicedesk"

    APP_Name: str = "IT Service Desk APP API"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
settings = Settings()