from fastapi import APIRouter, HTTPException, Request
from src.api.schemas.API import Thumbnail, ThumbnailsAndUsername, InitDataAndUsername, Username
from src.database.create import SessionDep
from src.api.dependencies.get_current_user import currentUserDep
from src.database.methods.user import get_user, set_username
import httpx

router = APIRouter()

@router.get("/thumbnail/{username}", response_model=Thumbnail, summary="Get thumbnail by username")
async def get_thumbnail_route(username: str, request: Request):
    client = request.app.state.http_client
    try:
        response = await client.get(f"/thumbnail/{username}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"Ошибка на стороне Node.js: {e.response.text}")
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail="Не удалось подключиться к Node.js")

@router.get("/thumbnail/id/{tg_id}", response_model=ThumbnailsAndUsername, summary="Get thumbnail by telegram id")
async def get_thumbnail_by_telegram_id_route(tg_id: int, session: SessionDep, request: Request):
    try:
        username = (await get_user(session, tg_id)).username
        client = request.app.state.http_client
        try:
            response = await client.get(f"/thumbnail/{username}")
            response.raise_for_status()
            response = response.json()
            response["username"] = username
            return response
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code,
                                detail=f"Ошибка на стороне Node.js: {e.response.text}")
        except httpx.RequestError as e:
            raise HTTPException(status_code=503, detail="Не удалось подключиться к Node.js")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ConnectionError:
        raise HTTPException(status_code=503, detail="Database connection failed")

@router.post("/username", response_model=Username, summary="Set username")
async def set_username_route(request_body: InitDataAndUsername, user: currentUserDep, session: SessionDep):
    try:
        success = await set_username(session, user.id, request_body.username)
        return {"success": success}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ConnectionError:
        raise HTTPException(status_code=503, detail="Database connection failed")