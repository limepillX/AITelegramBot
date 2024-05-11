from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class GPTConfig(BaseSettings):
    model: str = "gpt-3.5-turbo"
    max_tokens: int = 1000
    questions_cache_size: int = 10

    class Config:
        env_prefix = "OPENAI_GPT_"
        case_sensitive = False


class DALLEConfig(BaseSettings):
    model: str = "clip-dalle"
    amount_of_images: int = 1
    size: int = 256

    class Config:
        env_prefix = "OPENAI_DALLE_"
        case_sensitive = False


class OpenAIConfig(BaseSettings):
    api_key: str = ""
    gpt: GPTConfig = GPTConfig()
    dalle: DALLEConfig = DALLEConfig()

    class Config:
        env_prefix = "OPENAI_"
        case_sensitive = False


class TelegramBotConfig(BaseSettings):
    token: str = ""

    class Config:
        env_prefix = "TELEGRAM_BOT_"
        case_sensitive = False


class Settings(BaseSettings):
    name: str = "OpenAI Telegram Bot"
    project_path: Path = Path(__file__).parents[2]
    openai: OpenAIConfig = OpenAIConfig()
    telegram_bot: TelegramBotConfig = TelegramBotConfig()

    class Config:
        env_prefix = "APP_"
        case_sensitive = False


config = Settings()