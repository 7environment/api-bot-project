from sqlalchemy.exc import DBAPIError, IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from src.database.models.user import Users

from src.exeptions.database import UserAlreadyExistsError, DatabaseError

async def add_user(session: AsyncSession, tg_id: int) -> bool:
    try:
        result = await session.execute(select(Users).where(Users.tg_id == tg_id))
        existing_user = result.scalar_one_or_none()

        if existing_user:
            raise UserAlreadyExistsError(f"User with tg_id={tg_id} already exists")

        new_user = Users(tg_id=tg_id)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return True

    except UserAlreadyExistsError as e:
        raise
    except IntegrityError as e:
        await session.rollback()
        raise DatabaseError("Unique constraint failed") from e
    except DBAPIError as e:
        await session.rollback()
        raise DatabaseError("Database connection error") from e
    except Exception as e:
        await session.rollback()
        raise DatabaseError("Unexpected database error") from e

async def get_user(session: AsyncSession, tg_id: int) -> dict:
    try:
        result = await session.execute(select(Users).where(Users.tg_id == tg_id))
        user = result.scalar_one_or_none()

        if not user:
            raise ValueError("User not found")

        if not user.username:
            raise ValueError("Username not set")

        return user

    except DBAPIError as e:
        # Логгируй, если нужно
        raise ConnectionError("Database error") from e

async def set_username(session: AsyncSession, tg_id: int, username: str) -> bool:
    try:
        query = update(Users).where(Users.tg_id == tg_id).values(username=username)
        result = await session.execute(query)

        if result.rowcount == 0:
            raise ValueError("User not found")

        await session.commit()
        return True

    except DBAPIError as e:
        raise ConnectionError("Database connection error") from e