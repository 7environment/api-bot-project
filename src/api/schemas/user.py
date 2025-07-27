from pydantic import BaseModel, Field


class TelegramUser(BaseModel):
    id: int = Field(..., title="User ID")