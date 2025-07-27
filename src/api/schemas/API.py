from pydantic import BaseModel, Field


class Thumbnail(BaseModel):
    targetId: int = Field(..., title="Target ID")
    state: str = Field(..., title="State")
    imageUrl: str = Field(..., title="Image URL")
    version: str = Field(..., title="Version")


class ThumbnailsAndUsername(Thumbnail):
    username: str = Field(..., title="Username")


class Username(BaseModel):
    username: str = Field(..., title="Username", min_length=3, max_length=50)


class InitDataAndUsername(BaseModel):
    initData: str = Field(..., title="initData")
    data: Username = Field(..., title="Username")