class TelegramAuthError(Exception):
    pass

class InvalidInitDataError(TelegramAuthError):
    pass

class ExpiredInitDataError(TelegramAuthError):
    pass

class MissingInitDataError(TelegramAuthError):
    pass