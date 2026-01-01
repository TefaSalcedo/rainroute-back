from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "RainRoute API"
    API_V1_STR: str = "/api/v1"
    
    # Database (Placeholder for future config)
    # POSTGRES_SERVER: str
    # POSTGRES_USER: str
    # POSTGRES_PASSWORD: str
    # POSTGRES_DB: str

    class Config:
        case_sensitive = True

settings = Settings()
