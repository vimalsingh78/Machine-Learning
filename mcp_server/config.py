from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "MCP Server"
    DEBUG_MODE: bool = True
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "your-secret-key-here"  # Change this in production!
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database settings
    DATABASE_URL: str = "sqlite:///./mcp.db"
    
    class Config:
        case_sensitive = True

settings = Settings()
