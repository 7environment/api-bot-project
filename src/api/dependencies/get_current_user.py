from fastapi import Depends, HTTPException, Request
from typing import Annotated
from src.api.auth.auth import validate_telegram_webapp
from src.exeptions.telegram import InvalidInitDataError, ExpiredInitDataError
import json
from src.config.settings import settings
from src.api.schemas.user import TelegramUser

async def get_current_user(request: Request) -> TelegramUser:
    try:
        body = await request.json()
        init_data = body.get("initData")

        if not isinstance(init_data, str):
            raise InvalidInitDataError("initData must be a string")

        raw_user_data = validate_telegram_webapp(init_data, settings().BOT_TOKEN)
        user_json = raw_user_data["user"]
        user_dict = json.loads(user_json)

        return TelegramUser(**user_dict)

    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid user JSON")
    except ExpiredInitDataError:
        raise HTTPException(status_code=401, detail="Authentication data expired")
    except InvalidInitDataError:
        raise HTTPException(status_code=401, detail="Invalid authentication data")
    except Exception:
        raise HTTPException(status_code=500, detail="Authentication failed")

currentUserDep = Annotated[TelegramUser, Depends(get_current_user)]