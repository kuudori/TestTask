from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.queue import schemas
from src.queue.dependencies import check_existing_status
from src.queue.schemas import QueueStatusResponse
from src.queue.services import QueueStatusService

router = APIRouter(prefix='/queue-statuses')


@router.post("/create", response_model=QueueStatusResponse)
async def create_queue_status(status: schemas.QueueStatus, db: AsyncSession = Depends(get_db)):
    await check_existing_status(status, db)
    return await QueueStatusService().create_status(status, db)
