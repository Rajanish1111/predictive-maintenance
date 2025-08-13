from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Manages application settings loaded from a .env file.
    """
    # API settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_RELOAD: bool = True

    # Database settings
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DATABASE: str

    # Simulator settings
    SIMULATOR_INTERVAL_SECONDS: int = 10

    @property
    def database_url(self) -> str:
        """Constructs the database URL from individual components."""
        return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"

    # Configure Pydantic to load from a .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

# Create a single settings instance to be used across the application
settings = Settings()
