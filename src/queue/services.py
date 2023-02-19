from sqlalchemy.ext.asyncio import AsyncSession

from src.queue import schemas, models


class QueueStatusService:
    async def create_status(self, status: schemas.QueueStatus, db: AsyncSession):
        db_status = models.QueueStatus(**status.dict())
        db.add(db_status)
        await db.commit()
        await db.refresh(db_status)
        return db_status
