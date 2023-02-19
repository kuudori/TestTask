from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.queue import models, schemas


async def check_existing_status(queue_status: schemas.QueueStatus, db: AsyncSession):
    query = select(models.QueueStatus).filter_by(
        s_name=queue_status.s_name,
        c_name=queue_status.c_name,
        c_id=queue_status.c_id,
        a_type=queue_status.a_type,
        direction=queue_status.direction,
        activation=queue_status.activation,
        c_state=queue_status.c_state,
        control=queue_status.control
    )
    result = await db.execute(query)
    if existing_status := result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail=f"Status {existing_status.c_name} already exists")
    return queue_status
