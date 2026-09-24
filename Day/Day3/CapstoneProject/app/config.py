# This file defines all configuration values the app needs
# (DB connection info, app name, etc)

# pydantic_settings: automatically reads environment variables and validates
# their types
from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # MongoDB Settings
    MONGO_URI: str = Field(
        default="mongodb://localhost:27017",
        validation_alias=AliasChoices("MONGO_URI", "MONGODB_URI"),
    )
    MONGO_DB_NAME: str = Field(
        default="it_servicedesk",
        validation_alias=AliasChoices("MONGO_DB_NAME", "MONGODB_DB_NAME"),
    )

    # Gives the app a name
    APP_NAME: str = Field(
        default="IT Service Desk App API",
        validation_alias=AliasChoices("APP_NAME", "APP_Name"),
    )

    # Informs pydantic-settings to load values from .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


# Shared settings Object that all other files can import
settings = Settings()