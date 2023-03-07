import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv()


class Settings:

    PROJECT_NAME: str = "FASTGOODWE"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_KEY = os.getenv("DETA_PROJECT_KEY")


settings = Settings()
