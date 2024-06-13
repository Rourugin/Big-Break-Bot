from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select


async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user_id = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user_id:
            session.add(User(tg_id=tg_id))
            await session.commit()      