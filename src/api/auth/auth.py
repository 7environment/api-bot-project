import hmac
import hashlib
from urllib.parse import parse_qsl
from datetime import datetime, timedelta
from src.exeptions.telegram import InvalidInitDataError, ExpiredInitDataError, MissingInitDataError


def validate_telegram_webapp(init_data: str, bot_token: str) -> dict:
    if not init_data:
        raise MissingInitDataError("initData is missing")

    parsed_data = dict(parse_qsl(init_data))
    if "hash" not in parsed_data:
        raise InvalidInitDataError("Hash not found in initData")

    hash_from_data = parsed_data["hash"]
    data_check_list = [f"{k}={v}" for k, v in sorted(parsed_data.items()) if k != "hash"]
    data_check_string = "\n".join(data_check_list)

    secret_key = hmac.new(
        key=b"WebAppData",
        msg=bot_token.encode(),
        digestmod=hashlib.sha256
    ).digest()

    calculated_hash = hmac.new(
        key=secret_key,
        msg=data_check_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(calculated_hash, hash_from_data):
        raise InvalidInitDataError("HMAC verification failed")

    auth_date = parsed_data.get("auth_data")
    if auth_date:
        auth_timestamp = int(auth_date)
        now_timestamp = int(datetime.now().timestamp())
        if now_timestamp - auth_timestamp > 86400:
            raise ExpiredInitDataError("initData is expired")

    return parsed_data